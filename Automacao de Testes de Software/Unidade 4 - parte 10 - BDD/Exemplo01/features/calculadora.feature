Feature: Calculadora
    Como aluno de automação de testes de software
    Eu quero escrever um exemplo usando pytest-bdd
    Com um exemplo de soma entre dois numeros

Scenario: Soma dois numeros
    Given eu tenho o numero 2 como entrada para a calculadora
    And eu tambem tenho o numero 7 como entrada para a calculadora
    When eu solicito que realize a soma
    Then o resultado deve ser 9