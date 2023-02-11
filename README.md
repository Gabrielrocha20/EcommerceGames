# Este projeto e sobre uma Api de um Ecommerce pra jogos
foi criado somente o back end em django

# No terminal
python -m venv venv<br>
venv/Scripts/activate<br>
para instalar todas as dependencias<br>
pip install -r requirements.txt<br>

crie um banco de dados postgre e depois use este codigo<br>
python manage.py migrate<br>
python manage.py loaddata data1.json<br>
<br>
Pronto agora voce injetou os dados no seu banco de dados e esta pronto para testar a API<br>
Agora crie um Super User<br>
<br>
python manage.py createsuperuser<br>



# Url Produto
--Get<br>
http://127.0.0.1:8000/produto/api/v1/   <br>
http://127.0.0.1:8000/produto/api/v1/pk/   <br>
http://127.0.0.1:8000/produto/api/v1/variacao/pk/   <br>
   <br>
--Post   <br>
http://127.0.0.1:8000/produto/api/v1/register/   <br>
http://127.0.0.1:8000/produto/api/v1/register/variacao/pk/   <br>
   <br>
--Delete   <br>
http://127.0.0.1:8000/produto/api/v1/delete/variacoes/pk/   <br>
http://127.0.0.1:8000/produto/api/v1/{url}delete/pk/   <br>
   <br>
--Put   <br>
http://127.0.0.1:8000/produto/api/v1/update/variacoes/pk/   <br>
http://127.0.0.1:8000/produto/api/v1/update/pk/   <br>
<br>
Na Api de produto e possivel listar todos os produtos registrados, um unico produto, ou a variação do produto <br>
Ao registrar o produto o usuario deve ser redirecionado para registrar a variação deste produto<br>
e possivel tambem Atualizar o produto ou sua variação, e deletar tambem,sabendo que se deletar o produto deleta suas varaiçoes tambem<br>
mas se deletar a variação  nao deleta o produto.<br>
<br>
o registro de variação e do produto so pode ser feito pelo Adm do site
para ver os produtos tem que estar logado no site


# Url dos Pedidos
--Get<br>
http://127.0.0.1:8000/pedido/api/v1/pk/   <br>
http://127.0.0.1:8000/pedido/api/v1/item/pk/   <br>
   <br>
--Post   <br>
http://127.0.0.1:8000/pedido/api/v1/salvar/   <br>
http://127.0.0.1:8000/pedido/api/v1/pk/pagar   <br>
<br>
Na Api dos pedidos <br>
Para salvar os items do carrinho o fronte pode salvar na Session ou Localstorage<br>
e quando o usuario for fazer os pedidos o frontend envia as informaçoes de cada item salvo<br>

para termina a compra e preciso acessar a api de pagar e ela retornara os dados de subtotal, frete e total

# Url do Perfil
--Post   <br>
<br>
TOKENS
  http://127.0.0.1:8000/perfil/api/v1/token/   <br>
  http://127.0.0.1:8000/perfil/api/v1/token/refresh/   <br>
  http://127.0.0.1:8000/perfil/api/v1/token/verify/   <br>
<br>
http://127.0.0.1:8000/perfil/api/v1/login/   <br>
http://127.0.0.1:8000/perfil/api/v1/logout/   <br>
http://127.0.0.1:8000/perfil/api/v1/register/ <br>
http://127.0.0.1:8000/perfil/api/v1/register/perfil/pk  <br>

--Put<br>
http://127.0.0.1:8000/perfil/api/v1/update/perfil/pk   <br>
<br>
A Api do perfil serve para logar e deslogar o usuario, registrar o usuario, registrar o perfil do usuario e atualizar o perfil do usuario


