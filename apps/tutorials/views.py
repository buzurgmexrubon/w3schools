from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
# from apps.tutorials.models import Tutorial
# import markdown


# def tutorial_list(request):
#     tutorials = Tutorial.objects.all()
#     return render(request, 'tutorial_list.html', {'tutorials': tutorials})


# def tutorial_detail(request, slug):
#     tutorial = get_object_or_404(Tutorial, slug=slug)
#     content = markdown.markdown(tutorial.content)
#     return render(request, 'tutorial_detail.html', {'tutorial': tutorial, 'content': content})
