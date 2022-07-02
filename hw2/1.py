from itertools import permutations


post_office = (0, 2)
griboedov_st = (2, 5)
baker_st = (5, 2)
bolshaya_sadovaya = (6, 6)
evergreen_alley = (8, 3)

addresses = (griboedov_st, baker_st, bolshaya_sadovaya, evergreen_alley)
starting_point = (post_office,)
routes = []


class Route:
    def __init__(self, points):
        self.points = points
        self.path_length = [self.find_lengths(points[i], points[i + 1]) for i in range(len(self.points) - 1)]

    def find_lengths(self, point_1, point_2):
        return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


for permutation in permutations(addresses):
    points = starting_point + permutation + starting_point
    routes.append(Route(points))

optimal_route = min(routes, key=lambda x: sum(x.path_length))

optimal_route_output = str(optimal_route.points[0])
for i in range(1, len(optimal_route.points)):
    optimal_route_output += f' -> {optimal_route.points[i]}[{sum(optimal_route.path_length[:i])}]'
optimal_route_output += f' = {sum(optimal_route.path_length)}'

print(optimal_route_output)
