
from discord.ext import commands
import os
import uuid
from PIL import Image
import numpy as np
from keras.models import load_model

model = load_model('model/modelo.h5')

sinalizacoes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons'
          }

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print(f"{bot.user} está online!")

@bot.command(name = "predict")
async def save(ctx):
  try:
      file_path = ""
      imgName = str(uuid.uuid4()) + '.png'
      await ctx.message.attachments[0].save(imgName)
      file_path = os.getcwd()
      file_path = file_path + "\\"+imgName
      image = Image.open(file_path).convert("RGB")
      image = image.resize((30,30))
      image = np.expand_dims(image, axis=0)
      image = np.array(image)
      y_prob = model.predict(image)
      sign=(np.argmax(y_prob,axis=1) + 1)
      placa = sinalizacoes[int(sign)]
      print(placa)
      await ctx.send("Placa: " + placa) 

  except:
    print("Erro: Imagem não encontrada no Dataset")
    await ctx.send("Imagem não existe no dataset")
    
bot.run("OTgzMjEyNjUxMTI5NzM3MjE2.GQpbIz.Ht4p3g0x9VF5BnmaI1xJGvK9LTuMgzrFnMSlK4")
