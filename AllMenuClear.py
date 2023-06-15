from linebot import LineBotApi

channel_access_token = 'YOUR_CHANNEL_ACCESS_TOKEN'
line_bot_api = LineBotApi(channel_access_token)

# 獲取已設置的 Rich Menu 列表
rich_menu_list = line_bot_api.get_rich_menu_list()

# 刪除每個 Rich Menu
for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)
    line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)

print('All Rich Menus have been deleted.')
