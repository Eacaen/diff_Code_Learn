class Student(object):
    def __init__(self,value=60):
        self._score = value

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
print s.get_score()
s.set_score(60000)
print s.get_score()
print s._score