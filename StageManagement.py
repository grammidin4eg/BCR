import string


class Stage:
    def __init__(self):
        pass
    def render(self, screen):
        pass
    def update(self, events):
        return None
    def start(self):
        pass

class StageManager:
    def __init__(self):
        self.list = []
        self.names = []
        self.current = 0
        pass
    def add(self, newStage, name):
        self.list.append(newStage)
        self.names.append(name)
    def getCurrent(self):
        return self.list[self.current]
    def goTo(self, newName: str):
        self.current = self.names.index(newName)
        self.getCurrent().start()
    def render(self, screen):
        self.getCurrent().render(screen)
    def update(self, events):
        newScene = self.getCurrent().update(events)
        if newScene != None:
            if newScene == 'EXIT':
                return 'EXIT'
            self.goTo(newScene)
