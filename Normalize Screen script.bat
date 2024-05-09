@echo off
echo Tool: running command [powercfg -change monitor-timeout-ac 0]
echo Tool: To set monitor [display off] option to [never] (in situation that using AC power).
echo Tool: running command after 3 seconds.
timeout /t 3 /nobreak >nul 
powercfg -change monitor-timeout-ac 0

echo Tool: normalize screen setting successfully.
echo Tool: auto close program in 3 seconds.
timeout /t 3 /nobreak >nul 
