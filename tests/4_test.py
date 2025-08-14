import os
import sys
import subprocess
import importlib.util
from pathlib import Path
import pytest

SCRIPT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '4_task.py'
    )
)


def run_script(args, cwd=None):
    return subprocess.run(
        [sys.executable, SCRIPT] + args,
        capture_output=True,
        text=True,
        cwd=cwd
    )


def write_file(path: Path, contents: str):
    path.write_text(contents, encoding="utf-8")


def test_example1(tmp_path):
    # Пример 1 из ТЗ.
    input_file = tmp_path / "nums1.txt"
    write_file(input_file, "3\n6\n8\n9\n")

    p = run_script([str(input_file)])
    assert p.returncode == 0, f"Скрипт завершился с ошибкой {p.stderr}"
    assert p.stdout.strip() == "8"


def test_example2(tmp_path):
    # Пример 2 из ТЗ.
    input_file = tmp_path / "nums2.txt"
    write_file(input_file, "1\n16\n3\n20\n")

    p = run_script([str(input_file)])
    assert p.returncode == 0, f"Скрипт завершился с ошибкой {p.stderr}"
    expected = ("20 ходов недостаточно для приведения всех элементов "
                "массива к одному числу")
    assert p.stdout.strip() == expected


# Имя файла начинается с цифры, поэтому обычный import не подходит.
def test_find_min_moves():
    spec = importlib.util.spec_from_file_location("tested_script", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert hasattr(mod, "find_min_moves"), "find_min_moves не найдена"
    assert mod.find_min_moves([4, 5, 6]) == 2
    with pytest.raises(ValueError):
        mod.find_min_moves([])
