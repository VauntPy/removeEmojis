from pathlib import Path
import emojiArray
import os

emojis = emojiArray.emojis

path  = Path('./testfolder').absolute()
os.chdir(path)
for element in path.iterdir():
  for emoji in emojis:
    if(emoji in element.name):
      newName = element.name.replace(emoji, '')
      element.rename(newName)