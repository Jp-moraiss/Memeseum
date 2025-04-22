from django.shortcuts import render, get_object_or_404, redirect
from .models import Meme

def home(request):
    return render(request, 'index.html')

def add(request):

    if request.method =='POST':
        nomeMeme = request.POST.get('name')
        descricaoMeme = request.POST.get('descricao')
        anoMeme = request.POST.get('ano')

        meme = Meme(
            nome = nomeMeme,
            descricao = descricaoMeme,
            ano = anoMeme
        )

        meme.save()

    return render(request, 'add.html')

def visualizar(request):
    
    memes = Meme.objects.all()

    context = {
        'memes': memes
    }
    
    return render(request, 'visualizar.html', context)

def deletar (request, id):
    meme = get_object_or_404(Meme, id=id)
    meme.delete()

    return redirect ('visualizar')

def editar(request, id):
    meme = Meme.objects.filter(id=id).first()

    if request.method == 'POST':
        if meme:  # Certifica-se de que o meme existe
            meme.nome = request.POST.get('name')
            meme.descricao = request.POST.get('descricao')
            meme.ano = request.POST.get('ano')
            meme.save()
        return redirect('visualizar')  # Evita recarregar a página errada

    context = {'meme': meme}
    return render(request, 'add.html', context)
