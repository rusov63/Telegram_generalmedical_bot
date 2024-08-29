import unittest

from app.sofa.handlers.calc_EyeVerbalMotor import calculation_Eye_response, calculation_Verbal_response, \
    calculation_Motor_response, final_calculation_EyeVerbalMotor


class TestCalculationEyeResponse(unittest.TestCase):
    """
    Тестирование функций расчета реакций на глазные, вербальные и моторные стимулы.

    Модуль содержит классы тестов для проверки корректности работы следующих функций:
    - calculation_Eye_response: оценивает реакцию глаз на различные стимулы.
    - calculation_Verbal_response: оценивает вербальные реакции.
    - calculation_Motor_response: оценивает моторные реакции.
    - final_calculation_EyeVerbalMotor: вычисляет итоговый результат на основе оценок глазных, вербальных и моторных реакций.

    Каждый класс тестов наследует unittest.TestCase и включает в себя методы, которые проверяют различные сценарии, включая корректные и некорректные входные данные.

    Примеры тестируемых случаев:
    - Открытие глаз в ответ на различные стимулы (самопроизвольно, на голос, на боль и т.д.).
    - Вербальные реакции (осмысленные ответы, бессвязная речь и т.д.).
    - Моторные реакции (выполнение движений, локализация боли и т.д.).
    - Итоговая оценка на основе трех категорий реакций.

    Для запуска тестов используйте команду:
    python -m unittest -v app/sofa/tests/tests_calc_EyeVerbalMotor.py
    """

    def test_open_spontaneously(self):
        self.assertEqual(calculation_Eye_response('Открывает самопроизвольно, наблюдает'), 4)

    def test_open_to_voice(self):
        self.assertEqual(calculation_Eye_response('Открывает, в ответ на голос'), 3)

    def test_open_to_pain(self):
        self.assertEqual(calculation_Eye_response('Открывает, как реакция на болевое раздражение'), 2)

    def test_not_opening(self):
        self.assertEqual(calculation_Eye_response('Не открывает'), 1)

    def test_invalid_response(self):
        self.assertIsNone(calculation_Eye_response('Некорректный ответ'))


class TestCalculation_Verbal_response(unittest.TestCase):

    def test_oriented(self):
        self.assertEqual(calculation_Verbal_response('Ориентирован и контактен (осмысленный ответ)'), 5)

    def test_Pronounces_phrases(self):
        self.assertEqual(calculation_Verbal_response('Произносит фразы, но речь бессвязная'), 4)

    def test_individual_words(self):
        self.assertEqual(calculation_Verbal_response('Произносит отдельные слова'), 3)

    def test_MakesSounds(self):
        self.assertEqual(calculation_Verbal_response('Издает звуки, но не слова'), 2)

    def test_No_speech(self):
        self.assertEqual(calculation_Verbal_response('Отсутствие речи'), 1)


class TestCalculation_Motor_response(unittest.TestCase):

    def test_PerformingMovements(self):
        self.assertEqual(calculation_Motor_response('Выполнение движений по голосовой команде'), 6)

    def test_LocalizesPain(self):
        self.assertEqual(calculation_Motor_response('Локализует боль, пытается её избежать'), 5)

    def test_MeaninglessMovements(self):
        self.assertEqual(calculation_Motor_response('Бессмысленные движения в ответ на боль'), 4)

    def test_Bending(self):
        self.assertEqual(calculation_Motor_response('Патологическое сгибание в ответ на боль '
                                                    '(декортикационная ригидность)'), 3)

    def test_Extension(self):
        self.assertEqual(calculation_Motor_response('Патологическое разгибание в ответ на боль '
                                                    '(децеребрационная ригидность)'), 2)

    def test_notMove(self):
        self.assertEqual(calculation_Motor_response('Не двигается'), 1)


class TestFinal_calculation_EyeVerbalMotor(unittest.TestCase):

    def test_Result(self):
        self.assertEqual(final_calculation_EyeVerbalMotor(2, 1, 2), 4)
        self.assertEqual(final_calculation_EyeVerbalMotor(2, 3, 2), 3)
        self.assertEqual(final_calculation_EyeVerbalMotor(4, 4, 3), 2)
        self.assertEqual(final_calculation_EyeVerbalMotor(5, 3, 5), 1)
        self.assertEqual(final_calculation_EyeVerbalMotor(5, 5, 5), 0)

    def test_TypeError(self):
        # Тестируем некорректные значения, неправильный тип
        with self.assertRaises(TypeError):
            self.assertEqual(final_calculation_EyeVerbalMotor('a', 1, 1))


