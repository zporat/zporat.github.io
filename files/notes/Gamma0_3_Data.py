# Formats lists of matrices so that they are easier to read
from sage.repl.display.formatter import SagePlainTextFormatter
formatter = SagePlainTextFormatter()

def Gamma0_3_gens(N):
    if N.is_prime() == True:
        # Block 1: Initialize Parameters
        # N is the level of automorphic form
        S = [1, 2, 3, -1, -2 , -3] #generators of Free Group F(3)
        Index = N**2 + N + 1 #index of Gamma0 in SL3

        F = FreeGroup('x,y,z')
        M1 = Matrix([[1, 0, 1],[0, -1, -1],[0, 1, 0]])
        M2 = Matrix([[0, 1, 0],[0, 0, 1],[1, 0, 0]])
        M3 = Matrix([[0, 1, 0],[1, 0, 0],[-1, -1, -1]])

        # Builds a list of length one words and initializes A to include x (in Tietze notation)
        L_1 = Tuples(S,1).list()
        A = [[1]]

        # Block 2: Compares length 1 words to elements of A to see if they represent a new coset
        for a in range(0, len(L_1)):
            for b in range(0, len(A)):
                Test_Matrix = F(A[b])(M1,M2,M3) * (F(L_1[a])(M1,M2,M3))**(-1)
                if mod(Test_Matrix[1][0], N) == 0 and mod(Test_Matrix[2][0], N) == 0:
                    break
                else:
                    continue
            else: 
                A.append(L_1[a])

        # Block 3: Checks whether |A| = Index and builds length i+1 words from list of length i words in A
        for i in range(1, Index + 1):
            if len(A) == Index:
                break
            else:
                def length_test(element):
                    if len(element) == i:
                        return True
                    else: 
                        return False    

                L_i = list(filter(length_test, A))
                L_i_plus1 = []

                for j in range(0, len(L_i)):
                    for k in range(0, len(S)):
                        A_k = L_i[j] + [S[k]]
                        L_i_plus1.append(A_k)

        # Block 4: Tests potential length i+1 words against previous elements of A to see if they represent a new coset
                for m in range(0, len(L_i_plus1)):
                    for n in range(0, len(A)):
                        Test_Matrix_2 = F(A[n])(M1,M2,M3) * (F(L_i_plus1[m])(M1,M2,M3))**(-1)
                        if mod(Test_Matrix_2[1][0], N) == 0 and mod(Test_Matrix_2[2][0], N) == 0:
                            break
                        else:
                            continue
                    else: 
                        A.append(L_i_plus1[m])

        # Block 5: For each word g_l in A, concatenate by each generator in S on the right.  
        T = []
        for c in range(0, len(A)):
            for d in range(0, len(S)):
                    gls = A[c] + [S[d]]
                    T.append(gls)

        # Compute gls^-1 and checks what coset it is in, then builds the generator as gls(bar_gls)^-1
        V = []
        for e in range(0, len(T)):
            for f in range(0, len(A)):
                Test_Matrix_3 = F(A[f])(M1,M2,M3) * (F(T[e])(M1,M2,M3))**(-1)
                if mod(Test_Matrix_3[1][0], N) == 0 and mod(Test_Matrix_3[2][0], N) == 0:
                    rev = A[f][::-1]
                    inv = [ -h for h in rev]
                    gen = T[e] + inv
                    V.append(gen)
                    break
                else:
                    continue

        # Block 6: Converts potential generators in Tietze notation to elements of the free group and then along the isomorphism; removes identity
        Gen_Matrices = []
        for w in V:
            if F(w)(M1,M2,M3) == matrix.identity(3):
                continue
            else:
                Gen_Matrices.append(F(w)(M1,M2,M3))

        # Pulls out unique matrix generators
        Unique_Gens = [Gen_Matrices[0]]
        for mat in Gen_Matrices:
            if mat in Unique_Gens:
                continue
            else:
                Unique_Gens.append(mat)

        print(formatter(Unique_Gens))
    
    else:
        print(N, "is not prime.")

def Gamma0_3_coset_reps(N):
    if N.is_prime() == True:
        # Block 1: Initialize Parameters
        # N is the level of automorphic form
        S = [1, 2, 3, -1, -2 , -3] #generators of Free Group F(3)
        Index = N**2 + N + 1 #index of Gamma0 in SL3

        F = FreeGroup('x,y,z')
        M1 = Matrix([[1, 0, 1],[0, -1, -1],[0, 1, 0]])
        M2 = Matrix([[0, 1, 0],[0, 0, 1],[1, 0, 0]])
        M3 = Matrix([[0, 1, 0],[1, 0, 0],[-1, -1, -1]])

        # Builds a list of length one words and initializes A to include x (in Tietze notation)
        L_1 = Tuples(S,1).list()
        A = [[1]]

        # Block 2: Compares length 1 words to elements of A to see if they represent a new coset
        for a in range(0, len(L_1)):
            for b in range(0, len(A)):
                Test_Matrix = F(A[b])(M1,M2,M3) * (F(L_1[a])(M1,M2,M3))**(-1)
                if mod(Test_Matrix[1][0], N) == 0 and mod(Test_Matrix[2][0], N) == 0:
                    break
                else:
                    continue
            else: 
                A.append(L_1[a])

        # Block 3: Checks whether |A| = Index and builds length i+1 words from list of length i words in A
        for i in range(1, Index + 1):
            if len(A) == Index:
                break
            else:
                def length_test(element):
                    if len(element) == i:
                        return True
                    else: 
                        return False    

                L_i = list(filter(length_test, A))
                L_i_plus1 = []

                for j in range(0, len(L_i)):
                    for k in range(0, len(S)):
                        A_k = L_i[j] + [S[k]]
                        L_i_plus1.append(A_k)

        # Block 4: Tests potential length i+1 words against previous elements of A to see if they represent a new coset
                for m in range(0, len(L_i_plus1)):
                    for n in range(0, len(A)):
                        Test_Matrix_2 = F(A[n])(M1,M2,M3) * (F(L_i_plus1[m])(M1,M2,M3))**(-1)
                        if mod(Test_Matrix_2[1][0], N) == 0 and mod(Test_Matrix_2[2][0], N) == 0:
                            break
                        else:
                            continue
                    else: 
                        A.append(L_i_plus1[m])

        coset_reps = []
        for rep in A:
            coset_reps.append(F(rep)(M1,M2,M3))

        print(formatter(coset_reps))

    else:
        print(N, "is not prime.")