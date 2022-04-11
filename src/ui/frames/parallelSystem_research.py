from tkinter import (BOTH, BOTTOM, HORIZONTAL, LEFT, TOP, Button, Canvas,
                     Entry, Frame, Label, N, OptionMenu, Scrollbar, StringVar,
                     W, X)

from core.config.config import ALL_METHODS, DATA_PATH
from core.research import parallel_system_research, research
from PIL import Image, ImageTk


class ParallelSystemResearchFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.first_frame = Frame(self)
        self.second_frame = Frame(self)

    # ======================= ПАРЛЛЕЛЬНАЯ СИСТЕМА =======================
        self.parallel_label = Label(
            self.first_frame,
            text="Parallel system of research",
            font='Times 17',
            bg="#8afff9"
        )

        # ПАРАМЕТРЫ

        # Histogram
        self.hist_label = Label(self.first_frame, text="Histogram: ")
        self.hist_entry = Entry(self.first_frame, width=7,
                                highlightbackground='#FFAA00')

        # Scale
        self.scale_label = Label(self.first_frame, text="Scale: ")
        self.scale_entry = Entry(
            self.first_frame, width=7, highlightbackground='#FFAA00')

        # Gradient
        self.gradient_label = Label(self.first_frame, text="Gradient: ")
        self.gradient_entry = Entry(
            self.first_frame, width=7, highlightbackground='#FFAA00')

        # DFT
        self.dft_label = Label(self.first_frame, text="DFT: ")
        self.dft_entry = Entry(self.first_frame, width=7,
                               highlightbackground='#FFAA00')

        # DCT
        self.dct_label = Label(self.first_frame, text="DCT: ")
        self.dct_entry = Entry(self.first_frame, width=7,
                               highlightbackground='#FFAA00')

        # Запуск параллельного исследования
        self.parallel_button = Button(
            self.first_frame,
            text="Launch",
            command=lambda: self.parallel_research()
        )

    # ======================= ОТОБРАЖЕНИЕ ГРАФИКОВ =======================

        # Canvas для отображения графиков
        self.canvas = Canvas(self, width=1500, height=800)

        # Scroll
        self.scroll_x = Scrollbar(
            self,
            orient=HORIZONTAL,
            command=self.canvas.xview
        )

        self.columnconfigure(0, weight=1)
        self.canvas.config(
            xscrollcommand=self.scroll_x.set,
            scrollregion=self.canvas.bbox("all")
        )

        self.canvas.create_window((0, 0), window=self, anchor=N + W)

    # ======================= Местоположение виджетов =======================

        self.first_frame.pack(side=TOP, anchor=W)
        self.second_frame.pack(side=TOP, anchor=W)

        # Настройка первого фрейма
        # self.cons_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        # self.method_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        # self.method_drop.pack(side=TOP, padx=10, pady=7, anchor=W)
        # self.run_but.pack(side=TOP, padx=10, pady=7, anchor=W)

        self.parallel_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.hist_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.hist_entry.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.scale_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.scale_entry.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.gradient_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.gradient_entry.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.dft_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.dft_entry.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.dct_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.dct_entry.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.parallel_button.pack(side=TOP, padx=140, pady=7, anchor=W)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.canvas.pack(fill=BOTH, expand=True)

    def parallel_research(self) -> None:
        """
        Проведение исследований с параллельной системой
        и отображение результатов.
        """
        global image
        self.canvas.delete("all")
        self.result_images = []
        params = [
            ('hist', int(self.hist_entry.get())),
            ('scale', int(self.scale_entry.get())),
            ('grad', int(self.gradient_entry.get())),
            ('dft', int(self.dft_entry.get())),
            ('dct', int(self.dct_entry.get()))
        ]
        parallel_system_research("ORL", params)

        posx = 250
        posy = 250

        image = Image.open(DATA_PATH + "results/parallel_result.png")
        image = image.resize((500, 300))
        image = ImageTk.PhotoImage(image)
        self.result_images.append(image)
        self.canvas.create_image(posx, posy, image=image)
