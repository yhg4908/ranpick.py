import time
import hashlib
from typing import Union

class Ranpick:
    @staticmethod
    def number(start: Union[int, str] = 0, end: Union[int, str] = 100000000, precision: str = None) -> Union[int, float]:
        """
        Generates a random number within a given range, optionally with decimal precision.
        :param start: Starting value of the range (can be int or evaluatable str).
        :param end: Ending value of the range (can be int or evaluatable str).
        :param precision: Decimal precision format (e.g., "d3" for 3 decimal places).
        :return: Random number as int or float.
        """
        
        # Evaluate start and end if they are expressions
        if isinstance(start, str):
            start = eval(start)
        if isinstance(end, str):
            end = eval(end)
        
        # Ensure proper range
        if start > end:
            start, end = end, start

        # Generate a base seed using nanoseconds and a hash function
        current_time = time.time_ns()
        seed = int(hashlib.sha256(str(current_time).encode()).hexdigest(), 16)
        rng = seed % (end - start + 1) + start

        if precision and precision.startswith('d'):
            decimals = int(precision[1:])
            scale = 10 ** decimals
            rng = round(start + (rng % (end - start)) / scale, decimals)    

        return rng
