import re
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

# List of anime names
anime_database = [
    "Attack on Titan", "Naruto", "Fullmetal Alchemist: Brotherhood", "My Hero Academia", 
    "One Piece", "Demon Slayer: Kimetsu no Yaiba", "Death Note", "Dragon Ball Z", 
    "Tokyo Ghoul", "Sword Art Online", "Neon Genesis Evangelion", "Hunter x Hunter", 
    "One Punch Man", "Your Name", "Spirited Away", "Akira", "Steins;Gate", "Code Geass", 
    "Bleach", "Naruto Shippuden", "Fruits Basket", "Mob Psycho 100", 
    "Re:Zero - Starting Life in Another World", "Bleach: Thousand-Year Blood War", "Fairy Tail",
    "The Promised Neverland", "Black Clover", "JoJo’s Bizarre Adventure", "No Game No Life", 
    "Cowboy Bebop", "Trigun", "Inuyasha", "Fate/Zero", "Gurren Lagann", "Clannad", 
    "Violet Evergarden", "Made in Abyss", "Psycho-Pass", "Hellsing Ultimate", "Yu Yu Hakusho", 
    "Black Lagoon", "Elfen Lied", "Mob Psycho 100 II", "Angel Beats!", "Durarara!!", 
    "Cowboy Bebop: The Movie", "The Tale of the Princess Kaguya", "A Silent Voice", 
    "Weathering with You", "Howl’s Moving Castle", "The Wind Rises", "My Neighbor Totoro", 
    "Princess Mononoke", "Nausicaä of the Valley of the Wind", "The Secret World of Arrietty", 
    "Kiki’s Delivery Service", "The Cat Returns", "Ponyo", "When Marnie Was There", "Your Lie in April",
    "March Comes in Like a Lion", "The Ancient Magus’ Bride", "Akame ga Kill!", "Black Bullet", 
    "Re:Creators", "Slam Dunk", "Great Teacher Onizuka", "Mushishi", "The Irregular at Magic High School", 
    "Noir", "Witch Hunter Robin", "Fate/stay night: Unlimited Blade Works", "Log Horizon", 
    "Bleach: The DiamondDust Rebellion", "Rurouni Kenshin", "Berserk", "Gintama", "Sailor Moon", 
    "Fushigi Yûgi", "The Melancholy of Haruhi Suzumiya", "Love Live! School Idol Project", 
    "Toradora!", "Steins;Gate 0", "High School DxD", "The Rising of the Shield Hero", 
    "KonoSuba: God’s Blessing on this Wonderful World!", "My Teen Romantic Comedy SNAFU", 
    "Alderamin on the Sky", "ReLIFE", "March Comes in Like a Lion", "Noragami", "Maid-Sama!", 
    "Ouran High School Host Club", "K-On!", "Kimi ni Todoke", "Attack on Titan: The Final Season", 
    "Gintama°", "Hunter x Hunter (2011)", "Black Clover: Sword of the Wizard King", "Tokyo Revengers", 
    "Beastars", "Weathering with You", "The Garden of Words", "Children Who Chase Lost Voices", 
    "In This Corner of the World", "Fruits Basket (2019)", "A Place Further than the Universe", 
    "Made in Abyss: Dawn of the Deep Soul", "Shingeki no Kyojin: Lost Girls", "Monogatari Series", 
    "Mob Psycho 100 III", "Vinland Saga", "Beelzebub", "Goblin Slayer", 
    "Konosuba: An Explosion on This Wonderful World!", "Attack on Titan: No Regrets", "Nodame Cantabile", 
    "Kuroko no Basket", "Haikyuu!!", "D.Gray-man", "Monogatari Series: Second Season", "Katanagatari", 
    "Kuroko no Basket: Winter Cup", "Mob Psycho 100 II", "Violet Evergarden: Eternity and the Auto Memory Doll", 
    "The Promised Neverland: Season 2", "Sword Art Online: Alicization - War of Underworld", 
    "The World God Only Knows", "Bleach: Memories of Nobody", "Blue Exorcist", 
    "Promare", "The Witcher: Nightmare of the Wolf", "The Case Study of Vanitas", "Dr. Stone", 
    "Demon Slayer: Mugen Train", "The Irregular at Magic High School: The Girl Who Summons the Stars", 
    "My Hero Academia: Heroes Rising", "Jujutsu Kaisen", "The Seven Deadly Sins", "Dorohedoro", "Erased", 
    "Vinland Saga", "Demon Slayer", "Black Clover"
]

# Search function for anime names
def search_anime(text):
    for anime in anime_database:
        if re.search(r'\b' + re.escape(anime) + r'\b', text, re.IGNORECASE):  # Matching anime names
            return f"Found anime: {anime}"
    return None

# Message handler for real-time search
def handle_message(update: Update, context):
    message_text = update.message.text
    if update.message.chat.type == "group":  # Only works in groups
        anime_info = search_anime(message_text)
        if anime_info:
            update.message.reply_text(anime_info)  # Reply with found anime
        else:
            update.message.reply_text("Anime not found.")  # Reply if anime not found

# Start the bot
def main():
    # Telegram bot API token
    updater = Updater("7758423195:AAFzOGYwyaZMyrUgv5tqWanLStlP7DcgkLI", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex(r'.*'), handle_message))  # Text filter

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
