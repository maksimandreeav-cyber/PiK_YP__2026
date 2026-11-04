def print_result(fun):
    def decor(*args, **kwargs):
        res = fun(*args, **kwargs)
        print(fun.__name__)
        if isinstance(res, list):
            for item in res:
                print(item)
        elif isinstance(res, dict):
            for key, value in res.items():
                print(f'{key} = {value}')
        else:
            print(res)
        return res
    return decor


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

