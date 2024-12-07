# 파일 경로: ranpick/__init__.py
import time
import hashlib
import inspect
from typing import List, Tuple, Union

class RanpickError(Exception):
    """ranpick 모듈의 커스텀 에러 클래스"""
    def __init__(self, message: str, code: str):
        # 호출 위치 동적 추적
        frame = inspect.currentframe().f_back
        line_number = frame.f_lineno
        self.message = f"ranpickError: (Line {line_number}) {message}: {code}"
        super().__init__(self.message)

def ranrandom(*options: Union[str, Tuple[str, int]]) -> str:
    """
    리스트에서 랜덤으로 항목을 선택하는 함수.
    
    - 단순한 항목 리스트를 제공하거나, 확률을 지정 가능.
    - 확률 합이 100이 아니거나 선택 항목이 2개 미만인 경우 에러를 발생시킴.
    - 확률 미지정 시 균등 분배로 자동 설정.
    """
    # 입력 확인
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

    # 확률 자동 균등 분배
    if len(probabilities) == 0:
        probabilities = [100 // len(items)] * len(items)
        for i in range(100 % len(items)):  # 나머지 확률 분배
            probabilities[i] += 1

    # 확률 합 확인
    if sum(probabilities) != 100:
        raise RanpickError(
            "The sum of each probability does not add up to 100",
            code=str(options)
        )

    # 확률 기반 랜덤 선택
    cumulative_weights = []
    cumulative_sum = 0
    for p in probabilities:
        cumulative_sum += p
        cumulative_weights.append(cumulative_sum)

    random_seed = _generate_seed() % 100
    for idx, weight in enumerate(cumulative_weights):
        if random_seed < weight:
            return items[idx]
