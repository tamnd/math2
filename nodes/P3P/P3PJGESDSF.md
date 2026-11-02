---
tag: P3PJGESDSF
kind: definition
name: (p,q)-form
msc: [32W05, 58A10]
defines: DC81TCR98Y
uses: [0E3G0GRPZ6, 0MDMZ965VE, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_differential_form
---

## Definition

Let $U \subseteq \C^n$ be an open set, with coordinates $z_j = x_j + i y_j$.
Consider complex-valued [[differential forms|0E3G0GRPZ6]] on $U$, and put $dz_j = dx_j + i\, dy_j$ and $d\bar z_j = dx_j - i\, dy_j$.
For increasing tuples $I = (i_1 < \cdots < i_p)$ and $J = (j_1 < \cdots < j_q)$ of elements of $\set{1, \dots, n}$, write $dz_I = dz_{i_1} \wedge \cdots \wedge dz_{i_p}$ and $d\bar z_J = d\bar z_{j_1} \wedge \cdots \wedge d\bar z_{j_q}$.
Let $p, q \ge 0$ be integers.
A *$(p, q)$-form* on $U$ is a differential form
$$\omega = \sum_{\abs{I} = p, \ \abs{J} = q} \omega_{IJ} \, dz_I \wedge d\bar z_J,$$
where the sum runs over increasing tuples and each $\omega_{IJ} \colon U \to \C$ is a [[smooth function|0V33BNKZ9S]].

## Remarks

The forms $dz_I \wedge d\bar z_J$ with $\abs{I} + \abs{J} = k$ form a basis of the complex $k$-th [[exterior power|0MDMZ965VE]] of the cotangent space at each point.
So every complex $k$-form is, in a unique way, a sum of $(p, q)$-forms with $p + q = k$.
Example: $\omega = \bar z_1 \, dz_1 \wedge d\bar z_2$ on $\C^2$ is a $(1, 1)$-form, with $\omega_{(1)(2)} = \bar z_1$ and all other coefficients zero.
Non-example: $dx_1 = \tfrac12 dz_1 + \tfrac12 d\bar z_1$ is a $1$-form whose $(1, 0)$ and $(0, 1)$ parts are both nonzero, so it is not a $(p, q)$-form for any $(p, q)$.
A holomorphic change of coordinates $w = F(z)$ gives $dw_k = \sum_j \frac{\partial F_k}{\partial z_j} dz_j$ with no $d\bar z_j$ terms, so the type $(p, q)$ is preserved; thus $(p, q)$-forms are defined on complex manifolds.
The space of $(p, q)$-forms on $U$ is often written $\mathcal{E}^{p, q}(U)$.
