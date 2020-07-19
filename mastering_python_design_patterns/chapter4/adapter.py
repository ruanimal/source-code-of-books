"""
适配器模式, 实现不同接口之间的兼容
1. 不修改原有接口的实现
2. 不违反开放封闭原则

"""


import os,sys
work_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(work_dir); sys.path.insert(0, work_dir); del work_dir

from external import Synthesizer, Human


class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Adapter:

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))

if __name__ == "__main__":
    main()
