from bs4 import BeautifulSoup


class ScraperTool:

    def extract_text(self, html: str) -> str:

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        return soup.get_text(
            separator="\n",
            strip=True
        )