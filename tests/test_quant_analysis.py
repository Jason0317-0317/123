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
                "atr_14": 1.0,
                "ret_5": 0.01,
                "ret_20": 0.01,
                "vol_ratio": 1.0,
                "main_buy_5d": -100,
                "foreign_buy_5d": -80,
                "investment_trust_buy_5d": -30,
                "margin_change_pct": -0.01,
                "short_change_pct": 0.02,
            },
            {
                "symbol": "2222",
                "name": "High",
                "price": 50.0,
                "avg_vol": 5000.0,
                "avg_amt": 250000.0,
                "avg_amp": 0.08,
                "atr_14": 5.0,
                "ret_5": 0.12,
                "ret_20": 0.2,
                "vol_ratio": 3.0,
                "main_buy_5d": 300,
                "foreign_buy_5d": 250,
                "investment_trust_buy_5d": 120,
                "margin_change_pct": 0.03,
                "short_change_pct": -0.01,
            },
            {
                "symbol": "3333",
                "name": "Mid",
                "price": 40.0,
                "avg_vol": 3000.0,
                "avg_amt": 120000.0,
                "avg_amp": 0.04,
                "atr_14": 3.0,
                "ret_5": 0.05,
                "ret_20": 0.08,
                "vol_ratio": 1.8,
                "main_buy_5d": 50,
                "foreign_buy_5d": 40,
                "investment_trust_buy_5d": 10,
                "margin_change_pct": 0.01,
                "short_change_pct": 0.0,
            },
        ]
    )

    ranked = score_and_rank(df)

    assert ranked.iloc[0]["symbol"] == "2222"
    assert ranked["total_score"].is_monotonic_decreasing
    assert {
        "avg_amp_z",
        "atr_14_z",
        "vol_ratio_z",
        "ret_5_z",
        "foreign_buy_5d_z",
        "short_change_pct_inverse_z",
    }.issubset(ranked.columns)


def test_score_and_rank_returns_empty_dataframe_for_empty_input():
    empty = pd.DataFrame()

    ranked = score_and_rank(empty)

    assert ranked.empty
