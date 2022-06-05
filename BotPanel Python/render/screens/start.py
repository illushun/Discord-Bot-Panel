import dearpygui.dearpygui as dpg

import render.app as app
import bot.client as client
import storage.token as token

getTag={
    "window": "createBot_Window",
    "tokenType": "tokeType_List", 
    "tokenInput": "botToken_Input",
    "customToken": "customToken_Group",
    "storedToken": "storedToken_Group",
    "botPrefix": "botPrefix_Input",
    "tokenList": "tokenList_Combo",
    "displayBotName": "displayBotName_Text",
    "botName": "botName_Input",
    "eventMessages": "eventMessages_Input",
    "botStartupMessages": "botStartupMessages_Input",
    "memberJoinMessages": "memberJoinMessages_Input"
}

tokenInputList=["Custom Token", "Stored Tokens"]
tokenStoredList=[]

def close_bot_instance():
    dpg.delete_item(getTag["window"])

def start_bot(sender):
    botToken=""
    botPrefix=""

    if len(dpg.get_value(getTag["tokenInput"]))<=0:
        print("No token input...")
        if len(dpg.get_value(getTag["tokenList"]))<=0:
            print("No token list...")
            return
        print("Getting token from token list...")
        botToken=token.Token().get_property(dpg.get_value(getTag["tokenList"]), "token")
        botPrefix=token.Token().get_property(dpg.get_value(getTag["tokenList"]), "prefix")
    else:
        botToken=dpg.get_value(getTag["tokenInput"])
        botPrefix=dpg.get_value(getTag["botPrefix"])
    
    if len(botPrefix)<=0:
        print("No bot prefix...")
        return

    # run bot here...
    global get_client
    global event_loop
    event_loop=client.EventLoop().create()
    get_client=client.Client(botPrefix, event_loop).get_client()
    client.Client().run(event_loop, get_client, botToken)

def populate_stored_tokens():
    for object in token.Token().get_token_list():
        if not tokenStoredList.__contains__(object):
            tokenStoredList.append(object)
    dpg.configure_item(getTag["tokenList"], items=tokenStoredList)

def store_token():
    botToken=dpg.get_value(getTag["tokenInput"])
    botPrefix=dpg.get_value(getTag["botPrefix"])
    botName=dpg.get_value(getTag["botName"])

    if len(botToken)<=0 or len(botPrefix)<=0 or len(botName)<=0:
        return
    
    for object in token.Token().get_token_list():
        if object == botToken:
            break
        tokenStoredList.append(botName)
    token.Token().add(botName, botToken, botPrefix)

def get_token_type(sender, app_data):
    itemCfg=dpg.get_item_configuration(sender)
    for line, item in enumerate(itemCfg["items"]):
        if item==app_data:
            if app_data==tokenInputList[0]:
                dpg.hide_item(getTag["storedToken"])
                return
            if app_data==tokenInputList[1]:
                dpg.show_item(getTag["storedToken"])
                return
            dpg.hide_item(getTag["storedToken"])
            return

def update_selected_bot():
    if len(dpg.get_value(getTag["botName"]))<=0:
        dpg.set_value(getTag["displayBotName"], "None")
        return
    dpg.set_value(getTag["displayBotName"], dpg.get_value(getTag["botName"]))

def update_input_values(sender, app_data):
    botName=str(app_data)
    botToken=token.Token().get_property(botName, "token")
    botPrefix=token.Token().get_property(botName, "prefix")
    dpg.set_value(getTag["tokenInput"], botToken)
    dpg.set_value(getTag["botPrefix"], botPrefix)
    dpg.set_value(getTag["botName"], botName)


def update_textbox(tag: str, message: str):
    maxLength=40
    messageSplit=[message[i: i+maxLength] for i in range(0, len(message), maxLength)]
    for messages in messageSplit:
        dpg.set_value(tag, dpg.get_value(tag)+str(messages)+"\n")


# gui window
def start():
    dpg.push_container_stack(dpg.add_window(label="Manage a bot...", tag=getTag["window"], no_collapse=True, on_close=close_bot_instance, no_resize=True, no_move=True, width=app.WIDTH - 16, height=app.HEIGHT - 36))
    
    dpg.push_container_stack(dpg.add_tab_bar())

    dpg.push_container_stack(dpg.add_tab(label="Start"))

    dpg.push_container_stack(dpg.add_child_window(label="body", border=False, autosize_x=True, height=app.HEIGHT - 156))

    with dpg.group(horizontal=True):
        dpg.add_text("Selected Bot: ")
        dpg.add_button(label="Update", callback=update_selected_bot)

    dpg.add_text("None", tag=getTag["displayBotName"])
    
    dpg.add_separator()

    dpg.add_button(label="Start Bot", callback=start_bot)

    # pop child_window container
    dpg.pop_container_stack()

    dpg.push_container_stack(dpg.add_child_window(label="footer", no_scrollbar=True, autosize_x=True, autosize_y=True))
    with dpg.group(horizontal=False):
        dpg.add_text("Created by illusion#5641")
    
    # pop child_window container
    dpg.pop_container_stack()

    # pop first tab
    dpg.pop_container_stack()

    dpg.push_container_stack(dpg.add_tab(label="Setup"))

    dpg.push_container_stack(dpg.add_child_window(label="body", border=False, autosize_x=True, height=app.HEIGHT - 156))

    dpg.add_listbox(items=tokenInputList, callback=get_token_type, tag=getTag["tokenType"])

    with dpg.group(horizontal=False, tag=getTag["storedToken"], show=False):
        dpg.add_text("Token List:")
        with dpg.group(horizontal=True):
            dpg.add_combo(items=tokenStoredList, tag=getTag["tokenList"], callback=update_input_values)
            dpg.add_button(label="Update", callback=populate_stored_tokens)

    with dpg.group(horizontal=False, tag=getTag["customToken"], show=True):
        dpg.add_text("Bot Token:")
        with dpg.group(horizontal=True):
            dpg.add_input_text(tag=getTag["tokenInput"], password=True)

    dpg.add_text("Bot Name:")
    dpg.add_input_text(tag=getTag["botName"])

    dpg.add_text("Bot Prefix:")
    dpg.add_input_text(tag=getTag["botPrefix"])

    dpg.add_separator()

    dpg.add_button(label="Save", callback=store_token)

    # pop child_window container
    dpg.pop_container_stack()

    dpg.push_container_stack(dpg.add_child_window(label="footer", no_scrollbar=True, autosize_x=True, autosize_y=True))
    with dpg.group(horizontal=False):
        dpg.add_text("Created by illusion#5641")
    
    # pop child_window container
    dpg.pop_container_stack()

    # pop tab container
    dpg.pop_container_stack()

    dpg.push_container_stack(dpg.add_tab(label="Events"))

    with dpg.group(horizontal=True, width=(app.WIDTH - 40) / 2):
        with dpg.group(horizontal=False):
            dpg.add_text("Messages:")
            dpg.add_input_text(tag=getTag["eventMessages"], multiline=True)
            dpg.add_button(label="Export")

        with dpg.group(horizontal=False):
            dpg.add_text("Bot Connections:")
            dpg.add_input_text(tag=getTag["botStartupMessages"], multiline=True)
            dpg.add_button(label="Export")

    with dpg.group(horizontal=True, width=(app.WIDTH - 40) / 2):
        with dpg.group(horizontal=False):
            dpg.add_text("Member Joins:")
            dpg.add_input_text(tag=getTag["memberJoinMessages"], multiline=True)
            dpg.add_button(label="Export")

        with dpg.group(horizontal=False):
            dpg.add_text("Yet Another:")
            dpg.add_input_text(multiline=True)
            dpg.add_button(label="Export")

    # pop second tab
    dpg.pop_container_stack()

    # pop tab_bar
    dpg.pop_container_stack()

    # pop window
    dpg.pop_container_stack()