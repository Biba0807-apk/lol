import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from math import sqrt


# Функция для расчета площади треугольника по формуле Герона
def heron_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return area


# Функция для расчета по теореме Пифагора
def pythagoras(a, b, c):
    if a == 0:
        return sqrt(c ** 2 - b ** 2)
    elif b == 0:
        return sqrt(c ** 2 - a ** 2)
    elif c == 0:
        return sqrt(a ** 2 + b ** 2)
    return None


class GeometryApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Ввод сторон
        self.a_input = TextInput(hint_text="Введите сторону a", multiline=False)
        self.b_input = TextInput(hint_text="Введите сторону b", multiline=False)
        self.c_input = TextInput(hint_text="Введите сторону c", multiline=False)

        # Метка для вывода результата
        self.result_label = Label(text="Результат:", size_hint_y=None, height=40)

        # Кнопка для расчета по формуле Герона
        self.heron_button = Button(text="Рассчитать площадь по формуле Герона", on_press=self.calculate_heron)

        # Кнопка для расчета по теореме Пифагора
        self.pythagoras_button = Button(text="Рассчитать по теореме Пифагора", on_press=self.calculate_pythagoras)

        # Сетка для ввода
        self.grid = GridLayout(cols=2, padding=10)
        self.grid.add_widget(Label(text="a:"))
        self.grid.add_widget(self.a_input)
        self.grid.add_widget(Label(text="b:"))
        self.grid.add_widget(self.b_input)
        self.grid.add_widget(Label(text="c:"))
        self.grid.add_widget(self.c_input)

        # Добавление элементов на экран
        self.layout.add_widget(self.grid)
        self.layout.add_widget(self.heron_button)
        self.layout.add_widget(self.pythagoras_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_heron(self, instance):
        try:
            a = float(self.a_input.text)
            b = float(self.b_input.text)
            c = float(self.c_input.text)
            area = heron_area(a, b, c)
            self.result_label.text = f"Площадь треугольника: {area:.2f}"
        except ValueError:
            self.result_label.text = "Ошибка: Введите корректные значения!"

    def calculate_pythagoras(self, instance):
        try:
            # Получаем значения из полей ввода, обрабатываем пустые поля как нули
            a = float(self.a_input.text) if self.a_input.text else 0
            b = float(self.b_input.text) if self.b_input.text else 0
            c = float(self.c_input.text) if self.c_input.text else 0

            # Проверка, что введены ровно два значения (одно из значений остается 0)
            if (a == 0 and b > 0 and c > 0):
                a = sqrt(c ** 2 - b ** 2)
                self.result_label.text = f"Длина катета a: {a:.2f}"
            elif (b == 0 and a > 0 and c > 0):
                b = sqrt(c ** 2 - a ** 2)
                self.result_label.text = f"Длина катета b: {b:.2f}"
            elif (c == 0 and a > 0 and b > 0):
                c = sqrt(a ** 2 + b ** 2)
                self.result_label.text = f"Длина гипотенузы c: {c:.2f}"
            else:
                # Ошибка, если заполнено более двух полей
                self.result_label.text = "Ошибка: Введите только два известных значения!"
        except ValueError:
            self.result_label.text = "Ошибка: Введите числовые значения!"
        except Exception as e:
            self.result_label.text = f"Ошибка: {str(e)}"


if __name__ == '__main__':
    GeometryApp().run()
