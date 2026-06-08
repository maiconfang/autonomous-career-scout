# Autonomous Career Scout

Autonomous Career Scout is an Agentic AI project that autonomously discovers, analyzes, evaluates, and recommends job opportunities.

The goal is not simply to analyze job URLs provided by a user. The long-term vision is to build a real autonomous career assistant capable of receiving a goal, deciding which actions to take, collecting opportunities, reasoning about them, and generating recommendations with minimal human intervention.

---

# Vision

Example goal:

```text
Find remote QA Engineer jobs in Canada.
```

The user should not need to manually search for jobs and provide URLs.

The system is responsible for:

- Discovering opportunities
- Collecting job data
- Evaluating compatibility
- Ranking opportunities
- Generating recommendations
- Producing reports

---

# Objectives

- Search for job opportunities automatically
- Extract and normalize job descriptions
- Analyze job requirements using AI
- Compare job requirements against a candidate profile
- Classify opportunities as High, Medium, or Low Match
- Generate detailed reports with reasoning traces
- Build an autonomous career assistant using Agentic AI concepts

---

# High-Level Architecture

```text
User Goal
    │
    ▼
CareerScoutAgent
    │
    ├── Search Tool
    ├── Scrape Tool
    ├── Parse Tool
    ├── Match Tool
    ├── OpenAI Analysis Tool
    └── Report Tool
    │
    ▼
PostgreSQL
    │
    ▼
Reports
```

---

# Agent Reasoning Loop

```text
Goal
↓
Think
↓
Choose Tool
↓
Execute Tool
↓
Observe Result
↓
Update Context
↓
Goal Achieved?
    ├── No → Continue
    └── Yes → Generate Report
```

---

# Technology Stack

## Python

Main programming language used across the project.

## Playwright

Responsible for:

- Navigating websites
- Searching job opportunities
- Collecting job links
- Extracting HTML content

## BeautifulSoup + lxml

Responsible for:

- Cleaning HTML
- Extracting meaningful text
- Structuring page content

## Pydantic

Responsible for:

- Data validation
- Domain models
- Structured objects

Examples:

```text
JobPosting
CandidateProfile
JobMatchResult
```

## OpenAI

Responsible for:

- Reasoning
- Recommendations
- Opportunity analysis
- Career insights

## PostgreSQL

Responsible for:

- Job history
- Match history
- Execution history
- Future memory layer

## CrewAI (Future Phase)

CrewAI is planned for future versions of the project.

It will be used for:

- Multi-agent orchestration
- Task delegation
- Advanced planning workflows

The first versions focus on building robust tools and a solid agent foundation before introducing multi-agent architectures.

---

# Project Structure

```text
autonomous-career-scout/

├── data/
├── docs/
├── reports/
│
├── src/
│   ├── agents/
│   │   └── career_scout_agent.py
│   │
│   ├── models/
│   │   ├── candidate_profile.py
│   │   ├── job_posting.py
│   │   ├── job_match_result.py
│   │   └── search_criteria.py
│   │
│   ├── services/
│   │   ├── cv_parser.py
│   │   ├── job_parser.py
│   │   ├── profile_service.py
│   │   ├── job_matcher.py
│   │   ├── openai_analyzer.py
│   │   └── report_generator.py
│   │
│   ├── tools/
│   │   ├── playwright_client.py
│   │   ├── scraper_tool.py
│   │   ├── indeed_tool.py
│   │   ├── linkedin_tool.py
│   │   └── google_jobs_tool.py
│   │
│   ├── repositories/
│   │   ├── jobs_repository.py
│   │   ├── matches_repository.py
│   │   └── executions_repository.py
│   │
│   ├── prompts/
│   └── tasks/
│
├── tests/
├── .env.example
├── requirements.txt
├── README.md
└── main.py
```

---

# Current Status

🚧 In Development

Current focus:

- Playwright navigation
- Job content extraction
- Job parsing
- Candidate profile matching
- Agent reasoning foundations

---

# Future Roadmap

## Phase 1

- Indeed integration
- Job parsing
- Match engine
- Markdown reports

## Phase 2

- OpenAI-powered recommendations
- PostgreSQL persistence
- Historical analysis

## Phase 3

- CareerScoutAgent orchestration
- Autonomous reasoning loops
- Multi-source job discovery

## Phase 4

- CrewAI integration
- Multi-agent workflows
- Advanced career recommendations

---

# Example Future Execution

```text
User:
Find remote QA jobs in Canada

CareerScoutAgent:
↓

Searching Indeed...
Searching LinkedIn...
Searching Company Sites...

↓

47 jobs found

↓

Analyzing opportunities...

↓

Top Matches:

1. Senior QA Engineer (91%)
2. Playwright Automation Engineer (87%)
3. SDET (83%)

↓

Generating report...
```

---

# Disclaimer

This project is intended for educational, research, and portfolio purposes.

The focus is on Agentic AI, autonomous reasoning, decision-making, and career opportunity analysis rather than automated job applications.
