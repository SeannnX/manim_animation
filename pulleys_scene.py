# ...existing code...
from manim import *


class PulleyLecture(Scene):
    """Lecture scene explaining fixed and movable pulleys."""

    def construct(self):
        title = Text("动滑轮与定滑轮的对比与应用", font_size=60)
        subtitle = Text("机械优势、受力特点与绳长变化", font_size=36).next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle, shift=DOWN * 0.3))
        self.wait(1.5)
        self.play(FadeOut(subtitle))

        fixed_group = self.create_fixed_pulley_diagram()
        movable_group = self.create_movable_pulley_diagram()

        diagrams = VGroup(fixed_group, movable_group).arrange(RIGHT, buff=1.5).shift(DOWN * 0.5)
        fixed_title = Text("定滑轮", font_size=40)
        movable_title = Text("动滑轮", font_size=40)
        titles = VGroup(fixed_title, movable_title).arrange(RIGHT, buff=2).next_to(diagrams, UP)

        self.play(FadeIn(diagrams, shift=UP), FadeIn(titles))
        self.wait(0.5)

        self.explain_fixed_pulley(fixed_group)
        self.wait(0.5)
        self.explain_movable_pulley(movable_group)
        self.wait(0.5)

        comparison = VGroup(
            Text("定滑轮: 省力不省距离, 改变力的方向", font_size=34),
            Text("动滑轮: 省力但需要更长绳长, 不改变力的方向", font_size=34),
            Text("组合滑轮组可兼顾方向与省力", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT)
        comparison.to_edge(DOWN, buff=0.8)

        highlight_rect = SurroundingRectangle(comparison, color=YELLOW, buff=0.3)
        self.play(Write(comparison), Create(highlight_rect))
        self.wait(2)

    def create_fixed_pulley_diagram(self):
        ceiling = Line(LEFT * 2, RIGHT * 2).shift(UP * 2.5)
        pulley = Circle(radius=0.6, color=BLUE).shift(UP * 1.5)
        axle = Dot(pulley.get_center(), color=WHITE)
        hook = Line(pulley.get_center(), pulley.get_center() + UP * 1)

        load = Square(side_length=0.8, color=GRAY, fill_opacity=0.7).shift(DOWN * 1.2)
        load_label = Text("重物 G", font_size=32).next_to(load, DOWN, buff=0.2)

        rope_left = Line(LEFT * 2, pulley.get_left())
        rope_right = Line(pulley.get_right(), RIGHT * 2)
        rope_drop = Line(pulley.get_bottom(), load.get_top())

        force_arrow = Arrow(start=RIGHT * 2, end=RIGHT * 2 + DOWN * 1.2, color=YELLOW)
        force_text = Text("F", font_size=32, color=YELLOW).next_to(force_arrow, RIGHT * 0.3)

        group = VGroup(ceiling, pulley, axle, hook, load, load_label, rope_left, rope_right, rope_drop, force_arrow, force_text)
        return group

    def create_movable_pulley_diagram(self):
        ceiling = Line(LEFT * 2, RIGHT * 2).shift(UP * 2.5)
        pulley = Circle(radius=0.6, color=GREEN).shift(UP * 0.7)
        axle = Dot(pulley.get_center(), color=WHITE)

        load = Square(side_length=0.8, color=GRAY, fill_opacity=0.7).shift(pulley.get_center() + DOWN * 1.2)
        load_label = Text("重物 G", font_size=32).next_to(load, DOWN, buff=0.2)

        fixed_hook = Dot(ceiling.get_left())
        rope_top = Line(ceiling.get_left(), pulley.get_top())
        rope_bottom_left = Line(pulley.get_bottom(), load.get_top())
        rope_bottom_right = Line(load.get_top(), RIGHT * 2 + load.get_top() - load.get_center())

        free_end = RIGHT * 2 + load.get_top() - load.get_center()
        force_arrow = Arrow(start=free_end, end=free_end + DOWN * 1.2, color=YELLOW)
        force_text = Text("F", font_size=32, color=YELLOW).next_to(force_arrow, RIGHT * 0.3)

        ratio_text = Text("理论机械效率: 1/2", font_size=32).next_to(pulley, UP, buff=0.2)

        group = VGroup(
            ceiling,
            pulley,
            axle,
            load,
            load_label,
            fixed_hook,
            rope_top,
            rope_bottom_left,
            rope_bottom_right,
            force_arrow,
            force_text,
            ratio_text,
        )
        return group

    def explain_fixed_pulley(self, group):
        arrow = Arrow(start=group.get_right() + RIGHT * 0.5, end=group.get_right(), color=YELLOW)
        text = Text("轴固定不动\n输出力方向改变\n机械优势约为 1", font_size=30)
        box = VGroup(arrow, text.arrange(DOWN, aligned_edge=LEFT))
        box.next_to(group, RIGHT, buff=0.6)

        self.play(Create(arrow), Write(text))
        self.wait(1)
        self.play(Indicate(group[1], color=BLUE))
        self.play(Indicate(group[9], color=YELLOW))

    def explain_movable_pulley(self, group):
        arrow = Arrow(start=group.get_right() + RIGHT * 0.5, end=group.get_right(), color=YELLOW)
        text = Text("轴随重物移动\n分担重力: F≈G/2\n需要牺牲绳长", font_size=30)
        box = VGroup(arrow, text.arrange(DOWN, aligned_edge=LEFT))
        box.next_to(group, RIGHT, buff=0.6)

        self.play(Create(arrow), Write(text))
        self.wait(1)
        self.play(Indicate(group[1], color=GREEN))
        self.play(Indicate(group[9], color=YELLOW))
# ...existing code...