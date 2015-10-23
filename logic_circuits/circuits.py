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

def multiplexer_2to1(I_1, I_0, S, E=1, E_active_state='H'):
    if E_active_state == 'L':
        E = NOT(E)
    return OR(AND3(I_1, S,      E),
              AND3(I_0, NOT(S), E))

def multiplexer_4to1(I_3, I_2, I_1, I_0, S_1, S_0, E=1, E_active_state='H'):
    if E_active_state == 'L':
        E = NOT(E)
    return OR4(AND4(I_3, S_1,      S_0,      E),
               AND4(I_2, S_1,      NOT(S_0), E),
               AND4(I_1, NOT(S_1), S_0,      E),
               AND4(I_0, NOT(S_1), NOT(S_0), E))

def demultiplexer_1to2(I, S, E=1, E_active_state='H'):
    """
    @rtype: int, int
    @return: MSB, LSB
    """
    if E_active_state == 'L':
        E = NOT(E)
    return (AND3(I, S,      E),
            AND3(I, NOT(S), E))

def demultiplexer_1to4(I, S_1, S_0, E=1, E_active_state='H'):
    """
    @rtype: int, int, int, int
    @return: MSB, ..., LSB
    """
    if E_active_state == 'L':
        E = NOT(E)
    return (AND4(I, S_1,      S_0,      E),
            AND4(I, S_1,      NOT(S_0), E),
            AND4(I, NOT(S_1), S_0,      E),
            AND4(I, NOT(S_1), NOT(S_0), E))

# TODO: Add enable
def encoder_4to2(I_3, I_2, I_1, I_0):
    """
    @rtype: int, int
    @return: MSB, LSB
    """
    return (AND(NOT(I_1), NOT(I_0)),
            OR(I_3, I_1))

def decoder_2to4(I_1, I_0, E=1, E_active_state='H'):
    """
    @rtype: int, int, int, int
    @return: MSB, ..., LSB
    """
    if E_active_state == 'L':
        E = NOT(E)
    return (AND3(I_1,      I_0,      E),
            AND3(I_1,      NOT(I_0), E),
            AND3(NOT(I_1), I_0,      E),
            AND3(NOT(I_1), NOT(I_0), E))

