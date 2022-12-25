from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


app = ApplicationBuilder().token("5901572992:AAHqgxQb1WzJwTu04naITwnpc3Z9cId2fd8").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()



# import matplotlib.pyplot as plt
# import numpy as np
# plt.style.use('_mpl-gallery')

# # make data:
# np.random.seed(3)
# x = 0.5 + np.arange(8)
# y = np.random.uniform(2, 7, len(x))

# # plot
# fig, ax = plt.subplots()

# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.plot(list)
# plt.show()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# # Python is 👍
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# # Python is 👍
# print(emoji.demojize('Python is 👍'))
# # Python is :thumbs_up:
# print(emoji.emojize("Python is fun :red_heart:"))
# # Python is fun ❤
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# # Python is fun ❤️ #red heart, not black heart
# print(emoji.is_emoji("👍"))
# # True




# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()

# from isOdd import isOdd

# print(isOdd(1)) # //=> true
# print(isOdd(5)) # //=> true

# print(isOdd(0)) # //=> false
# print(isOdd(4)) # //=> false


# python -m pip freeze > requirements.txt
# python -m pip install -r requirements.txt
