---
tag: TDY6EY60DV
kind: definition
name: Kodaira–Spencer map
msc: [32G05, 14D15]
defines: EWZ1G10MAY
uses: [VKQSM3BCE4, PQ6Q143ARJ, WY6K3P4YCG]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira%E2%80%93Spencer_map
---

## Definition

Let $\varpi \colon \mathcal{X} \to B$ be a complex analytic family of compact complex manifolds, as in a [[deformation of complex structure|VKQSM3BCE4]], and let $t \in B$ with fibre $X_t$.
For a complex manifold $Y$ let $\Theta_Y$ denote the sheaf of holomorphic sections of its holomorphic [[tangent bundle|WY6K3P4YCG]].
Since $\varpi$ is a submersion, there is a short exact sequence of sheaves on $X_t$
$$0 \to \Theta_{X_t} \to \Theta_{\mathcal{X}}|_{X_t} \xrightarrow{d\varpi} T_t B \otimes \mathcal{O}_{X_t} \to 0.$$
The *Kodaira–Spencer map* of the family at $t$ is the connecting homomorphism of its long exact [[cohomology|PQ6Q143ARJ]] sequence,
$$\rho_t \colon T_t B = H^0(X_t, T_t B \otimes \mathcal{O}_{X_t}) \to H^1(X_t, \Theta_{X_t}).$$

## Remarks

The identification $H^0(X_t, T_t B \otimes \mathcal{O}_{X_t}) = T_t B$ uses that $X_t$ is compact and connected, so its global holomorphic functions are constants.
In Čech terms: cover $\mathcal{X}$ near $X_t$ by charts $(z_i, s)$ with $\varpi(z_i, s) = s$, glued by $z_i = f_{ij}(z_j, s)$.
For $v = \partial / \partial s$, the class $\rho_t(v)$ is represented by the vector fields $\sum_k \frac{\partial f_{ij}^k}{\partial s}(z_j, t)\, \frac{\partial}{\partial z_i^k}$ on the overlaps.

Example: for a trivial family $X \times B \to B$, the sequence splits, and $\rho_t = 0$ for all $t$.

Example: for the family $\C/(\Z + \tau\Z)$ over the upper half-plane, $\Theta_{X_\tau} \cong \mathcal{O}_{X_\tau}$, so $H^1(X_\tau, \Theta_{X_\tau})$ is one-dimensional, and $\rho_\tau$ is an isomorphism at every $\tau$.

A family with $\rho_t$ surjective at $t$ is complete at $t$: every small deformation of $X_t$ is pulled back from it, by a theorem of Kodaira and Spencer.
