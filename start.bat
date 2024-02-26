@echo off
SETLOCAL EnableExtensions

:: Check for Python & pip availability
python --version > NUL 2>&1
IF %ERRORLEVEL% neq 0 (
    ECHO Python is not installed or not in the PATH.
    ECHO Please install Python and ensure it is added to the system's PATH.
    EXIT /B
)

:: Check for virtual environment support
python -c "import venv" > NUL 2>&1
IF %ERRORLEVEL% neq 0 (
    ECHO The virtual environment module is not available.
    ECHO Please ensure your Python installation is complete and includes the venv module.
    EXIT /B
)

:: Create a virtual environment if it does not exist
IF NOT EXIST ".\venv\" (
    ECHO Creating Virtual Environment...
    python -m venv venv
    ECHO Virtual Environment Created.
)

:: Activate the virtual environment
CALL ".\venv\Scripts\activate"

:: Install requirements
ECHO Installing Requirements from requirements.txt...
pip install -r requirements.txt
ECHO Requirements Installed.

:: Run the application
ECHO Running the Application...
python app_v2.py

:: Deactivate the virtual environment on completion
deactivate

ENDLOCAL
