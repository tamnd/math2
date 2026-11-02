---
tag: 6MTVY6NYY7
kind: statement
role: theorem
name: Spectral decomposition theorem
msc: [37D20]
uses: [S31RTTJPDC, EY2W34JZA4, FR49Y9GQHR, B763QH5521]
about: [Z26Z4XZFVA]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_A
---

## Statement

Let $M$ be a compact smooth manifold and let $f \colon M \to M$ be a $C^1$ diffeomorphism that satisfies [[Axiom A|S31RTTJPDC]], with [[non-wandering set|EY2W34JZA4]] $\Omega(f)$.
Then:

1. There are pairwise disjoint closed sets $\Lambda_1, \ldots, \Lambda_k$ with $\Omega(f) = \Lambda_1 \cup \cdots \cup \Lambda_k$ such that $f(\Lambda_i) = \Lambda_i$ and $f|_{\Lambda_i}$ is [[topologically transitive|FR49Y9GQHR]] for each $i$.
2. Each $\Lambda_i$ is a union of pairwise disjoint closed sets $X_{i,1}, \ldots, X_{i,n_i}$ such that $f(X_{i,j}) = X_{i,j+1}$ for $j < n_i$, $f(X_{i,n_i}) = X_{i,1}$, and $f^{n_i}|_{X_{i,j}}$ is [[topologically mixing|B763QH5521]] for each $j$.

## Remarks

The sets $\Lambda_i$ are called basic sets; the decomposition into them is unique.
The idea of the proof is to group periodic points whose stable and unstable manifolds meet transversally in both directions.
The local product structure of the hyperbolic set makes the closures of these groups open and closed in $\Omega(f)$.
Compactness then makes them finite in number.
Part 1 is due to Smale, and part 2 to Bowen.
Example: for the north-south map of the circle, the basic sets are the two hyperbolic fixed points, with $n_i = 1$.
For an [[Anosov diffeomorphism|RCQH8P6DPQ]] of the torus, $\Omega(f)$ is the whole torus and there is one basic set.
Without hyperbolicity the conclusion fails: for the identity of the circle every point is non-wandering, and $\Omega(f)$ is connected but $f$ is not transitive on it.

## Explanations

### L1 human

The long-term dynamics of an Axiom A system breaks into finitely many separate blocks.
On each block the motion is irreducible: some orbit comes close to every point of it.
Each block in turn is made of a few pieces that the map visits in a cycle, and on each piece a power of the map mixes completely.
So the global behaviour is a finite combination of well-understood chaotic pieces.

### L2 human

The theorem is the starting point of the theory of Axiom A systems.
Orbits outside $\Omega(f)$ go from one basic set to another.
When there are no cycles among the basic sets, this gives a partial order on them, as in Conley's theory of [[chain recurrence|6MX5R482KJ]].
Each basic set admits a [[Markov partition|4VNHVDHTNN]], so the dynamics on it is a factor of a [[subshift of finite type|624XDXX8FN]].
This leads to equilibrium states, [[Sinai–Ruelle–Bowen measures|256NP6JBEQ]] and the counting of periodic orbits.
