from __future__ import annotations

import re
from typing import Any


SURPRISE_TERMS = {
    "first", "novel", "unexpected", "breakthrough", "discovery",
    "reveals", "unprecedented", "new method", "significantly",
}


def score_work(work: dict[str, Any]) -> dict[str, Any]:
    """Deterministic MVP score; AI scoring will replace this later."""
    title = (work.get("title") or "").lower()
    abstract = (work.get("abstract") or "").lower()
    text = f"{title} {abstract}"

    novelty = min(10, 4 + sum(1 for term in SURPRISE_TERMS if term in text))
    simplicity = max(1, min(10, 10 - max(0, len(title.split()) - 14) // 4))
    social = round((novelty * 0.6) + (simplicity * 0.4), 1)

    return {
        "scientific_score": round(novelty, 1),
        "viral_score": social,
    }


def make_hook(title: str | None) -> str:
    """Create a safe placeholder hook without inventing scientific claims."""
    clean = re.sub(r"\s+", " ", title or "New scientific study").strip()
    return f"Naukowcy opublikowali nowe badanie: {clean}"
