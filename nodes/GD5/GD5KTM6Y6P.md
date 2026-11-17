---
tag: GD5KTM6Y6P
kind: example
name: Which primes are sums of two squares
msc: ["11E25", "11A41"]
topics: [DME0TPC348]
audience: ug1
instance_of: [R2T42N5XGK]
uses: [R2T42N5XGK, 0SN0MAEKYX, 043B3ENSTY]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Conjecture
    locator: lead section
---

## Example

Which [[primes|0SN0MAEKYX]] $p$ can be written as $p = a^2 + b^2$ with integers $a, b$?
We [[form a conjecture|R2T42N5XGK]] from a table.

1. The data. Among the primes up to $113$, these are sums of two squares: $2 = 1^2 + 1^2$, $5 = 1^2 + 2^2$, $13 = 2^2 + 3^2$, $17 = 1^2 + 4^2$, $29 = 2^2 + 5^2$, $37 = 1^2 + 6^2$, $41 = 4^2 + 5^2$, $53 = 2^2 + 7^2$, $61 = 5^2 + 6^2$, $73 = 3^2 + 8^2$, $89 = 5^2 + 8^2$, $97 = 4^2 + 9^2$, $101 = 1^2 + 10^2$, $109 = 3^2 + 10^2$, $113 = 7^2 + 8^2$.
2. The rest. These are not: $3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107$.
3. The search for a pattern. The last digits do not separate the lists: $13$ and $23$ both end in $3$. The residues modulo $4$ do: every odd prime in step 1 is $\equiv 1 \pmod 4$, and every prime in step 2 is $\equiv 3 \pmod 4$.
4. The conjecture. An odd prime $p$ is a sum of two squares if and only if $p \equiv 1 \pmod 4$.
5. A test on new data. $1009 \equiv 1 \pmod 4$, and $1009 = 15^2 + 28^2$. $1019 \equiv 3 \pmod 4$, and a search finds no representation.
6. One direction proved. A square is $\equiv 0$ or $1 \pmod 4$, so a sum of two squares is $\equiv 0$, $1$ or $2 \pmod 4$. So a prime $p \equiv 3 \pmod 4$ is never a sum of two squares.
7. The other direction is [[Fermat's theorem on sums of two squares|043B3ENSTY]], whose proof is harder.

## Remarks

Step 3 tried a feature that failed (the last digit) before a feature that worked (the residue modulo $4$).
Trying several simple features is a standard way to find a pattern.
Step 6 is a short proof of half the conjecture, and it explains why residues modulo $4$ were the right feature.
Fermat stated the full result in 1640, and Euler published the first known proof.

## Explanations

### L1 human

Some primes are sums of two square numbers, like $13 = 4 + 9$, and some are not, like $7$.
Make two lists and look at them.
After dividing by $4$, the primes in the first list leave remainder $1$, and the odd primes in the second list leave remainder $3$.
That is the guess, and half of it has a two-line proof.
The other half is a famous theorem of Fermat.

### L2 human

We check that $1019$ is not a sum of two squares by search.

1. If $1019 = a^2 + b^2$ with $0 \leq a \leq b$, then $a^2 \leq 509$, so $a \leq 22$.
2. For $a = 0, 1, \ldots, 22$, the numbers $1019 - a^2$ are $1019, 1018, 1015, 1010, \ldots, 535$.
3. None of these $23$ numbers is a perfect square.
4. Step 6 of the example gives the same result at once, because $1019 \equiv 3 \pmod 4$.

The typical use: a search confirms single cases, and a congruence argument explains all of them.
A trap: a pattern found modulo $4$ on primes need not hold for all integers; $21 \equiv 1 \pmod 4$ is not a sum of two squares.
