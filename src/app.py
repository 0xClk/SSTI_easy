from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def filtered(template):
    # Define a blacklist of dangerous or undesired strings
    blacklist = ["self.__dict__", "url_for", "getitems", "../", "process", "7 * 7", "7*7"]

    # Remove any blacklisted strings from the template
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

    # Apply filtering to user-provided template
    filtered_template = filtered(template)

    # Render using filtered user-provided template
    return render_template_string(filtered_template)

if __name__ == '__main__':
    app.run(debug=True)
