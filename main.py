import PySimpleGUI as sg
import shop_list



add_btn = sg.Button("Add", key="Add")
input_scr = sg.Input(tooltip="enter a food", key="item")
shopping_listbox = sg.Listbox(values=shop_list.get_todos(), key='items',
                            enable_events=True, size=[49, 10])
edit_btn = sg.Button("Edit", key="Edit")
delete_btn = sg.Button("Delete", key="Delete")
message_added = sg.Text(key="add_message")

layout = [[add_btn, input_scr],[shopping_listbox],[edit_btn, delete_btn],[message_added]]
window = sg.Window("My Shopping List",layout=layout, font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            items = shop_list.get_items()
            item = values["item"] + "\n"
            items.append(item)
            shop_list.write_items(items)
            window["add_message"].update(f"Item added: {values['item']}")
            window['items'].update(values=items)
        case "Edit":
            item_edit = values["items"][0]
            new_item = values["item"]

            items = shop_list.get_items()
            index = items.index(item_edit)

            items[index] = new_item
            shop_list.write_items(items)
            window['items'].update(values=items)
            window["add_message"].update("item edited!")
        case "items":
            window["item"].update(value=(values["items"][0]))
        case "Delete":

        case sg.WINDOW_CLOSED:
            exit()



window.close()