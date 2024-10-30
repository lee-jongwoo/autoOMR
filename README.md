# autoOMR

## Requirements
- OpenCV
- Tensorflow
- pdf2image
- numpy
- matplotlib

## Usage
1. 필요한 라이브러리를 전부 설치한다.
```
pip install -r requirements.txt
```
2. 답안지 양식을 이용해 마킹, 회수한 후 스캐너로 스캔한다.
3. PDF 파일을 files 폴더 내에 input.pdf의 이름으로 저장한다.
4. 터미널에서, 프로그램 루트 디렉터리 (autoomr/)으로 `cd`한 후 다음 명령을 실행한다.
```
python3 autoomr.py
```
5. 화면의 안내를 따른다.
