# superlogica-case

O projeto em questão deve apresentar: 

    - Um sistema de login social com google como provedor e permitir o acesso com as mesmas credenciais ao django admin.

    - Uma opção de conversão de planilha como combinado no documento do case para a vaga
        Obs: só terá acesso ao conversor caso estiver logado


O projeto ao fazer o login social, permite acessar o administrador do django com as mesmas credenciais e salva os dados como um usuário do admin do Django com a tag de Staff ativa.
Caso faça o logout, será efetuado em ambas as páginas (home e admin).

Para o login social foi utilizada a biblioteca django-allauth onde é possível efetuar a autenticação social com vários provedores, além de ter um endpoint para gestão das contas.


Atualmente possuem duas formas de executar o projeto:

    1 - Utilizando o Docker:
        
        Necessário ter o Docker instalado na maquina Linux

        Comandos:
            
            Buildar e executar o container no docker:
            - sudo docker-compose up --build

            Rodar as migrações (caso necessário):
            - sudo docker-compose exec web python manage.py migrate
            

    2 - Sem conteinerização, utilizando somente um ambiente virtual:
        
        Necessário comentar a variavel DATABASES no settings.py (linha 94 a 103) e descomentar as linhas 105 a 110.
        Assim o banco de dados não será em postgres e não haverá container para a plicação e nem para o banco de dados. O banco será um arquivo do tipo sqlite3.

        Comandos:

            Criação do ambiente virtual:
            - python3 -m venv .venv

            Ativação do ambiente:
            - source .venv/bin/activate
            
            Instalação dos pacotes necessários:
            - pip install -r requirements.txt
                
            Rodar as migrações Necessário estar dentro do diretório app:
            - python3 manage.py migrate
    
            Rodar o projeto Django (Necessário estar dentro do diretório app):
            - python3 manage.py runserver



Para ter total acesso ao admin do Django como superuser é necessario criar um através do comando:

    Para o projeto com o Docker:
        - sudo docker-compose exec web python3 manage.py createsuperuser
    Para o projeto sem o Docker (necessário estar dentro do ambiente virtual e dentro do diretório app:
        - python3 manage.py createsuperuser
            
        
