# 파일 경로: ranpick/__init__.py
import time
import hashlib
import inspect
from typing import List, Tuple, Union

class RanpickError(Exception):
    """ranpick 모듈의 커스텀 에러 클래스"""
    def __init__(self, message: str, code: str):
        frame = inspect.currentframe().f_back
        line_number = frame.f_lineno
        self.message = f"ranpickError: (Line {line_number}) {message}: {code}"
        super().__init__(self.message)

def _generate_seed() -> int:
    """
    현재 시간을 기반으로 해시값을 생성하여 난수 시드를 반환하는 내부 함수.
    """
    current_time = time.time_ns()  # 나노초 단위 현재 시간
    time_hash = hashlib.sha256(str(current_time).encode()).hexdigest()
    seed = int(time_hash, 16)  # 16진수를 정수로 변환
    return seed

def ranrandom(*options: Union[str, Tuple[str, int]]) -> str:
    """
    리스트에서 랜덤으로 항목을 선택하는 함수.
    
    - 단순한 항목 리스트를 제공하거나, 확률을 지정 가능.
    - 확률 합이 100이 아니거나 선택 항목이 2개 미만인 경우 에러를 발생시킴.
    - 확률 미지정 시 균등 분배로 자동 설정.
    """
    if len(options) < 2:
        raise RanpickError(
            "At least two options must be provided",
            code=str(options)
        )

    items = []
    probabilities = []

    for option in options:
        if isinstance(option, tuple):
            item, probability = option
            if not isinstance(probability, int) or probability < 0:
                raise RanpickError(
                    "Invalid probability value",
                    code=str(option)
                )
            items.append(item)
            probabilities.append(probability)
        elif isinstance(option, str):
            items.append(option)
        else:
            raise RanpickError(
                "Invalid option format",
                code=str(option)
            )

    if len(probabilities) == 0:
        probabilities = [100 // len(items)] * len(items)
        for i in range(100 % len(items)):
            probabilities[i] += 1

    if sum(probabilities) != 100:
        raise RanpickError(
            "The sum of each probability does not add up to 100",
            code=str(options)
        )

    cumulative_weights = []
    cumulative_sum = 0
    for p in probabilities:
        cumulative_sum += p
        cumulative_weights.append(cumulative_sum)

    random_seed = _generate_seed() % 100
    for idx, weight in enumerate(cumulative_weights):
        if random_seed < weight:
            return items[idx]
