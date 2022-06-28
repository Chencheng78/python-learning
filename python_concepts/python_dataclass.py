from dataclasses import dataclass, asdict, field, fields
import json
import random
from typing import Optional, List, Dict, Any


def gen_random_id():
    return random.randint(1, 999999)


class Message:
    def __init__(self, mid: int, text: str) -> None:
        self.id: int = mid
        self.text: str = text

    def __repr__(self) -> str:
        return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)


@dataclass(frozen=True)
class Message1:
    text: str = field(default='nihaoa')
    id: int = field(default_factory=gen_random_id)

    @classmethod
    def load(cls, message: str):
        m = json.loads(message)
        id = m.get('id', None)
        text = m.get('text', None)
        return cls(text, id)


    # def __repr__(self) -> str:
    #     return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)


@dataclass
class employee:
    # Attributes Declaration
    # using Type Hints
    name: str
    age: int
    emp_id: str
    city: str = field(init=False, default="patna", repr=False)


@dataclass
class TestCase:
    project_id: int
    module_id: int
    suite_id: int
    test_case_id: str

    @classmethod
    def parse(cls, data: dict) -> "TestCase":
        print(fields(cls))
        for f in fields(cls):
            print(f)
            print(f.name)
        kwargs = {f.name: data[f.name] for f in fields(cls)}
        return cls(**kwargs)


@dataclass
class RunTaskEvent:
    task_id: Optional[int] = None
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    test_cases: List[TestCase] = field(default_factory=list)
    event_type: str = "run_task"

    @classmethod
    def parse(cls, data: Dict[str, Any]) -> "RunTaskEvent":
        self = cls(task_id=data.get("task_id"), device_id=data.get("device_id"), device_name=data.get("device_name"))
        for x in data.get("test_cases"):
            self.test_cases.append(TestCase(**x))
        return self


if __name__ == "__main__":
    # msg = Message1()
    # print(msg)
    #
    # msg2 = Message1.load('{"id": 2, "text": "world"}')
    # print(msg2, asdict(msg2))

    # emp = employee("Satyam", 21, "ksatyam858")
    # print(emp, emp.city)
    project_id: int
    module_id: int
    suite_id: int
    test_case_id: str
    d = {
        'project_id': 22,
        'module_id': 33,
        'suite_id': 44,
        'test_case_id': '55'
    }
    cases = TestCase.parse(d)
    print(cases)