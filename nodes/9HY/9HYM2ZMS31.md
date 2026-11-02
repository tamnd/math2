---
tag: 9HYM2ZMS31
kind: statement
role: theorem
name: Rader's FFT algorithm
msc: [65T50, 11Y16]
uses: [TST0GH66A5, 0F33KX9Q6F, 2Z29JN3VES, 9N8D9E5TB2]
about: [TST0GH66A5]
sources:
  - url: https://en.wikipedia.org/wiki/Rader's_FFT_algorithm
same_as:
  wikidata: Q7280126
  wikipedia: Rader's FFT algorithm
---

## Statement

Let $p$ be a prime, let $\omega = e^{-2\pi i/p}$, and let $g$ be a [[primitive root modulo $p$|0F33KX9Q6F]].
For an integer $j$ write $g^{j}$ and $g^{-j}$ for the residues in $\set{1, \ldots, p-1}$ of these powers modulo $p$.
Let $x \in \C^p$ and let $X$ be its [[discrete Fourier transform|TST0GH66A5]], $X_k = \sum_{n=0}^{p-1} x_n \omega^{nk}$.
Define sequences of period $p - 1$ by $a_m = x_{g^m}$ and $c_m = \omega^{g^{-m}}$.
Then $X_0 = \sum_{n=0}^{p-1} x_n$, and for $0 \le q \le p-2$,
$$X_{g^{-q}} = x_0 + \sum_{m=0}^{p-2} a_m\, c_{q-m}.$$
So a DFT of prime length $p$ reduces to a cyclic [[convolution|2Z29JN3VES]] of length $p - 1$ and $O(p)$ further additions.

## Remarks

Since $g$ generates the multiplicative group modulo $p$, the maps $m \mapsto g^m$ and $q \mapsto g^{-q}$ are bijections from $\set{0, \ldots, p-2}$ onto $\set{1, \ldots, p-1}$.
For $n = g^m$ and $k = g^{-q}$ one has $nk \equiv g^{-(q-m)} \pmod p$, and $\omega^{nk}$ depends only on $nk$ modulo $p$; this gives the formula.
The cyclic convolution of length $p-1$ can be computed by DFTs of length $p - 1$, which is composite for $p > 3$.
These can use the [[Cooley–Tukey algorithm|9N8D9E5TB2]], possibly after zero padding to a power of $2$.
Example: $p = 5$ and $g = 2$, so $(g^0, g^1, g^2, g^3) = (1, 2, 4, 3)$ and $(g^0, g^{-1}, g^{-2}, g^{-3}) = (1, 3, 4, 2)$.
The hypothesis that $p$ is prime gives a primitive root, and makes the nonzero indices a group under multiplication.
For composite lengths the nonzero indices do not form such a group.

## Explanations

### L1 human

Fast Fourier transforms usually split the length into factors, which fails when the length is prime.
Rader noticed that for a prime length the nonzero indices can be listed as powers of one number $g$.
In that order, the transform becomes a convolution, and convolutions can be done fast with other FFTs.

### L2 human

The algorithm uses the structure of $(\Z/p\Z)^\times$, which is cyclic of order $p - 1$.
Permuting inputs by $n = g^m$ and outputs by $k = g^{-q}$ turns the $(p-1) \times (p-1)$ block of the DFT matrix into a circulant matrix.
Circulant matrices are diagonalised by the DFT, which is why the convolution can be done in $O(p \log p)$ operations.
Winograd's short-length FFT modules are built on the same reduction.
Bluestein's algorithm is an alternative that works for every length and does not need a primitive root.
