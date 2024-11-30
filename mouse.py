"""def start():
    print("started!")

def stop():
    print("stoped!")

messge_hendel = {
    "Start": start,
    "Stop": stop
}

user_message = input("enter message: ")
do = messge_hendel.get(user_message)

if do:
    print(messge_hendel.keys())
    do()

 if received_message == "Hello There":
        await context.bot.send_message(chat_id=CHAT_ID, text=f"Hi, how can i help you?")

    elif "youtube.com" in received_message and "https://" in received_message:
        webbrowser.open(url=received_message)
        await context.bot.send_message(chat_id=CHAT_ID, text="Done.")

    elif "YouTubeSearch" in received_message:
        keyWord = received_message.replace("YouTubeSearch ", "")
        looper = 1
        links = [v.watch_url for v in Search(keyWord).results]
        for link in links[:4]:
            info = YoutubeDL({"quiet": True}).extract_info(link, download=False)
            await context.bot.send_message(
                chat_id=CHAT_ID,
                text=f"The results : (video {looper} : (Title: {info.get('title', 'N/A')}, Views: {info.get('view_count', 'N/A')}, Link: {link})\n)",
            )
            looper += 1
        await context.bot.send_message(chat_id=CHAT_ID, text="Done")

   elif "Goto" in received_message:
        path = received_message.replace("Goto ", "")
        for Name in range(len(FileManager(path).getFiles())):
            await context.bot.send_message(
                chat_id=CHAT_ID, text=f"{FileManager(path).getFiles()[Name]}"
            )

    elif "Getfrom" in received_message:
        path = received_message.replace("Getfrom ", "").split(" ")
        name = FileManager(path[0]).getpath(' '.join(path[1:]))
        try:
            await context.bot.sendDocument(
                chat_id=CHAT_ID,
                document=name,
                caption=f"This is {path[1]} from {path[0]} folder",
                write_timeout=120,
            )
        except Exception as ex:
            await context.bot.send_message(
                chat_id=CHAT_ID, text=f"I got {ex} Error :( "
            )

    elif "Site" in received_message:
        URL = received_message.replace("Site ", "")
        if "https://" not in URL:
            webbrowser.open(url=f"https://www.{URL}")
        else:
            webbrowser.open(url=URL)
    elif "lock" in received_message:

    elif "pause" in received_message:
        pass
"""
