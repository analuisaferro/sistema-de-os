from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def os_index(request):
    oss=OrdemDeServico.objects.all()
    context={
        'oss': oss
    }
    return render(request, 'iluminacao/index.html', context)


@login_required
def add_os(request):
    if request.method=='POST':
        form=OS_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_os')
    else:
        form=OS_Form(initial={'tipo': '1'})
    context={
        'form': form
    }
    return render(request, 'iluminacao/adicionar_os.html', context)


def detalhes_os(request, id):
    os=OrdemDeServico.objects.get(id=id)
    if request.method=='POST':        
        pass
    else:
        pass
    context={
        'os': os
    }
    return render(request, 'iluminacao/detalhes_os.html', context)

def funcionarios_listar(request):
    funcionarios=Funcionario.objects.all()
    context={
        'funcionarios': funcionarios
    }
    return render(request, 'equipe/funcionarios.html', context)

def funcionario_cadastrar(request):
    if request.method=='POST':
        form=Funcionario_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')
    else:
        form=Funcionario_Form()
        context={
            'form': form
        }
    return render(request, 'equipe/funcionarios_cadastrar.html', context)

def funcionario_editar(request, id):
    funcionario=Funcionario.objects.get(id=id)
    form=Funcionario_Form(instance=funcionario)
    if request.method=='POST':
        form=Funcionario_Form(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')
    context={
        'form': form,
        'funcionario': funcionario
    }     
    return render(request, 'equipe/funcionarios_editar.html', context)

def funcionario_deletar(request, id):
    funcionario=Funcionario.objects.get(id=id)
    funcionario.delete()

    return redirect('funcionarios')

def atribuir_equipe(request, id):
    try:
        instancia=OS_ext.objects.get(os=id)
        form=Equipe_Form(instance=instancia)        
    except:
        form=Equipe_Form(initial={'os': id})
        instancia=None
        
    if request.method=='POST':
        if instancia:
            form=Equipe_Form(request.POST, instance=instancia)
        else:
            form=Equipe_Form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('detalhes_os', id)
    context={
            'form':form,
        }
    return render(request, 'iluminacao/adicionar_ext.html', context)