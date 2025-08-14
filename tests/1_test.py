import os
import sys
import subprocess
import importlib.util
import pytest

SCRIPT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '1_task.py'
    )
)


def run_script(args):
    return subprocess.run(
        [sys.executable, SCRIPT] + args,
        capture_output=True,
        text=True
    )


@pytest.mark.parametrize("args,expected", [
    (["6", "3", "5", "4"], "13514253"),  # пример 1 из ТЗ.
    (["4", "2", "6", "4"], "123414"),  # пример 2 из ТЗ.
])
def test_examples(args, expected):
    p = run_script(args)
    assert p.returncode == 0, f"Скрипт завершился с ошибкой {p.stderr}"
    assert p.stdout.strip() == expected


# Имя файла начинается с цифры, поэтому обычный import не подходит.
def test_find_path():
    spec = importlib.util.spec_from_file_location("tested_script", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, "find_path"), "Функция find_path не найдена"
    assert mod.find_path(6, 3) == "135"
    assert mod.find_path(5, 4) == "14253"
