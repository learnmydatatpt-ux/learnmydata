# LearnMyData — Python Digital Marketing Website

A responsive digital marketing website built with **Python + Flask**.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Production

```bash
gunicorn app:app
```

The contact form posts to `/contact`. Connect that endpoint to your email provider or CRM before production launch.
