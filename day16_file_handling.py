with open("notes.txt", "r") as file:
  content = file.read()
  print(content)

with open("notes.txt", "w") as file:
   content = file.write("python\nOPPs\nJavaScript\nJava\nGenAI")

  
with open("notes.txt", "a") as file:
   file.write("\nSystem Design")