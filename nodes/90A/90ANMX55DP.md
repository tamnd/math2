---
tag: 90ANMX55DP
kind: definition
name: Series acceleration
msc: [65B10, 65B05, 40A25]
defines: B1S2XJPGYD
uses: [0XKWSSY8P2, 0NB643K60Q, 0JH4MN4K1C]
sources:
  - url: https://en.wikipedia.org/wiki/Series_acceleration
---

## Definition

A *sequence transformation* $T$ assigns to a sequence $(s_n)$ of real or complex numbers a new sequence $(t_n) = T(s_n)$.
Each $t_n$ depends on finitely many terms of $(s_n)$.
Let $(s_n)$ [[converge|0XKWSSY8P2]] to $s$, with $s_n \ne s$ for all large $n$.
The transformation $T$ *accelerates the convergence* of $(s_n)$ if $(t_n)$ converges to $s$ and
$$\lim_{n \to \infty} \frac{t_n - s}{s_n - s} = 0.$$
*Series acceleration* means applying such a transformation to the sequence of [[partial sums|0NB643K60Q]] of a convergent [[series|0JH4MN4K1C]].

## Remarks

Example: for $s_n = 2^{-n}$ with limit $0$, the transformation $t_n = s_n s_{n+1} = 2^{-2n-1}$ gives $t_n / s_n = 2^{-n-1} \to 0$, so it accelerates this sequence.
Non-example: the shift $t_n = s_{n+1}$ gives $t_n / s_n = \frac12$ for the same sequence.
The error is halved, but the ratio does not tend to $0$, so this is not acceleration in the sense above.
A given transformation accelerates some sequences and not others.

## Explanations

### L1 human

The new sequence must have the same limit and its error must become negligible compared with the old error.
Gaining a fixed factor is not enough.
