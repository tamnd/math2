---
tag: C2FFQAPJ9F
kind: statement
role: theorem
name: Borel–Ritt theorem
msc: ["30E15", 41A60, 34M30]
uses: [0DG0Z72CQD, 072W67KFYK, B53THC8F79]
about: [BJQTEPEZ9G]
sources:
  - url: https://en.wikipedia.org/wiki/Borel%27s_lemma
---

## Statement

Let $0 < r \le \infty$ and $\alpha < \beta$ be real numbers, and let
$$S = \set{z \in \C : 0 < \abs{z} < r, \ \alpha < \arg z < \beta}$$
be an open sector with vertex $0$, of any finite opening $\beta - \alpha$.
Let $\sum_{n \ge 0} a_n z^n$ be a [[formal power series|072W67KFYK]] with complex coefficients.
Then there is a [[holomorphic function|0DG0Z72CQD]] $f$ on $S$ with the following property.
On every closed subsector $\set{z : 0 < \abs{z} \le \rho, \ \alpha' \le \arg z \le \beta'}$ with $\rho < r$ and $\alpha < \alpha' < \beta' < \beta$,
$$f(z) \sim \sum_{n \ge 0} a_n z^n \quad \text{as } z \to 0,$$
in the sense of [[asymptotic expansions|B53THC8F79]] in powers of $z$.

## Remarks

Idea of the proof: after a rotation, one picks $\gamma > 0$ so small that $\operatorname{Re}(z^{-\gamma}) > 0$ on $S$ for a branch of $z^{-\gamma}$.
Then one sets $f(z) = \sum_{n} a_n z^n \left(1 - e^{-b_n z^{-\gamma}}\right)$ with positive numbers $b_n$ that tend to $0$ fast.
Each factor $1 - e^{-b_n z^{-\gamma}}$ is bounded on $S$ and at most $b_n \abs{z}^{-\gamma}$ in absolute value, which makes the series converge and keeps the tail small near $0$.
The function $f$ is never unique: adding $e^{-z^{-\gamma}}$ for a suitable $\gamma$ does not change the expansion.
The real analogue, with smooth functions on an interval, is [[Borel's lemma|KZHNA19FSS]].
If the opening of $S$ is larger than $2\pi$, $S$ is understood on the Riemann surface of the logarithm, and the theorem still holds.

## Explanations

### L1 human

Any formal power series, even one that diverges everywhere, is the asymptotic expansion of some holomorphic function on a sector.
So asymptotic expansions on sectors carry no growth condition on their coefficients.
This is the complex counterpart of the fact that every sequence of numbers is the sequence of derivatives at $0$ of a smooth function.

### L2 human

The theorem shows that the map from functions with an asymptotic expansion on a sector to formal power series is onto.
Its kernel consists of functions that are flat at $0$ in the sector, such as $e^{-1/z}$ on $\abs{\arg z} < \pi/2$.
To recover uniqueness one needs stronger conditions, such as Gevrey estimates on a sector of opening larger than $\pi/k$.
This is the starting point of $k$-summability and of [[Borel summation|8DJPSYSHGJ]] for divergent solutions of differential equations.
