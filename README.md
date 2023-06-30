# :construction: README em construção ! :construction:
A aplicação conta com as seguintes funcionalidades:

Testes de classes: Foram implementados testes para as classes Ingredient e Dish, garantindo que elas possam ser corretamente instanciadas, que seus métodos funcionem adequadamente (como repr, eq e hash), e que suas funcionalidades, como adicionar dependências de ingredientes e obter restrições, estejam corretas.

Mapeamento de pratos e ingredientes: A classe MenuData realiza a leitura de um arquivo CSV que contém informações sobre os pratos do cardápio, seus ingredientes e quantidades necessárias. Com base nesse arquivo, a classe realiza o mapeamento adequado dos pratos e ingredientes, criando as instâncias correspondentes.

Geração de cardápios: A classe MenuBuilder possui o método get_main_menu, responsável por gerar os cardápios. Esse método pode receber uma restrição alimentar como parâmetro, e retorna uma lista de dicionários contendo informações sobre os pratos disponíveis no cardápio, como nome, ingredientes, preço e restrições. Além disso, o método leva em consideração a disponibilidade dos ingredientes em estoque para gerar um cardápio atualizado.

Controle de estoque: A classe InventoryMapping é responsável por controlar o estoque de ingredientes. Ela possui métodos como check_recipe_availability, que verifica se uma receita está disponível para consumo com base nos ingredientes em estoque, e consume_recipe, que consome os ingredientes utilizados na receita do estoque, desde que estejam disponíveis. Isso garante que apenas pratos com ingredientes disponíveis possam ser incluídos no cardápio gerado.

Em resumo, a aplicação realiza testes, mapeia pratos e ingredientes, controla o estoque de ingredientes e gera cardápios dinâmicos levando em consideração as restrições alimentares dos clientes e a disponibilidade de ingredientes em estoque.

<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
