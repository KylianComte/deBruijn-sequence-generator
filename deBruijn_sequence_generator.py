def de_bruijn(k, n):
    """
    Generate the de Bruijn sequence for alphabet k and length n.
    :param k: Alphabet (list of characters)
    :param n: Length of subsequences
    :return: De Bruijn sequence as a string
    """
    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence.append(a[j])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return sequence

# Example usage:
k = 2  # Binary alphabet {0, 1}
n = 4  # Length of subsequences

subsequences = de_bruijn(k, n)

# Print the de Bruijn sequence
print(f"De Bruijn sequence for alphabet {k} and length {n} :")
print("".join(map(str, subsequences)))