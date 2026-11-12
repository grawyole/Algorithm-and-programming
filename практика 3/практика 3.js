// Крок 1: Ввід
let a = parseInt(prompt());
let b = parseInt(prompt());
console.log("Наступна дія: по черзі виконуємо арифметичні операції...");

// Крок 2: Арифметика по порядку
console.log("Сума:", a + b);
console.log("Різниця:", a - b);
console.log("Добуток:", a * b);
console.log("Ділення:", a / b);
console.log("Ціла частина:", Math.trunc(a / b));
console.log("Залишок:", a % b);