import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ranpick", # 모듈 이름
    version="0.1.0", # 버전
    author="raimy5810", # 제작자
    author_email="yhg4908@kakao.com", # contact
    description="Generates a random numbe", # 모듈 설명
    long_description=open('README.md').read(), # README.md에 보통 모듈 설명을 해놓는다.
    long_description_content_type="text/markdown",
    url="https://github.com/yhg4908/ranpick.py/",
    install_requires=[ # 필수 라이브러리들을 포함하는 부분인 것 같음, 다른 방식으로 넣어줄 수 있는지는 알 수 없음
    "matplotlib==3.5.2", 
    "numpy==1.21.5", 
    "pandas==1.4.4", 
    "scikit_learn==1.2.0", 
    "scipy==1.9.1", 
    "seaborn==0.11.2", 
    "setuptools==63.4.1", 
    ],
    package_data={'': ['LICENSE.txt']}, # 원하는 파일 포함, 제대로 작동되지 않았음
    include_package_data=True,
    packages = setuptools.find_packages(), # 모듈을 자동으로 찾아줌
    python_requires=">=3.12", # 파이썬 최소 요구 버전
)
