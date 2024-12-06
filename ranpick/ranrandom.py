from .errors import RanpickError

def ranrandom(*choices, k: int = 1):
    """
    리스트 요소 랜덤 선택 (다중 선택 지원).
    
    Args:
        choices:
          - 예: ("왼쪽"33, "오른쪽"33, "가운데"33, "꽝"1)
          - 각 옵션은 "옵션명"확률 형식으로 작성.
        k: 선택할 요소의 개수. 기본값은 1.
    
    조건:
        1. 옵션 최소 2개 이상.
        2. 확률의 합은 100이어야 함.
        3. k는 1 이상이어야 함.
    
    Returns:
        선택된 요소들의 리스트 (k = 1이면 단일 요소 반환).
    """
    # 유효성 검사
    if len(choices) < 2:
        raise RanpickError("You must provide at least two options to choose from.")
    if k < 1:
        raise RanpickError("The number of selections (k) must be at least 1.")
    
    elements = []
    probabilities = []

    for choice in choices:
        try:
            option, probability = choice[:-2], int(choice[-2:])
            elements.append(option)
            probabilities.append(probability)
        except (ValueError, IndexError):
            raise RanpickError(f"Invalid input format: {choice}. Expected format is 'option'percentage.")

    # 확률 합 확인
    if sum(probabilities) != 100:
        raise RanpickError(
            "The sum of each probability does not add up to 100.",
            line_number=choices.index(choice) + 1,
            code_snippet=str(choices)
        )

    # 랜덤 요소 선택
    from random import choices as random_choices
    selected = random_choices(elements, probabilities, k=k)
    return selected[0] if k == 1 else selected
