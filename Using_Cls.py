class Counter:
    count = 0

    def __init__(self):
        Counter.count += 2

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

c5 = Counter()
c6 = Counter()
c5 = Counter()

Counter.show_count()
