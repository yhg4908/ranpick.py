import time

import hashlib

from typing import Union, Optional



class RanPick:

    @staticmethod

    def number(

        start: Union[int, float] = 0, 

        end: Union[int, float] = 100000000, 

        decimal_places: Optional[int] = None

    ) -> Union[int, float]:

        """

        Generate a random number within a specified range.

        - start: Start of the range (inclusive).

        - end: End of the range (exclusive).

        - decimal_places: If specified, generates a floating-point number with this many decimal places.



        Uses nanoseconds and hash values to ensure randomness.

        """

        # Current nanoseconds for unique seed

        nano_time = time.time_ns()

        

        # Hash the nano_time for additional randomness

        hash_seed = int(hashlib.sha256(str(nano_time).encode()).hexdigest(), 16)

        

        # Compute a random value within range

        random_base = hash_seed % (10**8) / (10**8)  # Normalize to [0, 1)

        random_value = start + (end - start) * random_base



        # If decimal places are specified, round the result

        if decimal_places is not None:

            return round(random_value, decimal_places)

        

        # Otherwise, return an integer

        return int(random_value)
