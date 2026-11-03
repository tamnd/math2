---
tag: RZEGDKR7C7
kind: statement
role: theorem
name: Hamming bound
msc: [94B65]
uses: [TAE6K8NQ46, EP5HNGSXFA, M2X88AXM17, 6E7ZZ4DYX3, 0GBZM0MT0F, 95CYGNRQQ6]
about: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_bound
same_as:
  wikidata: Q1970635
  wikipedia: Hamming bound
---

## Statement

Let $A$ be an alphabet with $q \ge 2$ symbols, and let $C \subseteq A^n$ be an [[error-correcting code|TAE6K8NQ46]] of length $n$ with $M$ codewords and [[minimum distance|M2X88AXM17]] $d$.
Let $t = \floor{(d - 1)/2}$.
Then
$$M \sum_{i=0}^{t} \binom{n}{i} (q - 1)^i \le q^n.$$

## Remarks

The sum is the number of words in a ball of radius $t$ in the [[Hamming space|6E7ZZ4DYX3]] $A^n$.
There are $\binom{n}{i}$ ways to choose $i$ positions and $(q - 1)^i$ ways to change the symbols there.
The balls of radius $t$ around the codewords are disjoint, since a word in two of them would force two codewords at [[Hamming distance|EP5HNGSXFA]] at most $2t < d$.
So $M$ disjoint balls fit inside a space of $q^n$ words, which is the bound; for this reason it is also called the sphere-packing bound.
Example: the binary $[7, 4, 3]$ Hamming code has $t = 1$ and $M = 16$, and $16 \cdot (1 + 7) = 128 = 2^7$, so the bound holds with equality.
For $n = 7$, $q = 2$, $d = 5$, so $t = 2$, the bound gives $M \le 128/29$, so $M \le 4$.
Codes that reach equality are called perfect.
For long codes with $d \approx \delta n$, the bound shows that the rate $R = \log_q M / n$ is at most about $1 - H_q(\delta/2)$, where $H_q$ is the [[q-ary entropy function|95CYGNRQQ6]].

## Explanations

### L1 human

Around each codeword, draw the ball of all words with at most $t$ errors.
For the code to correct $t$ errors, these balls must not overlap.
So the number of codewords times the size of one ball cannot exceed the number of all words.
This caps how many messages a code can carry for a given length and error tolerance.

### L2 human

The Hamming bound is an upper bound on $A_q(n, d)$, the largest size of a $q$-ary code of length $n$ and minimum distance $d$.
It is tight only in rare cases, the perfect codes, which are classified for prime power alphabets.
For large relative distance, the Plotkin, Elias–Bassalygo and linear programming bounds are stronger.
In the other direction, the Gilbert–Varshamov bound shows that codes of size at least $q^n$ divided by the volume of a ball of radius $d - 1$ always exist.
