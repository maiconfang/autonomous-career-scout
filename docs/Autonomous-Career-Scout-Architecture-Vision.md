# Autonomous Career Scout - Architecture Vision (Updated)

## Vision

Autonomous Career Scout is not a job analysis tool.

It is an autonomous career assistant capable of receiving a goal, discovering opportunities, reasoning about them, and recommending the most relevant options with minimal human intervention.

---

## Example Goal

Find remote QA Engineer jobs in Canada.

The user should not need to provide job URLs manually.

The agent is responsible for:

1. Finding opportunities
2. Evaluating opportunities
3. Ranking opportunities
4. Explaining recommendations
5. Generating reports

---

# High-Level Architecture

User Goal
    |
    v
CareerScoutAgent
    |
    +-- Search Tool
    +-- Scrape Tool
    +-- Parse Tool
    +-- Match Tool
    +-- OpenAI Analysis Tool
    +-- Report Tool
    |
    v
PostgreSQL
    |
    v
Reports

---

# Agent Reasoning Loop

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

---

# Technology Responsibilities

Playwright
- Search websites
- Navigate pages
- Collect job links

BeautifulSoup + lxml
- Clean HTML
- Extract structured information

Pydantic
- Data validation
- Domain models

OpenAI
- Reasoning
- Recommendations
- Opportunity analysis

PostgreSQL
- Job history
- Match history
- Execution history

CrewAI (Future Phase)
- Multi-agent orchestration
- Advanced planning and delegation

---

# Long-Term Goal

User
|
+-- "Find remote QA jobs in Canada"
|
v
CareerScoutAgent
|
+-- Search jobs
+-- Filter jobs
+-- Analyze jobs
+-- Match profile
+-- Generate recommendations
|
v
Top Opportunities Report

The final objective is to build a real Agentic AI system that works as a career scout, helping users focus only on the opportunities that matter most.
