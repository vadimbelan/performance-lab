# Тестовое задание

**Ссылка на резюме:** https://hh.ru/resume/6ac3fce9ff0f3367fe0039ed1f4b71694c7979

**Файл с заданием:** https://disk.yandex.com/i/7yV7bpMuyO5FTg

[![Python CI](https://github.com/vadimbelan/performance-lab/actions/workflows/python-ci.yml/badge.svg)](https://github.com/vadimbelan/performance-lab/actions/workflows/python-ci.yml)

Решение задач представлено в файлах:
  - `1_task.py`
  - `2_task.py`
  - `4_task.py`

Тесты находятся в директории `tests/`:
  - `1_test.py`
  - `2_test.py`
  - `4_test.py`

#### 0. Для Windows:
```bash
python -m venv venv
source venv/Scripts/activate
```

#### 0. Для Linux и macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 1. Установка зависимостей
```bash
pip install pytest
```

#### 2. Запуск тестов
```bash
cd tests && pytest 1_test.py 2_test.py 4_test.py
```
