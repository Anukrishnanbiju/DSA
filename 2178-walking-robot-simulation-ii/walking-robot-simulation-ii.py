class Robot:

    def __init__(self, width: int, height: int):
        self.isOrigin = True
        self.i = 0

        self.pos = [((0, 0), "South")]

        for x in range(1, width):
            self.pos.append(((x, 0), "East"))

        for y in range(1, height):
            self.pos.append(((width - 1, y), "North"))

        for x in range(width - 2, -1, -1):
            self.pos.append(((x, height - 1), "West"))

        for y in range(height - 2, 0, -1):
            self.pos.append(((0, y), "South"))

    def step(self, num: int) -> None:
        self.isOrigin = False
        self.i = (self.i + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return list(self.pos[self.i][0])

    def getDir(self) -> str:
        if self.isOrigin:
            return "East"
        return self.pos[self.i][1]