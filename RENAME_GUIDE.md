# 이미지 파일 이름 변경 프로그램

## ? 사용 방법

### 방법 1: EXE 파일 실행 (권장)
1. `rename_images.exe` 파일을 더블클릭
2. 현재 이미지 목록 확인
3. `y`를 입력하여 변경 진행
4. 완료!

### 방법 2: Python 스크립트 실행
- Python이 설치되어 있는 경우:
  - `rename_images.bat` 파일을 더블클릭
  - 또는 터미널에서 `python rename_images.py` 실행

## ? 주요 기능

- **자동 감지**: `public/img` 폴더의 모든 이미지 파일을 자동으로 찾음
- **순서 정렬**: 파일명 순서대로 `photo.jpg`, `photo1.jpg`, `photo2.jpg`... 형식으로 변경
- **확장자 통일**: 모든 이미지를 `.jpg` 확장자로 통일
- **HTML 자동 업데이트**: `index.html` 파일의 이미지 목록도 자동으로 업데이트
- **안전한 변경**: 변경 전 확인 메시지를 표시하여 실수 방지

## ? 사용 예시

**변경 전:**
```
public/img/
  ├── 메뉴1.png
  ├── food_photo.jpg
  ├── menu_2023.jpeg
  └── 신메뉴.webp
```

**프로그램 실행 후:**
```
public/img/
  ├── photo.jpg
  ├── photo1.jpg
  ├── photo2.jpg
  └── photo3.jpg
```

**index.html도 자동 업데이트:**
```javascript
const images = [
  'img/photo.jpg',
  'img/photo1.jpg',
  'img/photo2.jpg',
  'img/photo3.jpg'
];
```

## ? 지원 이미지 형식

- JPG, JPEG
- PNG
- GIF
- WEBP
- BMP

## ?? 주의사항

- **되돌릴 수 없음**: 이미지 파일 이름 변경은 취소할 수 없으니 신중하게 사용하세요
- **백업 권장**: 중요한 파일은 미리 백업해두는 것을 권장합니다
- **폴더 필수**: `public/img` 폴더가 존재해야 합니다
- **Git 저장소**: 변경 후 Git에 커밋하여 Vercel에 배포하세요

## ? Vercel 배포 워크플로우

1. `public/img` 폴더의 기존 이미지 삭제
2. 새로운 메뉴 사진들을 `public/img` 폴더에 복사
3. `rename_images.exe` 실행
4. Git에 커밋 및 푸시
5. Vercel 자동 배포 완료!

```bash
git add .
git commit -m "Update menu images"
git push
```

## ?? 개발자용: EXE 파일 재생성 방법

EXE 파일을 직접 생성하려면 다음 명령어를 사용하세요:

```bash
# PyInstaller 설치
pip install pyinstaller

# EXE 파일 생성
pyinstaller --onefile --console --name=rename_images rename_images.py
```

생성된 `rename_images.exe` 파일은 `dist` 폴더에 있습니다.

