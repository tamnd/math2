---
tag: RAKXDDYNAM
kind: statement
role: theorem
name: Singleton bound
msc: [94B65]
uses: [TAE6K8NQ46, M2X88AXM17, E85KREWV60]
about: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Singleton_bound
same_as:
  wikidata: Q2116294
  wikipedia: Singleton bound
---

## Statement

Let $A$ be an alphabet with $q \ge 2$ symbols, and let $C \subseteq A^n$ be an [[error-correcting code|TAE6K8NQ46]] of length $n$ with $M$ codewords and [[minimum distance|M2X88AXM17]] $d$.
Then
$$M \le q^{n - d + 1}.$$
In particular, a [[linear code|E85KREWV60]] with parameters $[n, k, d]$ satisfies $k \le n - d + 1$.

## Remarks

Delete the last $d - 1$ coordinates of every codeword.
Two distinct codewords differ in at least $d$ positions, so they still differ after the deletion.
So the codewords give $M$ distinct words of length $n - d + 1$, and there are only $q^{n - d + 1}$ such words.
Example: the binary $[n, n - 1, 2]$ even-weight code has $k = n - 1 = n - d + 1$, so it meets the bound.
Example: the $[7, 4, 3]$ Hamming code has $k = 4 < 5 = n - d + 1$, so the bound is not reached; for binary codes the bound is reached only by trivial codes.
Codes that reach the bound are the maximum distance separable codes, such as the Reed–Solomon codes.

## Explanations

### L1 human

A code cannot have both many codewords and a large distance between them.
The Singleton bound makes this precise in the simplest way: each extra unit of distance costs at least one symbol of information.
It needs no counting of balls, only the remark that cutting off a few positions cannot merge two codewords.

### L2 human

For a linear code it says $d \le n - k + 1$, so the rate $k/n$ and the relative distance $d/n$ add up to at most $1 + 1/n$.
The bound is reached by [[MDS codes|3H9XZA1SR5]], such as Reed–Solomon codes, but only over alphabets that are large compared with the length.
For a fixed alphabet and long codes, the Hamming, Plotkin and Elias–Bassalygo bounds are much stronger.
