Feature: Carrinho de compras

    Como usario
    Eu quero adicionar e remover itens do meu carrinho de compras
    Para gerenciar minhas compras

Scenario: Adicionar itens ao carrinho
    Given que tenho um carrinho de compras com o item "Camiseta" e preco R$ 29.99
    When eu adiciono o item "Calca" com o preco R$ 49.99
    Then o total do carrinho de compras deve ser R$ 79.98

Scenario: Remover itens do carrinho
    Given que tenho um carrinho de compras com o item "Camiseta" e preco R$ 29.99
    When eu removo o item do carrinho
    Then o carrinho de compras deve estar vazio