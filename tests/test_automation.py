"""
automation.py 모듈 테스트
"""

import pytest
from datetime import datetime
from src.automation import (
    format_date_kr,
    calculate_business_days,
    format_currency,
    calculate_execution_rate,
)


class TestFormatDateKr:
    def test_specific_date(self):
        date = datetime(2026, 4, 9)
        assert format_date_kr(date) == "2026년 04월 09일"

    def test_default_today(self):
        result = format_date_kr()
        assert "년" in result and "월" in result and "일" in result


class TestCalculateBusinessDays:
    def test_full_week(self):
        start = datetime(2026, 4, 6)   # 월요일
        end = datetime(2026, 4, 10)     # 금요일
        assert calculate_business_days(start, end) == 5

    def test_includes_weekend(self):
        start = datetime(2026, 4, 6)   # 월요일
        end = datetime(2026, 4, 12)    # 일요일
        assert calculate_business_days(start, end) == 5

    def test_same_day(self):
        date = datetime(2026, 4, 9)    # 목요일
        assert calculate_business_days(date, date) == 1

    def test_invalid_range(self):
        start = datetime(2026, 4, 10)
        end = datetime(2026, 4, 1)
        with pytest.raises(ValueError):
            calculate_business_days(start, end)


class TestFormatCurrency:
    def test_basic(self):
        assert format_currency(1000000) == "1,000,000원"

    def test_negative(self):
        assert format_currency(-500000) == "-500,000원"

    def test_custom_unit(self):
        assert format_currency(1000, unit="달러") == "1,000달러"

    def test_zero(self):
        assert format_currency(0) == "0원"


class TestCalculateExecutionRate:
    def test_full_execution(self):
        assert calculate_execution_rate(100, 100) == 100.0

    def test_half_execution(self):
        assert calculate_execution_rate(50, 100) == 50.0

    def test_zero_budget_raises(self):
        with pytest.raises(ValueError):
            calculate_execution_rate(50, 0)

    def test_real_world_case(self):
        # 10억 예산 중 7억 3천만원 집행
        result = calculate_execution_rate(730000000, 1000000000)
        assert result == 73.0
