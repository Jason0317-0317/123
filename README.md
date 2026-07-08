# 台股隔日當沖量化篩選系統

這是一個基於 Python 的量化交易篩選工具，旨在從台股所有上市櫃股票中，根據流動性、波動性、動能及籌碼因子，篩選出最適合隔日當沖的前 10 名標的。

## 系統架構

1. `get_stock_list.py`: 從 twstock 取得上市櫃普通股清單。
2. `quant_analysis.py`: 核心分析腳本。
   - 自動計算成交量與成交金額的百分位數。
   - 篩選前 20% 流動性標的。
   - 計算 Z-score 標準化因子與綜合評分。
3. `main.py`: 整合執行入口，產出最終 CSV 排名與分析報告。
4. `.github/workflows/daily-email.yml`: 每天自動產生報告並寄出 email。

## 自動寄信時間

GitHub Actions 目前設定為每天台灣時間早上 04:00 執行。

```yaml
cron: "0 20 * * *"
```

GitHub Actions 使用 UTC 時區，因此 `20:00 UTC` 等於台灣時間隔天 `04:00`。

## 通知內容

- 程式目前會分析股票清單中的前 500 檔。
- 產出 `final_rankings.csv`，並作為 email 附件寄出。
- 控制台會輸出前 10 名優先關注標的。

## 安裝需求

請確保您的環境已安裝以下 Python 套件：

```bash
pip install pandas numpy yfinance twstock requests
```

或直接使用：

```bash
pip install -r requirements.txt
```

## 使用方法

直接執行 `main.py` 即可：

```bash
python main.py
```

執行完成後，系統會產出：

- `final_rankings.csv`: 完整的排名與因子數據。
- 控制台前 10 名推薦名單與市場分析。

## 注意事項

- 此工具僅供量化研究與交易前觀察，不構成投資建議。
- yfinance 資料可能受網路與資料源穩定性影響。
- 若要分析全市場，可將 `main.py` 中的 `df_info.iloc[:500]` 改為 `df_info`。
