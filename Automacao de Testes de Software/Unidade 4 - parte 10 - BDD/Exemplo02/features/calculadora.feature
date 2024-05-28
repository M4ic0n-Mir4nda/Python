Scenario Outline: Soma dois numeros
        Given Eu entro um numero <num1> na calculadora
        And Eu tambem entro com o valor <num2> na calculadora
        When Eu solicito para realizar a soma.
        Then Entao a soma deve ser <resultado>

        Examples:
            |   num1|   num2|   resultado|
            |      5|      2|           7|
            |      4|      8|          12|
            |    100|    200|         300|