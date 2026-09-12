from src.discovery.unpaywall import normalize_work
from src.analysis.scorer import make_hook, score_work


def test_normalize_work():
    raw = {
        "title": "A New Discovery in Artificial Intelligence",
        "doi": "10.1234/example",
        "year": 2026,
        "z_authors": [{"author_name": "Jane Doe"}],
        "journal_name": "Example Journal",
        "publisher": "Example Publisher",
        "is_oa": True,
        "oa_status": "gold",
        "best_oa_location": {
            "license": "cc-by",
            "url_for_landing_page": "https://example.org/paper",
            "url_for_pdf": "https://example.org/paper.pdf",
        },
    }

    result = normalize_work(raw)

    assert result["title"] == raw["title"]
    assert result["doi"] == raw["doi"]
    assert result["authors"] == ["Jane Doe"]
    assert result["pdf_url"].endswith(".pdf")


def test_score_and_hook_are_deterministic():
    raw = {
        "title": "Unexpected New Discovery",
        "abstract": "A novel method produced a significant result.",
    }
    score = score_work(raw)
    hook = make_hook(raw["title"])

    assert 1 <= score["scientific_score"] <= 10
    assert 1 <= score["viral_score"] <= 10
    assert raw["title"] in hook
