# StonFi Transaction Checker

Сервис для получения и проверки транзакций swap из DEX StonFi (TON blockchain).

## Функционал
- Поиск транзакций обмена
- Сохранение в БД
- Фильтрация по дате
- Проверка успешности транзакции

## Как запустить

```bash
docker-compose up -d
pip install -r requirements.txt
uvicorn app.main:app --reload"# sonfi_tansaction" 
