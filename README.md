# Autonomous Career Scout

Autonomous Career Scout is an Agentic AI project designed to discover, analyze, evaluate, and recommend job opportunities.

The long-term vision is to build a career intelligence platform capable of collecting opportunities from multiple sources, analyzing compatibility against a candidate profile, tracking career trends, identifying skill gaps, and supporting career decisions through AI-powered insights.

---

# Terminal - VS Code
tree src /A /F > src-tree.txt

---

# Vision

Example goal:

```text
Find remote QA Engineer jobs in Canada.
```

The user should not need to manually search for jobs and provide URLs.

The system will be responsible for:

* Discovering opportunities
* Collecting job data
* Evaluating compatibility
* Ranking opportunities
* Generating recommendations
* Tracking career progress
* Producing reports and insights

---

# Current Capabilities

The current version already supports:

* Resume parsing from DOCX files
* Candidate profile extraction
* Job description parsing
* Skill extraction
* Match score calculation
* Career recommendations
* Application decision analysis
* Opportunity analysis
* OpenAI-powered explanations
* JSON report generation
* PostgreSQL persistence
* Dockerized database infrastructure

---

# Objectives

* Search for job opportunities automatically
* Extract and normalize job descriptions
* Analyze job requirements using AI
* Compare job requirements against a candidate profile
* Classify opportunities as High, Medium, or Low Match
* Generate detailed reports with reasoning traces
* Store historical analyses
* Build an autonomous career assistant using Agentic AI concepts

---

# High-Level Architecture

```text
Resume (.docx)
        │
        ▼
Resume Parser
        │
        ▼
Candidate Profile
        │
        ▼
Job Parser
        │
        ▼
Match Engine
        │
        ▼
Career Advisor Agent
        │
        ▼
Decision Agent
        │
        ▼
Opportunity Analysis Agent
        │
        ▼
OpenAI Opportunity Explainer
        │
        ▼
Report Generator
        │
        ▼
PostgreSQL
        │
        ▼
Reports
```

---

# Current Execution Flow

```text
Resume (.docx)
        │
        ▼
Resume Parser

Jobs (.txt)
        │
        ▼
Job Parser

        ▼

MatchResult

        ▼

CareerRecommendation

        ▼

ApplicationDecision

        ▼

OpportunityAnalysis

        ▼

OpenAI Explanation

        ▼

opportunities.json

        ▼

PostgreSQL
```

---

# Technology Stack

## Python

Primary programming language.

## OpenAI

Responsible for:

* Opportunity explanations
* Recommendations
* Career insights
* Future reasoning workflows

## PostgreSQL

Responsible for:

* Opportunity history
* Match history
* Execution history
* Future memory layer

### PostgreSQL Querys
TRUNCATE TABLE
    opportunity_analysis,
    executions,
    opportunities
RESTART IDENTITY CASCADE;


SELECT COUNT(*) FROM opportunities;

SELECT COUNT(*) FROM executions;

SELECT COUNT(*) FROM opportunity_analysis;

## Docker

Responsible for:

* Local infrastructure
* PostgreSQL containerization
* Reproducible development environment

## Pydantic

Responsible for:

* Domain models
* Validation
* Structured objects

Examples:

```text
CandidateProfile
MatchResult
CareerRecommendation
ApplicationDecision
OpportunityAnalysis
```

## Playwright (Future Phase)

Will be responsible for:

* LinkedIn navigation
* Indeed navigation
* Monster navigation
* Job collection
* Automated discovery

## BeautifulSoup + lxml (Future Collection Phase)

Will be responsible for:

* HTML cleanup
* Content extraction
* Structured job descriptions

## CrewAI (Future Phase)

Planned for:

* Multi-agent orchestration
* Task delegation
* Planning workflows
* Advanced autonomous reasoning

---

# Project Structure

```text
autonomous-career-scout/

├── data/
│   ├── candidates/
│   ├── resumes/
│   └── jobs/
│
├── database/
│   ├── connection.py
│   ├── scripts/
│   └── examples/
│
├── docs/
├── reports/
│
├── src/
│   ├── agents/
│   │   ├── candidate_agent.py
│   │   ├── recruiter_agent.py
│   │   ├── match_analyst_agent.py
│   │   ├── career_advisor_agent.py
│   │   ├── decision_agent.py
│   │   └── opportunity_analysis_agent.py
│   │
│   ├── models/
│   ├── services/
│   ├── reporting/
│   ├── openai/
│   └── config/
│
├── tests/
├── docker-compose.yml
├── .env.example
├── requirements.txt
├── README.md
└── main.py
```

---

# Current Status

✅ Phase 1 - Analysis Engine (Completed)

* Resume Parser
* Job Parser
* Match Engine
* Career Recommendation Engine
* Decision Analysis
* Opportunity Analysis
* Report Generation

✅ Phase 2 - AI & Persistence (Completed)

* OpenAI Integration
* PostgreSQL Integration
* Docker Infrastructure
* Persistence Layer
* Database Validation
* Historical Storage Foundation

🚧 Phase 3 - Historical Intelligence (Next)

Planned:

* Execution history
* Opportunity history
* Skill gap tracking
* Career trend analysis
* Historical insights

🚧 Phase 4 - Playwright Collectors

Planned:

* LinkedIn Collector
* Indeed Collector
* Monster Collector
* Job normalization
* Database integration

🚧 Phase 5 - Autonomous Career Scout

Planned:

* Autonomous reasoning loops
* Tool selection
* Goal-driven execution
* Multi-source discovery

🚧 Phase 6 - Multi-Agent Platform

Planned:

* CrewAI integration
* Agent collaboration
* Advanced planning
* Career intelligence workflows

---

# Example Future Execution

```text
User:
Find remote QA jobs in Canada

CareerScoutAgent:

Searching LinkedIn...
Found 23 jobs

Searching Indeed...
Found 41 jobs

Searching Monster...
Found 17 jobs

Analyzing 81 opportunities...

Top Matches:

1. Senior QA Automation Engineer
   Score: 92%

2. SDET Playwright
   Score: 89%

3. Salesforce QA Engineer
   Score: 81%

Generating recommendations...

Saving results...

Execution completed.
```

---

# Long-Term Vision

```text
User Goal
    │
    ▼
CareerScoutAgent
    │
    ├── Search Tool
    ├── Collection Tool
    ├── Parsing Tool
    ├── Match Tool
    ├── OpenAI Analysis Tool
    ├── Persistence Tool
    └── Reporting Tool
    │
    ▼
PostgreSQL
    │
    ▼
Career Intelligence Platform
```

---

# Disclaimer

This project is intended for educational, research, and portfolio purposes.

The focus is on Agentic AI, autonomous reasoning, decision-making, career intelligence, and opportunity analysis.

The project does not automate job applications and is designed to assist users in making informed career decisions.
