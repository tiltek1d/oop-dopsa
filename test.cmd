@echo off

pip3 install pytest

cd task_1 || exit /b
pytest
cd ../task_2 || exit /b
pytest
cd ../task_3 || exit /b
pytest
cd ../task_4 || exit /b
pytest
