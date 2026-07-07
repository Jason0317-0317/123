import pandas as pd

from quant_analysis import score_and_rank


def test_score_and_rank_orders_by_total_score():
    df = pd.DataFrame(
        [
            {
                "symbol": "1111",
                "name": "Low",
                "price": 30.0,
                "avg_vol": 1000.0,
                "avg_amt": 30000.0,
                "avg_amp": 0.01,
                "ret_5": 0.01,
                "ret_20": 0.01,
                "vol_ratio": 1.0,
                "chip_proxy": 0.01,
            },
            {
                "symbol": "2222",
                "name": "High",
                "price": 50.0,
                "avg_vol": 5000.0,
                "avg_amt": 250000.0,
                "avg_amp": 0.08,
                "ret_5": 0.12,
                "ret_20": 0.2,
                "vol_ratio": 3.0,
                "chip_proxy": 1.25,
            },
            {
                "symbol": "3333",
                "name": "Mid",
                "price": 40.0,
                "avg_vol": 3000.0,
                "avg_amt": 120000.0,
                "avg_amp": 0.04,
                "ret_5": 0.05,
                "ret_20": 0.08,
                "vol_ratio": 1.8,
                "chip_proxy": 0.55,
            },
        ]
    )

    ranked = score_and_rank(df)

    assert ranked.iloc[0]["symbol"] == "2222"
    assert ranked["total_score"].is_monotonic_decreasing
    assert {"avg_amp_z", "vol_ratio_z", "ret_5_z", "chip_proxy_z"}.issubset(ranked.columns)


def test_score_and_rank_returns_empty_dataframe_for_empty_input():
    empty = pd.DataFrame()

    ranked = score_and_rank(empty)

    assert ranked.empty
