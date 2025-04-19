from enum import Enum, auto
from typing import Optional, Callable


class TimerState(Enum):
    """Состояния таймера."""
    IDLE = auto()
    WORK = auto()
    BREAK = auto()


class TimerService:
    """Сервис управления таймером Pomodoro."""

    def __init__(self):
        self._state = TimerState.IDLE
        self._remaining_seconds = 0
        self._settings = [
            {"work": 25 * 60, "break": 5 * 60},
            {"work": 30 * 60, "break": 10 * 60},
            {"work": 45 * 60, "break": 15 * 60}
        ]
        self._current_setting = 0
        self._callback: Optional[Callable[[int, str], None]] = None

    def set_callback(self, callback: Callable[[int, str], None]):
        """Установка callback для обновления UI."""
        self._callback = callback

    def start_work(self):
        """Запуск рабочего периода."""
        if self._state != TimerState.IDLE:
            return
        self._state = TimerState.WORK
        self._remaining_seconds = self._settings[self._current_setting]["work"]
        self._notify_ui()

    def start_break(self):
        """Запуск перерыва."""
        if self._state != TimerState.IDLE:
            return
        self._state = TimerState.BREAK
        self._remaining_seconds = self._settings[self._current_setting]["break"]
        self._notify_ui()

    def stop(self):
        """Остановка таймера."""
        self._state = TimerState.IDLE
        self._notify_ui()

    def next_setting(self):
        """Переключение на следующий режим."""
        self._current_setting = (self._current_setting + 1) % len(self._settings)

    def tick(self):
        """Обновление состояния таймера (вызывается каждую секунду)."""
        if self._state == TimerState.IDLE:
            return

        self._remaining_seconds -= 1
        if self._remaining_seconds <= 0:
            self._state = TimerState.IDLE

        self._notify_ui()

    def _notify_ui(self):
        """Уведомление UI об изменении состояния."""
        if self._callback:
            self._callback(self._remaining_seconds, self._state.name)
