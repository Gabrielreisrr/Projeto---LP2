from time import sleep
import sys
def barProgress():
    tam_bar_progress = 20
    total_time = tam_bar_progress/10
    for qtdSquare in range(1, tam_bar_progress + 1):
      print("[" + qtdSquare * "\033[31m\u25FE\033[0m" + (tam_bar_progress - qtdSquare) * "  " + "]" + f"{qtdSquare*(100/tam_bar_progress):.2f}% ({total_time:.1f}s)")
      sleep(0.08)
      total_time -= 0.08
      sys.stdout.write("\033[F")
      sys.stdout.write("\033[K")