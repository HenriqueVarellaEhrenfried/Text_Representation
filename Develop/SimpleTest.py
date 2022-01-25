import numpy as np
from numpy import linalg as LA

vector = [1,2,3,4]
# vector = [[50,63,27,12,13,82]]

# vetor_np = np.array([vector])
# vetor_np_transposed = np.transpose(vetor_np)

# print("\n","Vector >>", np.shape(vetor_np), "\n")
# print("\n","Vector T>>", np.shape(vetor_np_transposed), "\n")

# gram = np.matmul(vetor_np, vetor_np_transposed)

# gram2 = np.matmul(vetor_np_transposed,vetor_np)


# print("Shaper 1 > ", np.shape(gram),"\n" ,gram)
# print("Shaper 2 > ", np.shape(gram2),"\n" , gram2)


# det = LA.det(gram2)

# print(det)

# print(LA.eig(gram))

print(sum(vector))