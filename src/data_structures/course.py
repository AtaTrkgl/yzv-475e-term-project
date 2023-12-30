from data_structures.lesson import Lesson

class Course:
    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name
        self.lessons = []

    def __str__(self) -> str:
        return f"{self.code} - {self.name}, lesson count: {len(self.lessons)}"

    def __repr__(self) -> str:
        return self.__str__()

    def assign_lessons(self, lessons: list[Lesson]) -> None:
        self.lessons = [l for l in lessons if l.code == self.code]

    @staticmethod
    def from_rows(rows: list[str]) -> list:
        courses = []
        for cr in rows:
            if "#" in cr: continue
            cells = cr.split("|")
            if len(cells[0]) == 0: continue

            courses.append(Course(cells[0], cells[1]))

        return courses