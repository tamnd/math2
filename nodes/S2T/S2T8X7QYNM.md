---
tag: S2T8X7QYNM
kind: definition
name: Hardy spaces of harmonic functions
msc: [31B25, 31A20, 30H10]
defines: 6R2ZXY5VZW
uses: [0DEB0JMN0W, SASP14MA1Z, TCYSWCTYYM, PNNNFJVF6W, PJFH51Z48M]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_space
---

## Definition

Let $n \ge 2$, let $B = \set{x \in \R^n : \abs{x} < 1}$ be the open unit ball, and let $S = \partial B$ be the unit sphere.
Let $\sigma$ be the rotation-invariant Borel probability measure on $S$.
Let $1 \le p < \infty$.
The *harmonic Hardy space* $h^p(B)$ is the set of [[harmonic functions|0DEB0JMN0W]] $u \colon B \to \R$ such that
$$\norm{u}_{h^p} = \sup_{0 < r < 1} \left( \int_S \abs{u(r\zeta)}^p \, d\sigma(\zeta) \right)^{1/p} < \infty.$$
The space $h^\infty(B)$ is the set of bounded harmonic functions on $B$, with $\norm{u}_{h^\infty} = \sup_B \abs{u}$.

## Remarks

Each $h^p$ with $1 \le p \le \infty$ is a Banach space for the norm above.
Write $P(x, \zeta) = (1 - \abs{x}^2) / \abs{x - \zeta}^n$ for the [[Poisson kernel|TCYSWCTYYM]] of $B$.
For $1 < p \le \infty$, $u \in h^p$ if and only if $u(x) = \int_S P(x, \zeta) f(\zeta)\, d\sigma(\zeta)$ for some $f$ in the [[Lp space|SASP14MA1Z]] $L^p(\sigma)$, and then $\norm{u}_{h^p} = \norm{f}_{L^p}$.
For $p = 1$, $u \in h^1$ if and only if $u$ is the Poisson integral of a finite signed Borel measure on $S$.
Example: fix $\eta \in S$ and let $u = P(\cdot, \eta)$.
It is positive and harmonic, and by the mean value property its mean over each sphere $\abs{x} = r$ is $u(0) = 1$, so $u \in h^1$ with norm $1$.
It is not in $h^p$ for $p > 1$, since it is the Poisson integral of the point mass at $\eta$, which has no $L^p$ density.
Non-example: in the plane, let $u = \operatorname{Re}\left( \frac{1 + z}{1 - z} \right)^2$ on the unit disc.
For $e^{i\theta} \ne 1$, $u(r e^{i\theta}) \to -\cot^2(\theta / 2)$ as $r \to 1$, and this function is not integrable on the circle.
By Fatou's lemma the means of $\abs{u}$ over circles are unbounded, so $u \notin h^1$.
In the plane, if $1 < p < \infty$ and $f = u + iv$ is holomorphic with $v(0) = 0$, then $u \in h^p$ if and only if $f$ is in the holomorphic [[Hardy space|PNNNFJVF6W]] $H^p$, by the [[M. Riesz theorem|PJFH51Z48M]].
This fails for $p = 1$ and for $p = \infty$.
