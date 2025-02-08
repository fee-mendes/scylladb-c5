# ScyllaDB Configs

Below are the configurations used for ScyllaDB in this benchmark.

## Scylla config

```
--poll-mode in sysconfig
```

## scylla.yaml

```
compaction_static_shares: 50
stream_io_throughput_mb_per_sec: 98
compaction_throughput_mb_per_sec: 98
sstable_summary_ratio: 0.003
```

# Test commands used

Each directory contains a env file with all variables used for the test.
```
LATTE_THREADS=8
LATTE_OPERATIONS=standard1_insert,standard1_select
LATTE_CONNECTIONS=1
LATTE_TEST_NAME=50_50_uniform_tablets
LATTE_BIN_PATH=latte-main/target/release/
LATTE_DURATION=30m
LATTE_PROFILE=latte-main/workloads/basic/cass-5-0-initiative.rn
LATTE_RATE=180000
LATTE_HOST=172.31.57.182
  
latte  run  ${LATTE_PROFILE}  ${LATTE_HOST}  --rate  ${LATTE_RATE}  --duration  ${LATTE_DURATION}  --threads  ${LATTE_THREADS}  --connections  ${LATTE_CONNECTIONS}  -f  ${LATTE_OPERATIONS}
```
# Test specific configuration
## Uniform
```
index_cache_fraction: 0.5
ICS + SAG 1.5
```
