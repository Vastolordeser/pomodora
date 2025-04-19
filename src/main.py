import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from app.presentation.timer_presenter import TimerPresenter
from app.services.timer_service import TimerService
from app.ui.main_window import MainWindow

def main():
    # Добавляем путь к корню проекта в sys.path
    project_root = Path(__file__).parent
    sys.path.append(str(project_root))

    app = QApplication(sys.argv)

    view = MainWindow()
    service = TimerService()
    _ = TimerPresenter(view, service)

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
