# Autonomous Career Scout

Autonomous Career Scout is an Agentic AI project that autonomously discovers, analyzes, and evaluates job opportunities.

The goal is to combine Playwright, CrewAI, and OpenAI to create an intelligent career assistant capable of performing reasoning loops (Thought → Action → Observation) to assess job compatibility and generate actionable career insights.

## Objectives

* Search for job opportunities automatically
* Extract and normalize job descriptions
* Analyze job requirements using AI
* Compare job requirements against a candidate profile
* Classify opportunities as High, Medium, or Low Match
* Generate detailed reports with reasoning traces

## Architecture

```text
Job Posting URL
        ↓
 Playwright Scraper
        ↓
   Job Parser
        ↓
 Agentic Reasoning
        ↓
 Match Analysis
        ↓
 Markdown Report
```

## Tech Stack

* Python
* Playwright
* CrewAI
* OpenAI GPT-4o
* Markdown Reports

## Project Structure

```text
autonomous-career-scout/

├── main.py
│
├── src/
│   ├── agents/
│   ├── tasks/
│   ├── tools/
│   ├── services/
│   ├── models/
│   └── prompts/
│
├── reports/
├── data/
├── playwright/
├── requirements.txt
├── .env.example
└── README.md
```

## Current Status

🚧 In Development

Current focus:

* Playwright scraper
* Job content extraction
* Agent reasoning loop
* Job-to-profile matching

Future phases:

* Multi-agent workflows
* Career recommendations
* Skill gap analysis
* Market trend analysis

## Example Reasoning Loop

```text
Thought:
I need to evaluate whether this job matches the candidate profile.

Action:
Analyze candidate profile.

Observation:
10 years of QA experience.
Strong Playwright background.

Thought:
Analyze job description.

Action:
Extract job requirements.

Observation:
Playwright, Python, API Testing.

Thought:
Compare skills and experience.

Action:
Calculate match score.

Observation:
92% compatibility.

Final Answer:
HIGH MATCH
```

## Disclaimer

This project is intended for educational and portfolio purposes and focuses on Agentic AI reasoning rather than automated job applications.
