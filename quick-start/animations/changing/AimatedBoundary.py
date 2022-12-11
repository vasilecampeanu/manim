from manim import *

class AnimatedBoundary(Scene):
    def construct(self):
        text = Text("Hello world!")
        boundary = AnimatedBoundary(text, colors = [RED, GREEN, BLUE], cycle_rate = 3)

        self.add(text, boundary)
        self.wait(2)
        
        return super().construct()
