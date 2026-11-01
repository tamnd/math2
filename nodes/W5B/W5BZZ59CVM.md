---
tag: W5BZZ59CVM
kind: statement
role: theorem
name: Balog–Szemerédi–Gowers theorem
msc: [11P70, 11B30]
uses: [MAQKH72P6V, XNBN31HQWB, 082GHNPJ53]
about: [MAQKH72P6V, XNBN31HQWB]
sources:
  - url: https://en.wikipedia.org/wiki/Additive_combinatorics
---

## Statement

There are absolute constants $c > 0$ and $C > 0$ with the following property.
Let $G$ be an [[abelian group|082GHNPJ53]], let $K \ge 1$, and let $A, B \subseteq G$ be finite sets with $\abs{A} = \abs{B} = n$.
Suppose that the [[additive energy|MAQKH72P6V]] satisfies $E(A, B) \ge n^3 / K$.
Then there are subsets $A' \subseteq A$ and $B' \subseteq B$ such that
$$\abs{A'} \ge c K^{-C} n, \qquad \abs{B'} \ge c K^{-C} n, \qquad \abs{A' + B'} \le C K^{C} n.$$

## Remarks

The converse direction is easy: if $\abs{A + B} \le Kn$, then Cauchy–Schwarz gives $E(A, B) \ge n^4 / (Kn) = n^3/K$.
Large energy alone does not give a small sumset for the whole sets.
For example, let $A$ be the union of an arithmetic progression of length $n/2$ and $n/2$ random-looking integers.
Then $E(A, A)$ is at least of order $n^3$, but $\abs{A + A}$ is of order $n^2$; the theorem finds the progression part.
The proof is graph-theoretic.
One forms the bipartite graph on $A \cup B$ with an edge $ab$ when $a + b$ is a popular sum.
A dependent-random-choice argument then finds $A'$ and $B'$ joined by many paths of length three, which bounds $\abs{A' + B'}$.
Balog and Szemerédi proved the theorem first, and Gowers obtained polynomial dependence on $K$.

## Explanations

### L1 human

Additive energy counts how often sums of elements of two sets coincide.
If there are many coincidences, one would like to say that the sets are structured.
The theorem says that large pieces of the two sets are indeed structured, with few distinct sums.

### L2 human

The theorem lets one pass from a statistical statement, large energy, to a combinatorial one, a small sumset for large subsets.
After that, [[Freiman's theorem|KEPFYE6WYZ]] gives structure.
Gowers used this chain in his quantitative proof of [[Szemerédi's theorem|B23B0QEMN5]].
