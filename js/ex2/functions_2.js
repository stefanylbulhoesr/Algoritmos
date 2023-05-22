// podemos criar funções dentro de variáveis - function expression ou function anonymous
// parâmetros da função

const sum = function(number1,number2) {
    let total = number1 + number2
    return total
}

let number1 = 34
let number2 = 25
sum(number1, number2)
sum(2,3) //arguments - argumentos
sum(56,456789)

console.log(`o número 1 é ${number1}`)
console.log(`o número 2 é ${number2}`)
console.log(`a soma é ${sum(number1, number2)}`)

