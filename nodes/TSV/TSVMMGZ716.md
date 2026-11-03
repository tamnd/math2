---
tag: TSVMMGZ716
kind: statement
role: proposition
name: Bounded approximate identity of L1(G)
msc: [43A20, 22D15]
uses: [AHV05ZBCYW, 6GD25S53ND, 2Z29JN3VES, CDYXTW3PJF, VVE1P3SM6E]
about: [6GD25S53ND, CDYXTW3PJF]
sources:
  - url: https://en.wikipedia.org/wiki/Approximate_identity
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with left Haar measure $\mu$, and let $L^1(G)$ be its [[group algebra|6GD25S53ND]].
Let $\mathcal{U}$ be the set of compact neighbourhoods $U$ of the identity with $U = U^{-1}$, directed by reverse inclusion.
For each $U \in \mathcal{U}$ let $e_U \colon G \to [0, \infty)$ be a continuous function such that $e_U(x) = 0$ for $x \notin U$, $e_U(x^{-1}) = e_U(x)$ for all $x$, and $\int_G e_U \, d\mu = 1$.
Then for every $f \in L^1(G)$,
$$\lim_U \norm{e_U * f - f}_1 = 0 \quad \text{and} \quad \lim_U \norm{f * e_U - f}_1 = 0,$$
where $*$ is [[convolution|2Z29JN3VES]].
Since $\norm{e_U}_1 = 1$ for all $U$, the net $(e_U)$ is a two-sided [[approximate identity|CDYXTW3PJF]] of $L^1(G)$ bounded by $1$.

## Remarks

Functions $e_U$ exist: Urysohn's lemma gives a nonzero continuous $g \ge 0$ vanishing outside $U$, and $e_U$ is a multiple of $g(x) + g(x^{-1})$.
The idea of the proof: $e_U * f = \int_G e_U(y) \, L_y f \, d\mu(y)$ is an average of left translates $L_y f$ with $y \in U$.
Hence $\norm{e_U * f - f}_1 \le \sup_{y \in U} \norm{L_y f - f}_1$, which tends to $0$ by the continuity of translation in [[$L^1(G)$|VVE1P3SM6E]].
The right-hand case is similar, using right translations and the symmetry of $e_U$.

Example: on $G = \R$, the functions $e_n = \frac{n}{2} \mathbf{1}_{[-1/n, 1/n]}$, or continuous bumps of width $2/n$, give $e_n * f \to f$ in $L^1(\R)$.
This is the familiar smoothing of a function by averaging over shrinking intervals.

The group algebra has a unit exactly when $G$ is discrete, and then the unit is the point mass at the identity.
So for groups like $\R$ the approximate identity is the best substitute for a unit.

## Explanations

### L1 human

The algebra $L^1(\R)$ has no element that acts like the number $1$ under convolution.
But one can come as close as one wants: convolving with a tall narrow bump of total mass $1$ barely changes a function.
The narrower the bump, the smaller the change, and the bumps stay of size $1$ in the $L^1$ norm.
This holds on every locally compact group.

### L2 human

Bounded approximate identities are the standard replacement for a unit in Banach algebra arguments.
With Cohen's factorization theorem, the result gives $L^1(G) = L^1(G) * L^1(G)$.
It is the key step in proving that every bounded left multiplier of $L^1(G)$ is convolution by a measure ([[Wendel's theorem|E1GGS48ZFE]]).
It also shows that closed left ideals of $L^1(G)$ are exactly the closed left-translation-invariant subspaces.
