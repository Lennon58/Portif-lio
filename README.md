# Portif-lio
Portifólio para estágio
Este projeto consiste em um site para uma loja de roupas, atualmente em fase de desenvolvimento. Utilizando a linguagem de programação Python no backend, o framework escolhido para a implementação foi o Django.

Estrutura do Projeto:

Telas:

°Index: A tela principal do site, contendo seções como cabeçalho, campo de produtos e rodapé. O cabeçalho oferece navegação para todas as partes do site, enquanto o campo de produtos proporciona uma visualização dos produtos disponíveis. O rodapé inclui áreas para enviar comentários e informações de contato.

°Cadastro: Nesta tela, os usuários são solicitados a fornecer informações como nome, e-mail e senha. Após inserir os dados, ao clicar em "Cadastre-se", os usuários são redirecionados para a tela inicial (index) e suas informações são armazenadas no banco de dados.

°Login: Os usuários podem entrar com suas informações cadastrais nesta tela e serão redirecionados para a tela de login logo após a autenticação bem-sucedida.

Backend:

°Foi utilizado o framework Django para criar funções de registro no banco de dados. Os cadastros de usuários realizados no site são armazenados de forma segura.

Instalação do Projeto:
Para executar este projeto, é necessário instalar o framework Django. Siga os passos abaixo:

Baixe o Django:

Acesse o link https://www.djangoproject.com/download/ para baixar a versão mais recente do Django.

Instalação via Comando:

Abra o terminal ou prompt de comando.
Navegue até o diretório do projeto.
Execute o seguinte comando para instalar o Django: pip install django

Migrações e Criação do Banco de Dados:

Após instalar o Django, execute os seguintes comandos para aplicar as migrações e criar o banco de dados:python manage.py makemigrations
python manage.py migrate

Execução do Servidor:

Inicie o servidor Django com o comando:python manage.py runserver

Acesso ao Site:

Abra o navegador e acesse http://localhost:8000/ para visualizar o site.
