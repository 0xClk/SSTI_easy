from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def filtered(template):
    blacklist = ["self.__dict__", "url_for", "config", "getitems", "../", "process"]

    for b in blacklist:
        if b in template:
            template = template.replace(b, "")
  
    return template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/template", methods=["POST"])
def template():
    template = request.form.get("template")

    if template is None:
        return "No template provided", 400

    if len(template) > 500:
        return "Too long input", 400

    while filtered(template) != template:
        template = filtered(template)

    # This line introduces SSTI vulnerability
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
