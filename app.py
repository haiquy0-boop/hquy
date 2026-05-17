import telebot
import threading
import time
import random
import os
import json
from flask import Flask

# ================= WEB =================

app = Flask(__name__)

@app.route('/')
def home():
    return "ONLINE"

# ================= DATABASE =================

DATA_FILE = "bot_data.json"

def load_data():

    if os.path.exists(DATA_FILE):

        try:

            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

        except:
            pass

    return {
        "admins": [7153197678]
    }

def save_data(data):

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

db = load_data()

OWNER_ID = 7153197678

# ================= CONFIG =================

DELAY_TIME = 0.1

stop_event = threading.Event()

# ================= TOKEN =================

RAW_TOKENS = [
'8675065386:AAHVtY8NYQOykrCCEQ9tQDpe_mZK9XUmVV0', '8750639984:AAGAU7SsEe_V9CpZ9LAfxovI2iFWSCQ9riw',
    '8423233437:AAFPeFNFctZlgO8VU_KGkp_HT71FCTywUmI', '8705345450:AAHAxsFUHu7ux4USLvItL018KD4hBsTe4_Q',
    '8144155270:AAH-y47kIAFWgo7sge1VmCMrx2dc9CkYxOs', '8688293059:AAGoga_q3E7VbZQ3sL6xZ3-vzGgtC7RsTmc',
    '8652311818:AAGmFWSeRYW1-RQ-RH8jNguwkRtzFt0U-oQ', '8731497895:AAHHhCiAp7a62eflQBe0PztWw0jRjDPpyk4',
    '8684330434:AAEORwA4uvBXIm-orys4txSttOnkH2CRwZ4', '8796842934:AAENmEMod5CHQxfcl6Z5kl3nlwv8slQLJJc',
    '8668865669:AAGMgG3zBSN69eDYzTHENxl6Y9AAj6Kln4Q', '8429960682:AAHltNvwWjEn1QC_f5R8JPgz7uN1uFhny18', 
    '8481938728:AAGen1t8Tz3jeu02kJ8HoCIZLiPLdd687n8', '8739448460:AAGNLEW-WDvatvatMplzkziG5pd5hTRfqiE', 
    '8689807630:AAEoXvm45QaW1jlT-H_KzNlmCpu50Q3k2S4', '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', 
    '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0', '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', 
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA', 
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0', 
    '8650032681:AAE9TeiIIywG796f6hHLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0', 
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY', 
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4', 
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o'
]

VALID_BOTS = []

# ================= ADMIN =================

def is_admin(uid):

    return (
        uid == OWNER_ID
        or uid in db["admins"]
    )

# ================= LOAD TEXT =================

def get_text():

    lines = []

    for fname in ["chui.txt", "ngontagtele.txt"]:

        if os.path.exists(fname):

            try:

                with open(fname, "r", encoding="utf-8") as f:

                    for line in f:

                        clean = line.strip()

                        if clean:
                            lines.append(clean)

            except:
                pass

    if not lines:
        lines = ["Hai Quy"]

    chunk = max(1, len(lines) // 4)

    return {
        "sp": lines[:chunk],
        "sp2": lines[chunk:chunk*2],
        "sptag": lines[chunk*2:chunk*3],
        "spslow": lines[chunk*3:]
    }

KHO_DAN = get_text()

# ================= SPAM =================

def attack_logic(
    bot,
    chat_id,
    lines,
    mode="normal"
):

    while not stop_event.is_set():

        try:

            bot.send_message(
                chat_id,
                random.choice(lines)
            )

            if mode == "slow":
                time.sleep(2.5)
            else:
                time.sleep(DELAY_TIME)

        except:
            break

# ================= MAIN =================

def start_master():

    if not VALID_BOTS:
        print("NO BOT")
        return

    master = VALID_BOTS[0]

    @master.message_handler(func=lambda m: True)
    def handle_all(m):

        global DELAY_TIME

        try:

            uid = m.from_user.id
            gid = m.chat.id

            if not m.text:
                return

            args = m.text.strip().split()

            if not args:
                return

            cmd = args[0].lower()

            # ============ HELP ============

            if cmd == "/help":

    master.reply_to(
        m,
        (
            "───「 HAI QUY 2026 」───\n\n"

            "🔥 SPAM & TAG\n"
            "┣ /sp\n"
            "┣ /sp2\n"
            "┣ /sptag\n"
            "┣ /spslow\n"
            "┣ /spnd <text>\n\n"

            "⚙️ TIỆN ÍCH\n"
            "┣ /dung\n"
            "┣ /listbot\n"
            "┣ /info\n"
            "┗ /setdelay <s>"
        )
    )
                    )
                )

            # ============ ADMIN PANEL ============

            elif cmd == "/ad":

                if is_admin(uid):

                    master.reply_to(
                        m,
                        (
                            "👑 ADMIN PANEL\n\n"

                            "/addadm <id>\n"
                            "/xoaadm <id>\n"
                          
                        )
                    )

            # ============ INFO ============

            elif cmd == "/info":

                master.reply_to(
                    m,
                    (
                        f"👤 {m.from_user.first_name}\n"
                        f"🆔 {uid}\n"
                        f"💬 {gid}"
                    )
                )

            # ============ LISTBOT ============

            elif cmd == "/listbot":

                master.reply_to(
                    m,
                    f"🤖 Online: {len(VALID_BOTS)}"
                )

            # ============ SP ============

            elif cmd in [
                "/sp",
                "/sp2",
                "/sptag",
                "/spslow",
                "/spnd"
            ]:

                stop_event.clear()

                # custom text

                if cmd == "/spnd":

                    if len(args) < 2:

                        master.reply_to(
                            m,
                            "❌ Thiếu nội dung"
                        )

                        return

                    nd = [
                        " ".join(args[1:])
                    ]

                    for b in VALID_BOTS:

                        threading.Thread(
                            target=attack_logic,
                            args=(
                                b,
                                gid,
                                nd
                            ),
                            daemon=True
                        ).start()

                else:

                    dan = KHO_DAN.get(
                        cmd[1:],
                        KHO_DAN["sp"]
                    )

                    mode = (
                        "slow"
                        if cmd == "/spslow"
                        else "normal"
                    )

                    for b in VALID_BOTS:

                        threading.Thread(
                            target=attack_logic,
                            args=(
                                b,
                                gid,
                                dan,
                                mode
                            ),
                            daemon=True
                        ).start()

            # ============ STOP ============

            elif cmd == "/dung":

                stop_event.set()

                master.reply_to(
                    m,
                    "🛑 STOPPED"
                )

            # ============ ADMIN ============

            elif is_admin(uid):

                # add admin

                if cmd == "/addadm":

                    if len(args) < 2:
                        return

                    try:

                        new_id = int(args[1])

                        if new_id not in db["admins"]:

                            db["admins"].append(
                                new_id
                            )

                            save_data(db)

                        master.reply_to(
                            m,
                            "✅ Added"
                        )

                    except:

                        master.reply_to(
                            m,
                            "❌ ID lỗi"
                        )

                # remove admin

                elif cmd == "/xoaadm":

                    if len(args) < 2:
                        return

                    try:

                        rm_id = int(args[1])

                        if rm_id in db["admins"]:

                            db["admins"].remove(
                                rm_id
                            )

                            save_data(db)

                            master.reply_to(
                                m,
                                "🗑 Removed"
                            )

                    except:
                        pass

                # set delay

                elif cmd == "/setdelay":

                    if len(args) < 2:
                        return

                    try:

                        val = float(args[1])

                        if val < 0:
                            val = 0

                        DELAY_TIME = val

                        master.reply_to(
                            m,
                            f"⏳ {DELAY_TIME}s"
                        )

                    except:

                        master.reply_to(
                            m,
                            "❌ Delay lỗi"
                        )

        except Exception as ex:

            print("ERROR:", ex)

    master.infinity_polling(
        timeout=30,
        long_polling_timeout=30
    )

# ================= TOKEN FILTER =================

def filter_system():

    for t in RAW_TOKENS:

        try:

            bot = telebot.TeleBot(
                t,
                threaded=False
            )

            bot.get_me()

            VALID_BOTS.append(bot)

            print(
                f"Loaded: {bot.get_me().username}"
            )

        except:

            print(
                f"Dead token: {t[:15]}"
            )

# ================= MAIN =================

if __name__ == "__main__":

    threading.Thread(
        target=lambda: app.run(
            host="0.0.0.0",
            port=8080
        ),
        daemon=True
    ).start()

    filter_system()

    start_master()
