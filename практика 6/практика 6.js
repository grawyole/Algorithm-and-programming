// Крок 1: Ввід і підготовка
let n = parseInt(prompt());
let suma = 0;
let dobutok = 1;
console.log("Наступна дія: запуск циклу while для обробки цифр...");

// Крок 2: Цикл
while (n > 0) {
    let tsyfra = n % 10;
    suma = suma + tsyfra;
    dobutok = dobutok * tsyfra;
    n = Math.trunc(n / 10);
    console.log("Дія в циклі: чергова цифра оброблена, наступна дія циклу...");
}

console.log("Сума:", suma);
console.log("Добуток:", dobutok);