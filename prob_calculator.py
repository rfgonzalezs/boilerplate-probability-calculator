import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.full_hat = []
        self.y = 0
        # create list of all balls using passes dict
        for x in balls:
            ball_count = balls.get(x)
            while self.y < ball_count:
                self.full_hat.append(x)
                self.y += 1
                if self.y == ball_count:
                    self.y = 0
                    break
        self.contents = copy.copy(self.full_hat) # copy to allow 1st draw remainder

    # Random draw function without remplacement
    def draw(self, draw_number):
        self.contents = copy.copy(self.full_hat)
        if draw_number >= len(self.contents):
            return (self.full_hat)
        else:
            self.result = (random.sample(self.full_hat, k=draw_number))
            for x in self.result:
                self.contents.remove(x)
            return (self.result)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiment_number = 0
    m = 0  # overall matches
    match = 0  #  experiment match
    while experiment_number < num_experiments:
        ex_match = copy.copy(match)  # copy to allow reset
        experiment_number += 1
        result_list = (hat.draw(num_balls_drawn)) 
        result_to_check = {i: result_list.count(i)
                           for i in result_list}  # convert result to dict
        for k, v in expected_balls.items(): # dict comparison for result
            if k in result_to_check and v <= result_to_check.get(k):
                ex_match += 1
            if ex_match == len(expected_balls):
                m += 1
    return (m / num_experiments)