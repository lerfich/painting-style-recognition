import random
from tkinter import (LEFT, TOP, Button, Canvas, Entry, Frame, Label,
                     OptionMenu, StringVar, W)
from turtle import bgcolor

from core.config.config import DATA_PATH
from core.recognition import parallel_recognition
from PIL import Image, ImageTk


class ParallelSystemExperimentFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.consistent_frame = Frame(self)
        self.parallel_frame = Frame(self)
        self.canvas_frame = Frame(self)

    # =============== ПАРАЛЛЕЛЬНАЯ СИСТЕМА ===============
        self.parallel_label = Label(
            self.parallel_frame,
            text="Parallel system of experiment",
            font='Times 17',
            bg="#c296ff"
        )

        # ПАРАМЕТРЫ

        # Histogram
        self.hist_label = Label(self.parallel_frame,
                                text="Histogram: ")
        self.hist_entry = Entry(self.parallel_frame,
                                width=7, highlightbackground='#650CAE')

        # Scale
        self.scale_label = Label(self.parallel_frame, text="Scale: ")
        self.scale_entry = Entry(
            self.parallel_frame, width=7, highlightbackground='#650CAE')

        # Gradient
        self.gradient_label = Label(self.parallel_frame, text="Gradient: ")
        self.gradient_entry = Entry(
            self.parallel_frame, width=7, highlightbackground='#650CAE')

        # DFT
        self.dft_label = Label(self.parallel_frame, text="DFT: ")
        self.dft_entry = Entry(self.parallel_frame, width=7,
                               highlightbackground='#650CAE')

        # DCT
        self.dct_label = Label(self.parallel_frame, text="DCT: ")
        self.dct_entry = Entry(self.parallel_frame, width=7,
                               highlightbackground='#650CAE')

        # Число шаблонов
        self.templ_num_label = Label(self.parallel_frame, text="L: ")
        self.templ_num_entry = Entry(
            self.parallel_frame, width=7, highlightbackground='#C9F600')

        # Запуск параллельного исследования
        self.parallel_button = Button(
            self.parallel_frame,
            text="Launch",
            command=lambda: self.parallel_experiment()
        )

        self.canvas = Canvas(self.canvas_frame, width=1000, height=900)

    # =============== МЕСТОПОЛОЖЕНИЕ ВИДЖЕТОВ ===============

        # self.consistent_frame.pack(side=TOP, anchor=W)
        self.parallel_frame.pack(side=TOP, anchor=W)
        self.canvas_frame.pack(side=TOP, anchor=W)

        # Настройка фрейма для параллельной системы
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
        self.templ_num_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.templ_num_entry.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.parallel_button.pack(side=TOP, padx=140, pady=7, anchor=W)

        # Настройка фрейма с Canvas
        self.canvas.pack(side=TOP)

    def parallel_experiment(self) -> None:
        """
        Проведение эксперимента с параллельной системой
        и отображение результатов.
        """
        params = [
            ('hist', int(self.hist_entry.get())),
            ('scale', int(self.scale_entry.get())),
            ('grad', int(self.gradient_entry.get())),
            ('dft', int(self.dft_entry.get())),
            ('dct', int(self.dct_entry.get()))
        ]
        L = int(self.templ_num_entry.get())
        scores = parallel_recognition(
            db_name='ORL',
            params=params,
            templ_to=L
        )

        self.result_images = []

        posx = 250
        posy = 250

        image = Image.open(
            DATA_PATH + "results/parallel_experiment_result.png"
        )
        image = image.resize((500, 300))
        image = ImageTk.PhotoImage(image)
        self.result_images.append(image)
        self.canvas.create_image(posx, posy, image=image)
