function tableCreat(word1, word2){
    const table = document.createElement('table');
    let tr = document.createElement('tr');
    let td1 = document.createElement('td');
    td1.innerHTML = `${word1}`;
    let td2 = document.createElement('td');
    td2.innerHTML = `${word2}`;

    tr.appendChild(td1);
    tr.appendChild(td2);
    table.appendChild(tr);
    document.getElementById('divTable').appendChild(table);
}

tableCreat('<h4>Начало-Конец</h4>', '<h4>Название дисциплины</h4>')
tableCreat('8:00 - 9:35', 'Базы данных')
tableCreat('9:45 - 11:20', 'Методы вычислений')
tableCreat('11:45 - 13:20', 'Введение в машинное обучение')
tableCreat('13:30 - 15:05', 'Структуры и алгоритмы обработки данных')