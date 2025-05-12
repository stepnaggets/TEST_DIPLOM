"""
Модуль для обработки и анализа данных.
Содержит классы для загрузки, очистки и агрегации данных.
"""

import json
from typing import List, Dict, Optional
import pandas as pd
import numpy as np


class DataProcessor:
    """
    Класс для обработки данных из различных источников.
    Поддерживает CSV, JSON и Excel.
    """

    def __init__(self, file_path: str):
        """
        Инициализация процессора данных.
        
        Args:
            file_path (str): Путь к файлу с данными.
        """
        self.file_path = file_path
        self.data = None

    def load_data(self) -> Optional[pd.DataFrame]:
        """
        Загружает данные в зависимости от расширения файла.
        
        Returns:
            pd.DataFrame: Загруженные данные или None, если формат не поддерживается.
        """
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.json'):
            self.data = pd.read_json(self.file_path)
        elif self.file_path.endswith('.xlsx'):
            self.data = pd.read_excel(self.file_path)
        else:
            print("Unsupported file format!")
            return None
        return self.data

    def clean_data(self, drop_na: bool = True) -> pd.DataFrame:
        """
        Очищает данные от пропусков и дубликатов.
        
        Args:
            drop_na (bool): Удалять ли пропущенные значения (по умолчанию True).
        
        Returns:
            pd.DataFrame: Очищенные данные.
        """
        if self.data is None:
            raise ValueError("Data not loaded! Call load_data() first.")
        
        if drop_na:
            self.data = self.data.dropna()
        self.data = self.data.drop_duplicates()
        return self.data

    def aggregate_data(self, group_by: str, agg_func: str = 'mean') -> pd.DataFrame:
        """
        Агрегирует данные по заданному столбцу.
        
        Args:
            group_by (str): Столбец для группировки.
            agg_func (str): Функция агрегации ('mean', 'sum', 'count').
        
        Returns:
            pd.DataFrame: Агрегированные данные.
        """
        if self.data is None:
            raise ValueError("Data not loaded! Call load_data() first.")
        
        return self.data.groupby(group_by).agg(agg_func)


def calculate_statistics(data: List[float]) -> Dict[str, float]:
    """
    Вычисляет базовую статистику для списка чисел.
    
    Args:
        data (List[float]): Список числовых значений.
    
    Returns:
        Dict[str, float]: Статистика (среднее, медиана, стандартное отклонение).
    """
    if not data:
        return {}
    
    stats = {
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data)
    }
    return stats


if __name__ == "__main__":
    processor = DataProcessor("example.csv")
    processor.load_data()
    cleaned_data = processor.clean_data()
    aggregated = processor.aggregate_data("category", "sum")
    print(aggregated)