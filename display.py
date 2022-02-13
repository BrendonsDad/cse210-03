class Display:
    def __init__(self, player_lives):
        self.display4 = [('  ___  '), (' /___\ '), (' \   / '), ('  \ /  '),
                               ('   0   '), ('  /|\  '), ('  / \  '), ('       '), ('^^^^^^^')]
        self.display3 = [(' /___\ '), (' \   / '), ('  \ /  '),
                               ('   0   '), ('  /|\  '), ('  / \  '), ('       '), ('^^^^^^^')]
        self.display2 = [(' \   / '), ('  \ /  '),
                               ('   0   '), ('  /|\  '), ('  / \  '), ('       '), ('^^^^^^^')]
        self.display1 = [('  \ /  '),
                               ('   0   '), ('  /|\  '), ('  / \  '), ('       '), ('^^^^^^^')]
        self.display0 = [
                               ('   x   '), ('  /|\  '), ('  / \  '), ('       '), ('^^^^^^^')]
        

    def display_screen(self, player_lives):
        if player_lives == 4:
            for i in self.display4:
                print(i)
        if player_lives == 3:
            for i in self.display3:
                print(i)
        if player_lives == 2:
            for i in self.display2:
                print(i)
        if player_lives == 1:
            for i in self.display1:
                print(i)
        if player_lives == 0:
            for i in self.display0:
                print(i)