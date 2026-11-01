---
tag: HP56DJECMT
kind: statement
role: theorem
name: Hilbert–Serre theorem
msc: [13D40, 13A02]
uses: [8KB4SQGC0C, 07GNX8GCYP, 05QY1VEBYD, 04C5ZBG1WT, RMH4FBCFDA]
about: [RMH4FBCFDA]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_series_and_Hilbert_polynomial
---

## Statement

Let $k$ be a [[field|04C5ZBG1WT]] and let $S = k[x_1, \dots, x_r]$ be the [[polynomial ring|07GNX8GCYP]] with each $x_i$ of degree $1$.
Let $M = \bigoplus_{n \in \Z} M_n$ be a [[finitely generated|05QY1VEBYD]] [[graded|8KB4SQGC0C]] $S$-module, and let $H_M(n) = \dim_k M_n$.

1. The Hilbert series $\sum_{n \in \Z} H_M(n)\, t^n$ equals $Q(t)/(1 - t)^r$ for some Laurent polynomial $Q \in \Z[t, t^{-1}]$.
2. There is a unique polynomial $P_M \in \Q[t]$ such that $H_M(n) = P_M(n)$ for all sufficiently large $n$, and $P_M$ is zero or has degree at most $r - 1$.

## Remarks

The proof goes by induction on $r$.
Multiplication by $x_r$ gives an exact sequence of graded modules $0 \to K(-1) \to M(-1) \to M \to C \to 0$, where $K$ and $C$ are killed by $x_r$ and so are finitely generated graded modules over $k[x_1, \dots, x_{r-1}]$.
Taking dimensions degree by degree gives $(1 - t)$ times the Hilbert series of $M$ in terms of those of $C$ and $K$, and the induction hypothesis finishes the proof.
Part 2 follows from part 1 by expanding $1/(1-t)^r = \sum_{n \ge 0} \binom{n + r - 1}{r - 1} t^n$.
Example: for $M = S$ one has $Q = 1$ and $H_S(n) = \binom{n + r - 1}{r - 1}$ for $n \ge 0$.
When the Krull dimension of $M$ is at least $1$, the degree of $P_M$ is one less than this dimension.

## Explanations

### L1 human

A graded module splits into pieces of degree $0, 1, 2, \dots$, and each piece is a finite-dimensional vector space.
The theorem says that the dimensions of these pieces are eventually given by a polynomial in the degree.
So an infinite list of numbers is controlled by finitely many coefficients.

### L2 human

The polynomial $P_M$ is the [[Hilbert polynomial|RMH4FBCFDA]] of $M$.
In projective geometry, applied to the coordinate ring of a projective variety, it gives the dimension and the degree of the variety.
The local analogue is the existence of the Hilbert–Samuel polynomial, which is proved by applying this theorem to the associated graded ring; it underlies the [[dimension theorem for local rings|KW3HY77V6D]].
