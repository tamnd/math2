---
tag: 246NVGBMMX
kind: statement
role: theorem
name: Hellinger–Reissner principle
msc: [74B05, 74G65, 74S05]
uses: [6W00ZECYT0, SX32X1D537, 8QS6QMJF5Z, KG2XWEMJ30, SJZX81A783, 5B8NFYB2XQ, 0JW6MDHAZD, A5T30ZHVGH]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Hu%E2%80%93Washizu_principle
---

## Statement

Let $\Omega \subset \R^3$ be a bounded domain with Lipschitz boundary $\partial\Omega = \overline{\Gamma_D} \cup \overline{\Gamma_N}$, where $\Gamma_D$ and $\Gamma_N$ are disjoint and $\Gamma_D$ has positive surface measure.
Let $\mathsf{C}$ be a bounded symmetric [[elasticity tensor|SX32X1D537]] field that is uniformly positive definite on symmetric $3 \times 3$ matrices, and let $\mathsf{S} = \mathsf{C}^{-1}$ be the compliance tensor.
Let $f \in L^2(\Omega)^3$ be the body force and $g \in L^2(\Gamma_N)^3$ the surface traction.
For a displacement $v$ let $\varepsilon(v) = \tfrac12(\nabla v + \nabla v^T)$ be its linearised [[strain|8QS6QMJF5Z]].
Let $V = \set{v \in H^1(\Omega)^3 : v = 0 \text{ on } \Gamma_D}$ and let $L^2_{\mathrm{sym}}$ be the space of square-integrable fields of symmetric $3 \times 3$ matrices.
The Hellinger–Reissner functional on $V \times L^2_{\mathrm{sym}}$ is
$$\Pi_{HR}(v, \tau) = \int_\Omega \left( \tau : \varepsilon(v) - \tfrac12\, \mathsf{S}\tau : \tau - f \cdot v \right) dx - \int_{\Gamma_N} g \cdot v \, dS.$$
Then a pair $(u, \sigma) \in V \times L^2_{\mathrm{sym}}$ is a stationary point of $\Pi_{HR}$, that is, its [[first variation|5B8NFYB2XQ]] vanishes in all directions, if and only if:

1. $\mathsf{S}\sigma = \varepsilon(u)$, that is, $\sigma = \mathsf{C}\varepsilon(u)$;
2. $\int_\Omega \sigma : \varepsilon(v)\, dx = \int_\Omega f \cdot v \, dx + \int_{\Gamma_N} g \cdot v \, dS$ for all $v \in V$.

In that case $u$ is the unique [[weak solution|SJZX81A783]] of the problem of [[linear elasticity|6W00ZECYT0]] with these data, and $\sigma$ is its [[stress|KG2XWEMJ30]].
Moreover $(u, \sigma)$ is a [[saddle point|0JW6MDHAZD]]: $\Pi_{HR}(u, \tau) \le \Pi_{HR}(u, \sigma) \le \Pi_{HR}(v, \sigma)$ for all $v \in V$ and $\tau \in L^2_{\mathrm{sym}}$.

## Remarks

Varying $\tau$ gives $\int_\Omega \delta\tau : (\varepsilon(u) - \mathsf{S}\sigma)\,dx = 0$ for all $\delta\tau$, hence clause 1.
Varying $v$ gives clause 2.
Substituting $\sigma = \mathsf{C}\varepsilon(u)$ shows that clauses 1 and 2 hold exactly when $u$ minimises the total potential energy, so existence and uniqueness follow from the [[minimum total potential energy principle|A5T30ZHVGH]].
The functional is concave in $\tau$, because $\mathsf{S}$ is positive definite, and affine in $v$.
So $\sigma$ maximises $\Pi_{HR}(u, \cdot)$, and stationarity in $v$ makes $\Pi_{HR}(\cdot, \sigma)$ constant on $V$; this gives the saddle-point inequalities.

Example: for a bar $[0, \ell]$ with stiffness $k > 0$, clamped at $0$ and pulled by a force $P$ at $\ell$, $\Pi_{HR}(v, \tau) = \int_0^\ell (\tau v' - \tau^2 / (2k))\,dx - P v(\ell)$.
Its stationary point is $u(x) = Px / k$ and $\sigma = P$.

The principle is the Hu–Washizu principle after the strain has been eliminated by the constitutive law.
Another common form integrates $\int_\Omega \tau : \varepsilon(v)\,dx$ by parts, so that $\tau$ must have a square-integrable divergence and $v$ need only be square-integrable.

## Explanations

### L1 human

In elasticity one can treat the displacement and the stress as two independent unknowns.
The Hellinger–Reissner principle gives one expression in both of them whose stationary points are exactly the true solutions.
At the solution the expression is largest in the stress direction and flat in the displacement direction, so it is a saddle point, not a minimum.

### L2 human

The principle is the basis of two-field mixed finite element methods, in which stresses are approximated directly instead of being computed by differentiating displacements.
This often gives more accurate stresses and avoids locking in thin structures and in nearly incompressible materials.
Because the solution is a saddle point, the discrete stress and displacement spaces must satisfy an inf-sup condition to give a stable method.
It is the two-field case of the Hu–Washizu principle.
