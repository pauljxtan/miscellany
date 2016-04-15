#from abc import ABCMeta, abstractmethod

# TODO: make this class abstract
class FlipFlop(object):
    def __init__(self, Q_init):
        self.Q = Q_init
        self.Q_bar = not self.Q

class DFlipFlop(FlipFlop):
    def __init__(self, Q_init=0, D_init=0):
        FlipFlop.__init__(self, Q_init)
        self.D = D_init
        
    def cycle(self):
        if not self.D:
            self.Q = 0
        else:
            self.Q = 1

class TFlipFlop(FlipFlop):
    def __init__(self, Q_init=0, T_init=0):
        FlipFlop.__init__(self, Q_init)
        self.T = T_init

    def cycle(self):
        if not self.T:
            self.Q = self.Q
        else:
            self.Q = not self.Q

class SRFlipFlop(FlipFlop):
    def __init__(self, Q_init=0, S_init=0, R_init=0):
        FlipFlop.__init__(self, Q_init)
        self.S = S_init
        self.R = R_init
        self.check_forbidden()

    def check_forbidden(self):
        if self.S == self.R == 1:
            raise ValueError("S = R = 1 is forbidden")

    def cycle(self):
        self.check_forbidden()
        if not self.S:
            if not self.R:
                self.Q = self.Q
            else:
                self.Q = 0
        elif self.R:
            self.Q = 1

class JKFlipFlop(FlipFlop):
    def __init__(self, Q_init=0, J_init=0, K_init=0):
        FlipFlop.__init__(self, Q_init)
        self.J = J_init
        self.K = K_init

    def cycle(self):
        if not self.J:
            if not self.K:
                self.Q = self.Q
            else:
                self.Q = 0
        else:
            if not self.K:
                self.Q = 1
            else:
                self.Q = not self.Q
