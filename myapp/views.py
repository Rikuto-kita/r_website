from django.shortcuts import render
from django.views.generic import TemplateView


# TemplateViewをもとにclass作成
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self):
        ctxt =  super().get_context_data()
        ctxt["username"] = "kita"
        return ctxt


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        ctxt =  super().get_context_data()
        ctxt["num_services"] = 12345
        ctxt["skills"] = [
            "python",
            "java",
            "ruby"
        ]
        return ctxt