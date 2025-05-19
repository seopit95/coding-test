import random

A = random.randrange(2, 10000)
B = random.randrange(2, 10000)
C = random.randrange(2, 10000)

print(f"(A + B) % C: {(A + B) % C}")
print(f"((A % C) + (B % C)) % C: {((A % C) + (B % C)) % C}")
print(f"(A x B) % C: {(A * B) % C}")
print(f"((A % C) x (B % C)) % C: {((A % C) * (B % C)) % C}")