# openvino-benchmark
Simple setup for benchmarking ARC pro's AI performace.  Intel offers brief OpenVINO performace data for all openvino devcies except ARC.  

## first time setup
`models.lst` are models suggested in [OpenVINO Performance Benchmarks](https://docs.openvino.ai/2022.3/openvino_docs_performance_benchmarks.html)
```
omz_downloader --list models.lst
```

```
omz_converter --list models.lst
```

## benchmark all models 
```
./bmall.sh
```

## Create Report
```
./bmall.sh > i5a40.log
python3 collectlog.py bms.lst i5a40.log > i5a40.md
```

