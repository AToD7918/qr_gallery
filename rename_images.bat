@echo off
chcp 65001 > nul
echo ====================================
echo   ??  이미지 이름 변경 프로그램
echo ====================================
echo.

python rename_images.py

if errorlevel 1 (
    echo.
    echo ? Python이 설치되어 있지 않거나 오류가 발생했습니다.
    echo.
    echo Python을 설치하거나 rename_images.exe 파일을 사용해주세요.
    pause
)
