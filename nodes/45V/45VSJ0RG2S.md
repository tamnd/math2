---
tag: 45VSJ0RG2S
kind: definition
name: Hodge star operator
msc: [58A10, 15A75]
defines: 1Y4WX4XQWJ
uses: [0MDMZ965VE, 0NB0AWGJBW, 0QJJAQ6ZYZ, 7CBT4SM83Y, 0E3G0GRPZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Hodge_star_operator
---

## Definition

Let $V$ be a real vector space of dimension $n$ with an [[inner product|0NB0AWGJBW]] $\ip{\cdot}{\cdot}$ and an [[orientation|0QJJAQ6ZYZ]].
Let $\operatorname{vol} = e_1 \wedge \dots \wedge e_n$ for any positively oriented orthonormal basis $e_1, \dots, e_n$.
On the [[exterior power|0MDMZ965VE]] $\Lambda^k V$ use the inner product with $\ip{v_1 \wedge \dots \wedge v_k}{w_1 \wedge \dots \wedge w_k} = \det\bigl(\ip{v_i}{w_j}\bigr)$.
The *Hodge star operator* is the unique linear map $\star \colon \Lambda^k V \to \Lambda^{n-k} V$ such that
$$\alpha \wedge \star\beta = \ip{\alpha}{\beta} \operatorname{vol} \quad \text{for all } \alpha, \beta \in \Lambda^k V.$$
On an oriented [[Riemannian manifold|7CBT4SM83Y]] $(M, g)$, the Hodge star is applied pointwise to [[differential forms|0E3G0GRPZ6]], with $V = T_p^* M$ and the inner product induced by $g$.

## Remarks

Example: in $\R^3$ with the standard orientation, $\star dx = dy \wedge dz$, $\star dy = dz \wedge dx$ and $\star dz = dx \wedge dy$.
Check for $dx$: $dx \wedge \star dx = dx \wedge dy \wedge dz = \ip{dx}{dx} \operatorname{vol}$, and $dy \wedge \star dx = 0 = \ip{dy}{dx} \operatorname{vol}$, and the same for $dz$.

Non-example: in $\R^2$ the map with $dx \mapsto -dy$ and $dy \mapsto dx$ is not the Hodge star, since $dx \wedge (-dy) = -\operatorname{vol}$, while $\ip{dx}{dx} \operatorname{vol} = \operatorname{vol}$.
The Hodge star of $\R^2$ is $\star dx = dy$, $\star dy = -dx$, a rotation by a right angle.

On orthonormal bases, $\star(e_{i_1} \wedge \dots \wedge e_{i_k}) = \pm e_{j_1} \wedge \dots \wedge e_{j_{n-k}}$, where the $j$'s are the complementary indices and the sign is that of the permutation $(i_1, \dots, i_k, j_1, \dots, j_{n-k})$.
It satisfies $\star 1 = \operatorname{vol}$ and $\star\star = (-1)^{k(n-k)}$ on $\Lambda^k V$, and it is an isometry.
Reversing the orientation changes the sign of $\star$.
