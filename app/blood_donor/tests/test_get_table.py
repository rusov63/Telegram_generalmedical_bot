import asyncio
import unittest
from unittest.mock import AsyncMock, patch

from app.blood_donor.database.get_table import get_table_donor


class TestGetTableDonor(unittest.TestCase):

    @patch('config.db_manager')
    def test_get_table_donor_success(self, mock_db_manager):
        # Настройка имитации данных, возвращаемых из базы данных
        mock_db_manager.select_data = AsyncMock(return_value=[
            {'compatible': 'CcDee CCDee ccddee ccDee Ccddee', 'indications': 'отсутствуют'}
        ])

        recipient = 'CcDee'
        expected_result = (
            'Cовместимый фенотип: \n'
            '<b>CcDee CCDee ccddee ccDee Ccddee</b> \n'
            '\n'
            'При экстренных показаниях к трансфузии (переливанию): \n'
            '<b>отсутствуют</b>'
        )

        # Запуск тестируемой функции
        result = asyncio.run(get_table_donor(recipient))

        # Проверка результата
        self.assertEqual(result, expected_result)

    # @patch('config.db_manager')
    # def test_get_table_donor_no_data(self, mock_db_manager):
    #     # Настройка имитации отсутствия данных
    #     mock_db_manager.select_data = AsyncMock(return_value=[])
    #
    #     recipient = 'Unknown'
    #
    #     # Запуск тестируемой функции
    #     result = asyncio.run(get_table_donor(recipient))
    #
    #     # Проверка результата
    #     self.assertIsNone(result)
