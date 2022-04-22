class Car:
    tracks = []

    def __init__(self, i, xi, yi, max_age):
        self.i = i
        self.x = xi
        self.y = yi
        self.tracks = []
        self.done = False
        self.state = '0'
        self.age = 0
        self.max_age = max_age
        self.dir = None

    def get_id(self):  # For the ID
        return self.i

    def get_state(self):
        return self.state

    def get_dir(self):
        return self.dir

    def get_x(self):  # for x coordinate
        return self.x

    def get_y(self):  # for y coordinate
        return self.y

    def update_coordinates(self, xn, yn):
        self.age = 0
        self.tracks.append([self.x, self.y])
        self.x = xn
        self.y = yn

    def set_done(self):
        self.done = True

    def timed_out(self):
        return self.done

    def going_up(self, mid_start, mid_end):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][1] < mid_end <= self.tracks[-2][1]:
                    self.dir = 'up'
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def going_down(self, mid_start, mid_end):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][1] > mid_start >= self.tracks[-2][1]:

                    self.dir = 'down'
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def age_one(self):
        self.age += 1
        if self.age > self.max_age:
            self.done = True
        return True
