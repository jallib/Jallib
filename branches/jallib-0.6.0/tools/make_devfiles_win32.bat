REM *************************************************************************************
REM Script to generate the JAL device files
REM *************************************************************************************
REM
REM download the regina34w32.exe, for example from
REM for example from http://mirror.optus.net/sourceforge/r/re/regina-rexx/
REM install regina34w32.exe the package
REM Download the rexx regutil library from http://pages.interlog.com/~ptjm/software.html
REM unzip the package, copy the rexxutil.dll in the regina install directory
REM make sure the system PATH includes the regina install directory
REM run this script
REM
REM *************************************************************************************


mkdir d:\temp
mkdir d:\temp\mplab833
mkdir "d:\temp\mplab833\mpasm_suite"
mkdir "d:\temp\mplab833\mpasm_suite\LKR"
mkdir "d:\temp\mplab833\mplab_ide"
mkdir "d:\temp\mplab833\mplab_ide\device"

del "d:\temp\mplab833\mpasm_suite\LKR\*.*" /S /F /Q
del "d:\temp\mplab833\mplab_ide\device" /S /F /Q
 

copy "D:\pic\Microchip\MPASM Suite\LKR\*.*" "d:\temp\mplab833\mpasm_suite\LKR\"
copy "D:\pic\Microchip\MPLAB IDE\device\*.*" "d:\temp\mplab833\mplab_ide\device\"

subst k: /d
subst k: d:\temp

mkdir test
del test\*.* /S /F /Q

regina.exe Dev2Jal.cmd test

