import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

from src.models.opportunity_analysis import ( OpportunityAnalysis )

class OpportunityExplainer:

    def __init__(self):

        self.api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        print(
            "\n=== OPENAI DEBUG ==="
        )

        print(
            f"API Key Found: {bool(self.api_key)}"
        )

        self.client = None

        if self.api_key:

            self.client = OpenAI(
                api_key=self.api_key
            )
            
    def explain(
        self,
        analysis: OpportunityAnalysis
    ) -> dict:

        if not self.client:

            return self._fallback_explanation(
                analysis
            )

        try:

            prompt = f"""
                You are a senior QA career advisor.

                Analyze this opportunity.

                Score:
                {analysis.score}

                Matched Skills:
                {", ".join(analysis.matched_skills)}

                Missing Skills:
                {", ".join(analysis.missing_skills)}

                Top Strengths:
                {", ".join(analysis.strengths)}

                Top Gaps:
                {", ".join(analysis.weaknesses)}

                Recommendation:
                {analysis.recommendation}

                Return NO MORE than 120 words.

                Use EXACTLY this format:

                Why it fits:
                <short explanation>

                Top strengths:
                <comma separated list>

                Top gaps:
                <comma separated list>

                Recommendation:
                <one sentence>

                Do not use numbered lists.
                Do not use markdown.
                Keep it concise.
                """

            model_name = "gpt-4o-mini"

            response = self.client.chat.completions.create(
                model=model_name,
                max_tokens=150,
                temperature=0.3,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a practical senior QA career advisor."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return {
                "explanation": (
                    response
                    .choices[0]
                    .message
                    .content
                ),
                "model": model_name,
                "prompt_tokens": (
                    response.usage.prompt_tokens
                ),
                "completion_tokens": (
                    response.usage.completion_tokens
                ),
                "total_tokens": (
                    response.usage.total_tokens
                )
            }

        except Exception as ex:

            return {
                "explanation": (
                    f"OpenAI error: {str(ex)}"
                ),
                "model": "unknown",
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            }

    def _fallback_explanation(
        self,
        analysis: OpportunityAnalysis
    ) -> dict:

        strengths = (
            ", ".join(
                analysis.strengths
            )
            if analysis.strengths
            else "None"
        )

        gaps = (
            ", ".join(
                analysis.weaknesses
            )
            if analysis.weaknesses
            else "None"
        )

        return {
            "explanation": (
                f"Why it fits:\n"
                f"Score {analysis.score}%.\n\n"
                f"Top strengths:\n"
                f"{strengths}\n\n"
                f"Top gaps:\n"
                f"{gaps}\n\n"
                f"Recommendation:\n"
                f"{analysis.recommendation}"
            ),
            "model": "fallback",
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }