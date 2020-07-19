"""
职责链
    1. 直接访问首个节点
    2. 不能处理则转发给下个节点
    3. 直到没有下个节点
    4. 实现发送方与接收方的解耦(比如物流网络)
"""


class Event:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:

    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):

    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):

    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):

    def handle_down(self, event):
        print('MsgText: {}'.format(event))

def get_next_point(chain, cur):
    try:
        idx = chain.index(cur)
        return chain[idx+1] if idx < len(chain)-1 else None
    except ValueError:
        pass

def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    chain = (mw, sd, msg)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        point = chain[0]
        print('')
        while point:
            print('Sending event -{}- to {}'.format(evt, point.__class__.__name__))
            point.handle(evt)
            point = get_next_point(chain, point)

if __name__ == '__main__':
    main()
