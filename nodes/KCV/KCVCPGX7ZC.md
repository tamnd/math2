---
tag: KCVCPGX7ZC
kind: statement
role: theorem
name: Bergman's gap theorem
msc: [16P90]
uses: [MDVSY2NMD2, EHY4PYSMGZ, 3CTW1P4HBP, 04C5ZBG1WT, 0SDC934R52, MVGBS3J1P7]
about: [MDVSY2NMD2]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand–Kirillov_dimension
---

## Statement

Let $k$ be a [[field|04C5ZBG1WT]] and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $k$.
Then the [[Gelfand–Kirillov dimension|MDVSY2NMD2]] of $A$ is not in the open interval $(1, 2)$.
Together with the elementary fact that it is not in $(0, 1)$, this gives
$$\operatorname{GKdim} A \in \set{0} \cup \set{1} \cup [2, \infty].$$

## Remarks

The gap between $0$ and $1$ is easy: if a finitely generated algebra is infinite-dimensional, then $V^n \subsetneq V^{n+1}$ for all $n$, so $\dim V^n \ge n + 1$.
The gap between $1$ and $2$ is harder.
One reduces to algebras given by monomial relations, whose growth is governed by counting words in the generators.
Then a combinatorial argument on words applies.
If the number of nonzero words of some length $n$ is at most $n$, then the number of nonzero words of each length stays bounded.
So the growth is at most linear.
Since the dimension of a general algebra is the supremum over its finitely generated subalgebras, the gaps pass to all algebras.

Example: $k[x]$ has Gelfand–Kirillov dimension $1$, and the [[polynomial ring|0SDC934R52]] $k[x, y]$ has dimension $2$.
So both ends of the gap $(1, 2)$ are attained.
No further gap exists: every real number $r \ge 2$ is the Gelfand–Kirillov dimension of some finitely generated algebra.
This contrasts with the [[Krull dimension|MVGBS3J1P7]] of commutative rings, which takes only integer values or $\infty$.

## Explanations

### L1 human

The Gelfand–Kirillov dimension measures how fast an algebra grows, and one might expect any value to be possible.
Bergman's theorem says that values strictly between $1$ and $2$ never occur.
If the growth of an algebra is measured by an exponent $d$, so that it grows roughly like $n^d$, then $d$ is $0$, $1$, or at least $2$.

### L2 human

The theorem is a statement about the [[growth|EHY4PYSMGZ]] of algebras, and its heart is combinatorics on words.
It shows that Gelfand–Kirillov dimension behaves like an integer-valued dimension at the bottom of the scale, while above $2$ every real value can occur.
It is a basic input in the study of algebras of small Gelfand–Kirillov dimension, such as algebras of dimension $1$ and $2$, which are often compared with curves and surfaces.
