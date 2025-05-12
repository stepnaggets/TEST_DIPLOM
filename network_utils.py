"""
Утилиты для работы с сетевыми запросами.
Включает HTTP-клиент и обработку ответов.
"""

import requests
from requests.exceptions import RequestException
from typing import Dict, Any, Optional


class NetworkClient:
    """
    Клиент для выполнения HTTP-запросов.
    Поддерживает GET, POST, PUT, DELETE.
    """

    def __init__(self, base_url: str, timeout: int = 10):
        """
        Инициализация клиента.
        
        Args:
            base_url (str): Базовый URL API.
            timeout (int): Таймаут запроса в секундах.
        """
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Отправляет GET-запрос.
        
        Args:
            endpoint (str): Конечная точка API.
            params (Dict): Параметры запроса.
        
        Returns:
            Dict[str, Any]: Ответ в формате JSON.
        
        Raises:
            RequestException: Если запрос не удался.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise RequestException(f"GET request failed: {e}")

    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Отправляет POST-запрос с JSON-телом.
        
        Args:
            endpoint (str): Конечная точка API.
            data (Dict): Тело запроса.
        
        Returns:
            Dict[str, Any]: Ответ в формате JSON.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise RequestException(f"POST request failed: {e}")


def check_internet_connection() -> bool:
    """
    Проверяет доступность интернета.
    
    Returns:
        bool: True, если есть соединение.
    """
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except RequestException:
        return False


if __name__ == "__main__":
    client = NetworkClient("https://api.example.com")
    data = client.get("users", params={"id": 1})
    print(data)