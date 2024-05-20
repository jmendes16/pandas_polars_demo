@echo off

REM activate virtual environment
call C:\Users\joel.mendes\github\pandas_polars\pandas_polars\pandas_polars\Scripts\activate.bat

REM call pipeline script
python C:\Users\joel.mendes\github\pandas_polars\pandas_polars\polars_pipeline.py

REM deactivate virtual environment
deactivate

pause

REM name of task in scheduler: polars_pipeline_automation