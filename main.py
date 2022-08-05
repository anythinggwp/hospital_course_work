import sqlite3
import func
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.Qt import *
import medic
import re
import newgui

class MainWindow(QtWidgets.QMainWindow, medic.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dialog = None
        self.setupUi(self)
        self.get_date()
        self.action.triggered.connect(lambda: self.open_table('medical_card', 0))
        self.action_2.triggered.connect(lambda: self.open_table('time_table' + self.get_date(), 1))
        self.pushButton.clicked.connect(self.add_row)
        self.pushButton_2.clicked.connect(lambda: func.test(self.get_date()))
        self.pushButton_3.clicked.connect(self.delete_rows)
# Вывод баз данных

    def open_table(self, name, mode):
        if mode == 0:
            func.sql_table_creat_medicalcard('test.db', name)
        elif mode == 1:
            func.sql_table_creat_timetable("test.db", name)
        elif mode == 2:
            func.sql_table_creat_monthly('test.db', name)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('test.db')
        db.open()
        self.model = QSqlTableModel(self)
        self.model.setTable(name)
        if self.lineEdit.text() != "":
            s = re.sub("[\W_]+", "", self.lineEdit.text())
            filer = '''name LIKE "{}" '''.format(s)
            self.model.setFilter(filer)
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setSortingEnabled(True)
# добавление строк в таблицу

    def add_row(self):
        self.model.insertRow(self.model.rowCount())
        print(self.model.rowCount())
# удаление строк из таблицы

    def delete_rows(self):
        index_list = []
        for model_index in self.tableView.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)
        for index in index_list:
            self.model.removeRow(index.row())
        #self.model.removeRow(int(self.model.rowCount() - 1))
        if self.model.tableName() == 'medical_card':
            self.open_table(self.model.tableName(), 0)
        elif self.model.tableName() == 'time_table' + self.get_date():
            self.open_table(self.model.tableName(), 1)

# возвращаем дату
    def get_date(self):
        temp = str(self.dateEdit.date().toPyDate())
        result = re.sub("[^0-9]", "_", temp)
        return result


    def get_month(self):
        temp = self.dateEdit.date().toString()

    def open_result(self):
        self.dialog = Dialog()
        self.dialog.show()
        self.dialog.pushButton.clicked.connect(self.dialog.close)


class Dialog(QtWidgets.QDialog, newgui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())



