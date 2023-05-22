# Regular Expression
# 정규표현식(Regular Expression)은 문자열 패턴을 표현하고 검색, 추출, 대체 등의 문자열 처리 작업에 사용되는 강력한 도구입니다. 파이썬에서는 re 모듈을 통해 정규표현식을 지원하며, 다양한 문자열 작업에 유용하게 활용됩니다.

# 정규표현식의 필요성:

# 문자열의 패턴을 일치시키고 검색, 추출, 대체 등의 작업을 효율적으로 수행할 수 있습니다.
# 복잡한 문자열 검증이나 데이터 처리에 사용될 수 있습니다.
# 특정 형식의 문자열을 파싱하거나 필요한 정보를 추출하는 데 유용합니다.

# 파이썬에서의 정규표현식 기본 사용법 및 코드 예제

import re

pattern = r"apple"
text = "I love apples."
result = re.search(pattern, text)
if result:
    print("일치하는 패턴을 찾았습니다.")
else:
    print("일치하는 패턴이 없습니다.")

pattern = r"\d{3}-\d{4}-\d{4}"  # 전화번호 형식 (예: 000-0000-0000)
text = "010-1234-5678"
result = re.match(pattern, text)
if result:
    print("올바른 전화번호 형식입니다.")
else:
    print("잘못된 전화번호 형식입니다.")