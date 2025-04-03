import sys
from play import Play
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                            QVBoxLayout, QPushButton, QLabel)
from PyQt6.QtCore import Qt

class ChessWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window title and fixed size
        self.setWindowTitle("Chess Player")
        self.setFixedSize(600, 400)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Add the main text label
        title_label = QLabel("Choose your method")
        title_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Add "Play with Bot" button
        bot_button = QPushButton("Play with Bot")
        bot_button.setFixedSize(200, 50)
        bot_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        bot_button.clicked.connect(Play.play_with_bot)
        
        # Add "Play with Other" button
        other_button = QPushButton("Play with Other")
        other_button.setFixedSize(200, 50)
        other_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-size: 16px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        other_button.clicked.connect(Play.play_with_other)
        
        # Add buttons to layout with some spacing
        layout.addStretch()
        layout.addWidget(bot_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(20)  # Add space between buttons
        layout.addWidget(other_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        
        # Set layout margins
        layout.setContentsMargins(20, 40, 20, 40)

