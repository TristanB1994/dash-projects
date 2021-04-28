from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    """Landing page."""
    return render_template(
        'index.jinja2',
        title='Plotly Dash Flask Tutorial',
        description="Embed Plotly dash into flask apps",
        template='home-template',
        body="This is a homepage served by flask"
    )