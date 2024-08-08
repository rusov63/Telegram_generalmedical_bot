# from aiogram import types, Router, F
# from aiogram.utils.markdown import hbold, hitalic
#
# router_donor = Router()
#
#
# @router_donor.message(F.text == '📖 Подбор донора крови')
# async def donor_filter(message: types.Message):
#     await message.answer(f'{hbold("Введите фенотип реципиента: ")}\n'
#                          f'{hitalic("Например: CcDee, CwCDee, ccddee")}')
#
#
# RECIPIENT = ('CcDee', 'CCDee', 'CcDEe', 'ccddee', 'ccDEe', 'CwCDee', 'ccDEE', 'CwcDee', 'ccDee', 'Ccddee', 'CwcDEe',
#              'ccDweakee', 'CcddEe', 'CCDEe', 'ccddEe', 'CcDEE', 'Cwcddee', 'CCddee', 'CCDEE', 'CCddEe', 'CcddEE',
#              'ccddEE', 'CCDweakee', 'CcDweakee', 'ccDweakEe', 'ccDweakEE', 'CwcddEe', 'CwcDEE', 'kk', 'Kk', 'KK')
#
# @router_donor.message()
# async def donor_recipient(message: types.Message):
#
#     if message.text == 'CcDee':  # 1.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CcDee CCDee ccddee ccDee Ccddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('отсутствуют')}')
#
#     elif message.text == 'CCDee':  # 2.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CCDee CCddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('отсутствуют')}')
#
#     elif message.text == 'CcDEe':  # 3.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('Любой фенотип, кроме Cw +')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Любой фенотип, кроме Cw +')}')
#
#     elif message.text == 'ccddee':  # 4.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee')}')
#
#     elif message.text == 'ccDEe':  # 5.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccDEe ccddee ccDee ccDEE ccddEe')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CcDee CcDEe Ccddee CcddEe')}')
#
#     elif message.text == 'CwCDee':  # 6.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CwCDee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CCDee')}')
#
#     elif message.text == 'ccDEE':  # 7.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccDEE ccddEE')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('ccDEe CcDEE')}')
#
#     elif message.text == 'CwcDee':  # 8.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CwcDee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CcDee CCDee CwCdee')}')
#
#     elif message.text == 'ccDee':  # 9.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccDee ccddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CcDee Ccddee')}')
#
#     elif message.text == 'Ccddee':  # 10.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('Ccddee ccddee CCddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('ccddEe')}')
#
#     elif message.text == 'CwcDEe':  # 11.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CwcDEe ccDEe ccddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CcDee CcDEe')}')
#
#     elif message.text == 'ccDweakee':  # 12.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccDweakee ccddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee')}')
#
#     elif message.text == 'CcddEe':  # 13.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccddee Ccddee CcddEe ccddEe CCddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('отсутствуют')}')
#
#     elif message.text == 'CCDEe':  # 14.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CCDEe CCDee CCddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('отсутствуют')}')
#
#     elif message.text == 'ccddEe':  # 15.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccddEe ccddEE ccddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee CcddEe')}')
#
#     elif message.text == 'CcDEE':  # 16.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CcDEE ccDEE ccddEE')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CcDEe CcddEe ccddEe')}')
#
#     elif message.text == 'Cwcddee':  # 17.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('Cwcddee ccddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee')}')
#
#     elif message.text == 'CCddee':  # 18.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CCddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee ccddee')}')
#
#     elif message.text == 'CCDEE':  # 19.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CCDEE')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CCDEe CCDee')}')
#
#     elif message.text == 'CCddEe':  # 20.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CCddEe CCddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee ccddee')}')
#
#     elif message.text == 'CcddEE':  # 21.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CcddEE ccddEE')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CcddEe ccddEe ccddee')}')
#
#     elif message.text == 'ccddEE':  # 22.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccddEE')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('ccddEe')}')
#
#     elif message.text == 'CCDweakee':  # 23.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CCDweakee CCddee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CCDee')}')
#
#     elif message.text == 'CcDweakee':  # 24.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CcDweakee CCDweakee ccDweakee')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee ccddee')}')
#
#     elif message.text == 'ccDweakEe':  # 25.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccddee ccddEe ccDweakEe')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee CcddEe')}')
#
#     elif message.text == 'ccDweakEE':  # 26.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccDweakEE ccddEe ccddEE')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CcddEe ccddee')}')
#
#     elif message.text == 'CwcddEe':  # 27.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('ccddee ccddEe CwcddEe')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Ccddee CcddEe')}')
#
#     elif message.text == 'CwcDEE':  # 28.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('CwcDEE ccDEE ccddEE')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('CcDEe')}')
#
#     elif message.text == 'kk':  # 29.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('kk')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('отсутствуют')}')
#
#     elif message.text == 'Kk':  # 30.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('Kk kk KK')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('отсутствуют')}')
#
#     elif message.text == 'KK':  # 31.
#         await message.answer(f'Cовместимый, фенотип: \n'
#                              f'{hbold('KK')} \n\n'
#                              f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
#                              f'{hbold('Kk kk')}')
#
#
#     # elif message.text not in RECIPIENT:
#     #     await message.answer(f'Введите корректный фенотип!')
