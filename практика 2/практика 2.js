//Збираємо числа
let a = parseInt(prompt());
let b = parseInt(prompt());
let c = parseInt(prompt());

let naybilshe;

//Перевірка
if (a >= b && a >= c) {
    naybilshe = a;
} else {
    if (b >= a && b >= c) {
        naybilshe = b;
    } else {
        naybilshe = c;
    }
}

console.log("Найбільше:", naybilshe);