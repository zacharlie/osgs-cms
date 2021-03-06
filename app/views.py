from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import (
    ModelView,
    ModelRestApi,
    AppBuilder,
    expose,
    has_access,
    BaseView,
)

from . import appbuilder, db


class AboutView(BaseView):
    route_base = "/about"
    default_view = "aboutPage"

    @expose("/")
    def aboutPage(self):
        return render_template(
            "about.html",
            base_template=appbuilder.base_template,
            appbuilder=appbuilder,
        )


appbuilder.add_view_no_menu(AboutView())
# appbuilder.add_view(AboutView, "About")


class ArticlesView(BaseView):
    route_base = "/posts"
    default_view = "editPosts"

    @expose("/")
    def editPosts(self):
        return render_template(
            "posts/manage.html",
            base_template=appbuilder.base_template,
            appbuilder=appbuilder,
        )

    @expose("/create/post")
    def createPost(self):
        return render_template(
            "posts/wysiwyg.html",
            base_template=appbuilder.base_template,
            appbuilder=appbuilder,
        )

    @expose("/create/map")
    def createPost(self):
        return render_template(
            "posts/wysiwyg.html",
            base_template=appbuilder.base_template,
            appbuilder=appbuilder,
        )


appbuilder.add_view_no_menu(ArticlesView())
# appbuilder.add_view(ArticlesView, "Articles")

# Error codes

for errorcode in [
    item
    for elem in [
        [400, 401],
        range(403, 406 + 1, 1),
        range(408, 418 + 1, 1),
        [422, 423, 424, 428, 429, 431, 451],
        range(500, 505, 1),
    ]
    for item in elem
]:
    # https://werkzeug-doc.readthedocs.io/en/latest/exceptions.html

    @appbuilder.app.errorhandler(errorcode)
    def error(error):
        if error.code == 404:
            return (
                render_template(
                    "404.html",
                    base_template=appbuilder.base_template,
                    appbuilder=appbuilder,
                ),
                404,
            )
        else:
            return (
                render_template(
                    "error.html",
                    base_template=appbuilder.base_template,
                    appbuilder=appbuilder,
                    error_code=error.code,
                    error_description=error.description,
                    error_name=error.name,
                ),
                error.code,
            )


db.create_all()
