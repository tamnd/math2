---
tag: ERXD4K3GHG
kind: object
name: Ternary Golay code
msc: [94B25, 94B15]
instance_of: [E85KREWV60, 94K1WWWGF6]
uses: [E04GGZ1Q91, M2X88AXM17, JA3DP8NM0A, SM1TJSAR75]
sources:
  - url: https://en.wikipedia.org/wiki/Ternary_Golay_code
same_as:
  wikidata: Q7702927
  wikipedia: Ternary Golay code
---

## Description

The ternary Golay code $G_{11}$ is a [[linear code|E85KREWV60]] of length $11$ and dimension $6$ over the field $\F_3$, with [[minimum distance|M2X88AXM17]] $5$.
One construction: it is the [[cyclic code|E04GGZ1Q91]] of length $11$ over $\F_3$ with generator polynomial
$$g(x) = x^5 + x^4 - x^3 + x^2 - 1,$$
a divisor of $x^{11} - 1$ in $\F_3[x]$.
It has $3^6 = 729$ codewords and corrects $2$ errors.

It is a [[perfect code|94K1WWWGF6]].
A ball of radius $2$ in $\F_3^{11}$ contains $1 + 11 \cdot 2 + \binom{11}{2} \cdot 2^2 = 1 + 22 + 220 = 243 = 3^5$ words.
The balls around the codewords are disjoint, since $5 \ge 2 \cdot 2 + 1$, and together they contain $3^6 \cdot 3^5 = 3^{11}$ words, which is all of $\F_3^{11}$.

## Remarks

The nonzero codewords of $G_{11}$ have weights $5, 6, 8, 9, 11$, with $132, 132, 330, 110, 24$ codewords of each weight.
Adding a check symbol that makes the sum of the coordinates zero gives the extended ternary Golay code $G_{12}$, a $[12, 6, 6]$ code.
$G_{12}$ is self-dual: it equals its [[dual code|JA3DP8NM0A]].
Its nonzero weights are $6, 9, 12$, with $264, 440, 24$ codewords.
The automorphism group of $G_{12}$ is a double cover of the Mathieu group $M_{12}$, just as the [[binary Golay code|SM1TJSAR75]] is linked with $M_{24}$.

## Explanations

### L1 human

The ternary Golay code uses words of $11$ symbols, each symbol being $0$, $1$ or $2$.
Of all $3^{11}$ such words, $729$ are chosen as codewords, and any two of them differ in at least $5$ places.
So up to two damaged symbols can be repaired.
Like the Hamming codes and the binary Golay code, it is perfect: the zones of radius $2$ around the codewords fill the whole space exactly.
