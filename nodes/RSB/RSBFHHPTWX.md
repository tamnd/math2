---
tag: RSBFHHPTWX
kind: statement
role: theorem
name: Gromov's theorem on groups of polynomial growth
msc: [20F69, 20F18, 20F65]
uses: [082DWWXMRJ, 4CMRM3975W, 0Q7MMQHC1P, 0X1JXT47GA, 0DTXBQPA2S]
about: [4CMRM3975W, 0Q7MMQHC1P]
sources:
  - url: https://en.wikipedia.org/wiki/Gromov's_theorem_on_groups_of_polynomial_growth
same_as:
  wikidata: Q3527091
  wikipedia: Gromov's theorem on groups of polynomial growth
---

## Statement

Let $G$ be a [[finitely generated group|082DWWXMRJ]].
Then $G$ has polynomial [[growth|4CMRM3975W]] if and only if $G$ is virtually nilpotent, that is, $G$ has a [[nilpotent|0Q7MMQHC1P]] [[subgroup|0X1JXT47GA]] of finite [[index|0DTXBQPA2S]].

## Remarks

The direction "virtually nilpotent implies polynomial growth" was known before Gromov.
For a finitely generated nilpotent group the degree of growth is the integer $\sum_{k \ge 1} k \, r_k$.
Here $r_k$ is the torsion-free rank of the quotient $\gamma_k(G) / \gamma_{k+1}(G)$ of consecutive terms of the lower central series.
Gromov proved the hard direction.
His idea is to rescale the word metric of $G$ by $1/n$ and pass to a limit space as $n \to \infty$.
Polynomial growth makes this limit a finite-dimensional, locally compact space.
The solution of Hilbert's fifth problem turns its isometry group into a Lie group, on which $G$ acts.
From this action one extracts the nilpotent subgroup by induction on the degree.
Kleiner later gave a different proof based on harmonic functions on the Cayley graph.

Example: the integer Heisenberg group of upper unitriangular $3 \times 3$ integer matrices is nilpotent, with $r_1 = 2$ and $r_2 = 1$, so its growth is polynomial of degree $2 + 2 = 4$.

A consequence is a gap: the growth of a finitely generated group is either polynomial of an integer degree, or faster than every polynomial.
Groups of intermediate growth exist, such as the [[Grigorchuk group|M0WAT1VQZH]], so "faster than every polynomial" does not mean exponential.

## Explanations

### L1 human

Count the elements of a group that can be reached in at most $n$ steps from the identity.
If this count grows only like a power of $n$, the theorem says the group is very close to being commutative: up to a finite index, it is nilpotent.
So a purely geometric counting condition forces a strong algebraic structure.

### L2 human

The theorem shows that being virtually nilpotent is a [[quasi-isometry|6FKYSH729T]] invariant of finitely generated groups, because growth is.
For finitely generated linear groups the gap is sharper: by the [[Tits alternative|QYXGVES1XM]] and the Milnor–Wolf theorem for solvable groups, their growth is either polynomial or exponential.
It is also used in the study of random walks and of manifolds with almost nonnegative curvature.
