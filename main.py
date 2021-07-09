class Interpreter:
    def __init__(self, source):
        self.source = source
        self.buffer = [0] * 30_000
        self.buffer_pointer = 0
        self.source_pointer = -1

    def eat(self):
        self.source_pointer += 1
        if self.source_pointer >= len(self.source):
            return None

        return self.source[self.source_pointer]

    def spit(self):
        self.source_pointer -= 1
        if self.source_pointer < 0:
            return None

        return self.source[self.source_pointer]

    def eat_to_matching_close(self):
        depth = 1
        while depth != 0:
            token = self.eat()
            if token == "[":
                depth += 1
            elif token == "]":
                depth -= 1
            elif token is None:
                return

    def spit_to_matching_open(self):
        depth = 1
        while depth != 0:
            token = self.spit()
            if token == "]":
                depth += 1
            elif token == "[":
                depth -= 1
            elif token is None:
                return

    def run(self):
        while token := self.eat():
            if token == ">":
                self.buffer_pointer += 1
            elif token == "<":
                self.buffer_pointer -= 1
            elif token == "+":
                self.buffer[self.buffer_pointer] += 1
            elif token == "-":
                self.buffer[self.buffer_pointer] -= 1
            elif token == ",":
                self.buffer[self.buffer_pointer] = ord(input(">> "))
            elif token == ".":
                print(chr(self.buffer[self.buffer_pointer]), end="")

            elif token == "[":
                if not self.buffer[self.buffer_pointer]:
                    self.eat_to_matching_close()

            elif token == "]":
                if self.buffer[self.buffer_pointer]:
                    self.spit_to_matching_open()


code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
print(code)

Interpreter(code).run()
