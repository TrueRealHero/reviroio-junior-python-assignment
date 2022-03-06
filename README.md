# reviroio-junior-python-assignment

Kanye West app

структура <br />
/kanye-sayings     # Гость получает квоты <br />
/api         # Записанные в дб цитаты. Readonly <br /> 
/admin          # админка <br />

# Через docker
заходим в докер
1. git clone https://github.com/TrueRealHero/reviroio-junior-python-assignment.git
2. user TrueRealHero
3. токен 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
4. cd reviroio-junior-python-assignment
5. docker-compose build
6. docker-compose up -d
7. docker ps копируем или выписываем ID контейнера "reviroio....." (не постгреса)
8. docker exec -t -i АЙДИ КОНТЕЙНЕРА bash
9. python manage.py migrate<br />
    (можно пропустить) python manage.py createsuperuser для доступа в админку<br />
    как закончит миграцию можно exit<br />
10. OPEN PORT 8000

# Через локал
в kanyewest/settings.py поле DATABASE раскоментируйте <br />
а нижнюю часть наоборот можете убрать <br />
manage.py runserver или python manage.py runserver <br />
