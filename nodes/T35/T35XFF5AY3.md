---
tag: T35XFF5AY3
kind: statement
role: theorem
name: Dimension of a polynomial ring
msc: [13C15, 13F20]
uses: [MVGBS3J1P7, 0SDC934R52, 0670T59HGE, 00MHHZ9SNE, 0310REJJY8]
about: [MVGBS3J1P7, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_dimension
---

## Statement

Let $R$ be a [[commutative ring|0310REJJY8]] of finite [[Krull dimension|MVGBS3J1P7]] $\dim R$, and let $R[X]$ be the [[polynomial ring|0SDC934R52]] in one variable over $R$.

1. In general, $\dim R + 1 \le \dim R[X] \le 2 \dim R + 1$.
2. If $R$ is a [[Noetherian ring|0670T59HGE]], then $\dim R[X] = \dim R + 1$.

## Remarks

For the lower bound, a chain of [[prime ideals|00MHHZ9SNE]] $\mathfrak p_0 \subsetneq \cdots \subsetneq \mathfrak p_n$ of $R$ gives the chain $\mathfrak p_0[X] \subsetneq \cdots \subsetneq \mathfrak p_n[X] \subsetneq \mathfrak p_n[X] + (X)$ in $R[X]$.
For the upper bound, fix a prime $\mathfrak p$ of $R$ and let $\kappa(\mathfrak p)$ be the fraction field of $R/\mathfrak p$.
The primes of $R[X]$ that contract to $\mathfrak p$ correspond to primes of $\kappa(\mathfrak p)[X]$, so at most two of them lie in one chain.
In the Noetherian case one shows that a prime $\mathfrak P$ of $R[X]$ over $\mathfrak p$ has height at most $\operatorname{ht} \mathfrak p + 1$.
By induction, for a field $k$ the ring $k[X_1, \dots, X_n]$ has dimension $n$, and for a Noetherian ring $R$ of finite dimension, $\dim R[X_1, \dots, X_n] = \dim R + n$.
For example, $\dim \Z[X] = 2$, with the maximal chain $0 \subsetneq (2) \subsetneq (2, X)$.
Without the Noetherian hypothesis the equality in clause 2 can fail: there are non-Noetherian rings with $\dim R[X] > \dim R + 1$.

## Explanations

### L1 human

The Krull dimension counts how long a chain of prime ideals can be.
Adding one polynomial variable adds exactly one to this count when the ring is Noetherian.
This matches geometry: a line has dimension $1$, the plane $2$, and $n$-space $n$.

### L2 human

This result is the algebraic reason why affine $n$-space over a field has dimension $n$.
Together with [[Noether normalization|7Z28JY8QW4]] it shows that a finitely generated domain over a field has dimension equal to the transcendence degree of its fraction field.
The general bounds come from looking at the fibres of $\operatorname{Spec} R[X] \to \operatorname{Spec} R$, which are spectra of polynomial rings in one variable over fields.
