Outdoor Planner API
Descrição
A Outdoor Planner API é uma API que sugere os melhores horários e dias para praticar atividades ao ar livre, como corrida, ciclismo e trilha, com base nas condições climáticas de uma determinada cidade. A API utiliza dados da OpenWeather para obter informações sobre o clima e a OpenAI para fornecer recomendações personalizadas com base nas preferências do usuário.

Funcionalidades:
Autenticação de usuário com JWT.

Cadastro e listagem de atividades ao ar livre.

Registro e atualização das preferências do usuário (atividades favoritas e preferências climáticas).

Exibição de previsões meteorológicas.

Sugestões personalizadas de atividades com base no clima e nas preferências do usuário.

Tecnologias Usadas
Django: Framework web para Python.

Django Rest Framework (DRF): Para construção da API.

SimpleJWT: Para autenticação baseada em JSON Web Tokens (JWT).

OpenWeather API: Para obter dados de previsão do tempo.

OpenAI API: Para gerar recomendações personalizadas.

Estrutura do Projeto
bash
Copiar
Editar
outdoor_planner/
│── outdoor_planner/         # Configurações do Django
│── activities_api/          # App principal com a lógica da API
│   │── models.py            # Modelos do banco de dados
│   │── serializers.py       # Serializadores do DRF
│   │── views.py             # Lógica das requisições
│   │── urls.py              # Rotas da API
│── requirements.txt         # Dependências do projeto
│── manage.py                # Comando para rodar o Django
Instalação
Clone o repositório

bash
Copiar
Editar
git clone https://github.com/seu-usuario/outdoor-planner.git
cd outdoor-planner
Crie um ambiente virtual (opcional, mas recomendado)

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências

bash
Copiar
Editar
pip install -r requirements.txt
Configuração do banco de dados O projeto usa o banco de dados padrão do Django, SQLite. Caso queira configurar outro banco de dados, altere as configurações no settings.py.

Para rodar as migrações:

bash
Copiar
Editar
python manage.py migrate
Rodar o servidor

bash
Copiar
Editar
python manage.py runserver
A API estará acessível em http://127.0.0.1:8000/.

Endpoints
1. Autenticação JWT
POST /api/token/: Obtém o token JWT.

Requisição:

json
Copiar
Editar
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
Resposta:

json
Copiar
Editar
{
  "access": "seu_token_de_acesso",
  "refresh": "seu_token_de_atualizacao"
}
2. Atividades
GET /api/activities/: Lista todas as atividades disponíveis.

POST /api/activities/: Cria uma nova atividade.

3. Preferências do Usuário
GET /api/user/preferences/: Exibe as preferências do usuário logado.

POST /api/user/preferences/: Cria ou atualiza as preferências do usuário.

4. Previsão do Tempo
GET /api/weather/: Exibe as previsões de tempo armazenadas no banco.

Requisitos
Python 3.x

Django 3.x ou superior

Django Rest Framework

SimpleJWT

OpenWeather API Key (opcional para previsão do tempo real)

OpenAI API Key (opcional para recomendações personalizadas)

Configuração de API Keys
Você pode configurar as chaves de API da OpenWeather e OpenAI nas variáveis de ambiente ou diretamente no código.

OpenWeather API: Registre-se em OpenWeather e obtenha uma chave de API.

OpenAI API: Registre-se em OpenAI e obtenha uma chave de API.

Contribuindo
Faça um fork deste repositório.

Crie uma branch para a sua feature (git checkout -b feature-nome).

Faça commit das suas mudanças (git commit -m 'Adicionando nova feature').

Envie para o repositório remoto (git push origin feature-nome).

Abra um pull request.

