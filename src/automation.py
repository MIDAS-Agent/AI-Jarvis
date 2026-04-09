"""
AI-Jarvis: 대학 행정 업무 자동화 모듈
"""

from datetime import datetime, timedelta
from typing import Optional


def format_date_kr(date: Optional[datetime] = None) -> str:
    """날짜를 한국식 형식(YYYY년 MM월 DD일)으로 변환"""
    if date is None:
        date = datetime.now()
    return date.strftime("%Y년 %m월 %d일")


def calculate_business_days(start_date: datetime, end_date: datetime) -> int:
    """두 날짜 사이의 영업일(평일) 수 계산"""
    if start_date > end_date:
        raise ValueError("시작일이 종료일보다 늦을 수 없습니다.")

    business_days = 0
    current = start_date
    while current <= end_date:
        if current.weekday() < 5:  # 월~금
            business_days += 1
        current += timedelta(days=1)
    return business_days


def format_currency(amount: int, unit: str = "원") -> str:
    """금액을 천 단위 구분 형식으로 변환"""
    if amount < 0:
        return f"-{abs(amount):,}{unit}"
    return f"{amount:,}{unit}"


def calculate_execution_rate(executed: int, budget: int) -> float:
    """예산 집행률 계산 (백분율)"""
    if budget <= 0:
        raise ValueError("예산은 0보다 커야 합니다.")
    return round((executed / budget) * 100, 2)
