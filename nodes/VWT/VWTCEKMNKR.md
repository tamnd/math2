---
tag: VWTCEKMNKR
kind: definition
name: Holonomy
msc: [53C29]
defines: WHDZ3MK56B
uses: [5ZYRRVE8BW, TVAGN3D6W5]
sources:
  - url: https://en.wikipedia.org/wiki/Holonomy
---

## Definition

Let $M$ be a connected smooth manifold, let $E \to M$ be a smooth vector bundle with a [[connection|5ZYRRVE8BW]] $\nabla$, and let $p \in M$.
For a piecewise smooth loop $\gamma$ based at $p$, let $P_\gamma : E_p \to E_p$ be the [[parallel transport|TVAGN3D6W5]] along $\gamma$.
The *holonomy group* of $\nabla$ at $p$ is
$$\mathrm{Hol}_p(\nabla) = \set{P_\gamma : \gamma \text{ a piecewise smooth loop based at } p} \subset \mathrm{GL}(E_p).$$
The *restricted holonomy group* $\mathrm{Hol}^0_p(\nabla)$ is the subset given by the loops that are null-homotopic.

## Remarks

$\mathrm{Hol}_p(\nabla)$ is a group, because $P_{\gamma \cdot \delta} = P_\delta \circ P_\gamma$ and $P_{\gamma^{-1}} = P_\gamma^{-1}$.
It is a [[Lie subgroup|NM8XCPS1Q3]] of $\mathrm{GL}(E_p)$, and $\mathrm{Hol}^0_p(\nabla)$ is its identity component; the quotient is a quotient of $\pi_1(M, p)$.
Changing the base point along a curve $\sigma$ from $p$ to $q$ conjugates the group: $\mathrm{Hol}_q = P_\sigma \mathrm{Hol}_p P_\sigma^{-1}$.
Example: the flat connection on $T\R^n$ has $P_\gamma = \id$ for every loop, so $\mathrm{Hol}_p$ is trivial.
For the Levi-Civita connection of the round sphere $S^2$, $\mathrm{Hol}_p = \mathrm{SO}(2)$: the transport around a loop is the rotation by the enclosed area.
For the Levi-Civita connection of any Riemannian $n$-manifold, $\mathrm{Hol}_p \subset \mathrm{O}(T_pM)$, and $\mathrm{Hol}_p \subset \mathrm{SO}(T_pM)$ if $M$ is orientable.
Non-example: the flat connection on the Möbius line bundle over the circle has trivial restricted holonomy, but $\mathrm{Hol}_p = \set{\pm 1}$ is not trivial; so flatness alone does not force trivial holonomy.
