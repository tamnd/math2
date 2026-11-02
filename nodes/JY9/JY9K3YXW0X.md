---
tag: JY9K3YXW0X
kind: definition
name: Unit and counit
msc: [18A40]
defines: MYGWT305AB
uses: [TZHF6ZM92S, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_functors
---

## Definition

Let $F \colon \mathcal{C} \to \mathcal{D}$ be [[left adjoint|TZHF6ZM92S]] to $G \colon \mathcal{D} \to \mathcal{C}$ by the natural bijections $\varphi_{c, d} \colon \Hom_{\mathcal{D}}(F c, d) \to \Hom_{\mathcal{C}}(c, G d)$.

1. The *unit* of the adjunction is the family $\eta_c = \varphi_{c, F c}(\id_{F c}) \colon c \to G F c$ for objects $c$ of $\mathcal{C}$.
2. The *counit* of the adjunction is the family $\varepsilon_d = \varphi_{G d, d}^{-1}(\id_{G d}) \colon F G d \to d$ for objects $d$ of $\mathcal{D}$.

## Remarks

Both families are [[natural transformations|KYCPCC57FT]], $\eta \colon \mathrm{Id}_{\mathcal{C}} \Rightarrow G F$ and $\varepsilon \colon F G \Rightarrow \mathrm{Id}_{\mathcal{D}}$.
They satisfy the *triangle identities*
$$\varepsilon_{F c} \circ F(\eta_c) = \id_{F c}, \qquad G(\varepsilon_d) \circ \eta_{G d} = \id_{G d}.$$
They recover $\varphi$ by $\varphi(g) = G(g) \circ \eta_c$ for $g \colon F c \to d$.

Example: for the free vector space functor $F$ over a field $k$ and the forgetful functor $G$, the unit $\eta_X \colon X \to G F X$ sends $x$ to the basis vector $e_x$.
The counit $\varepsilon_V \colon F G V \to V$ sends the basis vector $e_v$ to the vector $v$.
Then $\varepsilon_{F X}(F(\eta_X)(e_x)) = \varepsilon_{F X}(e_{e_x}) = e_x$, which checks the first triangle identity.

Non-example: if the characteristic of $k$ is not $2$, the natural maps $\eta'_X(x) = 2 e_x$ are not a unit for this counit.
Here $\varepsilon_{F X} \circ F(\eta'_X)$ is multiplication by $2$, so the first triangle identity fails.
