from house import House
from mortgage import Mortgage
from simulation import Simulation
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QSlider, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QFormLayout, QVBoxLayout
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mortgage Simulation")
        self.plot = pg.PlotWidget()
        
        formLayout = QFormLayout()
        vLayout = QVBoxLayout()
        vLayout.addLayout(formLayout)
        # Numbers
        self.rateEdit = QLineEdit("7")
        self.rateEdit.textChanged.connect(self.updateSlider)
        self.termEdit = QLineEdit("30")
        self.termEdit.textChanged.connect(self.updateSlider)
        self.downPaymentEdit = QLineEdit("5")
        self.downPaymentEdit.textChanged.connect(self.updateSlider)
        self.budgetEdit = QLineEdit("2000")
        self.budgetEdit.textChanged.connect(self.updateSlider)

        # Slider
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimum(100000)
        self.slider.setMaximum(999999)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(50000)
        self.slider.setValue(200000)
        self.sliderLabel = QLabel("$0")
        self.slider.valueChanged.connect(self.updateSlider)
        self.updateSlider()
        formLayout.addRow("Monthly Budget [$]", self.budgetEdit)
        formLayout.addRow("Interest Rate [%]", self.rateEdit)
        formLayout.addRow("Down Payment [%]", self.downPaymentEdit)
        formLayout.addRow("Term [years]", self.termEdit)
        formLayout.addRow(self.sliderLabel, self.slider)

        layout = QHBoxLayout()
        layout.addLayout(vLayout)
        layout.addWidget(self.plot)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def updateSlider(self):
        self.sliderLabel.setText("${}".format(self.slider.value()))
        house = House(self.slider.value())
        rate = float(self.rateEdit.text()) / 100
        term = int(self.termEdit.text())
        downPayment = float(self.downPaymentEdit.text()) / 100
        budget = float(self.budgetEdit.text())
        mortgage = Mortgage(house, rate, term, downPayment)
        simulation = Simulation(mortgage, budget)
        simulation.run()       
        self.plot.clear()
        self.plot.plot(simulation.results["year"], simulation.results["principal"], pen=(1, 2), name="Principal")
        self.plot.plot(simulation.results["year"], simulation.results["interest"], pen=(2, 2), name="Interest")
        self.plot.addLegend()
        self.plot.showGrid(x=True, y=True, alpha=0.3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()