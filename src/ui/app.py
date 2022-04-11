from tkinter import Tk, ttk
from ui.frames import *


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("recognition of face by Nikita")
        # self.attributes("-zoomed", True)

        self.notebook = ttk.Notebook(self)

        # self.ex_tab = ExperimentFrame(self.notebook)
        # self.research_tab = ResearchFrame(self.notebook)

        # self.notebook.add(self.ex_tab, text="Эксперимент")
        # self.notebook.add(self.research_tab, text="Исследование")

        self.par_ex_tab = ParallelSystemExperimentFrame(self.notebook)
        self.ser_sys_ex_tab = SerialSystemExperimentFrame(self.notebook)

        self.par_res_tab = ParallelSystemResearchFrame(self.notebook)
        self.ser_sys_res_tab = SerialSystemResearchFrame(self.notebook)

        self.notebook.add(self.ser_sys_ex_tab,
                          text="Эксперимент: последовательная система")
        self.notebook.add(
            self.par_ex_tab, text="Эксперимент: параллельная система")
        self.notebook.add(self.ser_sys_res_tab,
                          text="Исследование: последовательная система")
        self.notebook.add(self.par_res_tab,
                          text="Исследование: параллельная система")

        self.notebook.pack(expand=1, fill="both")
