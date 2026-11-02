---
tag: J41Y7CCE6B
kind: statement
role: proposition
name: Matrix rings over simple rings are simple
msc: [16S50, 16D25]
uses: [62M0NC3E2T, 0FHVPRAE60, 0CD87SFM2N]
about: [62M0NC3E2T, 0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_ring
---

## Statement

Let $R$ be a ring with $1$ and let $n \ge 1$ be an integer.
Every [[two-sided ideal|0CD87SFM2N]] of the [[matrix ring|0FHVPRAE60]] $M_n(R)$ has the form $M_n(I)$ for a unique two-sided ideal $I$ of $R$.
In particular, if $R$ is a [[simple ring|62M0NC3E2T]], then $M_n(R)$ is a simple ring.

## Remarks

Let $J$ be a two-sided ideal of $M_n(R)$ and let $I$ be the set of all entries of all matrices in $J$.
With the matrix units $E_{kl}$, one has $E_{1i} A E_{j1} = a_{ij} E_{11}$, and multiplying by scalar matrices and matrix units moves an entry to any position.
From this, $I$ is a two-sided ideal of $R$ and $J = M_n(I)$.
For example, the ideals of $M_2(\Z)$ are the sets $M_2(m\Z)$ for $m \ge 0$.
If $R$ is simple, the only choices are $I = 0$ and $I = R$, so $M_n(R)$ has only the ideals $0$ and $M_n(R)$.

## Explanations

### L1 human

Square matrices whose entries come from a simple ring again form a simple ring.
So from one simple ring one gets an infinite family of simple rings, one for each size.
In particular the matrix rings over a field or a division ring are simple.

### L2 human

The bijection $I \mapsto M_n(I)$ between ideals is one instance of Morita equivalence: $R$ and $M_n(R)$ have equivalent module categories and the same lattice of two-sided ideals.
Combined with Wedderburn's theorem it shows that the simple Artinian rings are exactly the rings $M_n(D)$ with $D$ a division ring.
Note that $M_n(R)$ has many one-sided ideals even when $R$ is a field, such as the matrices whose only nonzero column is the first one.
