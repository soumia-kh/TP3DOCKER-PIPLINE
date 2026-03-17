import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from tasks import add_task, get_tasks, tasks

def setup_function():
    tasks.clear()

def test_add_task():
    add_task("learn Docker")
    assert "learn Docker" in get_tasks()

def test_multiple_tasks():
    add_task("Learn CI")
    add_task("Learn DevOps")
    current_tasks = get_tasks()
    assert "Learn CI" in current_tasks
    assert "Learn DevOps" in current_tasks