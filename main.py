import pandas as pd
from get_stock_list import get_stock_list
from quant_analysis import download_batch, score_and_rank
from datetime import datetime

def main():
    print(f"--- 台股當沖量化篩選啟動 ({datetime.now().strftime('%Y-%m-%d %H:%M')}) ---")
    
    # 1. 獲取股票清單
    print("正在獲取上市櫃股票清單...")
    df_info = get_stock_list()
    print(f"共找到 {len(df_info)} 檔普通股。")
    
    # 2. 下載數據並執行第一層篩選 (流動性前20%)
    # 提示：為了演示速度，此處取前 500 檔。如需全市場請改為 df_info
    print("正在下載歷史數據並執行流動性篩選...")
    df_res = download_batch(df_info.iloc[:500])
    
    # 3. 計算因子評分與排名
    print("正在計算因子評分 (Z-score)...")
    df_ranked = score_and_rank(df_res)
    
    # 4. 輸出結果
    output_file = "final_rankings.csv"
    df_ranked.to_csv(output_file, index=False)
    
    print("\n--- 最值得優先關注的前 10 名股票 ---")
    top_10 = df_ranked.head(10)
    print(top_10[['symbol', 'name', 'price', 'total_score']])
    
    print(f"\n完整數據已儲存至: {output_file}")

if __name__ == "__main__":
    main()
