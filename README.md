<h1><g-emoji class="g-emoji" alias="computer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4bb.png">💻</g-emoji> Gestor_de_Mídia_Back</h1>

<h4><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> Desrcição</h4>
<p align="left">🚀 Aplicação web para gerenciamento de mídias.</p>

<h4><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> Objetivo</h4>
<p align="left">Permitir que os usuários gerenciem e distribuam vídeos no formato .mp4 e fotos de maneira eficiente. A plataforma visa garantir acesso rápido e seguro aos conteúdos, proporcionando uma experiência otimizada e facilitando a manutenção do conteúdo.</p>

<h4><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> Scripts para Configuração Inicial</h4>

Estes passos foram realizados com o editor de código-fonte [VSCode](https://code.visualstudio.com/) no sistema operacional windows.

Certifique-se de estar utilizando versão do <b>Python 3.13</b>, abra o terminal e execute o camando:  <b><i>python --version</i></b>

Caso não tenha o python instalado ou esteja com a versão inferior, baixe a versão correta no<a href="https://www.python.org/downloads/"> site oficial.</a>

Crie um ambiente virtual, no terminal execute o comando: <b><i>python -m venv gestor-midias</i></b>

Ative o ambiente vurtual: <b><i>gestor-midias\Scripts\activate</i></b>

<b>No Windows</b>:  nome_da_venv\Scripts\activate.

Instalar o Django 5.0: <b><i>pip install django==5.0</i></b>

Confirme se foi instalado corretamente: <b><i>python -m django --version</i></b>

Criar um novo projeto: 	<b><i>django-admin startproject gestor_de_midias</i></b>

Este comando criará uma nova pasta chamada <b><i>gestor_de_midias</i></b>, com a seguinte estrutura de diretórios:

    gestor_de_midias/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

<b>Explicação da estrutura:</b>

<ul>
    <li>manage.py:
        <p>Script que ajuda a gerenciar o projeto Django, como rodar o servidor de desenvolvimento,
aplicar migrações, etc.</p></li>
    <li>gestor_de_midias/:
        <p>Diretório com o mesmo nome do projeto, contém a configuração principal do projeto.</p>
    </li>
    <li>settings.py:
        <p>Arquivo de configurações do projeto.</p>
    </li>
    <li>urls.py:
        <p>Arquivo onde você define as URLs do seu projeto.</p>
    </li>
    <li>asgi.py e wsgi.py:
    <p>Arquivos de configuração para deployment (geralmente não usados durante o desenvolvimento local).</p>
    </li>
</ul>

Após já ter criado o projeto, acesse o diretório do mesmo para começar a trabalhar:
<b><i>cd gestor_de_midias</i></b>

Inicie o servidor de desenvolvimento do Django para verificar se o projeto foi criado corretamente:
<b><i>python manage.py runserver</i></b>

Resposta da execução do servidor de desenvolvimento, você verá algo semelhante a:
<b>Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.</b>

Abra o seu navegador e acesse o endereço <b><i>http://127.0.0.1:8000/</i></b>.
Irá abrir a página inicial padrão do Django indicando que o projeto foi criado com sucesso.

Criar o arquivo <b><i>.gitignore</i></b> na raiz do projeto e adicionar as regras para ignorar os arquivos e diretórios que não devem ser versionados no Git.

Instalar o <b><i>Mysql Cli</i></b>, interface de linha de comando usada para interagir com o banco de dados MySQL, acesse o <a href="https://dev.mysql.com/downloads/installer/">site oficial.</a>

Verificar se em variáveis de ambiente de sistemas existe o <b>Path</b>, caminho do mysql, configurado conforme abaixo:
<b>C:\Program Files\MySQL\MySQL Server 8.0\bin</b>

Para acessar o MySQL Cli via terminal, digite o comando:
<b><i>mysql -u root -p</i></b>

O comando acima, irá solicitar as credenciais do usuário root, após estar autenticado, poderá utilizar a interface de linha de comando do MySQL para interagir com o banco de dados.

Verificar a versão do MySQL CLI instalado, execute o comando:
<b><i>mysql --version</i></b>

Ajustar configurações de banco de dados no arquivo <b><i>settings.py</i></b>,
acesse: gestor_de_midias\settings.py e insira os parâmetros de acordo com explicações abaixo:

<b>Explicação dos parâmetros:</b>

'ENGINE': O backend do banco de dados, para MySQL é 'django.db.backends.mysql'.
'NAME': O nome do banco de dados que você deseja usar.
'USER': O nome do usuário do MySQL que tem permissões para acessar o banco de dados.
'PASSWORD': A senha do usuário MySQL.
'HOST': O endereço do servidor MySQL. Para bancos de dados locais, use 'localhost'.
'PORT': A porta do servidor MySQL. A porta padrão é 3306.

<b>Dependências do MySQL:</b>
Certifique-se de que o Django já tenha a biblioteca do MySQL instalada.
Biblioteca recomendada para conectar Django ao MySQL:
<b><i>pip install mysqlclient</i></b>

Para gerar o arquivo <b>requirements.txt</b> com as dependências do projeto python, listando todos os pacotes instalados no ambiente, execute o comando:
<b><i>pip freeze > requirements.txt</i></b>

Caso queira instalar as dependências listadas no arquivo <b>requirements.txt</b>, execute o comando:
<b><i>pip install -r requirements.txt</i></b>


Docker
Docker compose
Entrypoint


Configurar pre-commit com isort e flake8 e instalar django rest e garantir que o requirements.txt seja atualizado sempre que uma nova dependência for instalada, além de configurar o pre-commit para rodar sempre que for feito um commit.

Para instalar as dependências, execute o comando:
<b><i>pip install pre-commit isort flake8 django djangorestframework</i></b>

pre-commit (rodar os hooks de commit).
isort (organizar importações).
flake8 (linting do código).
django (construção de aplicações web em Python).
djangorestframework (construir APIs da Web no Django).

Para configurar o pre-commit é necessário criar o arquivo <b>.pre-commit-config.yaml</b> na raiz do projeto.

Instalar os hooks do pre-commit
<b><i>pre-commit install</i></b>

Resposta após executar comando acima:
<b>pre-commit installed at .git\hooks\pre-commit</b>

Significa que, sempre que você tentar realizar um commit, o pre-commit executará os hooks de verificação configurados antes do commit ser efetivamente realizado, ajudando a garantir que seu código siga certos padrões de qualidade ou boas práticas (por exemplo, formatação, executar testes automatizados, lintar o código para garantir que ele siga padrões de estilo, análise de código, etc.).

Testando a configuração
Sempre que for realizado um commit, o pre-commit vai rodar os hooks do isort e do flake8 nos arquivos modificados. Se algum problema for encontrado, o commit será interrompido até que o problema seja resolvido.

Após instalações realizadas acima, atualizar o <b>requirements.txt</b> executando o comando abaixo:
<b><i>pip freeze > requirements.txt</i></b>

irá atualizar a lista de dependências de pacotes instalados no ambiente.

Configurar o Django Rest Framework no projeto:

No arquivo <b>settings.py</b>, adicione à lista de <b>INSTALLED_APPS:</b>

<b>'rest_framework',</b>

Criação de um novo app do Django:

Necessário abrir o <b>Docker Descktop</b>, executar o comando para criação do app via shell.
No VSCode, clicar em Docker, Containers e selecionar o projeto atual, com botão direito, selecione <b>Compose Start</b>, após projeto web e banco de dados ficarem ativos, clicar com o botão direito em seu projeto web e selecionar <b>Atach Shell</b>, irá abrir o terminal do shell conforme abaixo:
<b>* Executing task: Docker exec -it número do seu container sh</b>
	# <b><i>python manage.py startapp midias</i></b>

O comando irá criar uma nova aplicação dentro do projeto Django, poderá ser observado a pasta <b>mídias</b> na mesma estrutura do app <b>gestor_de_midias</b>, organizando o código em módulos lógicos. Agora, poderá começar a definir modelos, rotas, views e outros componentes específicos da funcionalidade.

Após definir a <b>models.py</b>, com a definição das tabelas que serão criadas, é necessário garantir que as tabelas e a estrutura do banco de dados sejam criadas.

Aplicar as migrações do banco de dados
<b><i>python manage.py migrate</i></b>

Crie um superusuário para acessar o painel de administração do Django:
<b><i>python manage.py createsuperuser</i></b>

Será solicitado na criação do super usuário:
usuário = seu nome,
email = seu email,
senha = sua senha

Acesse o Django Admin no navegador com o link abaixo:
<b><i>http://localhost:8000/admin/</i></b>

Será solicitado o login e a senha do superusuário criado acima.

<h4><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> Tecnologias Utilizadas</h2>

<a href="https://www.python.org/">🔗 Python</a>
<a href="https://docs.djangoproject.com/en/5.0/ref/contrib/admin/">🔗 Django admin</a>
<a href="https://www.django-rest-framework.org/">🔗 Django rest-framerok</a>
<a href="https://pypi.org/project/mysqlclient/">🔗 Mysqlclient </a>
<a href="https://github.com/PyCQA/flake8">🔗 Flake8</a>
<a href="https://github.com/PyCQA/autoflake">🔗 Autoflake</a>
<a href="https://github.com/pre-commit/pre-commit-hooks">🔗 Pre-commit-hooks</a>
<a href="https://github.com/asottile/pyupgrade">🔗 Pyupgrade</a>
<a href="https://github.com/pycqa/isort">🔗 Isort</a>

<h4><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> Status</h4>
<h4 align="center">
	🚧  Projeto  🚀 Em construção...  🚧
</h4>

<h4><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> Autor</h4>
<p>Feito por Fábio Cavadas. <g-emoji class="g-emoji" alias="wave" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f44b.png">👋</g-emoji></p>

[![Linkedin Badge](https://img.shields.io/badge/-in_Fábio_Cavadas-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/fábiocavadas/)](https://www.linkedin.com/in/fábiocavadas/)
[![Gmail Badge](https://img.shields.io/badge/-fabiocfferreira@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:fabiocfferreira@gmail.com)](mailto:fabiocfferreira@gmail.com)

<h4><g-emoji class="g-emoji" alias="memo" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png">📝</g-emoji> Licença</h2>
<p>Este projeto esta sobe a licença MIT.</p>
