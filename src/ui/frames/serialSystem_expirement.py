import random
from re import S
from tkinter import (N, S, LEFT, TOP, Button, Canvas, Entry, Frame, Label,
                     OptionMenu, StringVar, W)
from turtle import bgcolor

from core.config.config import ALL_METHODS
from core.recognition import recognition
from PIL import Image, ImageTk


class SerialSystemExperimentFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.consistent_frame = Frame(self)
        self.parallel_frame = Frame(self)
        self.canvas_frame = Frame(self)

    # =============== ПОСЛЕДОВАТЕЛЬНАЯ СИСТЕМА ===============

        self.cons_label = Label(
            self.consistent_frame,
            text="Consistent system of experiment",
            font='Times 17',
            bg="#c296ff"
        )

        self.method_label = Label(self.consistent_frame, text="Method: ")

        self.method = StringVar()
        self.method.set(ALL_METHODS[1])
        self.method_drop = OptionMenu(
            self.consistent_frame,
            self.method,
            *ALL_METHODS
        )
        self.method_drop.configure(width=10)

        # Параметр метода
        self.param_label = Label(self.consistent_frame, text="Parameter: ")
        self.p_entry = Entry(self.consistent_frame,
                             width=7, highlightbackground='#C9F600')

        # Номер, с которого будут браться шаблоны для каждого человека
        self.from_templ_label = Label(self.consistent_frame, text="From: ")
        self.from_template_entry = Entry(
            self.consistent_frame, width=7, highlightbackground='#650CAE')

        # Номер, по который будут браться шаблоны для каждого человека
        self.to_templ_label = Label(self.consistent_frame, text="To: ")
        self.to_template_entry = Entry(
            self.consistent_frame, width=7, highlightbackground='#650CAE')
        self.score_label = Label(self.consistent_frame, text="Accuracy:")
        self.score_result = Label(self.consistent_frame, text="")

        # Список классифицируемых изображений
        self.result_images = []

        # Список содержащий по шаблону для
        # каждого из классифицируемых изображений
        self.templates = []

        # Запуск исследования
        self.run_but = Button(
            self.consistent_frame,
            text="Launch",
            command=lambda: self.consistent_experiment()
        )

        self.canvas = Canvas(self.canvas_frame, width=500, height=900)

        # =============== МЕСТОПОЛОЖЕНИЕ ВИДЖЕТОВ ===============

        self.consistent_frame.pack(side=TOP, anchor=W)
        # self.parallel_frame.pack(side=TOP, anchor=W)
        self.canvas_frame.pack(side=TOP, anchor=W)

        # Настройка фрейма для последовательной системы
        self.cons_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.method_label.pack(side=TOP, anchor=W, padx=10, pady=7)
        self.method_drop.pack(side=TOP, anchor=W, padx=10, pady=7)

        self.param_label.pack(side=TOP, anchor=W, padx=10, pady=7)
        self.p_entry.pack(side=TOP, anchor=W, padx=10, pady=7)

        self.from_templ_label.pack(side=TOP, anchor=W, padx=10, pady=7)
        self.from_template_entry.pack(side=TOP, anchor=W, padx=10, pady=7)

        self.to_templ_label.pack(side=TOP, anchor=W, padx=10, pady=7)
        self.to_template_entry.pack(side=TOP, anchor=W, padx=10, pady=7)

        self.run_but.pack(side=TOP, anchor=W, padx=140, pady=7)

        self.score_label.pack(side=LEFT, anchor=W, padx=10)
        self.score_result.pack(side=TOP, anchor=W)

        self.canvas.pack(side=LEFT, anchor=N)

    def consistent_experiment(self) -> None:
        """
        Проведение эксперимента с последовательной системой
        и отображение результатов.
        """
        score, images, templates = recognition(
            "ORL",
            # research_method.get(),
            self.method.get(),
            int(self.p_entry.get()),
            int(self.from_template_entry.get()),
            int(self.to_template_entry.get()),
        )
        self.score_result.config(text=score)

        templ_posx = 50
        templ_posy = 50

        res_posx = 300
        res_posy = 50

        random_indexes = [random.randrange(len(images)) for _ in range(8)]

        for index in random_indexes:
            templ = Image.fromarray(templates[index])
            templ.resize((50, 50))
            templ = ImageTk.PhotoImage(templ)
            self.templates.append(templ)
            self.canvas.create_image(templ_posx, templ_posy, image=templ)

            templ_posy += 80

            img = Image.fromarray(images[index])
            img.resize((50, 50))
            img = ImageTk.PhotoImage(img)
            self.result_images.append(img)
            self.canvas.create_image(res_posx, res_posy, image=img)

            res_posy += 80
