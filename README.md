## VitaLab_PSW8
Aplicação de um laboratório de exames do intessivão em python + django da Pythonando

# Pré-requisitos
# Primeiro devemos criar o ambiente virtual:

Linux
```sh
python3 -m venv venv
```

Windows
```sh
python -m venv venv
```

# Após a criação do venv vamos ativa-lo:
Linux
```sh
source venv/bin/activate
```

Windows
```sh
venv\Scripts\Activate
```

## Caso algum comando retorne um erro de permissão execute o código e tente novamente:
```sh
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

# Agora vamos fazer a instalação das dependências das bibliotecas:
Linux
```sh
pip3 install -r requirements.txt
```

Windows
```sh
pip install -r requirements.txt
```

# Agora é só iniciar rodando o seguinte comando
Linux
```sh
python3 manage.py runserver
```

Windows
```sh
python manage.py runserver
```



