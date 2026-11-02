---
tag: 17BH73YHVT
kind: definition
name: Concentration of measure
msc: [52A23, "60E15", 60B11]
defines: CFZ1J559MK
uses: [0VKD1TP7F3, 059TJN0NZ1, P0DV2TCH1N]
sources:
  - url: https://en.wikipedia.org/wiki/Concentration_of_measure
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and $\mu$ a Borel [[probability measure|059TJN0NZ1]] on $X$.
For a Borel set $A \subseteq X$ and $r > 0$, let $A_r = \set{x \in X : d(x, A) < r}$.
The *concentration function* of $(X, d, \mu)$ is
$$\alpha(r) = \sup \set{1 - \mu(A_r) : A \subseteq X \text{ Borel}, \ \mu(A) \ge 1/2}, \qquad r > 0.$$
A sequence $(X_k, d_k, \mu_k)$ of such spaces exhibits *concentration of measure*, and is called a *normal Lévy family*, if there are constants $C, c > 0$ with
$$\alpha_k(r) \le C e^{-c k r^2} \quad \text{for all } k \ge 1 \text{ and } r > 0.$$

## Remarks

Example: take the unit sphere $S^{k}$ of $\R^{k+1}$ with the geodesic metric and the normalized surface measure.
Lévy's isoperimetric inequality gives such a bound with absolute constants $C$ and $c$, so the spheres form a normal Lévy family.
The [[Gaussian measure|P0DV2TCH1N]] $\gamma_n$ on $\R^n$ concentrates with a bound that does not depend on the dimension: if $\gamma_n(A) \ge 1/2$, then $\gamma_n(A_r) \ge 1 - \frac{1}{2} e^{-r^2/2}$.
Non-example: the two-point space $\set{0, 1}$ with $d(0, 1) = 1$ and $\mu(\set{0}) = \mu(\set{1}) = 1/2$; for $A = \set{0}$ and $r \le 1$ one has $A_r = A$, so $\alpha(r) \ge 1/2$ for $r \le 1$.
An equivalent form: $\mu(\set{x : \abs{f(x) - M_f} \ge r}) \le 2 \alpha(r)$ for every $1$-Lipschitz function $f \colon X \to \R$ with median $M_f$.
