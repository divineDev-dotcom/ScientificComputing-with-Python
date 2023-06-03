import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            return self.contents
        for _ in range(num_balls):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            drawn_balls.append(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        expected_balls_copy = copy.deepcopy(expected_balls)
        success = True
        for ball, count in expected_balls_copy.items():
            if drawn_balls.count(ball) < count:
                success = False
                break
        if success:
            num_successful_experiments += 1
    return num_successful_experiments / num_experiments
