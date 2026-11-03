---
tag: RG1Z4YXVF4
kind: statement
role: theorem
name: Hu–Washizu principle
msc: [74B05, 74G65, 74S05]
uses: [6W00ZECYT0, SX32X1D537, 8QS6QMJF5Z, KG2XWEMJ30, SJZX81A783, 5B8NFYB2XQ, A5T30ZHVGH]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Hu%E2%80%93Washizu_principle
same_as:
  wikidata: Q17027345
  wikipedia: Hu–Washizu principle
---

## Statement

Let $\Omega \subset \R^3$ be a bounded domain with Lipschitz boundary $\partial\Omega = \overline{\Gamma_D} \cup \overline{\Gamma_N}$, where $\Gamma_D$ and $\Gamma_N$ are disjoint and $\Gamma_D$ has positive surface measure.
Let $\mathsf{C}$ be a bounded symmetric [[elasticity tensor|SX32X1D537]] field that is uniformly positive definite on symmetric $3 \times 3$ matrices.
Let $f \in L^2(\Omega)^3$ be the body force, $g \in L^2(\Gamma_N)^3$ the surface traction, and $\bar u \in H^1(\Omega)^3$ a given displacement.
For a displacement $v$ let $\varepsilon(v) = \tfrac12(\nabla v + \nabla v^T)$ be its linearised [[strain|8QS6QMJF5Z]].
Let $U = \set{v \in H^1(\Omega)^3 : v = \bar u \text{ on } \Gamma_D}$, let $V = \set{v \in H^1(\Omega)^3 : v = 0 \text{ on } \Gamma_D}$, and let $L^2_{\mathrm{sym}}$ be the space of square-integrable fields of symmetric $3 \times 3$ matrices.
The Hu–Washizu functional on $U \times L^2_{\mathrm{sym}} \times L^2_{\mathrm{sym}}$ is
$$\Pi_{HW}(v, e, \tau) = \int_\Omega \left( \tfrac12\, \mathsf{C} e : e - \tau : \big(e - \varepsilon(v)\big) - f \cdot v \right) dx - \int_{\Gamma_N} g \cdot v \, dS.$$
Then a triple $(u, e, \sigma)$ is a stationary point of $\Pi_{HW}$, that is, its [[first variation|5B8NFYB2XQ]] vanishes in all directions of $V \times L^2_{\mathrm{sym}} \times L^2_{\mathrm{sym}}$, if and only if:

1. $e = \varepsilon(u)$ (kinematics);
2. $\sigma = \mathsf{C} e$ (constitutive law);
3. $\int_\Omega \sigma : \varepsilon(v)\, dx = \int_\Omega f \cdot v \, dx + \int_{\Gamma_N} g \cdot v \, dS$ for all $v \in V$ (weak equilibrium).

In that case $u$ is the unique [[weak solution|SJZX81A783]] of the problem of [[linear elasticity|6W00ZECYT0]] with these data, and $\sigma$ is its [[stress|KG2XWEMJ30]].

## Remarks

The proof is a direct computation of the three partial variations.
Varying $\tau$ gives $\int_\Omega \delta\tau : (e - \varepsilon(u))\,dx = 0$ for all $\delta\tau$, hence clause 1.
Varying $e$ gives $\int_\Omega (\mathsf{C} e - \sigma) : \delta e \, dx = 0$, hence clause 2, using the symmetry of $\mathsf{C}$.
Varying $v$ gives clause 3.
Clauses 1 to 3 together say that $u$ minimises the total potential energy, so existence and uniqueness follow from the [[minimum total potential energy principle|A5T30ZHVGH]].

The stationary point is a saddle point, not a minimum: the functional is linear in $\tau$.
Eliminating $e$ and $\tau$ by clauses 1 and 2 gives back the total potential energy; eliminating $e$ by clause 2 alone gives the Hellinger–Reissner functional.
The displacement condition on $\Gamma_D$ is imposed here in the space $U$; other versions add a boundary term to impose it weakly.

## Explanations

### L1 human

Linear elasticity links three fields: the displacement, the strain and the stress.
The Hu–Washizu principle writes one energy-like expression in which all three are free to vary independently.
Its stationary points are exactly the solutions where the three fields fit together correctly.
So one variational principle contains the strain–displacement relation, Hooke's law and the equilibrium equations.

### L2 human

The principle is the starting point of three-field mixed finite element methods.
One chooses separate finite-dimensional spaces for displacements, strains and stresses, and imposes stationarity on them.
Such methods are used to avoid locking, for instance in nearly incompressible materials, and the assumed-strain and enhanced-strain elements can be derived from it.
Unlike the potential energy, the functional is not convex, so the discrete spaces must satisfy inf-sup stability conditions.
