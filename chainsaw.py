from aiogram import Bot, Dispatcher
import asyncio
from aiogram import F
from aiogram.filters import Command, state
from aiogram.types import Message, ReplyKeyboardMarkup, message, InlineKeyboardMarkup

from aiogram.types import InputMediaPhoto
from namoztugmalari import menu,erkaklar_namozi,ayollar_namozi,viloyatlar,shaharlar_ruyhati,buxoro_shaharlari,samarqand_shahrlari

TOKEN = "8739471199:AAGgT9UZ-Q0GIPO4_l1cHzAFVmmTjGaMFXE"
ADMIN = 7302808868

dp = Dispatcher(token=TOKEN)



@dp.message(F.document)
async def vid(message:Message):
    document=message.document.file_id
    await message.answer(document)


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer("""
  Assalomu alaykum. Bizning botimizga xush kelibsiz!
Siz bu botimiz orqali namoz vaqtlarini, namoz turlari
va ularni qanday uqilishi kerakligi haqida ma'lumotga ega bo'lasiz
""",reply_markup=menu)

#erkaklar N
@dp.message(F.text=="👳🏻‍♂️Erkaklar namozi")
async def salom(message:Message):
    await message.answer("Turni tanlang",reply_markup=erkaklar_namozi)

#bomdod
@dp.message(F.text=="🌄Bomdod")
async def bomdod(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIEXWnFIdIwPMDzVjRdmI2WOuXYAiubAAKzkQACYPopSjFndKWxE_T0OgQ",caption="🌄Bomdod")

#Peshin
@dp.message(F.text=="🌤Peshin")
async def peshin(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIEZmnFI0N_k5qOQBsftsz_C2wXBNFGAALLigACJsexSmy5mhmrSsF6OgQ",caption="🌤Peshin")

#asr
@dp.message(F.text=="🌃Asr")
async def asr(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIEaGnFI_KHvzQwds2qXbk4ndvLZiO4AALMiQACjCexSJvITJKX2qtWOgQ",caption="🌃Asr")

#shom
@dp.message(F.text=="🌙Shom")
async def shom(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIEamnFJIu0W8Y8JenRFedWfG3GZl87AAINhQACz5GRSgvkQPeSeBJhOgQ",caption="🌙Shom")

#xufton
@dp.message(F.text=="🎇Xufton")
async def xufton(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIEbGnFJRqMdqQwJP6Rfz7glnxyZkOEAAKDgwACZNJBS1H6kTh8dkepOgQ",caption="🎇Xufton")

#ortga
@dp.message(F.text=="⬅️ORTGA")
async def ortga(message:Message):
    await message.answer("Asosiy oyna",reply_markup=menu)

#duolar
@dp.message(F.text=="🤲Duolar")
async def duolar(message:Message):
    await message.answer_document("BQACAgIAAxkBAAIFaWnHdeFMzL1TPIy-6i5flo68XiQBAALZkQAC7Pk5SiNEBdxd6QNmOgQ")

#bitta ortga qaytish
@dp.message(F.text=="⬅️Ortga")
async def bir_ortga(message:Message):
    await message.answer("Ortga qaytildi",reply_markup=viloyatlar)

#asosiy uyna
@dp.message(F.text=="Asosiy oyna")
async def ortga_yurish(message:Message):
    await message.answer("Asosiy oyna",reply_markup=menu)

#Ayollar namozi
@dp.message(F.text=="🧕🏻Ayollar namozi")
async def ayollar(message:Message):
    await message.answer("Turni tanlang",reply_markup=ayollar_namozi)

#bomdod
@dp.message(F.text=="Bomdod🌄")
async def bomdod_ayol(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIE-GnGt7b0130HiCJfxpbHigaIZOiOAAJqfwACdul5SiF_fR3fMyyKOgQ",caption="Bomdod🌄")

#peshin
@dp.message(F.text=="Peshin🌤")
async def peshin_ayol(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIE-mnGuJVLTkFF9z3KlrOtc1tHQ1KkAAIghAACSkaoSnBwU4um7497OgQ",caption="Peshin🌤")

#asr
@dp.message(F.text=="Asr🌃")
async def asr_ayol(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIE_GnGuVBbtBasmfGtMoqs8I4KPPQYAALceAAC0XaxSjY6y2QDolPrOgQ",caption="Asr🌃")

#shom
@dp.message(F.text=="Shom🌙")
async def shom_ayol(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIE_mnGudueHL7D_r8V7_YzFgABqL9UXQACf24AAsIXgUo9m0YQWhWCBzoE",caption="Shom🌙")

#hufton
@dp.message(F.text=="Xufton🎇")
async def xufton_ayol(message:Message):
    await message.answer_video("BAACAgIAAxkBAAIFAAFpxrpqMVjHqqxFGwnW1rshjNomLwACRoMAAkEvoEryiAPpA8RqbjoE",caption="Xufton🎇")

#namoz vaqtlari
@dp.message(F.text=="🕋Namoz vaqtlari")
async def namoz_vaqtlari(message:Message):
    await message.answer("Viloyatni tanlang",reply_markup=viloyatlar)

#toshkent
@dp.message(F.text=="Toshkent viloyati")
async def toshkent_viloyati(message:Message):
    await message.answer("Shaharlar ruyhatidan birini tanlang",reply_markup=shaharlar_ruyhati)

#toshkent shaharlari
@dp.message(F.text=="Toshkent")
async def toshkent_shahr(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFMWnHZfKlrsxRQv2IZHZ09KdWTtsHAAK8E2sb7Pk5Sibj5pjtNThkAQADAgADeQADOgQ")

#angren
@dp.message(F.text=="Angren")
async def toshkent_angren(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFM2nHZnEb6AEiPqzNK9mQymHnvlqLAALAE2sb7Pk5Soj3Y-GihRW1AQADAgADeQADOgQ")

#Piskent
@dp.message(F.text=="Piskent")
async def piskent_pisk(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFNWnHZuf3eSFFUYlRV7-fdCvZ2GuzAALCE2sb7Pk5SnVlhUJ1jjEPAQADAgADeQADOgQ")

#Bekobod
@dp.message(F.text=="Bekobod")
async def bekobody_bekobod(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFN2nHZ213GYSIsKuvKoEIe01PlTu8AALEE2sb7Pk5Sp_DdH__9W5JAQADAgADeQADOgQ")

#Parkent
@dp.message(F.text=="Parkent")
async def parkent_park(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFOWnHZ-EEknsUV2c8uXW_xnEuIb0UAALGE2sb7Pk5SpFNl1N_nAVwAQADAgADeQADOgQ")

#Go'zalkent
@dp.message(F.text=="Go'zalkent")
async def gozalkent_goz(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFO2nHaFatNK7I-PH2pDp5l-tBq5scAALJE2sb7Pk5StY6HFpWXx6tAQADAgADeQADOgQ")

#Olmaliq
@dp.message(F.text=="Olmaliq")
async def omaliq(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFPWnHaM4dM7Fcxpmxrhwcx75CIswYAALKE2sb7Pk5SlW19ZtCbt9cAQADAgADeQADOgQ")

#Bo'ka
@dp.message(F.text=="Bo'ka")
async def boka(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFP2nHaSHYT4FzpXOjG2xpHt_0a0-zAALLE2sb7Pk5SqPYahP5BMMoAQADAgADeQADOgQ")

#Yangi yo'l
@dp.message(F.text=="Yangi yo'l")
async def yangi_yo(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFQWnHaZ5HgGg2rjtHrB_A0ZDdgnuMAALPE2sb7Pk5Sp2JU8s9SHYmAQADAgADeQADOgQ")

#Nurafshon
@dp.message(F.text=="Nurafshon")
async def nurafshon(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFQ2nHae1nnNDA0oZxnr-ynExs7mppAALQE2sb7Pk5SrRRra_bJFYWAQADAgADeQADOgQ")

#Buxoro
@dp.message(F.text=="Buxoro viloyati")
async def buxor(message:Message):
    await message.answer("Shaharlardan birini tanlang",reply_markup=buxoro_shaharlari)

#buxoro shahri
@dp.message(F.text=="Buxoro")
async def bob(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFUWnHb-Ygr7MveFxOQWn-lkE01uhtAALmE2sb7Pk5SsSm6tpWlhwzAQADAgADeQADOgQ")

#Gazli
@dp.message(F.text=="Gazli")
async def gazli(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFVWnHcHiyUf3L3Y-t-aBrZt642VOOAALoE2sb7Pk5SibT2dJVPfxQAQADAgADeQADOgQ")

#G'ijdivon
@dp.message(F.text=="G'ijdivon")
async def Gijdivon(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFV2nHcNEhbEZiXlTTjKJfVX5eLEDvAALqE2sb7Pk5SuygC2Q1nE9EAQADAgADeQADOgQ")

#Qorako'l
@dp.message(F.text=="Qorako'l")
async def qorako(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFWWnHcRiQP33wpImXXy81WQnKePSLAALsE2sb7Pk5Sh7n2MCdvp9rAQADAgADeQADOgQ")

#Jondor
@dp.message(F.text=="Jondor")
async def jondor(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFW2nHcXSeZ4xf9rrZkIA-CswUkRw5AALtE2sb7Pk5SsAXPR2unlvaAQADAgADeQADOgQ")

#samarqand
@dp.message(F.text=="Samarqand viloyati")
async def samarqand(message:Message):
    await message.answer("Shaharlardan birini tanlang",reply_markup=samarqand_shahrlari)

#samarqand shahri
@dp.message(F.text=="Samarqand")
async def samarqand_sh(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFX2nHc34NSGWF7yETIFn5auw3_VAZAALwE2sb7Pk5SldUA5QwgUJWAQADAgADeQADOgQ")

#ishtixon
@dp.message(F.text=="Ishtixon")
async def ishtixon(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFYWnHc7z9JQc_9L-fgrwPaVMgjkUcAALxE2sb7Pk5SmqRQFzh5q7NAQADAgADeQADOgQ")

#Mirbozor
@dp.message(F.text=="Mirbozor")
async def mirbozor(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFY2nHdBX0vyOAAAFuRfO8XxtnQ8EBhwAC9BNrG-z5OUpRpHrqdRM-AwEAAwIAA3kAAzoE")

#kattaqo'rg'on
@dp.message(F.text=="Kattaqo'rg'on")
async def kattaqo(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFZWnHdGmE0VsMZYYYRoZG_hQEe9taAAL2E2sb7Pk5SqrKVLZQ9hPJAQADAgADeQADOgQ")

#urgut
@dp.message(F.text=="Urgut")
async def urgun(message:Message):
    await message.answer_photo("AgACAgIAAxkBAAIFZ2nHdLYnzFj0JwdjdkmU41r4o8bTAAL3E2sb7Pk5SuWDxBtDsOoFAQADAgADeQADOgQ")

#farg'ona viloyati
@dp.message(F.text=="Farg'ona viloyati")
async def fargon(message:Message):
    await message.answer("Shaharlardan birini tanlang",)




async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())