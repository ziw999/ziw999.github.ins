from django.shortcuts import render

from .models import Index, Accord, About, Carousel



def index(request):
    form = Index.objects.order_by('-id')[:6]
    accord = Accord.objects.order_by('-id')

    context = {
        'title': 'Страховая компания',
        'form': form,
        'accord': accord
    }

    return render(request, 'blog/index.html', context)


def about(request):
    carousel = Carousel.objects.all()
    forms = About.objects.order_by('-id')

    context = {
        'title': 'О нас',
        'forms': forms,
        'carousel': carousel,
    }

    return render(request, 'blog/about.html', context)



