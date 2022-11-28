from pathlib import Path
import emojiArray
import os

emojis = emojiArray.emojis
actName = ''
path  = Path('./RELATIVEPATHTOMAIN.PY').absolute()
print(path)

os.chdir(path)
for element in path.iterdir():
  actName = element.name
  for emoji in emojis:
    if(emoji in actName):
      newName = actName.replace(emoji, '')
      actName = newName
  print(element.name)
  element.rename(actName)
