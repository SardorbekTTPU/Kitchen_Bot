from environs import Env
# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = [952552114] #env.int("ADMINS") #Adminlar
IP = env.str("ip")  # Xosting ip manzili


