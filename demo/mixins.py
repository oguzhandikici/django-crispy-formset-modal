import inspect

import markdown
from extra_views import SuccessMessageMixin


class DemoViewMixin(SuccessMessageMixin):
    title = ""
    success_message = "Record successfully created!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["class_name"] = self.__class__.__name__
        context["docstring"] = self.get_docstring()
        context["title"] = self.title
        return context

    def get_docstring(self):
        docstring = inspect.getdoc(self.__class__)
        if docstring is not None:
            return markdown.markdown(docstring, extensions=["extra"])
        else:
            return ""
