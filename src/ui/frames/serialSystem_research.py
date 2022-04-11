from tkinter import (BOTH, BOTTOM, HORIZONTAL, TOP, Button, Canvas,
                     Frame, Label, N, E, OptionMenu, Scrollbar, StringVar,
                     W, X, Entry)

from core.config.config import ALL_METHODS, DATA_PATH
from core.research import parallel_system_research, research
from PIL import Image, ImageTk


class SerialSystemResearchFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.first_frame = Frame(self)
        self.second_frame = Frame(self)

    # ======================= ПОСЛЕДОВАТЕЛЬНАЯ СИСТЕМА =======================

        self.cons_label = Label(
            self.first_frame,
            text="Consistent system of research",
            font='Times 17',
            bg="#8afff9"
        )

        # Метод извлечения признаков
        self.method_label = Label(self.first_frame, text="Method")

        self.method = StringVar()
        self.method.set(ALL_METHODS[1])

        self.method_drop = OptionMenu(
            self.first_frame,
            self.method,
            *ALL_METHODS
        )
        self.method_drop.configure(width=10)

        self.to_templ_label = Label(self.first_frame, text="To: ")
        self.to_template_entry = Entry(
        self.first_frame, width=7, highlightbackground='#650CAE')

        # Список классифицируемых изображений
        self.result_images = []

        # Запуск исследования
        self.run_but = Button(
            self.first_frame, text="Launch", command=lambda: self.research()
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
        # self.second_frame.pack(side=TOP, anchor=W)

        # Настройка первого фрейма
        self.cons_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.method_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.method_drop.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.run_but.pack(side=TOP, padx=140, anchor=E)

        self.to_templ_label.pack(side=TOP, anchor=W, padx=10, pady=7)
        self.to_template_entry.pack(side=TOP, anchor=W, padx=10, pady=7)
        # self.parallel_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        # self.hist_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.hist_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.scale_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.scale_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.gradient_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.gradient_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.dft_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.dft_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.dct_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.dct_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        # self.parallel_button.pack(side=TOP, padx=10, pady=7, anchor=W)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.canvas.pack(fill=BOTH, expand=True)

    def research(self) -> None:
        """
        Проведение исследований с последовательной системой
        и отображение результатов.
        """
        self.canvas.delete("all")
        best_scores, _, _ = research("ORL", self.method.get(), int(self.to_template_entry.get()))
        self.result_images = []

        posx = 250
        posy = 250


        image = Image.open(DATA_PATH + f"results/result_1_n.png")
        image = image.resize((350, 350))
        image = ImageTk.PhotoImage(image)
        self.result_images.append(image)
        self.canvas.create_image(posx, posy, image=image)

        posx += 360
