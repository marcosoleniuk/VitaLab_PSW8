# VitaLab_PSW8
Aplicação de um laboratório de exames do intessivão em python + django da Pythonando

## 🔗 Link live do projeto:
https://intensivopythondjango.moleniuk.com/

## Pré-requisitos
## 1. Primeiro devemos criar o ambiente virtual:

Linux
```sh
python3 -m venv venv
```

Windows
```sh
python -m venv venv
```

## 2. Após a criação do venv vamos ativa-lo:
Linux
```sh
source venv/bin/activate
```

Windows
```sh
venv\Scripts\Activate
```

## Caso algum comando retorne um erro de permissão no VSCode execute o código e tente novamente:
```sh
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## 3. Agora vamos fazer a instalação das dependências das bibliotecas:
Linux
```sh
pip3 install -r requirements.txt
```

Windows
```sh
pip install -r requirements.txt
```

Criar usuário Admin 
```sh
python manage.py createsuperuser
```

## 4. Agora é só iniciar rodando o seguinte comando
Linux
```sh
python3 manage.py runserver
```

Windows
```sh
python manage.py runserver
```
Login e Cadastro de Usuário
```sh
http://127.0.0.1:8000
```
Área de administração
```sh
http://127.0.0.1:8000/admin
```




