from django.views.generic import View
from django.shortcuts import render

class Teste(View):
    def get(self, request, *args, **kwargs):
        return render(request, "base.html")