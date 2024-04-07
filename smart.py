from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )
from PyQt5.QtGui import QKeySequence

import json
import os

def writeToFile():
        with open("notes.json", "w", encoding='utf=8') as file:
            json.dump(notes,file,sort_keys=True)

with open("notes.json", "r", encoding='utf=8') as file:
    notes= json.load(file)

app = QApplication([])
window = QWidget()
main_width, main_height = 800,600

text_editor=QTextEdit()
text_editor.setStyleSheet('background-color: white;')
text_editor.setPlaceholderText("Введіть текст .....")

list_widget_1 = QListWidget()
list_widget_1.setStyleSheet('background-color: red;')

list_widget_2 = QListWidget()
list_widget_2.setStyleSheet('background-color: yellow;')

text_searcher = QLineEdit()
text_searcher.setPlaceholderText("Введіть текст .... ")
text_searcher.setStyleSheet('background-color: purple;')

input_dialog = QLineEdit()
input_dialog.setPlaceholderText("Введіть тег .... ")
input_dialog.setStyleSheet('background-color: purple;')

make_note = QPushButton()
make_note.setStyleSheet('background-color: orange;')
make_note.setText("Створити замітку")

delete_note = QPushButton()
delete_note.setStyleSheet('background-color: orange;')
delete_note.setText("Видалити замітку")

save_note = QPushButton()
save_note.setStyleSheet('background-color: orange;')
save_note.setText("Зберегти замітку")

search_for_text = QPushButton()
search_for_text.setStyleSheet('background-color: orange;')
search_for_text.setText("Шукати замітку по тексту замітку")

search_for_note = QPushButton()
search_for_note.setStyleSheet('background-color: orange;')
search_for_note.setText("Шукати замітку по тегу")

add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: purple;')
add_to_note.setText("Додати до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: purple;')
unpin_to_note.setText("Відкріпити до замітки")

action_theme_btn = QPushButton()
action_theme_btn.setStyleSheet('background-color: red;')
action_theme_btn.setText("Змінити на чорну тему")
export_as_text = QPushButton()
export_as_text.setText("Конвертувати у text")

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список запитань"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
col2.addWidget(QLabel("Список тегів"))
col2.addWidget(list_widget_2)
col2.addWidget(input_dialog)
col2.addWidget(text_searcher)

col2.addLayout(row2)

col2.addWidget(search_for_note)
col2.addWidget(search_for_text)
col2.addWidget(export_as_text)
col2.addWidget(action_theme_btn)

layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)


     



def sergio():
    if action_theme_btn.text() == "Змінити на чорну тему" :
        list_widget_1.setStyleSheet("background-color:purple; color:red")
        list_widget_2.setStyleSheet("background-color:purple; color:red")
        text_editor.setStyleSheet("background-color:purple; color:red")
        text_searcher.setStyleSheet("background-color:purple; color:red")
        input_dialog.setStyleSheet("background-color:purple; color:red")
        make_note.setStyleSheet("background-color:purple; color:red")
        delete_note.setStyleSheet("background-color:purple; color:red")
        save_note.setStyleSheet("background-color:purple; color:red")
        search_for_note.setStyleSheet("background-color:purple; color:red")
        search_for_text.setStyleSheet("background-color:purple; color:red")
        add_to_note.setStyleSheet("background-color:purple; color:red")
        unpin_to_note.setStyleSheet("background-color:purple; color:red")
        export_as_text.setStyleSheet("background-color:purple; color:red")
        action_theme_btn.setStyleSheet("background-color:purple; color:red")
        window.setStyleSheet('background-color: black; font-size:20px')
        action_theme_btn.setText("Змінити на рожевий")
    elif action_theme_btn.text() == "Змінити на рожевий":
        list_widget_1.setStyleSheet("background-color:black; color:green")
        list_widget_2.setStyleSheet("background-color:red; color:green")
        text_editor.setStyleSheet("background-color:white; color:green")
        text_searcher.setStyleSheet("background-color:red; color:green")
        input_dialog.setStyleSheet("background-color:pink; color:green")
        make_note.setStyleSheet("background-color:black; color:green")
        delete_note.setStyleSheet("background-color:green; color:green")
        save_note.setStyleSheet("background-color:red; color:green")
        search_for_note.setStyleSheet("background-color:white; color:red")
        search_for_text.setStyleSheet("background-color:purple; color:red")
        add_to_note.setStyleSheet("background-color:purple; color:red")
        unpin_to_note.setStyleSheet("background-color:purple; color:red")
        export_as_text.setStyleSheet("background-color:purple; color:red")
        action_theme_btn.setStyleSheet("background-color:purple; color:red")
        window.setStyleSheet('background-color: black; font-size:20px')
        action_theme_btn.setText("Змінити на чорну тему")






def show_notes():
    global key
    key = list_widget_1.selectedItems()[0].text()
    list_widget_2.clear()
    text_editor.setText(notes[key]["text"])
    list_widget_2.addItems(notes[key]["tag"])

def delete_note_1():
    key = list_widget_1.selectedItems()[0].text()
    if key in notes:
        notes.pop(key)
        list_widget_1.clear()
        list_widget_2.clear()
        list_widget_1.addItems(notes)
        writeToFile()

def save_note_def():
    if list_widget_1.currentItem():
         key = list_widget_1.currentItem().text()
         new_text_note = text_editor.toPlainText()
         notes[key]["Text"] = new_text_note
         writeToFile()

def add_mynote():
     note_name, ok= QInputDialog.getText(window,"ADD", "NAME")
     if note_name and ok:
          list_widget_1.addItem(note_name)
          notes[note_name] = {"text" : " ", "tag": [ ]}
          writeToFile()


def add_tag():
    key = list_widget_1.selectedItems()[0].text()
    if key in notes:
        tag_name, ok= QInputDialog.getText(window,"ADD", "NAME")
        if tag_name and ok:
             notes[key]["tag"].append(tag_name)
             writeToFile()
        list_widget_2.clear()
        list_widget_2.addItems(notes[key]["tag"])
        
def delete_tag():
    key= list_widget_1.selectedItems()[0].text()
    if key in notes:
        current_item = list_widget_2.currentItem()
        if current_item:
            list_widget_2.clear()
            tag_name = current_item.text()
            notes[key]["tag"].remove(tag_name)
            writeToFile()
        list_widget_2.clear()
        list_widget_2.addItems(notes[key]["tag"])
        

            
def search_note_for_text():
    text_to_search = text_searcher.text()
    if search_for_text.text() == 'Шукати замітку за текстом':
        filtered_notes = {}
        for key, note_data in notes.items():
            if text_to_search in note_data['text']:
                filtered_notes[key] = note_data
        search_for_text.setText('Скинути пошук')
        list_widget_1.clear()
        list_widget_1.addItems(filtered_notes.keys())
        list_widget_2.clear()
        text_editor.clear()

    elif search_for_text.text() == 'Скинути пошук':
        search_for_text.setText('Шукати замітку за текстом')
        list_widget_1.clear()
        list_widget_1.addItems(notes.keys())
        list_widget_2.clear()
        text_editor.clear()


def search_note():
    tag = input_dialog.text()
    if search_for_note.text() == 'Шукати замітку за тегом':
        filtered_notes = {}
        for key in notes:
            if tag in notes[key]['теги']:
                filtered_notes[key] = notes[key]
        search_for_note.setText('Скинути пошук')

        list_widget_1.clear()
        list_widget_1.addItems(filtered_notes)
        list_widget_2.clear()
        text_editor.clear()

    elif search_for_note.text() == 'Скинути пошук':
            search_for_note.setText('Шукати замітку за тегом')
            list_widget_1.clear()
            list_widget_1.addItems(notes.keys())
            list_widget_2.clear()
            text_editor.clear()
    

list_widget_1.addItems(notes)
list_widget_1.itemClicked.connect(show_notes)
delete_note.clicked.connect(delete_note_1)
save_note.clicked.connect(save_note_def)
search_for_text.clicked.connect(search_note_for_text)
search_for_note.clicked.connect(search_note)

make_note.clicked.connect(add_mynote)
add_to_note.clicked.connect(add_tag)
unpin_to_note.clicked.connect(delete_tag)
action_theme_btn.clicked.connect(sergio)
window.setStyleSheet('background-color: yellow; font-size:20px')
window.setLayout(layout_note)
window.resize(main_width, main_height)
window.show()
app.exec_()