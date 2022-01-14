from os.path import join, dirname
from flask import render_template
from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms.fields import SubmitField

from . import appbuilder

app = appbuilder.app


class PageDownForm(FlaskForm):
    pagedown = PageDownField("Enter markdown")
    submit = SubmitField("Submit")


@app.route("/wysiwyg", methods=["GET", "POST"])
def index():
    form = PageDownForm()
    if form.validate_on_submit():
        text = form.pagedown.data
        # write to file
        with open(join(dirname(__file__), "data/test_doc.md"), "w") as f:
            f.write(str(text))
    return render_template(
        "wysiwyg.html",
        form=form,
        base_template=appbuilder.base_template,
        appbuilder=appbuilder,
    )
