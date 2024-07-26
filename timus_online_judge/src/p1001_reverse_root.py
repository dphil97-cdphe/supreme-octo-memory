import sys
#from io import StringIO

#real_stdin = sys.stdin
#sys.stdin = StringIO(input)

tokens = reversed(sys.stdin.read().split())
out = [float(x) ** 0.5 for x in tokens]

sys.stdout.write('\n'.join(map(str, out)))