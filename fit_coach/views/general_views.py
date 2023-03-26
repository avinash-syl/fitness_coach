from django.shortcuts import render


class homepage_view():
    def homepage(request):
        return render(request, 'index.html')


class in_progress_view():
    def in_progress(request):
        return render(request, 'in_progress.html')


class user_details():
    pass
