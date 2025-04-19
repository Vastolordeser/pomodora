from src.app.services.timer_service import TimerService
from src.app.ui.main_window import MainWindow
from PyQt6.QtCore import QTimer


class TimerPresenter:
    def __init__(self, view: MainWindow, service: TimerService):
        self.view = view
        self.service = service

        # Настройка callback для обновления UI
        self.service.set_callback(self.view.update_display)

        # Связывание сигналов
        self.view.work_requested.connect(self.service.start_work)
        self.view.break_requested.connect(self.service.start_break)
        self.view.stop_requested.connect(self.service.stop)
        self.view.mode_changed.connect(self._handle_setting_change)

        # Таймер для обновления состояния сервиса
        self.timer = QTimer()
        self.timer.timeout.connect(self.service.tick)
        self.timer.start(1000)  # Обновление каждую секунду

    def _handle_setting_change(self):
        self.service.next_setting()
        self.view.reset_timer_display()

        self.service.set_callback(self.view.update_display)

        self.view.work_requested.connect(self.service.start_work)
        self.view.break_requested.connect(self.service.start_break)
        self.view.stop_requested.connect(self.service.stop)
        self.view.mode_changed.connect(self.service.next_setting)
