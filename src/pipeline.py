from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv

from src.analysis.scorer import make_hook, score_work
from src.discovery.unpaywall import UnpaywallClient, normalize_work


def main() -> None:
    load_dotenv()

    email = os.getenv("UNPAYWALL_EMAIL")
    if not email:
        raise SystemExit("Missing UNPAYWALL_EMAIL. Copy .env.example to .env and set your email.")

    query = os.getenv("SCIENCE_TOPIC", "artificial intelligence")
    results = int(os.getenv("SCIENCE_RESULTS", "20"))

    client = UnpaywallClient(email=email)
    payload = client.search(query, per_page=results)

    works = []
    for raw in payload.get("results", []):
        work = normalize_work(raw)
        work.update(score_work(raw))
        work["hook"] = make_hook(work.get("title"))
        works.append(work)

    output = {
        "query": query,
        "count": len(works),
        "works": works,
    }

    output_dir = Path("data/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "latest.json"
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Saved {len(works)} works to {output_path}")


if __name__ == "__main__":
    main()
