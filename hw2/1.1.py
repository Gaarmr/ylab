from dataclasses import dataclass, field


@dataclass
class Point:
    x: float
    y: float

    def distance(self, oth):
        return ((oth.x - self.x) ** 2 + (oth.y - self.y) ** 2) ** 0.5

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


@dataclass
class State:
    min_path: list[Point] = field(default_factory=list)
    min_cost: float = float('inf')

    def __str__(self) -> str:
        parts = []
        length = 0
        prev_point = self.min_path[0]
        for p in self.min_path:
            length += p.distance(prev_point)
            parts.append(f'{p}[{length}]')
            prev_point = p
        return ' -> '.join(parts) + f' = {length}'


def tsp(state: State, path: list[Point], cost: float = 0, depth: int = 0):
    path_length = len(path)

    if depth == path_length - 1:
        first_point = path[0]
        new_cost = cost + first_point.distance(path[-1])
        if new_cost < state.min_cost:
            state.min_cost = new_cost
            state.min_path = [*path, first_point]
        return

    cur_idx = depth
    next_idx = depth + 1

    for i in range(next_idx, path_length):
        path[next_idx], path[i] = path[i], path[next_idx]
        cur_point = path[cur_idx]
        next_point = path[next_idx]
        new_cost = cost + cur_point.distance(next_point)
        if new_cost < state.min_cost:
            tsp(state, path, new_cost, next_idx)
        path[next_idx], path[i] = path[i], path[next_idx]


state = State()
path = [
    Point(x=0, y=2),
    Point(x=2, y=5),
    Point(x=5, y=2),
    Point(x=6, y=6),
    Point(x=8, y=3),
]


tsp(state=state, path=path)
print(state)
