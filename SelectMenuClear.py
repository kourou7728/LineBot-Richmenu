from linebot import LineBotApi

channel_access_token = ''
rich_menu_id = ''


line_bot_api = LineBotApi(channel_access_token)
line_bot_api.delete_rich_menu(rich_menu_id)

print('Rich Menu deleted successfully.')
