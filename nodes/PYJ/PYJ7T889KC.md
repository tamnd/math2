---
tag: PYJ7T889KC
kind: statement
role: theorem
name: Boundary Harnack principle
msc: [31B25, 31B05, 35J25]
uses: [1GNKQ7NBAG, 0DEB0JMN0W, YNH832D50W]
about: [0DEB0JMN0W, 1GNKQ7NBAG]
sources:
  - url: https://en.wikipedia.org/wiki/Harnack%27s_inequality
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded [[Lipschitz domain|1GNKQ7NBAG]].
Then there are constants $r_0 > 0$ and $C \ge 1$, depending only on $\Omega$, with the following property.
Let $\zeta \in \partial\Omega$ and $0 < r < r_0$, and let $u, v$ be positive [[harmonic functions|0DEB0JMN0W]] on $\Omega \cap B(\zeta, 2r)$ that extend continuously by $0$ to $\partial\Omega \cap B(\zeta, 2r)$.
Then
$$\frac{u(x)}{v(x)} \le C\, \frac{u(y)}{v(y)} \qquad \text{for all } x, y \in \Omega \cap B(\zeta, r).$$

## Remarks

The constant $C$ does not depend on $\zeta$, $r$, $u$ or $v$; it depends only on $n$ and on the Lipschitz character of $\Omega$.
Inside $\Omega$, the ordinary [[Harnack inequality|YNH832D50W]] compares the values of one positive harmonic function at nearby points.
The boundary version compares two functions up to the boundary, where both tend to $0$: their ratio stays bounded above and below.
Idea of the proof: a Carleson-type estimate bounds $u$ near the boundary by its value at an interior point at distance about $r$ from $\zeta$.
Comparison with harmonic measure, using that the Lipschitz graph satisfies an exterior cone condition at every scale, then gives matching lower bounds.
Example, a local check in the upper half-plane near $\zeta = 0$: take $u(x, y) = y$ and $v(x, y) = y / ((x - 3)^2 + y^2)$, a constant multiple of the Poisson kernel with pole $3$.
On $B(0, 1)$ the ratio $v / u = 1 / ((x - 3)^2 + y^2)$ lies between $1/16$ and $1/4$, so the conclusion holds with $C = 4$.
The vanishing hypothesis is needed: with $u = y$ and $v = 1$, the ratio $u / v = y$ tends to $0$ at the boundary, and no constant works.

## Explanations

### L1 human

Two positive harmonic functions that both vanish on a piece of the boundary vanish there at the same rate.
So near that piece, one is roughly a constant multiple of the other.
This holds even when the boundary has corners, as long as it is a Lipschitz graph.

### L2 human

The principle is the key estimate in the boundary theory of harmonic functions on rough domains.
It implies that ratios of positive harmonic functions vanishing on a boundary portion are Hölder continuous up to the boundary.
From this one finds the Martin boundary of a Lipschitz domain: it equals the Euclidean boundary, and every boundary point is minimal.
It also underlies the comparison of harmonic measure with the Green function and the doubling property of harmonic measure on Lipschitz domains.
