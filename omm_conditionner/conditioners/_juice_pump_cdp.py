from libopensesame.py3compat import *
from ._base_conditioner import BaseConditioner
import serial

DEFAULT_PORT = 'COM4'

class JuicePumpCdp(BaseConditioner):
    def __init__(self, **kwargs):
        super(JuicePumpCdp, self).__init__(**kwargs)
        self._port = kwargs.get('port', DEFAULT_PORT)
        
        self.start = kwargs.get('start', 'S')  # Default start signal
        if not isinstance(self.start, str):
            raise TypeError(f"'start' doit être une chaîne, mais a reçu {type(self.start).__name__}")
        
        self.stop = kwargs.get('stop', 'E')   # Default stop signal
        if not isinstance(self.stop, str):
            raise TypeError(f"'stop' doit être une chaîne, mais a reçu {type(self.stop).__name__}")
        
        self.secondes = kwargs.get('secondes', 5)  # Default duration (5 sec)
        if not isinstance(self.secondes, (int, float)):
            raise TypeError(f"'secondes' doit être un nombre, mais a reçu {type(self.secondes).__name__}")
        
        print(f"kwargs reçus : {kwargs}")  # Debug : imprimer les arguments reçus
        
        self._serial = serial.Serial(self._port)

    def juice(self):
        """
        Activates the juice pump for the specified duration.
        """
        self._serial.write(self.start.encode())  # Send start signal
        self.clock.sleep(self.secondes * 1000)  # Wait for `self.secondes` seconds
        print(self.secondes)
        self._serial.write(self.stop.encode())  # Send stop signal
        print(self.start)

    def close(self):
        """
        Closes the serial connection.
        """
        self._serial.close()
