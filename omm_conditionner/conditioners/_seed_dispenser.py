from libopensesame.py3compat import *
from ._base_conditioner import BaseConditioner
import serial

DEFAULT_PORT = 'COM4'

# Seed dispenser
SEED_DISPENSER_ON = b'S10'
SEED_DISPENSER_OFF = b'S11'
# Other signals needed for initialization?
MEMORY_OFF = b'M0'
DIGITAL_ENTRY = b'IN1D'
# Left sound
SOUND_LEFT_ON = b'S21'
SOUND_LEFT_OFF = b'S20'
# Right sound
SOUND_RIGHT_ON = b'S31'
SOUND_RIGHT_OFF = b'S30'
# Parameter for seed dispenser
DEFAULT_MOTOR_N_PULSES = 5
DEFAULT_MOTOR_PAUSE = 200


class SeedDispenser(BaseConditioner):
    
    def __init__(self, **kwargs):
        
        super(SeedDispenser, self).__init__(**kwargs)
        self._port = kwargs.get('port', DEFAULT_PORT)
        self.motor_n_pulses = kwargs.get(
            'motor_n_pulses',
            DEFAULT_MOTOR_N_PULSES
        )
        self.motor_pause = kwargs.get(
            'motor_pause',
            DEFAULT_MOTOR_PAUSE
        )
        self._serial = serial.Serial(self._port)
        
    def _stop(self, seed_dispenser=False, sound_left=False, sound_right=False):
        
        self._serial.write(MEMORY_OFF)
        self._serial.write(DIGITAL_ENTRY)
        self._serial.write(SEED_DISPENSER_OFF)
        self._serial.write(SOUND_LEFT_OFF)
        self._serial.write(SOUND_RIGHT_OFF)
        self._serial.flush()
        
    def reward(self):
        print("get in there Lewis")

        self._stop(seed_dispenser=True)
        for _ in range(self.motor_n_pulses):
            self._serial.write(SEED_DISPENSER_ON)
            self._serial.flush()
            self.clock.sleep(self.motor_pause)
            self._serial.write(SEED_DISPENSER_OFF)
            self._serial.flush()
            self.clock.sleep(self.motor_pause)

    def sound_left(self):
        
        self._stop(sound_right=True)
        self._serial.write(SOUND_LEFT_ON)
        self._serial.flush()

    def sound_right(self):
        
        self._stop(sound_left=True)
        self._serial.write(SOUND_RIGHT_ON)
        self._serial.flush()
        
    def sound_off(self):
        
        self._stop(sound_left=True, sound_right=True)
    
    def sound_both(self):
        
        self._serial.write(SOUND_LEFT_ON)
        self._serial.write(SOUND_RIGHT_ON)
        self._serial.flush()

    def close(self):
        
        self._serial.close()
