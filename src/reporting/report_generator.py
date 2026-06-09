import json
from pathlib import Path


class ReportGenerator:

    def generate(
        self,
        results: list[dict]
    ) -> None:

        report = []

        for result in results:

            analysis = result[
                "opportunity_analysis"
            ]

            decision = result[
                "decision"
            ]

            report.append(
                {
                    "job_file": result[
                        "file_name"
                    ],

                    "score": analysis.score,

                    "matched_skills": (
                        analysis.matched_skills
                    ),

                    "missing_skills": (
                        analysis.missing_skills
                    ),

                    "strengths": (
                        analysis.strengths
                    ),

                    "weaknesses": (
                        analysis.weaknesses
                    ),

                    "recommendation": (
                        analysis.recommendation
                    ),

                    "decision": (
                        decision.decision
                    ),

                    "confidence": (
                        decision.confidence
                    ),

                    "reason": (
                        decision.reason
                    )
                }
            )

        reports_directory = Path(
            "reports"
        )

        reports_directory.mkdir(
            exist_ok=True
        )

        report_file = (
            reports_directory /
            "opportunities.json"
        )

        with open(
            report_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"\n[ReportGenerator] Report saved: "
            f"{report_file}"
        )