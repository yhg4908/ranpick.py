def ranrandom(options: dict, k: int = 1):
    """
    딕셔너리를 이용한 리스트 요소 랜덤 선택 (다중 선택 지원).
    
    Args:
        options (dict): 선택지와 확률을 나타내는 딕셔너리.
            예: {"왼쪽": 33, "오른쪽": 33, "가운데": 33, "꽝": 1}
        k (int): 선택할 요소의 개수. 기본값은 1.
    
    조건:
        1. 옵션 최소 2개 이상.
        2. 확률의 합은 100이어야 함.
        3. k는 1 이상이어야 함.
    
    Returns:
        선택된 요소들의 리스트 (k = 1이면 단일 요소 반환).
    """
    # 유효성 검사
    if not isinstance(options, dict):
        raise ValueError("ranpickError: Options must be provided as a dictionary.")
    if len(options) < 2:
        raise ValueError("ranpickError: You must provide at least two options to choose from.")
    if k < 1:
        raise ValueError("ranpickError: The number of selections (k) must be at least 1.")

    elements = list(options.keys())
    probabilities = list(options.values())

    # 확률 합 확인
    if sum(probabilities) != 100:
        raise ValueError(
            f"ranpickError: The sum of each probability does not add up to 100. (Input: {options})"
        )

    # 랜덤 요소 선택
    from random import choices as random_choices
    selected = random_choices(elements, probabilities, k=k)
    return selected[0] if k == 1 else selected
