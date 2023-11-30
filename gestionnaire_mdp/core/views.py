from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            return redirect('page_vierge')
        return response


def page_vierge(request):
    return render(request, 'page_vierge.html')
