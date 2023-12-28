import time
class Keyboard:
    def __init__(self, Keyboard_name):
        self.app = {'Ctrl+Alt+Delete': 'Запуск окна настроек.', 'CTRL+A': 'Выбор всех элементов в документе или окне.', 'Ctrl+~':'Открытие консоли'}
        self.Keyboard_name = Keyboard_name
        self.actions = []
        self.active_app = []

    def set_actions(self, actions):
        self.actions = actions

    def get_actions(self):
        return self.actions

    def new_action(self, action_name):
        self.actions.append(action_name)
        self.realise_action(action_name)

    def realise_action(self, press_name):
        if press_name in self.app:
            self.active_app.append(self.app[str(press_name)])
        else:
            self.active_app.append(str(press_name)+' -без действия')
    def delete_app(self,app):
        #app - приложение, которое нужно закрыть
        print('Закрытие: '+str(app))
    def undo_last_action(self):
        if len(self.actions) > 0:
            print('\nUndo last action:')
            last_action = self.actions.pop()
            print(f'Last press - {last_action}')
            last_active_app = self.active_app.pop()
            self.delete_app(last_active_app)
            print(f'Last app - {last_active_app}')

        else:
            print('No recent clicks')

    def print_actions_history(self):
        print('History:')
        for action in self.actions:
            print(action)
        print('')

    def print_actve_app(self):
        print('Active app:')
        for action in self.active_app:
            print(action)
        print('')

class Button:
    def __init__(self, ButtonName, Keyboard = False):
        self.ButtonName = ButtonName
        self.Keyboard = Keyboard
    def get_name(self):
        return self.ButtonName

    def setName(self, newButton):
        self.ButtonName = newButton
    def set_keyboard(self,Keyboard):
        self.Keyboard = Keyboard
    def use_Button(self):
        print(f'Button pressed: {self.ButtonName}')
        time.sleep(0.5)
        self.Keyboard.new_action(self.ButtonName)

    def reassign_Button(self, newButton, actions):
        print(f'Reassign: {self.ButtonName} ==> {newButton}')
        for action in actions:
            if action.get_name() == self.ButtonName:
                action.setName(newButton)
        return actions


if __name__ == '__main__':
    Keyboard1 = Keyboard('Keyboard')
    print(
        "Создать виртуальную клавиатуру с переназначаемыми действиями для клавиш и комбинаций клавиш, с возможностью отката действий назад.")
    Button1 = Button('Ctrl+Z',Keyboard1)
    Button1.use_Button()
    Button2 = Button('Ctrl+Alt+Delete',Keyboard1)
    Button2.use_Button()

    Keyboard1.print_actions_history()
    Keyboard1.print_actve_app()

    Keyboard1.undo_last_action()

    Keyboard1.print_actions_history()
    Keyboard1.print_actve_app()

