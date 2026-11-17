---
tag: GEHMF7T5FX
kind: example
name: The Gödel number of 0 = S0
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
instance_of: [MFJXPAF0R0]
uses: [MFJXPAF0R0, VK6WWSDMXK]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel_numbering
    locator: lead section
---

## Example

We use the prime-power [[Gödel numbering|MFJXPAF0R0]] with the symbol codes $c(0) = 13$, $c(=) = 7$ and $c(S) = 15$.
A string $s_1 \cdots s_n$ gets the code $2^{c(s_1)} 3^{c(s_2)} \cdots p_n^{c(s_n)}$, where $p_n$ is the $n$-th prime.
We compute and decode the code of the formula $0 = S0$.

1. The formula is the string of the four symbols $0, =, S, 0$, so its symbol codes are $13, 7, 15, 13$.
2. Its code is $\#(0 = S0) = 2^{13} \cdot 3^{7} \cdot 5^{15} \cdot 7^{13} = 52974066440027250000000000000$, a number with $29$ digits.
3. The map is computable: step 2 uses only the table of symbol codes, the list of primes and multiplication.
4. Decoding: we divide the number by $2$ until the result is odd, $13$ times, then by $3$, $7$ times, then by $5$, $15$ times, then by $7$, $13$ times. The result is $1$.
5. The exponents $13, 7, 15, 13$ give back the symbols $0, =, S, 0$, so decoding is computable and returns the formula.
6. Injectivity: by unique factorization, a number has only one list of prime exponents, so no other string has this code.
7. The number $10 = 2 \cdot 5$ is not a code, because the exponent of $3$ is $0$ while a later exponent is not. So the set of codes is a proper subset of $\N$, and step 4 decides membership.

## Remarks

The subterm $S0$ has the code $2^{15} \cdot 3^{13} = 52242776064$.
The code of a formula is larger than the codes of its parts, which makes the syntactic relations primitive recursive.
The closed term $\ulcorner 0 = S0 \urcorner$ is the [[numeral|VK6WWSDMXK]] of the number in step 2: the symbol $S$ written that many times in front of $0$.
So the term is very long, and in practice one works with the code and not with the term.
The formula $0 = S0$ is false in $\N$, and the [[consistency statement|4NBAX3VRQ7]] says that it has no proof.

## Explanations

### L1 human

The formula "0 = S0" says "zero equals one".
It has four symbols, and each symbol has a number: $13, 7, 15, 13$.
We pack the four numbers into one number as powers of the first four primes $2, 3, 5, 7$.
The result is a number with $29$ digits.
To unpack it, we count how many times each prime divides it.

### L2 human

1. Write the symbol codes in order: $13, 7, 15, 13$.
2. Multiply $2^{13} = 8192$ by $3^{7} = 2187$ to get $17915904$.
3. Multiply by $5^{15}$ and by $7^{13}$ to get the full code.
4. Decode by repeated division, and check that the last quotient is $1$.

The typical use is to compute $\ulcorner 0 = S0 \urcorner$ in the definition of $\mathrm{Con}(T)$.
A trap: the order of the symbols matters, and $S0 = 0$ has a different code, $2^{15} \cdot 3^{13} \cdot 5^{7} \cdot 7^{13}$.
