---
tag: G5MKMRTT62
kind: definition
name: Sequence space
msc: [46A45, 40H05]
defines: XYTN19EPF2
uses: [0QE8STGJH2, 05EGHEQZAW, 0EPTJA5QV4, 08P6T2WH6R]
sources:
  - url: https://en.wikipedia.org/wiki/Sequence_space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$.
Let $\omega$ be the set of all [[sequences|0QE8STGJH2]] $x = (x_n)_{n \ge 1}$ with terms in $\mathbb{K}$.
With termwise addition $(x + y)_n = x_n + y_n$ and scalar multiplication $(\lambda x)_n = \lambda x_n$, the set $\omega$ is a [[vector space|05EGHEQZAW]] over $\mathbb{K}$.
A *sequence space* is a [[linear subspace|0EPTJA5QV4]] of $\omega$.

## Remarks

Example: the set $\ell^\infty$ of bounded sequences is a sequence space.
It contains the zero sequence, and if $\abs{x_n} \le M$ and $\abs{y_n} \le N$ for all $n$, then $\abs{x_n + y_n} \le M + N$ and $\abs{\lambda x_n} \le \abs{\lambda} M$.
Other examples are $\omega$ itself, the [[spaces ℓ^p|08P6T2WH6R]], the space $c$ of convergent sequences and the space $c_0$ of null sequences.
Another is the space $\varphi$ of sequences with only finitely many nonzero terms.

Non-example: the set of sequences with $x_1 = 1$ is not a sequence space, because it does not contain the zero sequence.

The word is often used for a sequence space together with a norm or a topology, as in the theory of FK-spaces and BK-spaces.
