from PyQt5.QtWidgets import *

from class_csv_reader import CSVReader
from class_folium_factory import FoliumMapFactory
from class_excel_converter import ExcelConverter
from ui.class_first_trip import FirstTrip
from ui.class_recall_previous_trip import RecallPreviousTrip
from ui.class_select_planner import SelectPlanner
from ui.class_start_page import StartPage


class WindowController(QWidget):
    def __init__(self, db_connector):
        super().__init__()
        self.trip_name = None  # 여행 이름
        self.db_connector = db_connector    #db연결 인스턴스
        self.start_page = StartPage(self)  # 시작페이지 페이지
        self.first_trip = FirstTrip(self)  # 처음 여행 페이지
        self.prev_trip = RecallPreviousTrip(self)  # 이전 여행 페이지
        self.select_planner = SelectPlanner(self)  # 스케줄러 페이지
        self.folium_factory = FoliumMapFactory()  # Folium 팩토리
        self.excel_converter = ExcelConverter()  # 엑셀 저장 기능 인스턴스

    def move_to_edit_timeline(self):
        print("수정화면으로 이동하였습니다.")
        self.select_planner.show()
        self.select_planner.move_to_edit_timeline()
