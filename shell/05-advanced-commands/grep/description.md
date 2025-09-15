# Grep

`grep` is a tool that goes through a specified text file and prints out all lines that match a given regular expression.
Say you have a file `log.txt` with the following contents:

```text
2025/01/01 00:04:05 INFO 186.222.122.74 "GET /api/v1/user/38"
2025/01/01 00:18:56 ERROR 21.105.91.100 "GET /api/v1/sale/38"
2025/01/01 00:23:00 INFO 169.247.24.26 "GET /api/v1/sale/100"
2025/01/01 00:33:28 INFO 147.140.200.64 "GET /api/v1/item/14"
2025/01/01 00:46:33 WARNING 243.64.74.39 "GET /api/v1/user/57"
2025/01/01 06:58:10 ERROR 135.166.213.166 "GET /api/v1/item/81"
```

Using `grep` you can ask to only show you the lines containing `ERROR`:

```bash
$ grep ERROR ./log.txt
2025/01/01 00:18:56 ERROR 21.105.91.100 "GET /api/v1/sale/38"
2025/01/01 06:58:10 ERROR 135.166.213.166 "GET /api/v1/item/81"
```

## Question

We find the IP address `186.222.122.74` very suspicious and want to collect all requests originating from this address made on 2025/01/05.
Use `grep` to select all those lines from the included file `log.txt` and place the results in `solution.txt`.
