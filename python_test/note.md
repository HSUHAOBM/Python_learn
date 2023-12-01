# pytest
## 基本
pip install pytest
## 覆蓋率
pip install pytest-cov

pytest --cov=ex1 -v -s
python -m pytest day_test.py -v -s
-m 使用 pytest 模塊
-v 詳細說明
-s print 顯示

pytest --cov=ex1 ex1/ -v -s
pytest --cov=ex1 ex1/ --cov-report html -v -s

---

# unittest

python -m unittest tests.funtion.test_calculator

# 使用 nose : 便於測試
pip install nose
```
# 運行所有測試文件
nosetests -v tests/*
# 統計覆蓋率
nosetests --with-coverage -v tests/*
# 計算和報告 app 包中的代碼的覆蓋率
nosetests --with-coverage -v tests/funtion/test_calculator.py --cover-package=app
# 產報告
nosetests --with-coverage --cover-package=app --cover-erase --cover-html --cover-html-dir=coverage_report -v tests/*

```

---

# 記憶體
pip install memory-profiler
## 依賴(繪圖)
pip install matplotlib

```
# 生成 .dat
mprof run your_script.py
# 產生圖形
mprof plot
mprof plot -o memory_profile.png

```




