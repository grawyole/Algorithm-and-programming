// Крок 1: Ввід
let a = parseInt(prompt());
let b = parseInt(prompt());
let c = parseInt(prompt());
console.log("Наступна дія: пошук максимуму...");

let naybolshe = a;
if (b > naybolshe) {
    naybolshe = b;
}
if (c > naybolshe) {
    naybolshe = c;
}

console.log("Наступна дія: вивід найбільшого числа...");
console.log(naybolshe);