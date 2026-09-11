# У сучасній розробці програмісти рідко пишуть сирі SQL-запити у вигляді рядків SELECT * FROM....

# Замість цього використовують ORM (Object-Relational Mapping) — технологію, 
# яка перетворює таблиці бази даних на класи Python, а рядки таблиці — на об'єкти!

# Подивись, як красиво замикається коло: ООП + База Даних + Веб:

# from sqlalchemy import Column, Integer, String # type: ignore
# from sqlalchemy.orm import DeclarativeBase # type: ignore

# # Сучасний спосіб оголошення базового класу:
# class Base(DeclarativeBase):
#     pass

# class PlayerModel(Base):
#     __tablename__ = "players"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     score = Column(Integer, default=0)

# new_player = PlayerModel(name="Anna", score=100)
# print(f"Створено об'єкт: {new_player.name} з балами {new_player.score}")

print("--------Створення та збереження файлу БД у SQL--------")

import os
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import select

# 1. Створюємо папку "SQL", якщо її ще немає, щоб уникнути помилки
db_folder = "SQL"
os.makedirs(db_folder, exist_ok=True)

# 2. Формуємо шлях до файлу БД всередині папки SQL
# "sqlite:///SQL/game.db" (для відносного шляху)
db_path = os.path.join(db_folder, "game.db")
engine = create_engine(f"sqlite:///{db_path}", echo=True)


# 3. Моделі та збереження
class Base(DeclarativeBase):
  pass


class PlayerModel(Base):
  __tablename__ = "players"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  score = Column(Integer, default=0)


# Base.metadata.create_all(engine)

# new_player = PlayerModel(name="Anna", score=100)

# with Session(engine) as session:
#   session.add(new_player)
#   session.commit()
#   print(f"Об'єкт збережено у файл {db_path}! ID: {new_player.id}")

# print("--------Створення та збереження нового гравця файлі БД у SQL--------")

# # 1. Оголошуємо таку ж модель, щоб SQLAlchemy знала структуру таблиці
# class Base(DeclarativeBase):
#   pass

# # 2. Підключаємося до вже існуючого файлу бази даних
# engine = create_engine("sqlite:///SQL/game.db")

# # 3. Створюємо нового гравця
# another_player = PlayerModel(name="Max", score=80)

# # 4. Відкриваємо сесію та зберігаємо
# with Session(engine) as session:
#   session.add(another_player)
#   session.commit()

#   print(
#       f"Гравця {another_player.name} успішно додано з ID:"
#       f" {another_player.id}"
#   )

print("--------Видалення певного гравця файлі БД у SQL--------")

with Session(engine) as session:
  # 1. Шукаємо гравця в БД
  player_to_delete = session.scalars(
      select(PlayerModel).where(PlayerModel.name == "Max")
  ).first()

  # 2. Перевіряємо, чи знайшли гравця, і видаляємо
  if player_to_delete:
    session.delete(player_to_delete)
    session.commit()
    print(f"Гравця {player_to_delete.name} успішно видалено!")
  else:
    print("Гравця з таким іменем не знайдено.")

print("--------Перевірка додавання/видалення гравця у файлі БД у SQL--------")

with Session(engine) as session:
  # Отримуємо всіх гравців з таблиці
  players = session.scalars(select(PlayerModel)).all()

  print("\nСписок усіх гравців у БД:")
  for player in players:
    print(f"ID: {player.id} | Ім'я: {player.name} | Бали: {player.score}")