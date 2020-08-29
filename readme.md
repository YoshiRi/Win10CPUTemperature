# CPU temperature visualizar for python


根本的な問題としてパフォーマンスモニタつけないと温度が更新されないというのがあった。


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

```
re.split('[\n\r]', out)
```

- remove null list

```
[x for x in re.split('[\n\r=]', out) if x]
```


remove Text
```
re.split('[\n\r=]', out)
```