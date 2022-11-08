# Spacedout

Remove spaces from paths in an environmental variable.


This might especially be useful with WSL as mixing Linux and Windblows paths can result in errors due to spaces in the path names.
This repo holds a Python script which replaces any spaces with the `'\ '` escape sequence.
There is also a BASH script to drive the program.

Add the BASH and Python scripts somewhere in your PATH (they must be in the same folder), make the `spacedout` script executable, then invoke as `source spacedout <ENV VAR>` to update `ENV_VAR` to replace spaces with the proper escape character.
