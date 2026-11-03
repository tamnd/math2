---
tag: FH0VE9PQXJ
kind: statement
role: theorem
name: Serre's splitting theorem
msc: [19A13, 13C10]
uses: [0310REJJY8, 0670T59HGE, MVGBS3J1P7, HQA9YHDSH5, 1WTNGZ5T5A]
about: [HQA9YHDSH5]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_module
---

## Statement

Let $R$ be a commutative [[Noetherian ring|0670T59HGE]] of finite [[Krull dimension|MVGBS3J1P7]] $d$.
Let $P$ be a [[finitely generated projective|HQA9YHDSH5]] $R$-module whose [[rank|1WTNGZ5T5A]] is greater than $d$ at every prime ideal of $R$.
Then $P \cong P' \oplus R$ for some finitely generated projective $R$-module $P'$.

## Remarks

The proof finds a unimodular element of $P$, that is, an element $p$ such that $f(p) = 1$ for some linear form $f \colon P \to R$; then $P = Rp \oplus \ker f$.
Such an element is built by a general position argument.
Since the rank exceeds the dimension, one can choose $p$ so that its image in $P_\mathfrak{p}/\mathfrak{p} P_\mathfrak{p}$ is nonzero at every prime $\mathfrak{p}$.
Repeating the theorem shows that every finitely generated projective module of constant rank $n > d$ is $P_0 \oplus R^{n-d}$ with $P_0$ of rank $d$.

Example: for a Dedekind domain ($d \le 1$), every finitely generated projective module of rank $n \ge 1$ is $R^{n-1} \oplus I$ with $I$ of rank $1$.
This is part of the description of [[$K_0$ of a Dedekind domain|1V3XBPS48D]].

The rank hypothesis cannot be weakened to rank $d$.
Let $A = \R[x, y, z]/(x^2 + y^2 + z^2 - 1)$, of Krull dimension $2$, and let $P$ be the kernel of $(u, v, w) \mapsto ux + vy + wz$ from $A^3$ to $A$.
Then $P$ has rank $2$, and a free summand $A$ in $P$ would give a nowhere-vanishing tangent vector field on the $2$-sphere, which does not exist.

## Explanations

### L1 human

A projective module is like a vector bundle, and a free summand is like a nowhere-vanishing section.
In topology, a vector bundle whose rank exceeds the dimension of the base always has a nowhere-vanishing section.
Serre's theorem is the algebraic version: when the rank is larger than the Krull dimension, a copy of the ring splits off.

### L2 human

The theorem says that "large" projective modules carry no new information beyond a module of rank at most $d$.
Combined with the [[Bass cancellation theorem|2NEKYG83WZ]], it shows that in rank greater than $d$, a projective module is determined by its class in $K_0(R)$.
Over a ring of dimension $0$ or $1$ it reduces the classification to modules of rank at most $1$.
