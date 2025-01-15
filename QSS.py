QSS = '''
QWidget#mainWindow {
    background-color: #bca6ff;  /* Задаємо фон для головного вікна */
}

QWidget {
    font: 20px "Montserrat";  /* Встановлюємо шрифт для всіх віджетів */
}

QPushButton { 
    background-color: #734077;  /* Задаємо фон для кнопки */
    color: white;  /* Колір тексту на кнопці */
}

QPushButton:pressed {
    background-color: #9e93fc;  /* Задаємо фон кнопки, коли вона натиснута */
}

QListWidget {
    background-color: #ffffff;  /* Задаємо фон для списку */
}

QListWidget::item:selected {
    background-color: #d9ffee;  /* Задаємо фон для вибраного елемента списку */
}
'''