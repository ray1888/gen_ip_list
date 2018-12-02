# This Script is for gen the ip list into a file


## usage


### if input a ip like this "10.10.10.10-165"

the output file is like
```buildoutcfg
10.10.10.10
10.10.10.11
.......
10.10.10.165

```

### if input a ip like this "10.10.10-165.10"

the output file is like
```buildoutcfg
10.10.10.10 
....
10.10.10.254
10.10.11.1
...
10.10.11.254
....

10.10.164.1
...
10.10.164.254
10.10.165.1
.....
10.10.165.10

```

### if input a ip like this "10.10-165.10.10"

the output file is like
```buildoutcfg
10.10.10.10 
....
10.10.10.11
10.10.11.1
...
10.11.1.1
....
10.11.1.254
...
10.164.254.1
...
10.164.254.254
10.165.1.1
.....
10.165.1.254
...
10.165.10.1
....
10.165.10.10

```
