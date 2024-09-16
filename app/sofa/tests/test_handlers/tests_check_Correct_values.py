import unittest

from app.sofa.handlers.check_Correct_values import (check_correct_values_FioPao,
                                                    check_correct_kb_respiratory, check_correct_kb_platelet,
                                                    check_correct_kb_liver, check_correct_kb_creatinin,
                                                    check_correct_kb_hypotension, check_correct_kb_eye,
                                                    check_correct_kb_verbal, check_correct_kb_motor)


class TestCheckCorrectValuesFioPao(unittest.TestCase):

    def test_check_correct_values_FioPao(self):
        self.assertEqual(check_correct_values_FioPao("123"), "123")
        self.assertEqual(check_correct_values_FioPao("o"), None)
        self.assertEqual(check_correct_values_FioPao("0"), None)
        self.assertEqual(check_correct_values_FioPao('O'), None)
        self.assertEqual(check_correct_values_FioPao("abc"), None)
        self.assertEqual(check_correct_values_FioPao("45.67"), "45.67")  # Проверка на float

    def test_check_correct_kb_respiratory(self):
        self.assertEqual(check_correct_kb_respiratory('Да'), 'Да')
        self.assertEqual(check_correct_kb_respiratory('Нет'), 'Нет')
        self.assertEqual(check_correct_kb_respiratory('Может Да, а может Нет'), None)

    def test_check_correct_kb_platelet(self):
        self.assertEqual(check_correct_kb_platelet('> 151'),'> 151')
        self.assertEqual(check_correct_kb_platelet('<= 150'), '<= 150')
        self.assertEqual(check_correct_kb_platelet('<= 100'), '<= 100')
        self.assertEqual(check_correct_kb_platelet('<= 50'), '<= 50')
        self.assertEqual(check_correct_kb_platelet('<= 20'), '<= 20')
        self.assertEqual(check_correct_kb_platelet('good'), None)
        self.assertEqual(check_correct_kb_liver(123), None)

    def test_check_correct_kb_liver(self):
        self.assertEqual(check_correct_kb_liver('< 20'), '< 20')
        self.assertEqual(check_correct_kb_liver('20 - 32'), '20 - 32')
        self.assertEqual(check_correct_kb_liver('33 - 101'), '33 - 101')
        self.assertEqual(check_correct_kb_liver('102 - 204'), '102 - 204')
        self.assertEqual(check_correct_kb_liver('> 204'), '> 204')
        self.assertEqual(check_correct_kb_liver('good'), None)
        self.assertEqual(check_correct_kb_liver(123), None)

    def test_check_correct_kb_creatinin(self):
        self.assertEqual(check_correct_kb_creatinin('< 110'), '< 110')
        self.assertEqual(check_correct_kb_creatinin('110 - 170'), '110 - 170')
        self.assertEqual(check_correct_kb_creatinin('171 - 299'), '171 - 299')
        self.assertEqual(check_correct_kb_creatinin('300 - 440 или диурез <500 мл в сутки'),
                         '300 - 440 или диурез <500 мл в сутки')
        self.assertEqual(check_correct_kb_creatinin('> 440 или < 200 мл мочи/сутки'),
                         '> 440 или < 200 мл мочи/сутки')
        self.assertEqual(check_correct_kb_liver('good'), None)
        self.assertEqual(check_correct_kb_liver(123), None)

    def test_check_correct_kb_hypotension(self):
        self.assertEqual(check_correct_kb_hypotension('Нет гипотензии'),'Нет гипотензии')
        self.assertEqual(check_correct_kb_hypotension('АДср < 70 мм.рт.ст.'),'АДср < 70 мм.рт.ст.')
        self.assertEqual(check_correct_kb_hypotension('Допамин <= 5 или любая доза добутамина'),
                         'Допамин <= 5 или любая доза добутамина')
        self.assertEqual(check_correct_kb_hypotension('Допамин > 5 или адреналин <= 0.1 или НА <= 0.1'),
                         'Допамин > 5 или адреналин <= 0.1 или НА <= 0.1')
        self.assertEqual(check_correct_kb_hypotension('Допамин > 15 или адреналин > 0.1 или НА > 0.1'),
                         'Допамин > 15 или адреналин > 0.1 или НА > 0.1')
        self.assertEqual(check_correct_kb_liver('good'), None)
        self.assertEqual(check_correct_kb_liver(123), None)

    def test_check_correct_kb_eye(self):
        self.assertEqual(check_correct_kb_eye('Открывает самопроизвольно, наблюдает'),
                         'Открывает самопроизвольно, наблюдает')
        self.assertEqual(check_correct_kb_eye('Открывает, в ответ на голос'),
                         'Открывает, в ответ на голос')
        self.assertEqual(check_correct_kb_eye('Открывает, как реакция на болевое раздражение'),
                         'Открывает, как реакция на болевое раздражение')
        self.assertEqual(check_correct_kb_eye('Не открывает'), 'Не открывает')
        self.assertEqual(check_correct_kb_liver('good'), None)
        self.assertEqual(check_correct_kb_liver(123), None)

    def test_check_correct_kb_verbal(self):
        self.assertEqual(check_correct_kb_verbal('Ориентирован и контактен (осмысленный ответ)'),
                         'Ориентирован и контактен (осмысленный ответ)')
        self.assertEqual(check_correct_kb_verbal('Произносит фразы, но речь бессвязная'),
                         'Произносит фразы, но речь бессвязная')
        self.assertEqual(check_correct_kb_verbal('Произносит отдельные слова'),
                         'Произносит отдельные слова')
        self.assertEqual(check_correct_kb_verbal('Издает звуки, но не слова'),
                         'Издает звуки, но не слова')
        self.assertEqual(check_correct_kb_verbal('Отсутствие речи'), 'Отсутствие речи')
        self.assertEqual(check_correct_kb_liver("Непонятно"), None)
        self.assertEqual(check_correct_kb_liver(123), None)

    def test_check_correct_kb_motor(self):
        self.assertEqual(check_correct_kb_motor('Выполнение движений по голосовой команде'),
                         'Выполнение движений по голосовой команде')
        self.assertEqual(check_correct_kb_motor('Локализует боль, пытается её избежать'),
                         'Локализует боль, пытается её избежать')
        self.assertEqual(check_correct_kb_motor('Бессмысленные движения в ответ на боль'),
                         'Бессмысленные движения в ответ на боль')
        self.assertEqual(check_correct_kb_motor('Патологическое сгибание в ответ на боль (декортикационная ригидность)'),
                         'Патологическое сгибание в ответ на боль (декортикационная ригидность)')
        self.assertEqual(check_correct_kb_motor('Патологическое разгибание в ответ на боль (децеребрационная ригидность)'),
                         'Патологическое разгибание в ответ на боль (децеребрационная ригидность)')
        self.assertEqual(check_correct_kb_motor('Не двигается'), 'Не двигается')
        self.assertEqual(check_correct_kb_liver("Движение"), None)
        self.assertEqual(check_correct_kb_liver(123), None)