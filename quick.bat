@ECHO OFF 

TITLE Quickstart apache tools.

%KAFKA_HOME%\bin\windows\zookeeper-server-start.bat %KAFKA_HOME%\config\zookeeper.properties

PAUSE