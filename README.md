### Описание:

### Как запустить проект:

1. Клонировать репозиторий:

```
git clone https://github.com/sejapoe/api_final_yatube.git
```
2. Перейти в него через командную строку:
```
cd api_final_yatube
```

3. Cоздать и активировать виртуальное окружение:

Для Mac OS:
```
python3 -m venv .venv
```
```
source .venv/bin/activate
```
Для Windows:
```
python -m venv .venv
```
```
venv\Scripts\activate
```
4. Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

5. Выполнить миграции:

```
python3 manage.py migrate
```

6. Перейти в папку проекта и запустить его:

```
cd yatube_api/
```
```
python3 manage.py runserver
```

### Примеры API:

#### Получение публикаций | `GET /api/v1/posts`

Параметры запроса

- `limit` (integer, optional): Количество публикаций на страницу
- `offset` (integer, optional): Количество публикаций после которых начинать выдачу

Пример запроса:

```bash
GET /api/v1/posts/?limit=10&offset=3
```

Пример ответа:

```json
{
  "count": 123,
  "next": "http://localhost:8000/api/v1/posts/?offset=40&limit=10",
  "previous": "http://localhost:8000/api/v1/posts/?offset=20&limit=10",
  "results": [
    {
      "id": 0,
      "author": "admin",
      "text": "Lorem ipsum dolor sit amet.",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "group": 7
    }
  ]
}
```

#### Создание публикаций | `POST /api/v/posts/`

Тело запроса

- `text` (string): текст публикации
- `image` (binary, optional): изображение к публикации
- `group` (integer, optional): ID сообщества, в котором сделана публикация

Пример запроса:

```
POST /api/v1/posts/
{
    "text": "Lorem ipsum dolor amet.",
    "image": "string",
    "group": 7
}
```

Пример ответа:
```json
{
  "id": 12,
  "author": "admin",
  "text": "Lorem ipsum dolor amet.",
  "pub_date": "2024-09-09T14:15:22Z",
  "image": null,
  "group": 7
}
```