---
tag: MHNNV51NDS
kind: conjecture
name: Kakeya maximal function conjecture
msc: [42B25, 28A75]
uses: [6PEN7AKC7M, SASP14MA1Z, 2Z2QVWZ262, VX1A56P5KQ, T62369RFH6, SSNFTHZ6YJ]
about: [6PEN7AKC7M]
sources:
  - url: https://en.wikipedia.org/wiki/Kakeya_set
history:
  posed_by: "Jean Bourgain"
  first_stated: "1991"
  notes: "Bourgain stated the conjecture explicitly in this form in 1991. Antonio Córdoba had introduced the Kakeya maximal function and proved the planar case in 1977."
---

## Statement

Let $n \ge 2$ and let $S^{n-1}$ be the unit [[sphere|T62369RFH6]] in $\R^n$, with its surface measure.
For $0 < \delta < 1$, a unit vector $e \in S^{n-1}$ and a point $a \in \R^n$, let $T_e^\delta(a)$ be the closed $\delta$-neighbourhood of the segment $\set{a + te : 0 \le t \le 1}$.
For a locally integrable function $f$ on $\R^n$, the *Kakeya maximal function* is
$$f^*_\delta(e) = \sup_{a \in \R^n} \frac{1}{\abs{T_e^\delta(a)}} \int_{T_e^\delta(a)} \abs{f(x)} \, dx, \qquad e \in S^{n-1},$$
where $\abs{T}$ is the [[Lebesgue measure|2Z2QVWZ262]] of $T$.
Then for every $\varepsilon > 0$ there is a constant $C_{n,\varepsilon}$ such that
$$\norm{f^*_\delta}_{L^n(S^{n-1})} \le C_{n,\varepsilon} \, \delta^{-\varepsilon} \norm{f}_{L^n(\R^n)}$$
for every $0 < \delta < 1$ and every $f \in$ [[$L^n(\R^n)$|SASP14MA1Z]].

## Remarks

The function $f^*_\delta(e)$ is the largest average of $\abs{f}$ over a thin tube of length $1$, width $\delta$ and direction $e$.
It is a directional relative of the [[Hardy–Littlewood maximal function|VX1A56P5KQ]].
Some loss in $\delta$ is needed, because of [[Kakeya sets|6PEN7AKC7M]] of measure zero.

The conjecture implies the Kakeya set conjecture, that every Kakeya set in $\R^n$ has [[Hausdorff dimension|SSNFTHZ6YJ]] $n$.
The idea is to cover a Kakeya set by small balls and to apply the bound to the indicator function of a thickened union of these balls.
This function has average about $1$ on a tube in every direction, so the bound forces the union to have large measure, which rules out a small dimension.

Status: the case $n = 2$ is a theorem of Córdoba, with a logarithmic loss in place of $\delta^{-\varepsilon}$.
For $n \ge 3$ the conjecture is open in general, and only partial results are known, such as bounds on $L^p$ for smaller $p$.
In 2025 Hong Wang and Joshua Zahl proved the Kakeya set conjecture in $\R^3$.
The [[restriction conjecture|9CE11G48JY]] is known to imply the Kakeya set conjecture.

## Explanations

### L1 human

Take a function on space and, for each direction, look at its average over thin tubes pointing in that direction.
Keep the largest average for each direction; this is the Kakeya maximal function.
The conjecture says this maximal function is controlled by the size of the original function, up to a very small loss as the tubes get thinner.
It is a quantitative form of the statement that thin tubes pointing in all directions cannot overlap too much.
That statement, in turn, says that Kakeya sets are large in the sense of dimension.
