import random


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = set()

    def is_mine(self, x, y):
        return y * self.width + x in self.mines

    def adjacent_mines(self, x, y):
        return sum(1 for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                   if (dx != 0 or dy != 0) and
                   0 <= x + dx < self.width and
                   0 <= y + dy < self.height and
                   self.is_mine(x + dx, y + dy))

    def reveal(self, x, y):
        if (x, y) in self.revealed:
            return

        self.revealed.add((x, y))
        if self.is_mine(x, y):
            return

        if self.adjacent_mines(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        self.reveal(x + dx, y + dy)

    def display(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) not in self.revealed:
                    print('?', end=' ')
                elif self.is_mine(x, y):
                    print('*', end=' ')
                else:
                    count = self.adjacent_mines(x, y)
                    print(count if count else '.', end=' ')
            print()

    def is_win(self):
        return len(self.revealed) + len(self.mines) == self.width * self.height

    def is_loss(self, x, y):
        return self.is_mine(x, y)

    def play(self):
        while True:
            self.display()
            x, y = map(int, input("Enter coordinates (x y): ").split())
            if 0 <= x < self.width and 0 <= y < self.height:
                self.reveal(x, y)
                print(self.is_loss(x, y))
                if self.is_loss(x, y):
                    print("Boom! You hit a mine.")
                    self.display()
                    break
                elif self.is_win():
                    print("Congratulations! You've cleared the board.")
                    self.display()
                    break
            else:
                print("Invalid coordinates. Please try again.")


if __name__ == '__main__':
    while True:
        x, y, m = map(int, input("Enter board size and number of mines (x y m): ").split())
        game = Minesweeper(x, y, m)
        game.play()
        tmp = input("type anything to keep playing. type exit to finish.")
        if tmp == "exit":
            break
