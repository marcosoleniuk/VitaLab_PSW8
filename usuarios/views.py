from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Cpf


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        primeiro_nome = request.POST.get("primeiro_nome")
        ultimo_nome = request.POST.get("ultimo_nome")
        cpf = request.POST.get("cpf")
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if (
            User.objects.filter(username=username).exists()
            or User.objects.filter(email=email).exists()
        ):
            messages.add_message(
                request,
                constants.ERROR,
                "Este nome de usuário ou email já está em uso.",
            )
            return redirect("/usuarios/cadastro")

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não são iguais!")
            return redirect("/usuarios/cadastro")
        if len(senha) < 6:
            messages.add_message(
                request, constants.ERROR, "A senha deve ter pelo menos 6 caracteres"
            )
            return redirect("/usuarios/cadastro")

        try:
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
            Cpf.objects.create(user=user, cpf=cpf)

            messages.add_message(
                request, constants.SUCCESS, "Usuário cadastrado com sucesso!!"
            )
        except:
            messages.add_message(
                request,
                constants.ERROR,
                "Erro interno do sistema, contate um Administrador",
            )
            return redirect("/usuarios/cadastro")

        return redirect("/usuarios/login")


def logar(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect("/exames/solicitar_exames")
        else:
            messages.add_message(request, constants.ERROR, "Usuário ou senha inválidos")
            return redirect("/usuarios/login")

    return redirect("/usuarios/login")
