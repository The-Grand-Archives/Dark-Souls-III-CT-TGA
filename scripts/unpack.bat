for /f "delims=" %%i in ('where .\dist:DS3_TGA_v*.CT') do set RESULT=%%i
ce2fs -i "%RESULT%" %*
