
# Ranpick



`Ranpick`은 기존의 PRNG 방식의 단점을 보완하고 나노초, 해시 기반의 시스템으로 난수를 생성합니다.

현재 문자를 이용한 시스템도 개발중에 있습니다.

버전: V2.0.0

---



## 설치



1. `pip`을 사용하여 ranpick을 설치합니다.:

   ```bash
   pip install ranpick
   ```
2. 코드(.py)에 아래 import문을 추가하여 ranpick을 불러옵니다.:

   ```python
   import ranpick
   ```



## 모듈 및 사용가이드


`2024.12.6 (KST)` 기준으로 현재 이용가능한 모듈은 아래와 같습니다.

- rannumber : `숫자형태의 난수를 생성합니다.`
- ranrandom : `리스트에서 랜덤한 값을 선택합니다.` (2.1.0 부터 적용예정)


### rannumber - 숫자난수 생성


`number`는 일반적인 숫자형태의 난수를 생성합니다.

최대 100000000 까지의 수를 생성할수 있습니다.



#### 기본



아래와 같은 방식으로 number 모듈을 사용할수 있습니다.
```python
random_number = ranpick.rannumber() # random_number 변수에 ranpick number 모듈로 뽑은 난수(~100000000)를 저장합니다.

print(random_number) # random_number 변수의 값을 출력합니다.
print(ranpick.rannumber()) # ranpick number 모듈로 뽑은 난수의 값을 출력합니다.
```
기본적인 number 모듈 사용방법 입니다. `ranpick.rannumber()`로 난수를 생성할 수 있습니다.


#### 난수의 수 제한



난수의 수를 제한할수도 있습니다. 아래 예제코드는 난수를 5~10 사이로 제한하는 코드입니다.
```python
limit_number = ranpick.rannumber(5, 10)

print(limit_number)
print(ranpick.rannumber(5, 10))
```
`ranpick.rannumber(5, 10)`은 난수의 수를 5~10 사이로 제한할수 있는 코드입니다. `()` 안에 `시작숫자,도착숫자`를 넣어 완성할 수 있습니다.

`2+3,10/2`등 계산식을 이용해서도 난수의 수를 제한할 수 있으며 이 후 서술할 모든 내용에서도 사용 가능합니다.


#### 소수점 자릿수 설정



기본적으로 생성된 난수는 오직 정수로만 생성이 가능합니다. 하지만 아래 예제를 참고하면 소수의 출력도 가능합니다.
```python
decimal_number = ranpick.rnanumber(0, 1, "d3")

print(decimal_number)
print(ranpick.rannumber(0, 1, "d3"))
```
이 예제코드는 0~1 사이의 수를 소수 셋째자리 수까지 출력하는 코드입니다. `"d3"`는 소수 셋째자리 수까지 출력한다는 의미입니다.

만약 `"d4"`를 사용하면 소수 넷째자리 수까지 출력이 가능합니다.

최대 10자리 수까지 가능합니다.


#### 응용



아래의 코드들은 이 모듈과 다른 라이브러리, 모듈을 응용하여 제작된 코드입니다. 여기서 사용된 예 외에도 다양한 다른 라이브러리와 응용이 가능합니다.

##### datetime 라이브러리 응용
아래는 datetime 라이브러리를 사용하여 응용한 코드입니다.
```python
import ranpick
from datetime import datetime

date_number = int(datetime.now().strftime("%Y%m%d%H%M%S"))

print(ranpick.rannumber(date_number, date_number × 10))
```
이 코드는 datetime 라이브러리에서 출력된 시간을 활용하여 난수를 출력하도록 만들었습니다.

##### ramdom 모듈 응용
아래는 random 모듈을 사용하여 응용한 코드입니다.
```python
import random
import random

random_number = random.randint(1,10)

print(random_number, 100)
```
이 코드는 random 모듈로 출력된 난수를 아용해 또 한번 난수를 생성합니다. 응용을 하면 거의 예측 불가능의 난수를 만들 수 있습니다.

다만 이 방식의 코드를 사용하면 컴퓨터의 많은 리소스가 요구되기 때문에 권장하지 않습니다.


### ranrandom - 랜덤한 값 선택
`random`은 리스트에서 값을 하나 선택하여 출력합니다.


#### 기본
아래의 방식으로 random 모듈을 사용할수 있습니다.
```python
random = ranpick.ranrandom("왼쪽", "오른쪽", "가운데", "꽝")

print(random)
print("왼쪽", "오른쪽", "가운데", "꽝")
```
`ranpick.ranrandom()`을 이용할수 있습니다. `()` 안에는 `("당첨", "꽝")`같은 형식으로 작성할 수 있습니다.
이곳에 넣은 항목들 중 하나를 랜덤으로 선택합니다.
이곳의 항목은 두개 이상 작성되어야 합니다.


#### 확률설정
각 항목의 확률을 설정할 수 있습니다. 아래 예제코드를 참조해주세요.
```python
random = ranpick.ranrandom(("왼쪽", 33), ("오른쪽", 33), ("가운데", 33), ("꽝", 1))

print(random)
print(("왼쪽", 33), ("오른쪽", 33), ("가운데", 33), ("꽝", 1))
```
`()`안에 또 하나의 `()`를 추가합니다. 추가한 `()`안에는 `("항목명1", 확률[%])`형식으로 작성할 수 있습니다.
모든 확률은 총 합 100이 되어야 하며 합이 안될경우 오류가 발생합니다.

```python
print("왼쪽", ("오른쪽", 50), "가운데", "꽝")
```
이와같이 확률이 일부 누락될경우 누락되어있는 남은 확률을 자동적으로 재분배 합니다.

## 버그 리포트

버그 리포트를 할때는 아래 사이트(github)에서 해주세요.

<https://github.com/yhg4908/ranpick.py/issues>
