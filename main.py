from winotify import Notification, audio

toast = Notification(
    app_id="Hakanx",
    title="Hepimiz Aynıyız",
    msg="Buraya Tıkla",
    duration="long",
    icon=r"C:\Users\Candan Bilgisayar\Desktop\bildirimcik\warning_icon_preview.png")

toast.add_actions(label="Tıkla",
launch="aaaa")
toast.set_audio(audio.Reminder, loop=False)
toast.show()