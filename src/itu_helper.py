from data_structures.lesson import Lesson
from data_structures.course import Course
from logger import Logger

from requests import get
from os import path

BUILDING_CODES_URL = r"https://raw.githubusercontent.com/itu-helper/data/main/building_codes.txt"
LESSONS_URL = r"https://raw.githubusercontent.com/itu-helper/data/main/lesson_rows.txt"
COURSES_URL = r"https://raw.githubusercontent.com/itu-helper/data/main/course_rows.txt"

class ItuHelper:
    def __init__(self) -> None:
        self.initilize_data()

    def initilize_data(self):
        # Fetch the lessons
        lesson_rows = self._fetch_data(LESSONS_URL, "lesson_rows")
        self.lessons = Lesson.from_rows(lesson_rows)

        # Fetch the courses
        courses_rows = self._fetch_data(COURSES_URL, "course_rows")
        self.courses = Course.from_rows(courses_rows)
        for c in self.courses:
            c.assign_lessons(self.lessons)

        # Fetch the building codes
        building_rows = self._fetch_data(BUILDING_CODES_URL, "building_codes")
        self._building_map = dict()
        for row in building_rows[:-1]:
            cells = row.split("|")
            self._building_map[cells[0]] = [cells[1], cells[2]]

    def print_counts(self):
        print("Total number of lessons:", len(self.lessons))  
        print("Total number of courses:", len(self.courses))
        print("Total number of buildings:", len(self._building_map))

    def get_building_from_lesson(self, lesson: Lesson) -> tuple[list[str], list[str]]:
        buildings, campuses = [], []
        for c in lesson.buildings:
            b, ca = self._get_building_info(c)
            buildings.append(b)
            campuses.append(ca)

        return buildings, campuses

    def _get_building_info(self, building_code: str) -> tuple[str, str]:
        # if the building is not specified
        if "--" in building_code:
            return None, None
        
        if building_code not in self._building_map:
            Logger.log_error(f"Could not find building code for {building_code}")
            return None, None

        data = self._building_map[building_code]
        return data[0], data[1]

# region DATA FETCHERS
    def _cache_file(self, lines: list[str], name: str) -> None:
        with open(f"./data/{name}.txt", "w", encoding="utf-16") as f:
            f.writelines([r + "\n" for r in lines])
    
    def _read_cache(self, name: str) -> list[str] | None:
        if not path.exists(f"./data/{name}.txt"):
            return None

        with open(f"./data/{name}.txt", "r", encoding="utf-16") as f:
            return f.readlines()
    
    def _fetch_data(self, url: str, name: str) -> list[str]:
        Logger.log_info(f"Fetching {name} data...")
        try:
            # try to fetch the data from the url
            rows = get(url).text.split("\n")
        except Exception:
            # if an error occurs, try to read from cache
            Logger.log_error("An error occured while fetching data, reading from cache...")
            rows = self._read_cache(name)
        
        if rows is None:
            raise Exception(f"Could not fetch {name} rows")
        else:
            Logger.log_info(f"Saving {name} data to cache...")
            self._cache_file(rows, name)

        rows = [row for row in rows if len(row.strip()) > 0]

        return rows
# endregion