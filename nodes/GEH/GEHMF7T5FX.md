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

The formula $0 = S0$ says "zero equals one", and we turn it into a single number and back.
We use the prime-power [[Gödel numbering|MFJXPAF0R0]] with the symbol codes $c(0) = 13$, $c(=) = 7$ and $c(S) = 15$.
A string $s_1 \cdots s_n$ gets the code $2^{c(s_1)} 3^{c(s_2)} \cdots p_n^{c(s_n)}$, where $p_n$ is the $n$-th prime.

1. The formula is the string of the four symbols $0, =, S, 0$, so its symbol codes are $13, 7, 15, 13$.
2. We put the codes on the first four primes and multiply:
   $$\#(0 = S0) = 2^{13} \cdot 3^{7} \cdot 5^{15} \cdot 7^{13} = 52974066440027250000000000000.$$
   The result has $29$ digits.
3. The map is computable, because step 2 uses only the table of symbol codes, the list of primes and multiplication.
4. To decode, we divide by $2$ until the result is odd, which takes $13$ divisions.
   Then we divide by $3$ seven times, by $5$ fifteen times and by $7$ thirteen times, and the result is $1$.
5. The exponents $13, 7, 15, 13$ give back the symbols $0, =, S, 0$, so decoding is computable and returns the formula.
6. The map is injective, because a number has only one list of prime exponents, so no other string has this code.
7. Not every number is a code.
   The number $10 = 2 \cdot 5$ has exponent $0$ at the prime $3$ and a nonzero exponent after it, so it codes no string.
   The divisions of step 4 decide membership in the set of codes.

Check: $2^{13} \cdot 5^{13} = 10^{13}$, which explains the $13$ final zeros, and $3^{7} \cdot 5^{2} \cdot 7^{13} = 5297406644002725$ gives the other $16$ digits.

## Remarks

The parts of the formula have smaller codes.
The term $S0$, read as a string of its own, has the code $2^{15} \cdot 3^{13} = 52242776064$.
This is the general pattern of prime-power codes, and it is why checks such as "is this a formula" are searches below the code, hence primitive recursive.

The order of the symbols matters.
The formula $S0 = 0$ has the same four symbols in another order, and its code is $2^{15} \cdot 3^{13} \cdot 5^{7} \cdot 7^{13}$, a different number.

Inside a formula of arithmetic we cannot write the number of step 2 directly.
We write its [[numeral|VK6WWSDMXK]] $\ulcorner 0 = S0 \urcorner$, which is the symbol $S$ written that many times in front of $0$.
That term is far too long to write out, so in practice one works with the code and not with the term.
The formula $0 = S0$ is false in $\mathbb{N}$, and the [[consistency statement|4NBAX3VRQ7]] says that it has no proof, using exactly this code.

## Explanations

### L1 human

The formula "0 = S0" says "zero equals one".
It has four symbols, and each symbol has a number: $13, 7, 15, 13$.
We pack the four numbers into one number as powers of the first four primes $2, 3, 5, 7$.
The result is a number with $29$ digits.
To unpack it, we count how many times each prime divides it.

### L2 human

We build the code in stages, to see the size grow.
First, $2^{13} = 8192$ and $3^{7} = 2187$, so the first two symbols give
$$2^{13} \cdot 3^{7} = 17915904.$$
This number is the code of the string $0 =$, which is not a formula.
Multiplying by $5^{15}$ adds the symbol $S$, and multiplying by $7^{13}$ adds the final $0$.
Each new symbol multiplies the code by a power of a new prime, so the code of a formula grows very fast with its length.
Arithmetic does not mind, since it reasons about the code through formulas and never writes the number out.
