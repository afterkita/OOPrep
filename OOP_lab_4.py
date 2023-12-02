import time


class Button:
    def __init__(self, ButtonName):
        self.ButtonName = ButtonName

    def getName(self):
        return self.ButtonName

    def setName(self, newButton):
        self.ButtonName = newButton

    def use_Button(self):
        print(f'Button pressed: {self.ButtonName}')
        time.sleep(0.5)
        actions.append(self)

    def reassign_Button(self, newButton, actions):
        print(f'Reassign: {self.ButtonName} ==> {newButton}')
        for action in actions:
            if action.getName() == self.ButtonName:
                action.setName(newButton)
        return actions


def undo_last_action(actions):
    if len(actions) > 0:
        last_action = actions.pop()
        print(f'Last press - {last_action.getName()}')
    else:
        print('No recent clicks')


def printHistory(actions):
    print('History:')
    for action in actions:
        print(action.getName())
    print('\n')


if __name__ == '__main__':
    actions = []
    print(
        "Создать виртуальную клавиатуру с переназначаемыми действиями для клавиш и комбинаций клавиш, с возможностью отката действий назад.")
    Button1 = Button('Ctrl+Z')
    Button1.use_Button()
    Button2 = Button('Ctrl+Alt+Delete')
    Button2.use_Button()

    print(
        "\nПродемонстрировать работу клавиатуры сделал Workflow из нажатий различных комбинаций клавиш и откатов назад. Симулировать демонстрацию нажатий клавиш путем вывода значения в консоль и задержкой между нажатиями")
    printHistory(actions)

    undo_last_action(actions)
    printHistory(actions)
    Button2.use_Button()
    printHistory(actions)

    print("\nПродемонстрировать переназначение клавиши и комбинации клавиш с перезапуком Workflow")
    actions = Button2.reassign_Button('Ctrl+G', actions)
    printHistory(actions)
