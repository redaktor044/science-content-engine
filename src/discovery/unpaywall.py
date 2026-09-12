from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx


API_URL = "https://api.unpaywall.org/v2"


@dataclass(frozen=True)
class UnpaywallClient:
    email: str
    timeout: float = 20.0

    def get_by_doi(self, doi: str) -> dict[str, Any]:
        """Fetch Unpaywall metadata for a DOI."""
        url = f"{API_URL}/{doi}"
        response = httpx.get(
            url,
            params={"email": self.email},
            timeout=self.timeout,
            follow_redirects=True,
        )
        response.raise_for_status()
        return response.json()

    def search(self, query: str, *, page: int = 1, per_page: int = 20) -> dict[str, Any]:
        """Search Unpaywall for works matching a query."""
        response = httpx.get(
            f"{API_URL}/search",
            params={
                "query": query,
                "email": self.email,
                "is_oa": "true",
                "page": page,
                "per-page": per_page,
            },
            timeout=self.timeout,
            follow_redirects=True,
        )
        response.raise_for_status()
        return response.json()


def normalize_work(work: dict[str, Any]) -> dict[str, Any]:
    """Convert an Unpaywall record into the stable MVP schema."""
    best = work.get("best_oa_location") or {}
    return {
        "title": work.get("title"),
        "doi": work.get("doi"),
        "year": work.get("year"),
        "authors": [a.get("author_name") for a in work.get("z_authors", []) if a.get("author_name")],
        "journal": work.get("journal_name"),
        "publisher": work.get("publisher"),
        "is_oa": work.get("is_oa", False),
        "oa_status": work.get("oa_status"),
        "license": best.get("license"),
        "oa_url": best.get("url_for_landing_page") or best.get("url"),
        "pdf_url": best.get("url_for_pdf"),
    }
