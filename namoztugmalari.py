from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#menu
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👳🏻‍♂️Erkaklar namozi"),
            KeyboardButton(text="🧕🏻Ayollar namozi")
        ],
        [
            KeyboardButton(text="🤲Duolar")
        ],
        [
            KeyboardButton(text="🕋Namoz vaqtlari")
        ]
    ],
    resize_keyboard=True
)
#Erkaklar namozi
erkaklar_namozi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌄Bomdod"),
            KeyboardButton(text="🌤Peshin"),
            KeyboardButton(text="🌃Asr")
        ],
        [
            KeyboardButton(text="🌙Shom"),
            KeyboardButton(text="🎇Xufton")
        ],
        [
            KeyboardButton(text="⬅️ORTGA")
        ]
    ],
    resize_keyboard=True
)

#ayollar namozi
ayollar_namozi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bomdod🌄"),
            KeyboardButton(text="Peshin🌤"),
            KeyboardButton(text="Asr🌃")
        ],
        [
            KeyboardButton(text="Shom🌙"),
            KeyboardButton(text="Xufton🎇")
        ],
        [
            KeyboardButton(text="⬅️ORTGA")
        ]
    ],
    resize_keyboard=True
)

#viloyatlar
viloyatlar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent viloyati"),
            KeyboardButton(text="Buxoro viloyati"),
            KeyboardButton(text="Farg'ona viloyati"),
            KeyboardButton(text="Sirdaryo viloyati")
        ],
        [
            KeyboardButton(text="Jizzax viloyati"),
            KeyboardButton(text="Navoiy viloyati"),
            KeyboardButton(text="Namangan viloyati"),
            KeyboardButton(text="Xorazm viloyati")
        ],
        [
            KeyboardButton(text="Samarqand viloyati"),
            KeyboardButton(text="Surxondaryo viloyati"),
            KeyboardButton(text="Qashqadaryo viloyati"),
            KeyboardButton(text="Andijon viloyati")
        ],
        [
            KeyboardButton(text="⬅️ORTGA")
        ]
    ],
    resize_keyboard=True
)
shaharlar_ruyhati=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Angren"),
            KeyboardButton(text="Piskent"),
            KeyboardButton(text="Bekobod")
        ],
        [
            KeyboardButton(text="Parkent"),
            KeyboardButton(text="Go'zalkent"),
            KeyboardButton(text="Olmaliq"),
            KeyboardButton(text="Bo'ka")
        ],
        [
            KeyboardButton(text="Yangi yo'l"),
            KeyboardButton(text="Nurafshon"),
            KeyboardButton(text="⬅️Ortga"),
            KeyboardButton(text="Asosiy oyna")
        ]
    ],
    resize_keyboard=True
)
buxoro_shaharlari=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Gazli"),
            KeyboardButton(text="G'ijdivon")
        ],
        [
            KeyboardButton(text="Qorako'l"),
            KeyboardButton(text="Jondor"),
            KeyboardButton(text="⬅️Ortga")
        ],
        [
            KeyboardButton(text="Asosiy oyna")
        ]
    ],
    resize_keyboard=True
)
samarqand_shahrlari=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Samarqand"),
            KeyboardButton(text="Ishtixon"),
            KeyboardButton(text="Mirbozor")
        ],
        [
            KeyboardButton(text="Kattaqo'rg'on"),
            KeyboardButton(text="Urgut"),
            KeyboardButton(text="⬅️Ortga")
        ],
        [
            KeyboardButton(text="Asosiy oyna")
        ]
    ],
    resize_keyboard=True
)

fargona_shahrlari=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Farg'ona"),
            KeyboardButton(text="Marg'ilon"),
            KeyboardButton(text="Qo'qon")
        ],
        [
            KeyboardButton(text="Quva"),
            KeyboardButton(text="Rishton"),
            KeyboardButton(text="Bog'dod")
        ],
        [
            KeyboardButton(text="Oltiariq"),
            KeyboardButton(text="⬅️Ortga"),
            KeyboardButton(text="Asosiy oyna")
        ]
    ],
    resize_keyboard=True
)

