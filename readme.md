# CPU temperature visualizar for python

## os popen 

```
fh = os.popen(cmd)
output = fh.read()
print(output)
fh.close()
```

## Subprocess popen multiple line

- separate cmd with & will work
- not work for some program

Tips: we need to escape command!

```
cmd = """wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value"""
```

- remove \n and \r