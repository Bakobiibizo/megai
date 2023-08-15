class TheCount():
    count: int = 0

    def up(self) -> int:
        self.count += 1
        return self.count

    def down(self) -> int:
        if self.count >= 1:
            self.count -= 1
        else:
            self.count = 0
        return self.count

    def value(self) -> int:
        return self.count

    def set(self, value: int) -> int:
        value = max(value, 0)
        self.count = value
        return self.count

    def reset(self) -> int:
        self.count = 0
        return self.count


if __name__ == '__main__':
    TheCount()
