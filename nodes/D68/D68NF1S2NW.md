---
tag: D68NF1S2NW
kind: example
name: Hamming code
msc: [94B05, 94B25]
instance_of: [E85KREWV60, 94K1WWWGF6]
uses: [Y4JB44WWFG, M2X88AXM17, ZH3QHHP8H7]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_code
same_as:
  wikidata: Q853922
  wikipedia: Hamming code
---

## Example

Let $r \ge 2$ and $n = 2^r - 1$.
Let $H$ be the $r \times n$ matrix over $\F_2$ whose columns are the $n$ nonzero vectors of $\F_2^r$, in some order.
The binary *Hamming code* of length $n$ is the [[linear code|E85KREWV60]] with [[parity-check matrix|Y4JB44WWFG]] $H$, that is, $C = \set{x \in \F_2^n : Hx^T = 0}$.
The columns of $H$ include the $r$ unit vectors, so $H$ has rank $r$ and $C$ has dimension $n - r$.
No column is zero and no two columns are equal, so no one or two columns are linearly dependent.
Three columns such as $e_1, e_2, e_1 + e_2$ are dependent.
Hence the [[minimum distance|M2X88AXM17]] is $3$, and $C$ is a $[2^r - 1, 2^r - 1 - r, 3]$ code.
For $r = 3$ this is the $[7, 4, 3]$ Hamming code.

The code is [[perfect|94K1WWWGF6]] with radius $1$.
A ball of radius $1$ in $\F_2^n$ has $1 + n = 2^r$ words.
The balls around the $2^{n-r}$ codewords are disjoint, since $3 \ge 2 \cdot 1 + 1$.
Together they hold $2^{n-r} \cdot 2^r = 2^n$ words, which is all of $\F_2^n$.

## Remarks

[[Syndrome decoding|ZH3QHHP8H7]] is very simple here.
If one bit $i$ of a codeword is flipped, the syndrome is the $i$-th column of $H$, which names the position of the error.
If the columns of $H$ are the binary expansions of $1, 2, \dots, n$ in order, the syndrome is the binary expansion of $i$.
Over any finite field $\F_q$ there are $q$-ary Hamming codes, of length $(q^r - 1)/(q - 1)$, built from one nonzero vector on each line through the origin of $\F_q^r$.
The dual of the binary Hamming code is the simplex code, a punctured Hadamard code.

## Explanations

### L1 human

The $[7, 4, 3]$ Hamming code sends $4$ bits of data with $3$ check bits, $7$ bits in all.
Each check bit covers a different group of positions, and the pattern of failed checks spells out, in binary, the position of a flipped bit.
So one error can be found and fixed, at the price of less than twice the data, while the repetition code needs three times the data for the same task.
The code wastes nothing: every possible $7$-bit word is either a codeword or one flip away from exactly one codeword.
