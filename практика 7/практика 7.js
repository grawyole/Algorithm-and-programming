// Крок 1: Ввід рядка
let s = prompt();
let dovzhyna = s.length;
let pershyy = s[0];
let ostanniy = s[dovzhyna - 1];
console.log("Наступна дія: запуск циклу для розвороту рядка...");

let zvorotniy = "";
let i = dovzhyna - 1;
while (i >= 0) {
    zvorotniy = zvorotniy + s[i];
    i = i - 1;
}

console.log("Наступна дія: вивід результатів...");
console.log(dovzhyna, pershyy, ostanniy, zvorotniy);