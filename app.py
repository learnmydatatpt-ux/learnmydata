from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

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
