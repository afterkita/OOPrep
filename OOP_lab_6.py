class Control:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        print(f"Вызван метод getPosition из контролла {type(self).__name__}")
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# Класс формы
class Form(Control):
    def __init__(self):
        super().__init__()
        self.controls = []
        print("Форма создана")

    def addControl(self, control):
        self.controls.append(control)

    def getControls(self):
        return self.controls

    def getInfo(self):
        print("\n.....Форма......")
        print("Cоздание формы с координатами" + self.getPosition())
        for i in self.getControls():
            if type(i).__name__ != "ComboBox":
                print(f"{type(i).__name__} = " + i.getText())
                print(f"{type(i).__name__} Coords = " + i.getPosition())
            else:
                print(f"{type(i).__name__} : ")
                for j in i.getItems():
                    print("   - " + j)
                print(f"{type(i).__name__} Coords = " + i.getPosition())

        print("\n")


class Label(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("- setText -для- Label")
        self.text = text

    def getText(self):
        print("- getText -для- Label")
        return self.text


class TextBox(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("- setText -для- TextBox")
        self.text = text

    def getText(self):
        print("- getText -для- TextBox")
        return self.text

    def onValueChanged(self):
        print("- onValueChanged -для- TextBox")


class ComboBox(Control):
    def __init__(self):
        super().__init__()
        self.selectedIndex = -1
        self.items = []

    def setSelectedIndex(self, index):
        print("- setSelectedIndex -для- ComboBox")
        self.selectedIndex = index

    def getSelectedIndex(self):
        print("- getSelectedIndex -для- ComboBox")
        return self.selectedIndex

    def setItems(self, items):
        print("- setItems -для- ComboBox")
        self.items = items

    def getItems(self):
        print("- getItems -для- ComboBox")
        return self.items


class Button(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("- setText -для- Button")
        self.text = text

    def getText(self):
        print("- getText -для- Button")
        return self.text

    def click(self):
        print("- click -для- Button")


class AbstractFactory:
    def createForm(self):
        pass

    def createLabel(self):
        pass

    def createTextBox(self):
        pass

    def createComboBox(self):
        pass

    def createButton(self):
        pass

class WindowsFactory(AbstractFactory):
    def __init__(self):
        print("Создан обьект Windows ")

    def createForm(self):
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()
class LinuxFactory(AbstractFactory):
    def __init__(self):
        print("Создан обьект Linux ")

    def createForm(self):
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()
class MacOSFactory(AbstractFactory):
    def __init__(self):
        print("Создан обьект MacOS")

    def createForm(self):
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()



if __name__ == "__main__":
    factory = LinuxFactory()

    form = factory.createForm()

    label = factory.createLabel()
    textbox = factory.createTextBox()
    combobox = factory.createComboBox()
    button = factory.createButton()

    label.setText("Продажа мёртвых душ")
    label.setPosition(0, 1)

    textbox.setText("Сколько желаете приобрести?")
    textbox.setPosition(1, 1)

    combobox.setItems(["1", "5", "20"])
    combobox.setSelectedIndex(1)
    combobox.setPosition(1, 5)

    button.setText("Купить")
    button.setPosition(6, 6)

    form.addControl(label)
    form.addControl(textbox)
    form.addControl(combobox)
    form.addControl(button)

    form.getInfo()