// Крок 1: Ввід числа
let n = parseInt(prompt());
console.log("Наступна дія: витягуємо кожну цифру по черзі...");

// Крок 2: Розбиваємо на цифри
let edynytsi = n % 10;
let desyatky = (Math.trunc(n / 10)) % 10;
let sotni = (Math.trunc(n / 100)) % 10;
let tysyachi = Math.trunc(n / 1000);

console.log("Наступна дія: збираємо число у зворотному порядку...");
let obratno = (edynytsi * 1000) + (desyatky * 100) + (sotni * 10) + tysyachi;
console.log(obratno);