from linebot import LineBotApi

channel_access_token = 'YOUR_CHANNEL_ACCESS_TOKEN'
rich_menu_id = 'rich_menu_id'


line_bot_api = LineBotApi(channel_access_token)
line_bot_api.delete_rich_menu(rich_menu_id)

print('Rich Menu deleted successfully.')
