
# Ranpick



`Ranpick`은 기존의 PRNG 방식의 단점을 보완하고 나노초, 해시 기반의 시스템으로 난수를 생성합니다.

현재 문자를 이용한 시스템도 개잘중에 있습니다.

---



## 설치



1. `pip`을 사용하여 ranpick을 설치합니다.:

   ```bash
   pip install ranpick
   ```
2. 코드(.py)에 아래 import문을 추가하여 ranpick을 불러옵니다.:

   ```python
   from ranpick import (불러올 ranpick 모듈)
   ```



## 모듈 및 사용가이드


`2024.12.3 (KST)` 기준으로 현재 이용가능한 모듈은 아래와 같습니다.

- number : `숫자형태의 난수를 생성합니다.`


### number - 숫자난수 생성


`number`는 일반적인 숫자형태의 난수를 생성합니다.

number 모듈은 아래 import문으로 불러올수 있습니다.
```python
from ranpick import number
```
