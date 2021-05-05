from .api import fetch_repos
from .repo import Repo
from .format import Format

class CLI(): 
    def _init_(self): 
        self._user_input =""
    
    def start(self):
        print(f'\n{Format.BLUE}{Format.BOLD}Welcome to Github on CLI...{Format.CLEAR}\n')
        self.get_input()
        fetch_repos(self._user_input)
        self.show_repos()

    def get_input(self): 
        try: 
            self._user_input = input(f'\n{Format.BLUE}What is your GitHub username?{Format.CLEAR}\n')
            #print(self._user_input)
        except ValueError: 
            print(f'{Format.RED}Wrong input')
            self.get_input()

    def show_repos(self): 
        for i, repo in enumerate(Repo.all):
            repo = Repo.find_by_id(i)
            print(f'Repo {i} - {repo.info}')
        #repo = Repo.find_by_id()
        

if __name__ == '__main__':
    app = CLI()
