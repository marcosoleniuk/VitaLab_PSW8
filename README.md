## VitaLab_PSW8
Aplicação de um laboratório de exames do intessivão em python + django da Pythonando

# Pré-requisitos
# Primeiro devemos criar o ambiente virtual:

Linux
python3 -m venv venv

Windows
python -m venv venv

# Após a criação do venv vamos ativa-lo:
Linux
source venv/bin/activate

Windows
venv\Scripts\Activate

## Caso algum comando retorne um erro de permissão execute o código e tente novamente:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Agora vamos fazer a instalação das dependências das bibliotecas:
Linux
pip3 install -r requirements.txt

Windows
pip install -r requirements.txt

# Agora é só iniciar rodando o seguinte comando
Linux
python3 manage.py runserver

Windows
python manage.py runserver



