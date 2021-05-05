from .format import Format

class Repo():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._description = data['description']
        self._language = data['language']
        self._save()
    
    def _save(self): 
        self.all.append(self)
        # self.count += 1
    
    @property
    def info(self):
        description = self._description
        if description == None: 
            description = "This repo has no description"
        return f'{Format.GREEN}{self._name.upper()}: {Format.CLEAR}{description}\n\tLanguages used: {self._language} '
    
    @classmethod
    def find_by_id(cls, index):
        return cls.all[int(index)]
    

