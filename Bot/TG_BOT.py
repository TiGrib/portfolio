#!/usr/bin/env python
# coding: utf-8

# In[2]:


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import consts
import logging
import os






def start(bot, update):
    bot.effective_message.reply_text("Hi!")
def echo(bot, update):
    update.effective_message.reply_text(update.effective_message.text)
def error(bot, update, error):
    logger.warning(f'Update {update} caused error {error}')

if __name__== '__main__':
    TOKEN=consts.token
    NAME="Itgmessage"
    PORT=os.environ.get('PORT')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    logger = logging.getLogger(__name__)
    updater=Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.setWebhook(f"https://{NAME}.herokuapp.com/{TOKEN}")
    updater.idle()



# In[ ]:




