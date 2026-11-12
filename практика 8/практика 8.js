// Крок 1: Ввід та розбиття на масив
let tekst = prompt();
let elementy = tekst.split(" ");
let spysok = [];
for (let i = 0; i < elementy.length; i++) {
    spysok.push(parseInt(elementy[i]));
}
console.log("Наступна дія: послідовний підрахунок суми, кількості та добутку...");

// Крок 2: Підрахунки
let suma = 0;
for (let i = 0; i < spysok.length; i++) {
    suma = suma + spysok[i];
}

let kilkist = 0;
for (let i = 0; i < spysok.length; i++) {
    kilkist = kilkist + 1;
}

let dobutok = 1;
for (let i = 0; i < spysok.length; i++) {
    dobutok = dobutok * spysok[i];
}

let serednye = suma / kilkist;
console.log("Наступна дія: вивід фінішних даних...");
console.log(suma, dobutok, kilkist, serednye);