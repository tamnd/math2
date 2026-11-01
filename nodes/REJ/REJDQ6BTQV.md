---
tag: REJDQ6BTQV
kind: statement
role: theorem
name: Fundamental identity for ramification and inertia
msc: [11R04, 11S15]
uses: [MWBDFS2KJ5, B7KNZCBFYT, H5RC67SD24, 7NPY2CN5KB, 0QMZAQ6QQ4, 0EAJ2XXADC, 7X92G8CQ33]
about: [B7KNZCBFYT, H5RC67SD24]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_of_prime_ideals_in_Galois_extensions
---

## Statement

Let $L/K$ be a finite extension of [[algebraic number fields|MWBDFS2KJ5]] of [[degree|0EAJ2XXADC]] $n$, with rings of integers $\mathcal{O}_K \subseteq \mathcal{O}_L$.
Let $\mathfrak{p}$ be a nonzero prime ideal of $\mathcal{O}_K$, with [[factorisation|B7KNZCBFYT]] $\mathfrak{p}\mathcal{O}_L = \mathfrak{P}_1^{e_1} \cdots \mathfrak{P}_g^{e_g}$ into distinct prime ideals.
Let $f_i = [\mathcal{O}_L/\mathfrak{P}_i : \mathcal{O}_K/\mathfrak{p}]$ be the residue degrees.
Then
$$\sum_{i=1}^{g} e_i f_i = n.$$
If moreover $L/K$ is a [[Galois extension|0QMZAQ6QQ4]], then $e_1 = \cdots = e_g = e$ and $f_1 = \cdots = f_g = f$, and $efg = n$.

## Remarks

Proof idea: count elements of $\mathcal{O}_L/\mathfrak{p}\mathcal{O}_L$.
It is a vector space over $\mathcal{O}_K/\mathfrak{p}$ of dimension $n$, by localising at $\mathfrak{p}$, where $\mathcal{O}_L$ becomes free of rank $n$.
By the Chinese remainder theorem it is the product of the rings $\mathcal{O}_L/\mathfrak{P}_i^{e_i}$, and each has dimension $e_i f_i$, using the filtration by powers of $\mathfrak{P}_i$.
In the Galois case, the Galois group acts transitively on the $\mathfrak{P}_i$, and conjugate primes have the same $e$ and $f$.

Example: in $\Q(\sqrt{-5})/\Q$, with $n = 2$: the prime $2$ has $e = 2, f = 1, g = 1$; the prime $3$ has $e = 1, f = 1, g = 2$; the prime $11$ is inert since $-5$ is not a square modulo $11$, with $e = 1, f = 2, g = 1$.
In each case $efg = 2$.

## Explanations

### L1 human

When a prime ideal of a small field breaks into primes of a larger field, the pieces must add up to the degree of the extension.
Each piece counts with its exponent times the size of its residue field extension.
So a prime in a quadratic field either splits into two, stays prime with a bigger residue field, or becomes a square.

### L2 human

The identity limits the possible splitting types and is used constantly in computations.
In a Galois extension, $e f$ is the order of the [[decomposition group|7X92G8CQ33]] of any prime over $\mathfrak{p}$, and $e$ is the order of its inertia group.
For a cyclic extension of prime degree $\ell$, the identity leaves only three cases: split completely ($g = \ell$), inert ($f = \ell$) or totally ramified ($e = \ell$).
