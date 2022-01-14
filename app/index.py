from flask_appbuilder import IndexView


class DefaultIndexView(IndexView):
    index_template = 'index.html'
