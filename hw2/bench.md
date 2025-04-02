```console
Running 10s test @ http://localhost/
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     8.16ms  561.25us  14.09ms   88.13%
    Req/Sec     3.08k   111.20     3.28k    69.75%
  122534 requests in 10.00s, 70.00MB read
Requests/sec:  12250.02
Transfer/sec:      7.00MB
```

```console
Running 10s test @ http://localhost/static/index.html
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   182.34us  309.40us  11.27ms   95.26%
    Req/Sec   139.63k     6.96k  165.67k    72.75%
  5556967 requests in 10.00s, 1.38GB read
Requests/sec: 555662.47
Transfer/sec:    141.49MB
```