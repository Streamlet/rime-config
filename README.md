# 我的 Rime 配置
---

## 使用方法

### Windows
```batch
Del /S /Q %AppData%\Rime
git clone git@github.com:Streamlet/rime-config.git %AppData%\Rime
```


### Mac
```bash
rm -rf ~/Library/Rime
git clone git@github.com:Streamlet/rime-config.git ~/Library/Rime
```

---

## 搜狗词库
```bash
python tools/install_sogou_dict.py
```
