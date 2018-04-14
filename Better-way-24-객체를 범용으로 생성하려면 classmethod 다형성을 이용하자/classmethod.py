# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 파이썬에서는 클래스별로 생성자를 한 개(__init__ 메서드)만 만들 수 있다.
* 클래스에 필요한 다른 생성자를 정의하려면 @classmethod를 사용하자.
* 구체 서브클래스들을 만들고 연결하는 범용적인 방법을 제공하려면 클래스 메서드 다형성을 이용하자.

## 참고

* 이 파일은 실행용이 아닌, 정리용입니다. 아래로 가면서 변화를 정리하였습니다.
'''
import os


class InputDate(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")
    
    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers):
    threads = [Thread(target=-w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


class GenericInputData(object):
    def read(self):
        raise NotImplementedError
    
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    # ...
    def read(self):
        raise open(self.path).read()
    
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    # ...
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError
    
    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    # ...


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    config = {"data_dir": tmpdir}
    result = mapreduce(Linecountworker, PathInputData, config)
