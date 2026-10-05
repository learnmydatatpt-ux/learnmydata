from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")


@app.get("/ai-assistant")
def ai_assistant():
    return render_template("ai_assistant.html")

@app.post("/api/ai-assistant")
def ai_assistant_api():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"ok": False, "message": "Please enter a marketing question."}), 400
    if len(message) > 4000:
        return jsonify({"ok": False, "message": "Please keep your question under 4,000 characters."}), 400

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return jsonify({"ok": False, "message": "AI Assistant is not configured yet. Please add OPENAI_API_KEY in Render environment variables."}), 503

    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-6-luna"),
            instructions="""You are LearnMyData AI Marketing Assistant, a helpful digital marketing consultant.
LearnMyData provides SEO, AEO, GEO, PPC/performance marketing, social media, content marketing, web design, conversion optimization, and analytics.
Give practical, concise, ethical recommendations for startups and growing businesses.
Do not invent LearnMyData pricing, guarantees, client results, or company facts.""",
            input=message,
            max_output_tokens=700
        )
        return jsonify({"ok": True, "message": response.output_text})
    except Exception:
        app.logger.exception("AI assistant error")
        return jsonify({"ok": False, "message": "The AI Assistant is temporarily unavailable. Please try again shortly."}), 502

@app.get("/services")
def services():
    return render_template("services.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/process")
def process():
    return render_template("process.html")

@app.get("/faq")
def faq():
    return render_template("faq.html")

@app.get("/sitemap.xml")
def sitemap():
    return render_template("sitemap.xml"), 200, {"Content-Type": "application/xml"}

@app.post("/contact")
def contact():
    data = request.get_json(silent=True) or request.form
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"ok": False, "message": "Please complete all fields."}), 400

    # Connect this endpoint to your email service or CRM when you are ready.
    return jsonify({
        "ok": True,
        "message": f"Thanks {name}! We received your enquiry."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
