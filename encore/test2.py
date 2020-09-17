def square(x):
    print(__name__)
    return x ** 2음

# 메인에서 쓰일 때만 실행되는 코드이며 해당 파일이 모듈로서 쓰일 때는 아래 코드가 실행되지 않
if __name__ == "__main__":
    print(square(5))
    print('-' * 10)