# MarketMind — AI Digital Marketing Website

A polished digital marketing website built with **Python, Flask, and TensorFlow**.

## Features

- Responsive marketing landing page
- Performance marketing / funnel / AI analytics service sections
- TensorFlow neural-network lead scoring demo
- Flask JSON API at `POST /api/score`
- No database required for the demo

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000.

## Production note

The TensorFlow model is intentionally trained on synthetic data so the repository runs immediately. For real marketing decisions, replace the training set with validated historical CRM/campaign outcomes, add proper train/validation/test splits, calibration, monitoring, and privacy controls.
