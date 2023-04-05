# Скрипт для выгрузки фотографий из VK

## Что необходимо для начала:
---
- python 3.10
- Poetry
- vk_token = 'Ваш токен'
- vk_id = "Ваш ID пользователя"
---
[Документация Poetry](https://python-poetry.org/)

[Документация по VK API](https://dev.vk.com/guide)

[Видео о том как получить VK API и настроить разрешение](https://www.youtube.com/watch?v=f8D6RYNEtlk)


----
## Подготовка
В документации смотрим как получить VK_TOKEN и дать разрешение на [photos](https://vk.com/dev/permissions).

Заменяем vk_token и vk_id на ваши.

----
## Запуск
```Shell
poetry run python main.py
```
----