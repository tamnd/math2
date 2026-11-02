---
tag: HNGT8S7JAG
kind: definition
name: Carlson symmetric forms
msc: ["33E05", 33F05]
defines: MK3ASPEN8A
uses: [NXMCYGCB59, 05KQ3F99BQ]
sources:
  - url: https://en.wikipedia.org/wiki/Carlson_symmetric_form
---

## Definition

Let $x, y, z$ be nonnegative real numbers, at most one of which is $0$, and let $p > 0$.
The *Carlson symmetric forms* are [[improper integrals|05KQ3F99BQ]].
They are
$$R_F(x, y, z) = \frac{1}{2} \int_0^\infty \frac{dt}{\sqrt{(t + x)(t + y)(t + z)}},$$
$$R_J(x, y, z, p) = \frac{3}{2} \int_0^\infty \frac{dt}{(t + p)\sqrt{(t + x)(t + y)(t + z)}},$$
together with the special cases
$$R_C(x, y) = R_F(x, y, y), \qquad R_D(x, y, z) = R_J(x, y, z, z),$$
where for $R_C$ one takes $x \ge 0$ and $y > 0$, and for $R_D$ one takes $z > 0$.

## Remarks

The integrals converge: near $t = \infty$ the integrand of $R_F$ behaves like $t^{-3/2}$, and near $t = 0$ at most one factor vanishes, which gives at worst $t^{-1/2}$.
$R_F$ is symmetric in $x, y, z$, $R_J$ in $x, y, z$, and $R_D$ in $x, y$.
Example: $R_F(x, x, x) = \frac12\int_0^\infty (t + x)^{-3/2}\,dt = x^{-1/2}$ for $x > 0$.
Non-example: $R_F(0, 0, 1)$ is not defined, since two arguments are $0$ and the integrand $1/(t\sqrt{t + 1})$ is not integrable at $t = 0$.
With $k' = \sqrt{1 - k^2}$ and $0 \le k < 1$, the complete [[elliptic integrals|NXMCYGCB59]] are
$$K(k) = R_F(0, k'^2, 1), \qquad E(k) = R_F(0, k'^2, 1) - \frac{k^2}{3} R_D(0, k'^2, 1).$$
$R_C$ is elementary; for $0 \le x < y$ it equals $\arccos(\sqrt{x/y}) / \sqrt{y - x}$.
