from pyrogram import *
from pyrogram.types import *
from textwrap import dedent

app = Client("bot",
	api_id = 7465008,
	api_hash = "993f01369ad7b0c8093ff0fbf4855e0e",
	bot_token = "5104123933:AAFVuT4vJ8tDf6hmsX7OSZIR1sDU5ge1jYM")

@app.on_message(filters.command("start",prefixes = "/") & filters.private)
def main_menu(client,message):
	app.send_message(message.chat.id, "О чем вы хотите получить информацию?",
        reply_markup=ReplyKeyboardMarkup(
            [
                ["Объекты Nedvex", "Программа лояльности"],
                ["Партнерская программа"],  
            ],
            resize_keyboard=True
        )
    )

@app.on_message(filters.regex("Объекты Nedvex"))
def objects(client, message):
	app.send_message(message.chat.id,"Выберите интересующий объект:", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Atrium Avenue",
				callback_data = "Atrium Avenue"
				)
			],
			[
				InlineKeyboardButton(
				"Volna Hotel Resort & SPA",
				callback_data = "Волна"
				)
			],	
			[   
				InlineKeyboardButton(
				"Volna Residence",
				callback_data = "Волна Резиднес"
				)
			],
			[   
				InlineKeyboardButton(
				"Моне",
				callback_data = "Моне"
				)
			],
			[   
				InlineKeyboardButton(
				"Атлас",
				callback_data = "Атлас"
				)
			],
			[
				InlineKeyboardButton(
				"Diamond",
				callback_data = "Diamond"
				)
			
			], 
			[   
				InlineKeyboardButton(
				"Лучезарный",
				callback_data = "Лучезарный"
				)
			],
			[   
				InlineKeyboardButton(
				"Woodland",
				callback_data = "Woodland"
				)
			],
			[   
				InlineKeyboardButton(
				"Monteville village",
				callback_data = "Monteville village"
				)
			],
			[   
				InlineKeyboardButton(
				"Олимпик 2",
				callback_data = "Olympic"
				)
			],
			[   
				InlineKeyboardButton(
				"Сидней",
				callback_data = "Sydney"
				)
			],
			[   
				InlineKeyboardButton(
				"Морская симфония 2",
				callback_data = "Морская симфония"
				)
			],
			[   
				InlineKeyboardButton(
				"Морской квартал",
				callback_data = "Морской квартал"
				)
			],
			[   
				InlineKeyboardButton(
				"Verdi",
				callback_data = "Verdi"
				)
			],
			[   
				InlineKeyboardButton(
				"Grand Royal",
				callback_data = "Grand Royal"
				)
			],
			[   
				InlineKeyboardButton(
				"Александрит",
				callback_data = "Александрит"
				)
			],
			[   
				InlineKeyboardButton(
				"Sunhills Olginka",
				callback_data = "Sunhills Olginka"
				)
			]	
		]
	)
)

@app.on_callback_query(filters.regex("Atrium Avenue"))
def AtriumAvenue(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Atrium Avenue", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "AtriumAvenuePresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "AtriumAvenueVideo"
				)
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "AtriumAvenueRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "AtriumAvenueInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "AtriumAvenueLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "AtriumAvenueChess"
				)
			],
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "AtriumAvenueContacts"
				)
			
			], 
			[
				InlineKeyboardButton(
				"Назад◀️",
				callback_data = "Back"
				)
			
			]
		]
	)
)


@app.on_callback_query(filters.regex("AtriumAvenuePresentation"))
def AtriumAvenuePresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, document = "Атриум Авеню_мобильная.pdf")
	cb_qry.answer()

@app.on_callback_query(filters.regex("AtriumAvenueVideo"))
def AtriumAvenueVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1fje4uZ9qOA-olk0ozBUMw9UF1m_j6244", cb_qry.message.chat.id)
	cb_qry.answer()
@app.on_callback_query(filters.regex("AtriumAvenueRenders"))
def AtriumAvenueRenders(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1f_tB1GYFiuhycoQYA3AGKX6OraAiVEQs", cb_qry.message.chat.id)
	cb_qry.answer()

@app.on_callback_query(filters.regex("AtriumAvenueInvestForecast"))
def AtriumAvenueInvestForecast(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1nnIwlabMkDIn-Hm0l0JUC2OCvMNAnL_q", cb_qry.message.chat.id)
	cb_qry.answer()

@app.on_callback_query(filters.regex("AtriumAvenueLayout"))
def AtriumAvenueLayout(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1fcmI0SyaTfPTPdxzAQxAtYxeH1ORYh0N", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("AtriumAvenueChess"))
def AtriumAvenueChess(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1fi3yAthG3ary-yy8-bXyGgAkQYEJNK8W", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("AtriumAvenueContacts"))
def AtriumAvenueContacts(client,cb_qry:CallbackQuery):
	contacts = """Контакты 
	8968-300-25-77
	Сочи, ул. Яна Фабрициуса, 33
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>", cb_qry.message.chat.id ,parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.576794, 39.747999)
	cb_qry.answer()


@app.on_callback_query(filters.regex("Волна"))
def Volna(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Volna Hotel Resort & SPA", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "VolnaPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "VolnaVideo"
				)
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "VolnaRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "VolnaInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "VolnaLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "VolnaChess"
				)
			],
						[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "VolnaContacts"
				)
			
			],
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back"
				)
			]
		]
	)
)

@app.on_callback_query(filters.regex("VolnaPresentation"))
def ВолнаPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, document = "Volna Resort.pdf")
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaVideo"))
def ВолнаVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/16xwP7iILJJMOx0IwNo_5glkQr_ydA_7y/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaRenders"))
def ВолнаRenders(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1vJ3A5Z3TVySSBrDofyhEe3JmCiQsvr-D", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaInvestForecast"))
def ВолнаInvestForecast(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1Ig5fK2BpTl1MSmtoWIrVbkf6dxXr5Ip3",cb_qry.message.chat.id)

@app.on_callback_query(filters.regex("VolnaLayout"))
def ВолнаLayout(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1vAVw7Xf4Lskpi9m5ttgXFkCktn9jJPZc",cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaChess"))
def ВолнаChess(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1v3PTqRhi_iqXHxzvHLM8GzeKkIDcBn9L", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaContacts"))
def VolnaContacts(client,cb_qry:CallbackQuery):
	contacts = """Контакты 
	8962-886-00-56
	Адлер, ул. Ленина, 219А  
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.473634, 39.895781)
	cb_qry.answer()




@app.on_callback_query(filters.regex("Волна Резиднес"))
def VolnaResidence(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Volna Residence", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "VolnaRezidnesPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "VolnaRezidnesVideo"
				)
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "VolnaRezidnesRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "VolnaRezidnesInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "VolnaRezidnesLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "VolnaRezidnesChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "VolnaRezidnesContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)

@app.on_callback_query(filters.regex("VolnaRezidnesPresentation"))
def VolnaRezidnesPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, "Микропрезентация Volna Residence.pdf")
	
@app.on_callback_query(filters.regex("VolnaRezidnesVideo"))
def VolnaRezidnesVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1ZWiYI_iLAqr3o01mWUwN6JNppCA5iXQM", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaRezidnesRenders"))
def VolnaRezidnesRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1ZUG5Nn6OQ-J55Xx4J9CjA_GNGPWO3em2", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaRezidnesInvestForecast"))
def VolnaRezidnesInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/spreadsheets/d/1WcHXdMSN-j-L7Gxz9C82iWUtCfAsnPnvAQ3gCa9LoCE/edit#gid=0", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaRezidnesLayout"))
def VolnaRezidnesLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1ZV0Wn8dpMVpJ_Vi0TvWwTMWS50pgOeCR", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaRezidnesChess"))
def VolnaRezidnesChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/spreadsheets/d/1WcHXdMSN-j-L7Gxz9C82iWUtCfAsnPnvAQ3gCa9LoCE/edit#gid=0", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("VolnaRezidnesContacts"))
def VolnaRezidnesContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	8962-886-00-56
	Адлер, ул. Ленина, 219А
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.473634, 39.895781)
	cb_qry.answer()



@app.on_callback_query(filters.regex("Моне"))
def Mone(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Моне", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "MonePresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "MoneVideo"
				)
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "MoneRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "MoneInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "MoneLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "MoneChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "MoneContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)

@app.on_callback_query(filters.regex("MonePresentation"))
def MonePresentation(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1zNQcbGRR-rYPZc6mpiCqMmLTrTeOExIj", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("MoneVideo"))
def MoneVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1zNQcbGRR-rYPZc6mpiCqMmLTrTeOExIj", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("MoneRenders"))
def MoneRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1zUD32YFVTZnpWuD3X3crYUAj2wWLv_Mi", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("MoneInvestForecast"))
def MoneInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1AGMTZAn8M85Uf8KZ9FWFyZ-2Sqb9Yloz", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("MoneLayout"))
def MoneLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1zJQMDW1FYcGNVHdAq0h8itxM7TP9Qhqf", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("MoneChess"))
def MoneChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1Dpi0egOgNVbvR4nfWJQJuENOJMv0pc2o", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("MoneContacts"))
def MoneContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	8962-886-00-56
	Адлер, ул. Ленина, 217А
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.462414, 39.899778)
	cb_qry.answer()





@app.on_callback_query(filters.regex("Атлас"))
def Atlas(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Атлас", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "AtlasPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "AtlasVideo"
				)
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "AtlasRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "AtlasInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "AtlasLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "AtlasChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "AtlasContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)


@app.on_callback_query(filters.regex("AtlasPresentation"))
def AtlasPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, "Презентация Атлас.pdf")
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("AtlasVideo"))
def AtlasVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1AkdXeVjlTw-uTlBlu7p0VqSImiDFNJLp/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("AtlasRenders"))
def AtlasRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/10frIWlu0ZmMdqipNF5MW6VZ7nsdzfiaF", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("AtlasInvestForecast"))
def AtlasInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1OITzWifdd2Lrf8dLS5yHhYXHng-Mer8D", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("AtlasLayout"))
def AtlasLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1X04XZ3XgSiIlyBMgFcl1gVzur2BA05Ib", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("AtlasChess"))
def AtlasChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1WrbEmu-TZhm_MWygO73rvnCuyl83IGls", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("AtlasContacts"))
def AtlasContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	Сочи, ул. Транспортная, 46  
	8962-886-00-40
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.590579, 39.760854)
	cb_qry.answer()


@app.on_callback_query(filters.regex("Diamond"))
def diamond(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Diamond", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "diamondVideo"
				)
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "diamondRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "diamondInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "diamondLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "diamondChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "diamondContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)


	
@app.on_callback_query(filters.regex("diamondVideo"))
def diamondVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://youtu.be/UJRHB5xppTg", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("diamondRenders"))
def diamondRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/16ksTTDu2xTPcQ_IxxItj4Tn2ljAPLcwz", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("diamondInvestForecast"))
def diamondInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1-1V5cnceiCRLooHeUUrSQhLms4Kt7EEt", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("diamondLayout"))
def diamondLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1CI3-H6apTwGL935AtWvWWhqStqsU5_GR", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("diamondChess"))
def diamondChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1BpM0KiTJYk4OdSfVsonxa_z7Fd-rz5G-", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("diamondContacts"))
def diamondContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	Сочи, Ул . Яна Фабрициуса 64
	8966-770-30-22
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.589286, 39.754889)
	cb_qry.answer()




@app.on_callback_query(filters.regex("Лучезарный"))
def Luchezarniy(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Лучезарный", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "LuchezarniyPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "LuchezarniyRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "LuchezarniyInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "LuchezarniyLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "LuchezarniyChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "LuchezarniyContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)




@app.on_callback_query(filters.regex("LuchezarniyPresentation"))
def LuchezarniyPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, "Буклет Лучезарный.pdf")
	cb_qry.answer()
	
	
@app.on_callback_query(filters.regex("LuchezarniyRenders"))
def LuchezarniyRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1YlmEYe0kR0d70UB5gWo27T4c65N6exyd", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("LuchezarniyInvestForecast"))
def LuchezarniyInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/file/d/1sYbuejkKSZnQQnWOHZT-9B9lUZbBSEI_/edit?usp=docslist_api&filetype=mspresentation", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("LuchezarniyLayout"))
def LuchezarniyLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1iSL96UzhSnf0k2DvnBb4uNfKCCPfDcnr", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("LuchezarniyChess"))
def LuchezarniyChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1iQVnzUtMNysR_0w5lmJhU0bRpNs_UgTq", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("LuchezarniyContacts"))
def LuchezarniyContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	Сочи, Дагомыс пос., ул. Лучезарная, 1 
	8800-600-71-83
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.668534, 39.610817)
	cb_qry.answer()





@app.on_callback_query(filters.regex("Woodland"))
def Woodland(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Woodland", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "woodlandPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "woodlandVideo"
				)
			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "woodlandRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "woodlandInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "woodlandLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "woodlandChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "woodlandContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)



@app.on_callback_query(filters.regex("woodlandPresentation"))
def WoodlandPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, "Презентация Woodland.pdf")
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("woodlandVideo"))
def WoodlandVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1-HHvBGE8lyBEGsNDkZibJmlB6kuv7F-V/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("woodlandRenders"))
def WoodlandRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/19tf521utC89MjujdDshVtn38Eh70x03U", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("woodlandInvestForecast"))
def WoodlandInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1AUQgYK4Xtpinw38YL48PzO4mDakEF-2_/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("woodlandLayout"))
def WoodlandLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/19v8Ebm6aI6hi55MVq2k3m-Ilj1APr4hg", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("woodlandChess"))
def WoodlandChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/file/d/1i_2fiUg52-6dRDvTTIDU9l1_hsg0t7MP/edit?usp=docslist_api&filetype=msexcel", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("woodlandContacts"))
def WoodlandContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	8988-418-51-41
	Сочи, Морской переулок, 1/1а
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.576238, 39.724993)
	cb_qry.answer()




@app.on_callback_query(filters.regex("Monteville village"))
def monteville(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Monteville village", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "montevillePresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "montevilleVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "montevilleRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "montevilleInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "montevilleLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "montevilleChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "montevilleContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)


@app.on_callback_query(filters.regex("montevillePresentation"))
def montevillePresentation(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1djyPJg15NadkffVBjo0T2NQi8LEWwRJs", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("montevilleVideo"))
def montevilleVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1djyPJg15NadkffVBjo0T2NQi8LEWwRJs", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("montevilleRenders"))
def montevilleRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1PhiUqmkYCY36keSxxOjdb8lgSxiLNgkp", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("montevilleInvestForecast"))
def montevilleInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1SnIyJxucGBQ9kNDHHSmePhvLDuWXxzHS/view?usp=sharing", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("montevilleLayout"))
def montevilleLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1dhAHH7wYh0a90xDkaBrThNpgGNRV1iIx", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("montevilleChess"))
def montevilleChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/spreadsheets/d/1fcc_S-lX2jzyAoJmLsNRw-epU8GmYBg6rHic1k-NdE0/edit?usp=sharing", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("montevilleContacts"))
def montevilleContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	+7 988 418-51-41
	Сочи, Морской переулок, 1/1а
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.576238, 39.724993)
	cb_qry.answer()




@app.on_callback_query(filters.regex("Olympic"))
def monteville(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Олимпик 2", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "oplympicPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "oplympicVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "oplympicRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "oplympicInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "oplympicLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "oplympicChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "oplympicContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)


@app.on_callback_query(filters.regex("oplympicPresentation"))
def oplympicPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, r"Презентация Олимпик 2.pdf")
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("oplympicVideo"))
def oplympicVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1g-phaJrzBLRTShHFp7ZRYme9cENp2RHq/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("oplympicRenders"))
def oplympicRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1vbRM8zqrWEo9hv7UKsCPa5w1VA8qlma_", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("oplympicInvestForecast"))
def oplympicInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1NweoUrCNeE8qjNySEWyPn20WqIOw65BT/view?usp=drives", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("oplympicLayout"))
def oplympicLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1vebcyv-awjOya4zksIvKNxEhq_N2sXmM", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("oplympicChess"))
def oplympicChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1vlQcgofOZuCQxV2wG6MSXEFPgz2urWVD", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("oplympicContacts"))
def oplympicContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	+7 988 418-51-41
	Сочи, Морской переулок, 1/1а
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.576238, 39.724993)
	cb_qry.answer()





@app.on_callback_query(filters.regex("Sydney"))
def sydney(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Сидней", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "sydneyPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "sydneyVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "sydneyRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "sydneyInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "sydneyLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "sydneyChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "sydneyContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)


@app.on_callback_query(filters.regex("sydneyPresentation"))
def sydneyPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, "Презентация Sydney.pdf")
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sydneyVideo"))
def sydneyVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1L8xlHr93GYU1bPrwrYEu3j82yGngRu6i", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sydneyRenders"))
def sydneyRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1QNcfiKDlfN_LGUkFZN2uCvVvc5xaeZRG", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sydneyInvestForecast"))
def sydneyInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1jfUkfu-3wY-3Q4JPyzvMBQmgnWVV2_eW/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sydneyLayout"))
def sydneyLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1KrPGCW5VGgKgzhkb0qRPv63zbM5nA04R", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sydneyChess"))
def sydneyChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/spreadsheets/d/1W9lz1QHkAlcheuHet_nLUJX_HnUW771mv0UpDv5tL6s/edit ", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sydneyContacts"))
def sydneyContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	+7 988 418-51-41
	Сочи, Морской переулок, 1/1а
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.576238, 39.724993)
	cb_qry.answer()



@app.on_callback_query(filters.regex("Морская симфония"))
def simphony(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Морская симфония", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "simphonyPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "simphonyVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "simphonyRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "simphonyInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "simphonyLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "simphonyChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "simphonyContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)


@app.on_callback_query(filters.regex("simphonyPresentation"))
def simphonyPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, "Презентация Морская симфония 2 - Пентхаусы.pdf")
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("simphonyVideo"))
def simphonyVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/14brwX_AD964VG4U5JARohEdp5ak5_34y/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("simphonyRenders"))
def simphonyRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1gd-l2FJ5NE_lmfyXUsGGh1o_149MnJ33", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("simphonyInvestForecast"))
def simphonyInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1jfUkfu-3wY-3Q4JPyzvMBQmgnWVV2_eW/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("simphonyLayout"))
def simphonyLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/15LiRFIeszJkij_D-G8RCfBcbeKXqOhv9/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("simphonyChess"))
def simphonyChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/file/d/1lhzaRybJ-zqjQ41W-1xh1zmwk8Nq_i4f/edit?usp=docslist_api&filetype=msexcel", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("simphonyContacts"))
def simphonyContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	Адлер, Курортный городок, ул. Ленина, 298
	8800-770-05-66 
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.485847, 39.895817)
	cb_qry.answer()




@app.on_callback_query(filters.regex("Морской квартал"))
def kvartal(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Морской квартал", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "kvartalPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "kvartalVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "kvartalRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "kvartalInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "kvartalLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "kvartalChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "kvartalContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)








@app.on_callback_query(filters.regex("kvartalPresentation"))
def kvartalPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, "Морской Квартал моб презентация.pdf")
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("kvartalVideo"))
def kvartalVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1F7DMkqV5KDVpgE89lNhKb1nqsUcCW1-8/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("kvartalRenders"))
def kvartalRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/15KnVi2fs9hdDwixK8wkErsg8Z7T4Ijne", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("kvartalInvestForecast"))
def kvartalInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1dKNclzBvC-T4LK-N8qfnlV482OyKn13_", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("kvartalLayout"))
def kvartalLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/16FBMrORYcV8WB05NZZ5hjL_TYXstK4Qm", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("kvartalChess"))
def kvartalChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1ekxorcLXK7Rrlmi1096Y0jHGMbz58Im", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("kvartalContacts"))
def kvartalContacts(client, cb_qry:CallbackQuery):	
	contacts = """Контакты 
	8800-600-51-29
	Сочи, ул. Львовская, 74
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.728913, 39.555310)
	cb_qry.answer()









@app.on_callback_query(filters.regex("Verdi"))
def verdi(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Verdi", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "verdiPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "verdiVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "verdiRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "verdiForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "verdiLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "verdiChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "verdiContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)





@app.on_callback_query(filters.regex("verdiPresentation"))
def verdiPresentation(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1Pfu023RyhuO_k63t7a7znQ2aSIJi2ior", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("verdiVideo"))
def verdiVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1AhWg0efILpiWoqiyxDnCyh-Gp_X1EXiB", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("verdiRenders"))
def verdiRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/14VUjEkFnHHfETh1D70YwDC0n7Y3Q7cml", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("verdiInvestForecast"))
def verdiInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/10L5xV-GcUzA6-UNmvr8HNehzf7odGvSV", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("verdiLayout"))
def verdiLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1I5cusaso_6Ae6KWSHQv3RjFlwK9IlxgY", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("verdiChess"))
def verdiChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/spreadsheets/d/1_C2Q9hJpxxGf1U07_w55drO4O3Q4wHcuSAAM8jLiV-4/edit#gid=0", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("verdiContacts"))
def verdiContacts(client, cb_qry:CallbackQuery):	
	contacts = """
	Контакты 
	8800-770-72-23 
	Сочи, ул. Курортный пр., 53
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.576180, 39.728955)
	cb_qry.answer()




@app.on_callback_query(filters.regex("Grand Royal"))
def Royal(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Grand Royal", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "royalPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "royalVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "royalRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "royalInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "royalLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "royalChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "royalContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)



@app.on_callback_query(filters.regex("royalPresentation"))
def royalPresentation(client,cb_qry:CallbackQuery):
	app.send_document(cb_qry.message.chat.id, "Книга -презентация Гранд Роял.pdf")
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("royalVideo"))
def royalVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1r2msFl1cHLZtujDvHfzktO_p7mNjNaiw/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("royalRenders"))
def royalRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1ki2cKSUM5oa2RTvREKjPPzhSs7W7JXFP", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("royalInvestForecast"))
def royalInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/file/d/1IMwOHozrJ4DidH7zFJwoqKolutrTb-EN/view?usp=drivesdk", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("royalLayout"))
def royalLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1k_dEKHSWxxnrSP1rCwXDC8wvI9x72KVf", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("royalChess"))
def royalChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1klvb2bC3GfCbYzRPts50FAnBNpKSLWPq", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("royalContacts"))
def royalContacts(client, cb_qry:CallbackQuery):	
	contacts = """
	Контакты 
	8800-770-01-28
	Сочи, ул. Виноградная, 14
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.576180, 39.728955)
	cb_qry.answer()



@app.on_callback_query(filters.regex("Александрит"))
def Aleksandrit(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Александрит", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "aleksandritVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "aleksandritRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "aleksandritLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "aleksandritChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "aleksandritContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)


	
@app.on_callback_query(filters.regex("aleksandritVideo"))
def aleksandritVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1UvNP-XSWSW4YeLqqFoSXVSKhU-ifkJCH", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("aleksandritRenders"))
def aleksandritRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1-JRJW2dUvzPI4wSVe8w1lNiaehhEb8NP", cb_qry.message.chat.id)
	cb_qry.answer()
	
	
@app.on_callback_query(filters.regex("aleksandritLayout"))
def aleksandritLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1-CO6BQEcJqv_ucmQkWlLDzj4TGUZTlgY", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("aleksandritChess"))
def aleksandritChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/spreadsheets/d/1JihDr-ZQ3Udfivdx1gHpHtBdvX0pAsX4/edit?rtpof=true", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("aleksandritContacts"))
def aleksandritContacts(client, cb_qry:CallbackQuery):	
	contacts = """
	Контакты 
	8 (800) 770-72-23 
	Сочи, Завокзальный, ул. Дагомысская, 27
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 43.599843, 39.739645)
	cb_qry.answer()



@app.on_callback_query(filters.regex("Sunhills Olginka"))
def sun(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Sunhills Olginka", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Презентация",
				callback_data = "sunPresentation"
				)
			],
			[
				InlineKeyboardButton(
				"Видео",
				callback_data = "sunVideo"
				)			
			],
			[
				InlineKeyboardButton(
				"Визуализация",
				callback_data = "sunRenders"
				)
			],
			[
				InlineKeyboardButton(
				"Инвест прогнозы",
				callback_data = "sunInvestForecast"
				)
			],
			[
				InlineKeyboardButton(
				"Планировки",
				callback_data = "sunLayout"
				)
			],
			[
				InlineKeyboardButton(
				"Шахматка",
				callback_data = "sunChess"
				)
			],	
			[
				InlineKeyboardButton(
				"Контакты",
				callback_data = "sunContacts"
				)
			], 
			[
				InlineKeyboardButton(
				"Назад◀",
				callback_data = "Back️"
				)
			]
		]
	)
)





@app.on_callback_query(filters.regex("sunPresentation"))
def sunPresentation(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1AinGTjTVWNOIYI0BddVnV45fxdgY2Z64", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sunVideo"))
def sunVideo(client,cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1AinGTjTVWNOIYI0BddVnV45fxdgY2Z64", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sunRenders"))
def sunRenders(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1ARZy-7lGhF_e5-5yjUL49VuPQaiZXI54", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sunInvestForecast"))
def sunInvestForecast(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1hbEuwvwxQVEwcc0XPhYJSeqsMB0Ba7t5", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sunLayout"))
def sunLayout(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://drive.google.com/drive/folders/1AeFsCX9cNeIhs8V7paYb5O69UJNqN85t", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sunChess"))
def sunChess(client, cb_qry:CallbackQuery):
	cb_qry.message.reply_text("https://docs.google.com/spreadsheets/d/1WJ_kUM2QhaNVcy2LkkMlkVzNUZk5zyqFmL83XrC-vM8/edit?usp=drive_web&ouid=115270691017003339089", cb_qry.message.chat.id)
	cb_qry.answer()
	
@app.on_callback_query(filters.regex("sunContacts"))
def sunContacts(client, cb_qry:CallbackQuery):	
	contacts = """
	Контакты 
	8999-428-09-79 
	8999-428-09-80
	Ольгинка, Краснодарский край, ул.Солнечная, 1/1 
	"""
	contacts = dedent(contacts)
	cb_qry.message.reply_text(f"<b>{contacts}</b>",cb_qry.message.chat.id, parse_mode = "HTML")
	app.send_location(cb_qry.message.chat.id, 44.199914, 38.890548)
	cb_qry.answer()



@app.on_callback_query(filters.regex("Back"))
def Back(client,cb_qry:CallbackQuery):
	cb_qry.message.edit("Выберите интересующий объект:", reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				"Atrium Avenue",
				callback_data = "Atrium Avenue"
				)
			],
			[
				InlineKeyboardButton(
				"Volna Hotel Resort & SPA",
				callback_data = "Волна"
				)
			],	
			[   
				InlineKeyboardButton(
				"Volna Residence",
				callback_data = "Волна Резиднес"
				)
			],
			[   
				InlineKeyboardButton(
				"Моне",
				callback_data = "Моне"
				)
			],
			[   
				InlineKeyboardButton(
				"Атлас",
				callback_data = "Атлас"
				)
			],
			[
				InlineKeyboardButton(
				"Diamond",
				callback_data = "Diamond"
				)
			],
			[   
				InlineKeyboardButton(
				"Лучезарный",
				callback_data = "Лучезарный"
				)
			],
			[   
				InlineKeyboardButton(
				"Woodland",
				callback_data = "Woodland"
				)
			],
			[   
				InlineKeyboardButton(
				"Monteville village",
				callback_data = "Monteville village"
				)
			],
			[   
				InlineKeyboardButton(
				"Олимпик 2",
				callback_data = "Olympic"
				)
			],
			[   
				InlineKeyboardButton(
				"Сидней",
				callback_data = "Sydney"
				)
			],
			[   
				InlineKeyboardButton(
				"Морская симфония 2",
				callback_data = "Морская симфония"
				)
			],
			[   
				InlineKeyboardButton(
				"Морской квартал",
				callback_data = "Морской квартал"
				)
			],
			[   
				InlineKeyboardButton(
				"Verdi",
				callback_data = "Verdi"
				)
			],
			[   
				InlineKeyboardButton(
				"Grand Royal",
				callback_data = "Grand Royal"
				)
			],
			[   
				InlineKeyboardButton(
				"Александрит",
				callback_data = "Александрит"
				)
			],
			[   
				InlineKeyboardButton(
				"Sunhills Olginka",
				callback_data = "Sunhills Olginka"
				)
			]	
		]
	)
)
	























	
@app.on_message(filters.regex("Программа лояльности"))
def loyal_program(client,message):
	app.send_document(message.chat.id, "Программа лояльности (Mobile).pdf")

@app.on_message(filters.regex("Партнерская программа"))
def partner_program(client,message):
	app.send_document(message.chat.id, "Партнерская программа (Mobile).pdf")



app.run()
