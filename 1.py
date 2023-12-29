import time

def f(file_path):
  s = 0
  with open(file_path, 'r') as file:
    for line in file:
      line = line.strip()
      l = next((char for char in line if char.isdigit()), None)
      r = next((char for char in reversed(line) if char.isdigit()), None)
      if l and r:
        s += int(l+r)
    return s
  
DIGITS = {
  'one': '1', 'two': '2', 'three': '3', 
  'four': '4', 'five': '5', 'six': '6', 
  'seven': '7', 'eight': '8', 'nine': '9'
}

def g(file_path):
  s = 0
  with open(file_path, 'r') as file:
    for line in file:
      line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
      line = line.strip()
      l = next((char for char in line if char.isdigit()), None)
      r = next((char for char in reversed(line) if char.isdigit()), None)
      if l and r:
        s += int(l+r)
    return s

if __name__ == "__main__":
  t1 = time.perf_counter()
  print(f('./1_1.in'))
  t2 = time.perf_counter()
  print(f"Exec time: {t2-t1}")
  
  t1 = time.perf_counter()
  print(g('./1_1.in'))
  t2 = time.perf_counter()
  print(f"Exec time: {t2-t1}")
