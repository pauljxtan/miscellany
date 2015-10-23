from gates import AND, AND3, AND4, NOT, OR, OR4, XOR

def half_adder(A, B):
    S = XOR(A, B)
    C = AND(A, B)
    return C, S

def full_adder(A, B, C_in):
    S = XOR(XOR(A, B), C_in)
    C_out = OR(AND(XOR(A, B), C_in), AND(A, B))
    return C_out, S

def ripple_carry_adder(A, B, C_0=0):
    """
    @type  A  : int array
    @param A  : binary number (1 bit per element)
    @type  B  : int array
    @param B  : binary number (1 bit per element)
    @type  C_0: int
    @param C_0: carry in

    @rtype: int, int array
    @return: carry out, sum
    """
    if len(A) != len(B):
        raise ValueError("Operands have different bit lengths")
    n_bits = len(A)

    C = [None] * (n_bits + 1)
    C[0] = C_0
    S = [None] * n_bits

    # Reverse A and B since indexing from right to left by convention
    # e.g. A = [A_3, A_2, A_1, A_0]
    A = list(reversed(A))
    B = list(reversed(B))

    # Get the sum of each bit and propagate the carry
    for i in range(n_bits):
        C[i + 1], S[i] = full_adder(A[i], XOR(B[i], C_0), C[i])

    return C[n_bits], list(reversed(S))

def ripple_carry_subtractor(A, B):
    return ripple_carry_adder(A, B, 1)

def multiplexer_2to1(S, A, B, E=1, E_active_state='H'):
    if E_active_state == 'L':
        E = NOT(E)
    return OR(AND3(A, NOT(S), E),
              AND3(B, S,      E))

def multiplexer_4to1(S_0, S_1, A, B, C, D, E=1, E_active_state='H'):
    if E_active_state == 'L':
        E = NOT(E)
    return OR4(AND4(A, NOT(S_0), NOT(S_1), E),
               AND4(B, S_0,      NOT(S_1), E),
               AND4(C, NOT(S_0), S_1,      E),
               AND4(D, S_0,      S_1,      E))
