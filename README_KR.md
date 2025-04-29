![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![PyPI](https://img.shields.io/badge/PyPI-3775A9?style=for-the-badge&logo=PyPI&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


# Ranpick
[![PyPI - Version](https://img.shields.io/pypi/v/ranpick)](https://pypi.org/project/ranpick)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ranpick)
[![PyPI Downloads](https://static.pepy.tech/badge/ranpick/month)](https://pepy.tech/projects/ranpick)
[![PyPI Downloads](https://static.pepy.tech/badge/ranpick)](https://pepy.tech/projects/ranpick)



`Ranpick`은 기존의 PRNG 방식의 단점을 보완하고 나노초, 해시 기반의 시스템으로 난수를 생성합니다.


---



## 설치



1. `pip`을 사용하여 ranpick을 설치합니다.:

   ```bash
   pip install ranpick
   ```
2. 코드(.py)에 아래 import문을 추가하여 ranpick을 불러옵니다.:

   ```python
   from ranpick import (사용할 모듈)
   ```



## 모듈 및 사용가이드


`2024.12.22 (KST)` 기준으로 현재 이용가능한 모듈은 아래와 같습니다.

- rannumber : `숫자형태의 난수를 생성합니다.`
- ranrandom : `리스트에서 랜덤한 값을 선택합니다.` (2.1.0~)


### rannumber - 숫자난수 생성


`rannumber`는 일반적인 숫자형태의 난수를 생성합니다.

최대 0~1(3.0.0~) 까지의 수를 생성할수 있습니다.



#### 기본



아래와 같은 방식으로 number 모듈을 사용할수 있습니다.
```python
random_number = rannumber() # random_number 변수에 ranpick number 모듈로 뽑은 난수(~100000000)를 저장합니다.

print(random_number) # random_number 변수의 값을 출력합니다.
print(rannumber()) # ranpick number 모듈로 뽑은 난수의 값을 출력합니다.
```
기본적인 number 모듈 사용방법 입니다. `rannumber()`로 난수를 생성할 수 있습니다.


#### 난수의 수 제한



난수의 수를 제한할수도 있습니다. 아래 예제코드는 난수를 5~10 사이로 제한하는 코드입니다.
```python
limit_number = rannumber(5, 10)

print(limit_number)
print(rannumber(5, 10))
```
`rannumber(5, 10)`은 난수의 수를 5~10 사이로 제한할수 있는 코드입니다. `()` 안에 `시작숫자,도착숫자`를 넣어 완성할 수 있습니다.

`2+3,10/2`등 계산식을 이용해서도 난수의 수를 제한할 수 있으며 이 후 서술할 모든 내용에서도 사용 가능합니다.


#### 소수점 자릿수 설정



기본적으로 생성된 난수는 오직 정수로만 생성이 가능합니다. 하지만 아래 예제를 참고하면 소수의 출력도 가능합니다.
```python
decimal_number = rnanumber(0, 1, "d3")

print(decimal_number)
print(rannumber(0, 1, "d3"))
```
이 예제코드는 0~1 사이의 수를 소수 셋째자리 수까지 출력하는 코드입니다. `"d3"`는 소수 셋째자리 수까지 출력한다는 의미입니다.

만약 `"d4"`를 사용하면 소수 넷째자리 수까지 출력이 가능합니다.

최대 20자리 수까지 가능합니다.(3.0.0~)


#### 응용



아래의 코드들은 이 모듈과 다른 라이브러리, 모듈을 응용하여 제작된 코드입니다. 여기서 사용된 예 외에도 다양한 다른 라이브러리와 응용이 가능합니다.

##### datetime 라이브러리 응용
아래는 datetime 라이브러리를 사용하여 응용한 코드입니다.
```python
import ranpick
from datetime import datetime

date_number = int(datetime.now().strftime("%Y%m%d%H%M%S"))

print(rannumber(date_number, date_number × 10))
```
이 코드는 datetime 라이브러리에서 출력된 시간을 활용하여 난수를 출력하도록 만들었습니다.

### ranrandom - 랜덤한 값 선택
`ranrandom`은 리스트에서 값을 하나 선택하여 출력합니다.


#### 기본
아래의 방식으로 random 모듈을 사용할수 있습니다.
```python
random = ranrandom("왼쪽", "오른쪽", "가운데", "꽝")

print(random)
print(ranrandom("왼쪽", "오른쪽", "가운데", "꽝"))
```
`ranrandom()`을 이용할수 있습니다. `()` 안에는 `("당첨", "꽝")`같은 형식으로 작성할 수 있습니다.
이곳에 넣은 항목들 중 하나를 랜덤으로 선택합니다.
이곳의 항목은 두개 이상 작성되어야 합니다.


#### 확률설정
각 항목의 확률을 설정할 수 있습니다. 아래 예제코드를 참조해주세요.
```python
random = ranrandom(("왼쪽", 33), ("오른쪽", 33), ("가운데", 33), ("꽝", 1))

print(random)
print(ranrandom(("왼쪽", 33), ("오른쪽", 33), ("가운데", 33), ("꽝", 1)))
```
`()`안에 또 하나의 `()`를 추가합니다. 추가한 `()`안에는 `("항목명1", 확률[%])`형식으로 작성할 수 있습니다.
모든 확률은 총 합 100이 되어야 하며 합이 안될경우 오류가 발생합니다.

```python
print("왼쪽", ("오른쪽", 50), "가운데", "꽝")
```
이와같이 확률이 일부 누락될경우 누락되어있는 남은 확률을 자동적으로 재분배 합니다.

#### 중복선택 (2.2.0~)
중복선택도 당연히 가능합니다. 아래 예제를 따라주세요.
```python
random = ranrandom("a", "b", "c", "d", DS=2)

print(random)
```
이 코드는 a, b, c, d 중 2개를 선택하여 출력한다는 것입니다. 몇개를 선택하여 출력하는지는 DS가 담당합니다.

DS의 값이 2이면 리스트에서 2개를 선택합니다. 만약 `DS=3`를 한다면 3개를 선택하여 출력합니다.
```r
a, d
```
이런식으로 출력됩니다.

##### 리스트형태로 출력하기
중복선택된 값은 리스트현태로도 출력이 가능합니다.
```python
random = ranrandom("a", "b", "c", "d", DS=3, as_list=True)

print(random)
```
리스트형태로 출력하려면 `as_list`를 사용하면 됩니다. as_list의 값은 True로 설정하고 실행하면 아래와 같이 출력됩니다.
```r
['b', 'c', 'a']
```

## 버그 리포트

버그 리포트를 할때는 아래 사이트(github)에서 해주세요.

<https://github.com/yhg4908/ranpick.py/issues>
