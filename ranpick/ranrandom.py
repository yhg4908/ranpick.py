def ranrandom(options: dict, k: int = 1):
    """
    리스트 요소 랜덤 선택 (다중 선택 지원, 딕셔너리 형식).
    
    Args:
        options: 딕셔너리 형식으로 항목과 확률을 전달. 예: {"왼쪽": 33, "오른쪽": 33}
        k: 선택할 요소의 개수. 기본값은 1.
    
    Returns:
        선택된 요소들의 리스트 (k = 1이면 단일 요소 반환).
    """
    if not choices:
        raise ValueError("No choices provided. Please pass at least one option.")
    
    if k <= 0:
        raise ValueError(f"Invalid k value: {k}. It must be a positive integer.")
    
    if k > len(choices):
        raise ValueError(f"Invalid k value: {k}. It cannot be greater than the number of choices.")
  
    elements = list(options.keys())
    probabilities = list(options.values())

    from random import choices as random_choices
    selected = random_choices(elements, probabilities, k=k)
    return selected[0] if k == 1 else selected
