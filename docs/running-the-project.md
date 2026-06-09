# Running Autonomous Career Scout

This guide explains how to set up and run the project after cloning it from GitHub.

---

# Prerequisites

Before running the project, make sure the following tools are installed:

## Python

Recommended:

```text
Python 3.12.x
```

Also supported:

```text
Python 3.13.x
```

Why?

This project uses modern Python libraries such as:

* CrewAI
* OpenAI SDK
* Playwright
* Pydantic

These libraries work best with Python 3.12 and 3.13.

Older Python versions may introduce dependency conflicts or compatibility issues.

Verify your Python version:

```bash
python --version
```

Expected output:

```text
Python 3.12.x
```

or

```text
Python 3.13.x
```

---

# Clone the Repository

Clone the project:

```bash
git clone https://github.com/maiconfang/autonomous-career-scout.git
```

Navigate to the project folder:

```bash
cd autonomous-career-scout
```

---

# Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

---

# Activate the Virtual Environment

## Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Expected result:

```text
(.venv)
```

appears at the beginning of the terminal line.

Example:

```text
(.venv) PS C:\workspace\autonomous-career-scout>
```

---

# Upgrade pip

Upgrade pip before installing dependencies:

```bash
python -m pip install --upgrade pip
```

---

# Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

This may take a few minutes depending on your internet connection.

Expected result:

```text
Successfully installed ...
```

with no errors.

---

# Install Playwright Browsers

Install Playwright browser binaries:

```bash
playwright install
```

or

```bash
python -m playwright install
```

Expected result:

```text
Chromium installed
```

or

```text
Browsers already installed
```

---

# Configure Environment Variables

Copy:

```text
.env.example
```

to:

```text
.env
```

and update the required values.

Example:

```text
OPENAI_API_KEY=your_openai_api_key
```

---

# Verify the Installation

Create a temporary test file:

```python
from openai import OpenAI
from crewai import Agent
from playwright.sync_api import sync_playwright

print("OK")
```

Run:

```bash
python test.py
```

Expected output:

```text
OK
```

If you see this message, the main dependencies were installed successfully.

---

# Run the Project

Execute:

```bash
python main.py
```

Expected output:

```text
=== JOB ===

JobPosting(...)

=== CANDIDATE ===

CandidateProfile(...)

=== MATCH RESULT ===

{
    "score": 33,
    "matched_skills": [...],
    "missing_skills": [...]
}
```

Example:

```text
=== MATCH RESULT ===

{
    'score': 33,
    'matched_skills': ['Salesforce CPQ', 'Selenium'],
    'missing_skills': ['Provar', 'Apex', 'Visualforce', 'Lightning']
}
```

---

# What Does This Mean?

The application is:

1. Loading a job posting
2. Parsing the job requirements
3. Loading a candidate profile
4. Comparing skills
5. Generating a match result

This confirms that the core pipeline is working correctly.

---

# Current Architecture

```text
Job Description
        ↓
Job Parser
        ↓
Candidate Profile
        ↓
Matching Engine
        ↓
Match Result
```

Future versions will expand this workflow with:

```text
Playwright Job Scraping
AI Analysis
OpenAI Integration
CrewAI Agents
Recommendation Engine
Report Generation
```

---

# Troubleshooting

## ModuleNotFoundError

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

---

## Playwright Browser Missing

Install browsers:

```bash
playwright install
```

---

## OpenAI Authentication Error

Verify:

```text
OPENAI_API_KEY
```

inside your:

```text
.env
```

file.

---

# Author

Maicon Fang

GitHub:
https://github.com/maiconfang

LinkedIn:
https://www.linkedin.com/in/maiconfang/
