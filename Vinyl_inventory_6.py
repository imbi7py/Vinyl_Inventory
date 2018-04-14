#! python3
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

# TODO: Error Handling on integer inputs

conn = sqlite3.connect('vinyl_inventory.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS vinyl(id INTEGER, rack INTEGER, shelf INTEGER, box INTEGER, album TEXT, artist TEXT, year INTEGER, revisions INTEGER)")

def assign_address():
    # pulls address of highest address item from db
    c = conn.cursor()
    c.execute('SELECT MAX(rack), MAX(shelf), MAX(box) FROM vinyl')
    address = list(c.fetchall())
    rack = address[0][0]
    # first itteration will yield None while db is empty
    if rack == None:
        rack = 1
    shelf = address[0][1]
    if shelf == None:
        shelf = 1
    box = address[0][2]
    if box == None:
        box = 1
    address_output = [str(int(rack)), str(int(shelf)), str(int(box))]
    c.close()
    return address_output

def retrieve_info(item_num):
    c = conn.cursor()
    c.execute('SELECT * FROM vinyl WHERE id = ?', str(item_num))
    from_db = c.fetchall()
    return from_db

def item_max():
    c = conn.cursor()
    c.execute('SELECT MAX(id) FROM vinyl')
    max_id = c.fetchone()
    return int(max_id[0])
    
def item_min():
    c = conn.cursor()
    c.execute('SELECT MIN(id) FROM vinyl')
    min_id = c.fetchone()
    return int(min_id[0])

class Ui_Vinyl_Inventory_Main(object):
    def setupUi(self, Vinyl_Inventory_Main):
        Vinyl_Inventory_Main.setObjectName("Vinyl_Inventory_Main")
        Vinyl_Inventory_Main.resize(803, 619)
        self.centralwidget = QtWidgets.QWidget(Vinyl_Inventory_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -1, 801, 581))
        self.tabWidget.setObjectName("tabWidget")
  
        current_address = assign_address()        
        
        # add inventory tab start
        self.Inventory_Add = QtWidgets.QWidget()
        self.Inventory_Add.setObjectName("Inventory_Add")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Inventory_Add)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_Add = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_Add.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Add.setObjectName("gridLayout_Add")
        self.Box_Label_Add = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Box_Label_Add.setFont(font)
        self.Box_Label_Add.setObjectName("Box_Label_Add")
        self.gridLayout_Add.addWidget(self.Box_Label_Add, 2, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Rack_Label_Add = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Rack_Label_Add.setFont(font)
        self.Rack_Label_Add.setObjectName("Rack_Label_Add")
        self.gridLayout_Add.addWidget(self.Rack_Label_Add, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Year_Input_Add = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Year_Input_Add.setObjectName("Year_Input_Add") # year input (add tab)
        self.gridLayout_Add.addWidget(self.Year_Input_Add, 5, 3, 1, 1)
        self.Artist_Label_Add = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Artist_Label_Add.setFont(font)
        self.Artist_Label_Add.setObjectName("Artist_Label_Add")
        self.gridLayout_Add.addWidget(self.Artist_Label_Add, 4, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Rack_Input_Add = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Rack_Input_Add.setObjectName("Rack_Input_Add") # rack input (add tab)
        self.Rack_Input_Add.setText(str(current_address[0]))
        self.gridLayout_Add.addWidget(self.Rack_Input_Add, 3, 1, 1, 1)
        self.Submit_Data_Add = QtWidgets.QPushButton(self.gridLayoutWidget_3)       # submit data button (add tab)
        font = QtGui.QFont()                                                        # submit data button (add tab)
        font.setPointSize(14)                                                       # submit data button (add tab)
        self.Submit_Data_Add.setFont(font)                                          # submit data button (add tab)
        self.Submit_Data_Add.setObjectName("Submit_Data_Add")                       # submit data button (add tab)
        self.gridLayout_Add.addWidget(self.Submit_Data_Add, 8, 1, 3, 3)             # submit data button (add tab)
        self.Box_Input_Add = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Box_Input_Add.setObjectName("Box_Input_Add") # box input (add tab)
        self.Box_Input_Add.setText(str(current_address[2]))
        self.gridLayout_Add.addWidget(self.Box_Input_Add, 3, 3, 1, 1)
        self.Year_Label_Add = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Year_Label_Add.setFont(font)
        self.Year_Label_Add.setObjectName("Year_Label_Add")
        self.gridLayout_Add.addWidget(self.Year_Label_Add, 4, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Item_Num_Label_Add = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Item_Num_Label_Add.setObjectName("Item_Num_Label_Add")
        self.gridLayout_Add.addWidget(self.Item_Num_Label_Add, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Shelf_Input_Add = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Shelf_Input_Add.setObjectName("Shelf_Input_Add") # shelf input (add tab)
        self.Shelf_Input_Add.setText(str(current_address[1]))
        self.gridLayout_Add.addWidget(self.Shelf_Input_Add, 3, 2, 1, 1)
        self.Album_Label_Add = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Album_Label_Add.setFont(font)
        self.Album_Label_Add.setObjectName("Album_Label_Add")
        self.gridLayout_Add.addWidget(self.Album_Label_Add, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Album_Input_Add = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Album_Input_Add.setObjectName("Album_Input_Add") # album input (add tab)
        self.gridLayout_Add.addWidget(self.Album_Input_Add, 5, 1, 1, 1)
        self.Artist_Input_Add = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Artist_Input_Add.setObjectName("Artist_Input_Add") # artist input (add tab)
        self.gridLayout_Add.addWidget(self.Artist_Input_Add, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_Add.addItem(spacerItem, 1, 4, 10, 1)
        self.Shelf_Label_Add = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Shelf_Label_Add.setFont(font)
        self.Shelf_Label_Add.setObjectName("Shelf_Label_Add")
        self.gridLayout_Add.addWidget(self.Shelf_Label_Add, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_Add.addItem(spacerItem1, 1, 0, 10, 1)
        self.Warning_Label_Add = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Warning_Label_Add.setObjectName("Warning_Label_Add")
        self.gridLayout_Add.addWidget(self.Warning_Label_Add, 7, 1, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Warning_Label_Add_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Warning_Label_Add_2.setObjectName("Warning_Label_Add_2")
        self.gridLayout_Add.addWidget(self.Warning_Label_Add_2, 6, 1, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.tabWidget.addTab(self.Inventory_Add, "")

        # edit inventory tab start
        self.Inventory_Edit = QtWidgets.QWidget()
        self.Inventory_Edit.setObjectName("Inventory_Edit")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Inventory_Edit)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_Edit = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_Edit.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Edit.setObjectName("gridLayout_Edit")
        self.Submit_Data_Edit = QtWidgets.QPushButton(self.gridLayoutWidget_2)       # submit data button (edit tab)
        font = QtGui.QFont()                                                         # submit data button (edit tab)
        font.setPointSize(14)                                                        # submit data button (edit tab)
        self.Submit_Data_Edit.setFont(font)                                          # submit data button (edit tab)
        self.Submit_Data_Edit.setObjectName("Submit__Data_Edit")                     # submit data button (edit tab)
        self.gridLayout_Edit.addWidget(self.Submit_Data_Edit, 8, 1, 3, 3)            # submit data button (edit tab)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_Edit.addItem(spacerItem2, 1, 0, 10, 1)
        self.Rack_Input_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Rack_Input_Edit.setObjectName("Rack_Input_Edit")
        self.gridLayout_Edit.addWidget(self.Rack_Input_Edit, 3, 1, 1, 1)
        self.Album_Label_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Album_Label_Edit.setFont(font)
        self.Album_Label_Edit.setObjectName("Album_Label_Edit")
        self.gridLayout_Edit.addWidget(self.Album_Label_Edit, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Artist_Label_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Artist_Label_Edit.setFont(font)
        self.Artist_Label_Edit.setObjectName("Artist_Label_Edit")
        self.gridLayout_Edit.addWidget(self.Artist_Label_Edit, 4, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Shelf_Input_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Shelf_Input_Edit.setObjectName("Shelf_Input_Edit")
        self.gridLayout_Edit.addWidget(self.Shelf_Input_Edit, 3, 2, 1, 1)
        self.Shelf_Label_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Shelf_Label_Edit.setFont(font)
        self.Shelf_Label_Edit.setObjectName("Shelf_Label_Edit")
        self.gridLayout_Edit.addWidget(self.Shelf_Label_Edit, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Box_Input_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Box_Input_Edit.setObjectName("Box_Input_Edit")
        self.gridLayout_Edit.addWidget(self.Box_Input_Edit, 3, 3, 1, 1)
        self.Year_Input_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Year_Input_Edit.setObjectName("Year_Input_Edit")
        self.gridLayout_Edit.addWidget(self.Year_Input_Edit, 5, 3, 1, 1)
        self.Year_Label_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Year_Label_Edit.setFont(font)
        self.Year_Label_Edit.setObjectName("Year_Label_Edit")
        self.gridLayout_Edit.addWidget(self.Year_Label_Edit, 4, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Album_Input_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Album_Input_Edit.setObjectName("Album_Input_Edit")
        self.gridLayout_Edit.addWidget(self.Album_Input_Edit, 5, 1, 1, 1)
        self.Artist_Input_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Artist_Input_Edit.setObjectName("Artist_Input_Edit")
        self.gridLayout_Edit.addWidget(self.Artist_Input_Edit, 5, 2, 1, 1)
        self.Rack_Label_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Rack_Label_Edit.setFont(font)
        self.Rack_Label_Edit.setObjectName("Rack_Label_Edit")
        self.gridLayout_Edit.addWidget(self.Rack_Label_Edit, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Box_Label_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Box_Label_Edit.setFont(font)
        self.Box_Label_Edit.setObjectName("Box_Label_Edit")
        self.gridLayout_Edit.addWidget(self.Box_Label_Edit, 2, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_Edit.addItem(spacerItem3, 1, 4, 10, 1)
        self.Warning_Label_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Warning_Label_Edit.setObjectName("Warning_Label_Edit")
        self.gridLayout_Edit.addWidget(self.Warning_Label_Edit, 6, 1, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Warning_Label_2_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Warning_Label_2_Edit.setObjectName("Warning_Label_2_Edit")
        self.gridLayout_Edit.addWidget(self.Warning_Label_2_Edit, 7, 1, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Item_Num_Label_Edit = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Item_Num_Label_Edit.setObjectName("Item_Num_Label_Edit")
        self.gridLayout_Edit.addWidget(self.Item_Num_Label_Edit, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.Item_Num_Input_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Item_Num_Input_Edit.setObjectName("Item_Num_Input_Edit")
        self.gridLayout_Edit.addWidget(self.Item_Num_Input_Edit, 1, 2, 1, 1)        # item number view button (edit tab)
        self.Item_Num_View_Edit = QtWidgets.QPushButton(self.gridLayoutWidget_2)    # item number view button (edit tab)
        self.Item_Num_View_Edit.setObjectName("Item_Num_View_Edit")                 # item number view button (edit tab)
        self.gridLayout_Edit.addWidget(self.Item_Num_View_Edit, 1, 3, 1, 1)         # item number view button (edit tab)
        self.tabWidget.addTab(self.Inventory_Edit, "")

        # View inventory tab start
        input_range = 10
        self.Inventory_View = QtWidgets.QWidget()
        self.Inventory_View.setObjectName("Inventory_View")
        self.tableWidget = QtWidgets.QTableWidget(self.Inventory_View)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 761, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(input_range)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Inventory_View)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 0, 761, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Viewing_item_num_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Viewing_item_num_label.setObjectName("Viewing_item_num_label")
        self.horizontalLayout.addWidget(self.Viewing_item_num_label)
        self.item_num_input_1_view = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.item_num_input_1_view.setObjectName("item_num_input_1_view")
        self.horizontalLayout.addWidget(self.item_num_input_1_view)
        self.Viewing_item_num_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Viewing_item_num_label_2.setObjectName("Viewing_item_num_label_2")
        self.horizontalLayout.addWidget(self.Viewing_item_num_label_2)
        self.item_num_input_2_view = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.item_num_input_2_view.setObjectName("item_num_input_2_view")
        input_high = item_max()
        if input_high - input_range < item_min():
            input_low = item_min()
        else:
            input_low = input_high - input_range
        self.item_num_input_1_view.setText(str(input_low))
        self.item_num_input_2_view.setText(str(input_high))
        header_labels = ['ID', 'Rack', 'Shelf', 'Box', 'Album', 'Artist', 'Year', 'Revisions']
        self.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnWidth(4, 250)
        self.tableWidget.setColumnWidth(5, 250)
        self.update_view_data()
        #self.tableWidget.setEditTriggers(
        self.horizontalLayout.addWidget(self.item_num_input_2_view)
        self.update_view = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.update_view.setObjectName("update_view")
        self.horizontalLayout.addWidget(self.update_view)
        self.tabWidget.addTab(self.Inventory_View, "")
        Vinyl_Inventory_Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Vinyl_Inventory_Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        Vinyl_Inventory_Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Vinyl_Inventory_Main)
        self.statusbar.setObjectName("statusbar")
        Vinyl_Inventory_Main.setStatusBar(self.statusbar)

        # button calls
        self.Submit_Data_Add.clicked.connect(self.submit_data_add)
        self.Submit_Data_Edit.clicked.connect(self.submit_data_edit)
        self.Item_Num_View_Edit.clicked.connect(self.lookup_item)
        self.update_view.clicked.connect(self.update_view_data)
        
        # GUI calls
        self.retranslateUi(Vinyl_Inventory_Main)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Vinyl_Inventory_Main)

    def retranslateUi(self, Vinyl_Inventory_Main):
        _translate = QtCore.QCoreApplication.translate
        Vinyl_Inventory_Main.setWindowTitle(_translate("Vinyl_Inventory_Main", "Vinyl Inventory"))
        self.Box_Label_Add.setText(_translate("Vinyl_Inventory_Main", "Box Number"))
        self.Rack_Label_Add.setText(_translate("Vinyl_Inventory_Main", "Rack Number"))
        self.Artist_Label_Add.setText(_translate("Vinyl_Inventory_Main", "Artist Name"))
        self.Submit_Data_Add.setText(_translate("Vinyl_Inventory_Main", "Submit Data"))
        self.Year_Label_Add.setText(_translate("Vinyl_Inventory_Main", "Year of Album"))
        item_num_label_add = "Item Number: " + str(item_max()+1)
        self.Item_Num_Label_Add.setText(_translate("Vinyl_Inventory_Main", item_num_label_add))        ### text label, insert item num variable here (add tab)
        self.Album_Label_Add.setText(_translate("Vinyl_Inventory_Main", "Album Name"))
        self.Shelf_Label_Add.setText(_translate("Vinyl_Inventory_Main", "Shelf Number"))
        self.Warning_Label_Add.setText(_translate("Vinyl_Inventory_Main", "All Submitted Data is Final! There is no \"Undo\" Functionality!"))
        self.Warning_Label_Add_2.setText(_translate("Vinyl_Inventory_Main", "WARNING!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inventory_Add), _translate("Vinyl_Inventory_Main", "Add Inventory"))
        self.Submit_Data_Edit.setText(_translate("Vinyl_Inventory_Main", "Submit Data"))
        self.Album_Label_Edit.setText(_translate("Vinyl_Inventory_Main", "Album Name"))
        self.Artist_Label_Edit.setText(_translate("Vinyl_Inventory_Main", "Artist Name"))
        self.Shelf_Label_Edit.setText(_translate("Vinyl_Inventory_Main", "Shelf Number"))
        self.Year_Label_Edit.setText(_translate("Vinyl_Inventory_Main", "Year of Album"))
        self.Rack_Label_Edit.setText(_translate("Vinyl_Inventory_Main", "Rack Number"))
        self.Box_Label_Edit.setText(_translate("Vinyl_Inventory_Main", "Box Number"))
        self.Warning_Label_Edit.setText(_translate("Vinyl_Inventory_Main", "WARNING!"))
        self.Warning_Label_2_Edit.setText(_translate("Vinyl_Inventory_Main", "All Submitted Data is Final! There is no \"Undo\" Functionality!"))
        self.Item_Num_Label_Edit.setText(_translate("Vinyl_Inventory_Main", "Viewing Item Number:"))
        self.Item_Num_View_Edit.setText(_translate("Vinyl_Inventory_Main", "View Item"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inventory_Edit), _translate("Vinyl_Inventory_Main", "Edit Inventory"))
        self.Viewing_item_num_label.setText(_translate("Vinyl_Inventory_Main", "Viewing Item Numbers:"))
        self.Viewing_item_num_label_2.setText(_translate("Vinyl_Inventory_Main", "to"))
        self.update_view.setText(_translate("Vinyl_Inventory_Main", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inventory_View), _translate("Vinyl_Inventory_Main", "View Inventory"))

    def submit_data_add(self, data_add):
        _translate = QtCore.QCoreApplication.translate
        rack_value = int(float(self.Rack_Input_Add.text()))
        shelf_value = int(self.Shelf_Input_Add.text())
        box_value = int(self.Box_Input_Add.text())
        item_value = item_max() + 1
        album_value = self.Album_Input_Add.text()
        artist_value = self.Artist_Input_Add.text()
        year_value = int(self.Year_Input_Add.text())
        c.execute("INSERT INTO vinyl (id, rack, shelf, box, album, artist, year, revisions) values (?, ?, ?, ?, ?, ?, ?, 0)", (item_value, rack_value, shelf_value, box_value, album_value, artist_value, year_value))
        conn.commit()
        new_item_num_label_add = "Item Number: " + str(item_max + 1)
        self.Item_Num_Label_Add.setText(_translate("Vinyl_Inventory_Main", new_item_num_label_add))
        self.Album_Input_Add.clear()
        self.Artist_Input_Add.clear()
        self.Year_Input_Add.clear()

    def submit_data_edit(self, data_edit):
        item_value_edit = self.Item_Num_Input_Edit.text()
        rack_value_edit = int(float(self.Rack_Input_Edit.text()))
        shelf_value_edit = int(float(self.Shelf_Input_Edit.text()))
        box_value_edit = int(float(self.Box_Input_Edit.text()))
        album_value_edit = self.Album_Input_Edit.text()
        artist_value_edit = self.Artist_Input_Edit.text()
        year_value_edit = int(float(self.Year_Input_Edit.text()))
        edit_item_lookup = retrieve_info(item_value_edit)
        revision_num_edit = 1 + edit_item_lookup[0][7]
        c.execute("UPDATE vinyl SET rack = ?, shelf = ?, box = ?, album = ?, artist = ?, year = ?, revisions = ? WHERE id = ?", 
                  (rack_value_edit, shelf_value_edit, box_value_edit, album_value_edit, artist_value_edit, year_value_edit, revision_num_edit, item_value_edit))
        conn.commit()
        self.Rack_Input_Edit.clear()
        self.Shelf_Input_Edit.clear()
        self.Box_Input_Edit.clear()
        self.Album_Input_Edit.clear()
        self.Artist_Input_Edit.clear()
        self.Year_Input_Edit.clear()

    def lookup_item(self):
        item_selection_edit = int(self.Item_Num_Input_Edit.text())
        edit_item_lookup = retrieve_info(item_selection_edit)
        rack_lookup = edit_item_lookup[0][1]
        shelf_lookup = edit_item_lookup[0][2]
        box_lookup = edit_item_lookup[0][3]
        album_lookup = edit_item_lookup[0][4]
        artist_lookup = edit_item_lookup[0][5]
        year_lookup = edit_item_lookup[0][6]
        self.Rack_Input_Edit.setText(str(rack_lookup))
        self.Shelf_Input_Edit.setText(str(shelf_lookup))
        self.Box_Input_Edit.setText(str(box_lookup))
        self.Album_Input_Edit.setText(str(album_lookup))
        self.Artist_Input_Edit.setText(str(artist_lookup))
        self.Year_Input_Edit.setText(str(year_lookup))
    
    def update_view_data(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
            self.tableWidget.hideRow(0)
        list_min = int(self.item_num_input_1_view.text())
        list_max = int(self.item_num_input_2_view.text())
        # makes sure data is within database
        min_id = item_min()
        max_id = item_max()
        if max_id == None:
            return
        elif list_max > max_id:
            list_max = max_id
        if min_id > list_min:
            list_min = min_id
        
        # populates view field
        list_range = []
        item_id = list_min
        if list_max == list_min:
            list_range.append(list_min)
        else:
            while item_id < list_max + 1:
                list_range.append(item_id)
                item_id += 1
        self.tableWidget.setRowCount(len(list_range))
        for row in list_range:
            item_view_data = retrieve_info(row)
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row,0, QtWidgets.QTableWidgetItem(str(item_view_data[0][0])))
            self.tableWidget.setItem(row,1, QtWidgets.QTableWidgetItem(str(item_view_data[0][1])))
            self.tableWidget.setItem(row,2, QtWidgets.QTableWidgetItem(str(item_view_data[0][2])))
            self.tableWidget.setItem(row,3, QtWidgets.QTableWidgetItem(str(item_view_data[0][3])))
            self.tableWidget.setItem(row,4, QtWidgets.QTableWidgetItem(str(item_view_data[0][4])))
            self.tableWidget.setItem(row,5, QtWidgets.QTableWidgetItem(str(item_view_data[0][5])))
            self.tableWidget.setItem(row,6, QtWidgets.QTableWidgetItem(str(item_view_data[0][6])))
            self.tableWidget.setItem(row,7, QtWidgets.QTableWidgetItem(str(item_view_data[0][7])))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Vinyl_Inventory_Main = QtWidgets.QMainWindow()
    ui = Ui_Vinyl_Inventory_Main()
    ui.setupUi(Vinyl_Inventory_Main)
    Vinyl_Inventory_Main.show()
    sys.exit(app.exec_())

# I moved these here, because if I include them where they were, they closed the cursor and connection too soon(probably)
c.close() 
conn.close()
