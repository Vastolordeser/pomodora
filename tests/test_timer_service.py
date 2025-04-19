import pytest
import sys
from pathlib import Path

# Добавляем путь к src в PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from src.app.services.timer_service import TimerService, TimerState


@pytest.fixture
def timer_service():
    return TimerService()


def test_initial_state(timer_service):
    assert timer_service._state == TimerState.IDLE
    assert timer_service._remaining_seconds == 0


def test_start_work(timer_service):
    timer_service.start_work()
    assert timer_service._state == TimerState.WORK
    assert timer_service._remaining_seconds == 25 * 60


def test_start_break(timer_service):
    timer_service.start_break()
    assert timer_service._state == TimerState.BREAK
    assert timer_service._remaining_seconds == 5 * 60


def test_stop(timer_service):
    timer_service.start_work()
    timer_service.stop()
    assert timer_service._state == TimerState.IDLE


def test_next_setting(timer_service):
    assert timer_service._current_setting == 0
    timer_service.next_setting()
    assert timer_service._current_setting == 1
    timer_service.next_setting()
    assert timer_service._current_setting == 2
    timer_service.next_setting()
    assert timer_service._current_setting == 0
