from pathlib import Path


class JobLoader:

    def load_jobs(self) -> list[tuple[str, str]]:
        """
        Load all job files from data/jobs.

        Returns:
            [
                ("qa_automation_engineer.txt", "...job content..."),
                ("sdet_playwright.txt", "...job content...")
            ]
        """

        jobs_directory = Path("data/jobs")

        jobs = []

        for file in jobs_directory.glob("*.txt"):

            content = file.read_text(
                encoding="utf-8"
            )

            jobs.append(
                (
                    file.name,
                    content
                )
            )

        return jobs