
class Lesson:
    def __init__(self, crn: int, code: str, instructor: str, buildings: list[str], capacity: int, enrolled: int, days: list[str], times: list[str]) -> None:
        self.crn = crn
        self.code = code
        self.instructor = instructor
        self.buildings = buildings
        self.capacity = capacity
        self.enrolled = enrolled
        self.days = [d for d in days if d.strip() != ""]
        self.times = [t for t in times if t.strip() != ""]

    def __str__(self) -> str:
        return f"{self.code} ({self.crn}), [Instructor: {self.instructor}, Building: {self.buildings} Capacity: {self.enrolled}/{self.capacity}]"

    def __repr__(self) -> str:
        return self.__str__()

    def get_fullnes(self) -> float | None:
        return self.enrolled / self.capacity if self.capacity > 0 else None
    
    @staticmethod
    def from_rows(rows: list[str]) -> list:
        lessons = []
        for lr in rows:
            cells = lr.split("|")

            lessons.append(Lesson(
                int(cells[0]), cells[1], cells[3], cells[4].split(" "),
                int(cells[8]) if len(cells[8]) > 0 else 0,
                int(cells[9]) if len(cells[9]) > 0 else 0,
                cells[5].lower().split(" "), cells[6].lower().split(" ")
            ))

        return lessons
