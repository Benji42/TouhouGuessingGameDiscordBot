from app.bot import Bot

def main():
    #Entrypoint for bot
    global bot
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()