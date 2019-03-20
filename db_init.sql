DROP TABLE meals;
DROP TABLE cart;
DROP TABLE info_meals;

CREATE TABLE IF NOT EXISTS meals (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    meal TEXT NOT NULL ,
    amount REAL NOT NULL,
    price REAL NOT NULL,
    categorie TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS info_meals (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    meal_id INTEGER NOT NULL,
    callories REAL NOT NULL,
    fats REAL NOT NULL,
    proteins REAL NOT NULL,
    carbohydrates INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS cart (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    new_id INTEGER NOT NULL,
    meal_id INTEGER NOT NULL
);


INSERT INTO meals(meal, amount, price, categorie)
VALUES 
('Винигрет овощной', 150, 30, 1),
('Салат "Мясной" с ветчиной', 150, 45, 1),
('Салат "Сыроежка"', 130, 30, 1),
('Салат из корня сельдерея с овощами', 130, 35, 1),
('Салат из молодой капусты с овощами', 130, 30, 1),
('Салат из редиса с огурцом', 130, 35, 1),
('Салат из свежик огурцов с зеленью', 130, 35, 1),
('Салат из свежик помидоров со сладким перцем', 130, 40, 1);

INSERT INTO meals(meal, amount, price, categorie)
VALUES 
('Суп рисовый с овощами (постный)', 300, 30, 2),
('Суп рыбный с овощами', 300, 45, 2),
('Суп-крем из овощей с грибами', 300, 45, 2);

INSERT INTO meals(meal, amount, price, categorie)
VALUES 
('Бедро индейки тушенное с овощами', 90, 106, 3),
('Гуляш из индейки в томатном соусе (филе грудки)', 90, 95, 3),
('Индейка в грибном соусе (филе грудки)', 90, 106, 3),
('Котлеты из индейки жареные', 90, 75, 3),
('Котлеты по-киевски', 120, 116, 3),
('Курица с кабачком запеченная (филе грудки)', 100, 95, 3),
('Люля-кебаб из говядины', 90, 100, 3),
('Перец, фаршированный овощами и рисом', 250, 80, 3),
('Печень(куриная) жареная с овощами', 100, 70, 3),
('Треска жареная под маринадом', 90, 95, 3);

INSERT INTO meals(meal, amount, price, categorie)
VALUES 
('Брокколи с грибами в кунжуте', 175, 55, 4),
('Драники с сыром', 160, 50, 4),
('Капуста цветная, запеченная под соусом', 200, 65, 4),
('Картофельное пюре', 175, 35, 4),
('Макароны с овощами', 175, 35, 4),
('Рис отварной с чечевицей', 175, 25, 4),
('Тыква натуральная (пост)', 160, 50, 4),
('Фасоль стручковая в яйце', 175, 45, 4);

INSERT INTO meals(meal, amount, price, categorie)
VALUES 
('Компот из свежих фруктов', 250, 25, 5);
