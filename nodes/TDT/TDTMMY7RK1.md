---
tag: TDTMMY7RK1
kind: statement
role: theorem
name: Kaplansky density theorem
msc: [46L10, 46L05]
uses: [HM2HHE3J51, BMDG4JQPEH, 6HSJBJ8TTQ, KHJ2G2R5G7, MM0EJ2GDE4]
about: [PSFWQVZ0FS]
sources:
  - url: https://en.wikipedia.org/wiki/Kaplansky_density_theorem
same_as:
  wikidata: Q1209546
  wikipedia: Kaplansky density theorem
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] with [[algebra of bounded operators|BMDG4JQPEH]] $B(H)$.
Let $A$ be a subalgebra of $B(H)$ that is closed under the [[adjoint|6HSJBJ8TTQ]].
Let $B$ be the closure of $A$ in the [[strong operator topology|KHJ2G2R5G7]].
For a set $X \subseteq B(H)$ write $X_1 = \set{T \in X : \|T\| \le 1}$ and $X_{sa}$ for its self-adjoint elements.
Then:

1. $A_1$ is strongly dense in $B_1$;
2. $(A_{sa})_1$ is strongly dense in $(B_{sa})_1$;
3. if $A$ is a C*-algebra that contains $I$, then the [[unitary|MM0EJ2GDE4]] elements of $A$ are strongly dense in the unitary elements of $B$.

## Remarks

One may replace $A$ by its norm closure, which does not change the strong closure of its unit ball, so $A$ may be taken to be a C*-algebra.
The key step uses the function $f(t) = 2t/(1 + t^2)$.
The map $T \mapsto f(T)$ is strongly continuous on self-adjoint operators.
Also, $f$ maps $\R$ into $[-1, 1]$ and restricts to a homeomorphism of $[-1, 1]$ onto itself.
Write an element of $(B_{sa})_1$ as $f(S)$ with $S$ self-adjoint in $B$.
Approximate $S$ strongly by self-adjoint elements $S_i$ of $A$.
Then the elements $f(S_i)$ of $(A_{sa})_1$ tend strongly to $f(S)$.
This gives part 2; part 1 follows by applying part 2 to the self-adjoint $2 \times 2$ operator matrix with entries $0, T, T^*, 0$.

Without the theorem, an element of $B_1$ is a strong limit of a net in $A$, but the norms along the net might be unbounded.
Such nets are hard to use, since multiplication is jointly strongly continuous only on bounded sets.
Kaplansky's theorem says that elements of $B$ of norm at most $1$ are strong limits of elements of $A$ of norm at most $1$.
When $H$ is separable, the strong topology on bounded sets is metrizable, so one can then even use sequences.

## Explanations

### L1 human

When an algebra of operators is completed by taking strong limits, new elements appear.
This theorem says that each new element of size at most one can be reached by elements of the original algebra that also have size at most one.
So no "blow-up" is needed to approximate.

### L2 human

The theorem is used together with the [[bicommutant theorem|BSA6GFT8SQ]].
If $A$ is a unital C*-algebra on $H$, then the unit ball of $A$ is strongly dense in the unit ball of the von Neumann algebra $A''$.
This is how properties such as approximate finite dimensionality pass from a C*-algebra to the von Neumann algebra it generates.
It also shows that the unit ball of $A''$ is the closure of the unit ball of $A$ in the weak operator topology, which is compact.
