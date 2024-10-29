import os
import numpy as np
from pdf2image import convert_from_path

from source.preprocessing import preprocess
from source.ocr import load, predict
from source.export import export
from source.visualize import visualize

os.chdir(os.path.dirname(__file__))

print("""
              _         ___  __  __ ____  
   __ _ _   _| |_ ___  / _ \\|  \\/  |  _ \\ 
  / _` | | | | __/ _ \\| | | | |\\/| | |_) |
 | (_| | |_| | || (_) | |_| | |  | |  _ < 
  \\__,_|\\__,_|\\__\\___/ \\___/|_|  |_|_| \\_\\
                    (c) 2024, Team autoOMR
                                          """)

print("Initializing...")
try:
  pages = convert_from_path("files/input.pdf")
except:
  print("Error: PDF file not found.")
  print("Be sure to place input.pdf in the 'files' directory.")
  exit()
model = load()
results = {}
print("CNN Model loaded.")
input("Press Enter to start processing...")

for i, page in enumerate(pages):
  image = np.array(page)
  croppedrects = preprocess(image)
  answers = []
  for img in croppedrects:
    text = predict(model, img)
    answers.append(text)
  if answers:
    results[answers[0]] = answers[1:]
  else:
    print(f'No answers found on page {i+1}. Skipping...')

print(results)

print("Done. Displaying graph...")
visualize(results)

print("Exporting results to CSV...")
export(results)