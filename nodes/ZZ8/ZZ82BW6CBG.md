---
tag: ZZ82BW6CBG
kind: definition
name: Elliptic gamma function
msc: ["33E20", "33D05"]
defines: JTXBDYXJET
uses: [Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_gamma_function
---

## Definition

Let $p, q$ be complex numbers with $\abs{p} < 1$ and $\abs{q} < 1$.
For $z \in \C \setminus \set{0}$ with $p^j q^k z \ne 1$ for all integers $j, k \ge 0$, the *elliptic gamma function* is
$$\Gamma(z; p, q) = \prod_{j, k \ge 0} \frac{1 - p^{j+1} q^{k+1} / z}{1 - p^j q^k z}.$$

## Remarks

With the theta function $\theta(z; p) = (z; p)_\infty\, (p/z; p)_\infty$, built from the [[q-Pochhammer symbol|Y1X8ZZQ7VM]] $(a; p)_\infty = \prod_{j \ge 0}(1 - a p^j)$, the function satisfies
$$\Gamma(qz; p, q) = \theta(z; p)\, \Gamma(z; p, q).$$
Check: in the quotient $\Gamma(qz)/\Gamma(z)$ all factors cancel except the factors with $k = 0$, which give $\prod_{j \ge 0}(1 - p^{j+1}/z)(1 - p^j z) = \theta(z; p)$.

Example: replacing $z$ by $pq/z$ exchanges the numerator and the denominator of the product, so $\Gamma(z; p, q)\, \Gamma(pq/z; p, q) = 1$.

Non-example of a valid argument: $z = 1$ makes the factor $1 - p^0 q^0 z$ vanish, so $\Gamma(z; p, q)$ has a pole at $z = 1$.

The function is symmetric in $p$ and $q$.
