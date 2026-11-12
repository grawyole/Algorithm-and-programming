// Крок 1: Ввід розмірів та створення матриці
let m = parseInt(prompt("Кількість рядків: "));
let n = parseInt(prompt("Кількість стовпців: "));
let matrytsya = [];

for (let i = 0; i < m; i++) {
    let ryadok_str = prompt("Введіть рядок через пробіл: ");
    let chastyny = ryadok_str.split(" ");
    let chysla_ryadku = [];
    for (let j = 0; j < chastyny.length; j++) {
        chysla_ryadku.push(parseInt(chastyny[j]));
    }
    matrytsya.push(chysla_ryadku);
}
console.log("Наступна дія: обхід матриці та пошук мінімуму, максимуму і суми...");

let zagalna_suma = 0;
let maksimum = matrytsya[0][0];
let minimum = matrytsya[0][0];
let max_i = 0, max_j = 0, min_i = 0, min_j = 0;

for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
        let znachennya = matrytsya[i][j];
        zagalna_suma = zagalna_suma + znachennya;
        
        if (znachennya > maksimum) {
            maksimum = znachennya;
            max_i = i;
            max_j = j;
        }
        if (znachennya < minimum) {
            minimum = znachennya;
            min_i = i;
            min_j = j;
        }
    }
}

console.log("Наступна дія: вивід результатів матриці...");
console.log("Max:", maksimum, max_i, max_j);
console.log("Min:", minimum, min_i, min_j);
console.log("Сума:", zagalna_suma);