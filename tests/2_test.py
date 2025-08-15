import os
import sys
import subprocess
import importlib.util
from pathlib import Path
import pytest  # noqa: F401

SCRIPT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '2_task.py'
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


def test_examples(tmp_path):
    ellipse_file = tmp_path / "ellipse.txt"
    points_file = tmp_path / "points.txt"

    write_file(ellipse_file, "0 0\n5 3\n")  # пример 1 из ТЗ.
    write_file(points_file, "0 3\n0 0\n6 0\n")  # пример 2 из ТЗ.

    p = run_script([str(ellipse_file), str(points_file)])
    assert p.returncode == 0, f"Скрипт завершился с ошибкой {p.stderr}"
    out_lines = p.stdout.strip().splitlines()
    assert out_lines == ["0", "1", "2"]


# Имя файла начинается с цифры, поэтому обычный import не подходит.
def test_find_point_position():
    spec = importlib.util.spec_from_file_location("tested_script", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, "find_point_position"), (
        "find_point_position не найдена")
    center = [0.0, 0.0]
    radius = [5.0, 3.0]
    assert mod.find_point_position(center, radius, [0.0, 3.0]) == 0
    assert mod.find_point_position(center, radius, [0.0, 0.0]) == 1
    assert mod.find_point_position(center, radius, [6.0, 0.0]) == 2
