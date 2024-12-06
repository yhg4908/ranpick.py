import time
import hashlib
from typing import Union, Optional
from .errors import RanpickError

def _generate_seed() -> int:
    """나노초를 해시하여 시드 생성"""
    current_time = time.time_ns()
    seed_hash = hashlib.sha256(str(current_time).encode()).hexdigest()
    return int(seed_hash[:16], 16)

def _random_from_seed(seed: int, start: float, end: float, decimal_places: int = 0) -> Union[int, float]:
    """랜덤 숫자 생성"""
    multiplier = 10 ** decimal_places
    scaled_start = int(start * multiplier)
    scaled_end = int(end * multiplier)

    random_value = (seed % (scaled_end - scaled_start + 1)) + scaled_start
    return random_value / multiplier if decimal_places > 0 else random_value

def rannumber(
    start: Union[int, float] = 0, 
    end: Union[int, float] = 100000000, 
    decimal_option: Optional[str] = None
) -> Union[int, float]:
    """
    난수 생성.
    
    - 기본값: 0~100,000,000 사이 정수.
    - start, end 범위 설정 가능.
    - decimal_option: "dX"로 소수 자릿수 설정.
    """
    if isinstance(start, str):
        try:
            start = eval(start)
        except Exception as e:
            raise RanpickError("Invalid start expression.", code_snippet=start) from e
    if isinstance(end, str):
        try:
            end = eval(end)
        except Exception as e:
            raise RanpickError("Invalid end expression.", code_snippet=end) from e

    decimal_places = 0
    if decimal_option and decimal_option.startswith("d"):
        try:
            decimal_places = int(decimal_option[1:])
        except ValueError as e:
            raise RanpickError("Invalid decimal option format.", code_snippet=decimal_option) from e

    if start >= end:
        raise RanpickError("Start value must be less than end value.")

    seed = _generate_seed()
    return _random_from_seed(seed, start, end, decimal_places)
