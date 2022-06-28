def common_attrs(*objs):
    assert len(objs) > 0
    attrs = set(dir(objs[0]))
    for obj in objs[1:]:
        attrs &= set(dir(obj))
    attrs -= set(dir(object))
    return attrs


def gen_666(meet_yield):
    print('start')
    if meet_yield:
        print('yield')
        yield 666
        print('back')
    print('end')
    return 'finished'

class MyCustomData:
    @property
    def size(self):
        return self.size

    def get_value(self, index):
        return index

    def __iter__(self):
        index = -1
        while index < 2:
            index += 1
            yield self.get_value(index)


def coro_averager():
    """计算移动平均值"""
    count = 0
    total = 0
    avg = None
    while True:
        try:
            val = yield avg
        except GeneratorExit:
            return total, count, avg
        else:
            total += val
            count += 1
            avg = total / count