

class PDController:
    def __init__(self, k_p, k_d, x_target=0, v_target=0):
        # Constants
        self.KP = k_p
        self.KD = k_d

        # Variables
        self.torque = 0
        self.x_target = x_target
        self.x = 0
        self.v_target = v_target
        self.v = 0
        self.t = 0

    def set_target(self, x_target):
        '''
        Method to reset x target to be achieved
        
        `x_target` = 
        '''
        self.x_target = x_target

    def update(self, time_interval, x):
        '''Increases time interval and increases the '''
        self.v = (x - self.x) / time_interval
        self.x = x
        e_x = self.x - self.x_target
        e_v = self.v - self.v_target
        self.t += time_interval
        self.torque = self.KP * e_x + self.KD * e_v
        return self.torque
