---
tag: GZMAH9W2SK
kind: statement
role: theorem
name: Lusin's theorem
msc: [28A20, 26A15]
uses: [2Z2QVWZ262, YYNCJSR0PJ, 0R6EWFKRCF, 0X3WGX95FE]
about: [YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Lusin%27s_theorem
same_as:
  wikidata: Q1361393
  wikipedia: Lusin's theorem
---

## Statement

Let $n \ge 1$, let $\lambda$ be [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$, and let $A \subseteq \R^n$ be a Lebesgue measurable set with $\lambda(A) < \infty$.
Let $f \colon A \to \R$ be a [[measurable function|YYNCJSR0PJ]].
Then for every $\varepsilon > 0$ there is a [[compact set|0R6EWFKRCF]] $K \subseteq A$ with $\lambda(A \setminus K) < \varepsilon$ such that the restriction $f|_K$ is [[continuous|0X3WGX95FE]].

## Remarks

One proof approximates $f$ by simple functions and uses that each measurable set is nearly closed.
For $f = \mathbf{1}_B$, choose closed $F_1 \subseteq B$ and $F_2 \subseteq A \setminus B$ with small leftover measure; $f$ is constant on each of the disjoint closed sets $F_1$ and $F_2$, so it is continuous on $F_1 \cup F_2$.
For general $f$, take a sequence of simple functions that converges to $f$ pointwise, and use Egorov's theorem to make the convergence uniform on a large compact set.
Example: $f = \mathbf{1}_{\Q}$ on $A = [0, 1]$ is discontinuous at every point, but its restriction to a compact set $K$ of irrational numbers with $\lambda(K) > 1 - \varepsilon$ is the constant $0$.
The conclusion is about $f|_K$, not about $f$: the points of $K$ need not be points of continuity of $f$.
By the Tietze extension theorem, there is also a continuous $g \colon \R^n \to \R$ with $g = f$ on $K$.
The same result holds for every Radon measure on a locally compact Hausdorff space, for functions on sets of finite measure.

## Explanations

### L1 human

A measurable function can be very irregular, such as a function that jumps between $0$ and $1$ on the rational and irrational numbers.
Lusin's theorem says that after removing a set of small measure, what is left of the function is continuous.
So every measurable function is continuous up to an arbitrarily small set.

### L2 human

This is the second of Littlewood's three principles.
It explains why continuous functions with compact support are dense in $L^p$ spaces for $1 \le p < \infty$, together with the density of simple functions.
It is a basic tool for passing from statements about continuous functions to statements about measurable ones.
In the other direction, a function with this property for every $\varepsilon$ is measurable, so the property characterises measurability on sets of finite measure.
