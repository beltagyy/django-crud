from django.shortcuts import render
from django.http import HttpResponse
from score.models import Score
from score.forms import ScoreForm

def index(request):
    context = {}
    form = ScoreForm()
    scores = Score.objects.all()
    context['scores'] = scores
    context['title'] = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = ScoreForm(request.POST)
            else:
                score = Score.objects.get(id=pk)
                form = ScoreForm(request.POST, instance=score)
            form.save()
            form = ScoreForm()
        elif 'edit' in request.POST:
            id = request.POST.get('edit')
            score = Score.objects.get(pk=id)
            form = ScoreForm(instance=score)
            context['form'] = form
            context['edit'] = True
            context['id'] = id
        elif 'delete' in request.POST:
            id = request.POST.get('delete')
            score = Score.objects.get(pk=id)
            score.delete()
        
    context['form'] = form
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    context['title'] = 'Contact'
    return render(request, 'contact.html', context)

def add(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved')
    else:
        form = ScoreForm()
    return render(request, 'add.html', {'form': form})