from django.shortcuts import redirect

#Redirecionar para a tela de login ou cadastro
def redirecionar_login(request):
    return redirect("usuarios/login")
