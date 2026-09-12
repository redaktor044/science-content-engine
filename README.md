# Science Content Engine

Automated research-to-social-media pipeline powered by Open Access scientific literature.

## MVP

Pipeline:

`Unpaywall → paper metadata → filtering → scoring → content-ready JSON`

The first milestone focuses on reliable discovery of Open Access papers. Content generation and publishing integrations come later.

## Project structure

```text
science-content-engine/
├── config/
│   └── topics.yaml
├── src/
│   ├── analysis/
│   ├── content/
│   ├── discovery/
│   ├── papers/
│   └── pipeline.py
├── tests/
├── data/
│   ├── papers/
│   └── outputs/
├── .env.example
└── requirements.txt
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `UNPAYWALL_EMAIL` in `.env`. The API requires an email address for identification.

## Usage

```bash
python -m src.pipeline
```

## Roadmap

- [x] Repository foundation
- [ ] Unpaywall discovery client
- [ ] Topic configuration
- [ ] Paper metadata normalization
- [ ] Scientific/social potential scoring
- [ ] Open-access full-text retrieval
- [ ] AI paper analysis
- [ ] Hook and carousel generation
- [ ] Image/video generation
- [ ] Social publishing
- [ ] Scheduled automation
