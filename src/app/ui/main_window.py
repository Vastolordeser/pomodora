from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QComboBox
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal


class MainWindow(QMainWindow):

    work_requested = pyqtSignal()
    break_requested = pyqtSignal()
    stop_requested = pyqtSignal()
    mode_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.setFixedSize(300, 250)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.timer_label = QLabel("25:00")
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 48px;")
        layout.addWidget(self.timer_label)

        self.status_label = QLabel("Ready")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        self.work_btn = QPushButton("Start Work")
        self.work_btn.clicked.connect(self._on_work_requested)
        layout.addWidget(self.work_btn)

        self.break_btn = QPushButton("Start Break")
        self.break_btn.clicked.connect(self._on_break_requested)
        layout.addWidget(self.break_btn)

        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self._on_stop_requested)
        layout.addWidget(self.stop_btn)


        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["25/5", "30/10", "45/15"])
        self.mode_combo.currentIndexChanged.connect(self._on_mode_changed)
        layout.addWidget(self.mode_combo)

        self.ui_timer = QTimer()
        self.ui_timer.timeout.connect(self._update_ui)
        self.ui_timer.start(1000)

    def _on_work_requested(self):

        self.work_requested.emit()

    def _on_break_requested(self):
        self.break_requested.emit()

    def _on_stop_requested(self):
        self.stop_requested.emit()

    def _on_mode_changed(self, index):

        self.mode_changed.emit(index)

    def update_display(self, seconds: int, state: str):

        mins, secs = divmod(seconds, 60)
        self.timer_label.setText(f"{mins:02d}:{secs:02d}")

        if state == "WORK":
            self.status_label.setText("Working...")
            self.timer_label.setStyleSheet("font-size: 48px; color: red;")
        elif state == "BREAK":
            self.status_label.setText("On Break")
            self.timer_label.setStyleSheet("font-size: 48px; color: green;")
        else:
            self.status_label.setText("Ready")
            self.timer_label.setStyleSheet("font-size: 48px; color: black;")
            self.reset_timer_display()

    def _update_ui(self):

        pass

    def reset_timer_display(self):

        work_durations = [25, 30, 45]
        duration = work_durations[self.mode_combo.currentIndex()]
        self.timer_label.setText(f"{duration:02d}:00")
