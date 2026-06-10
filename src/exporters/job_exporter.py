import json
from pathlib import Path
from dataclasses import asdict


class JobExporter:

    @staticmethod
    def export_to_json(
        jobs,
        output_file="out/jobs.json"
    ):

        Path("out").mkdir(
            exist_ok=True
        )

        data = [
            asdict(job)
            for job in jobs
        ]

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"\nExported {len(jobs)} jobs to:"
        )

        print(output_file)