// objetos - objetos possuem funcionalidades ou métodos

console.log({
    name: "Stefany",
    idade: 27,
    andar: function(){
        console.log('andar')
    }
})

// Array é uma lista ou agrupamento de dados

console.log([
    "Leite",
    "Ovos",
    2 
])

//podemos criar uma VARIAVEL com var, let e const. let e var são muito parecidos, mas let tem escopo local e var escopo global. const não pode ser mudado e também é local

var clima = "Quente"
clima = "Frio"
console.log(clima)

let clima1 = "Frio"
clima1 = "Quente"
console.log(clima1)

const clima2 = "Tropical"
console.log(clima2)

//bloco
var x = 0

console.log("Existe x antes do bloco?", x)


{
    let x = 1
    console.log("Existe x dentro do bloco?", x)
}

console.log("Existe x depois do bloco?", x)

// Variáveis e tipos de dados
// declaração ou declaration

var name

// assignment ou atribuição de valor

name = "stefany"

// que tipo de dado foi colocado na variável

console.log(typeof name)

//agrupamento de declarações

//let age = 27
//let isHuman = true

let age, isHuman
age = 27
isHuman = true

// multiplos argumentos na função
console.log(name, age, isHuman)
//concatenando os valores
console.log("A " + name + " tem " + age + " anos.")
//interpolando valores com template literals ou template strings
console.log(`A ${name} tem ${age} anos.`)

//Object

const person = {
    name: 'John',
    age: 30,
    weight: 88.6,
    isAdmin: true
}

console.log(person.name)
console.log(person.weight)
console.log(`${person.name} tem ${person.age} anos e pesa ${person.weight} kg`)

//Arrays

const animals = [
    'Lion',
    'Monkey',
    {
        species: 'cat',
        ageOfCat: 3
    }

]

// acessar valores dentro do array

console.log(animals[0])
console.log(animals.length)
console.log(animals[2].species)



