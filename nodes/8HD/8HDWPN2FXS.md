---
tag: 8HDWPN2FXS
kind: definition
name: Determinant line bundle
msc: [58J52, 47A53]
defines: 5DST3VKEMX
uses: [8HWGKWD6ZM, HM2HHE3J51, P4DZM975BV]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant_line_bundle
---

## Definition

Let $H_0$ and $H_1$ be complex [[Hilbert spaces|HM2HHE3J51]], and let $Y$ be a topological space.
Let $y \mapsto T_y$ be a map from $Y$ to the [[Fredholm operators|8HWGKWD6ZM]] $H_0 \to H_1$ that is continuous in the operator norm.
For a finite-dimensional space $V$ write $\det V = \Lambda^{\dim V} V$, with $\det 0 = \C$.
The *determinant line* of $T_y$ is
$$\det T_y = (\det \ker T_y)^* \otimes \det \operatorname{coker} T_y.$$
The *determinant line bundle* is the set $\det T = \bigsqcup_{y \in Y} \det T_y$ with the following topology.
Near a point $y_0$, choose a finite-dimensional subspace $V \subseteq H_1$ with $\operatorname{im} T_y + V = H_1$ for all $y$ near $y_0$.
Then the spaces $T_y^{-1}(V)$ form a [[vector bundle|P4DZM975BV]] over a neighbourhood of $y_0$.
The exact sequence $0 \to \ker T_y \to T_y^{-1}(V) \to V \to \operatorname{coker} T_y \to 0$ gives a canonical isomorphism $\det T_y \cong (\det T_y^{-1}(V))^* \otimes \det V$.
The right side is a line bundle near $y_0$.
The topology of $\det T$ is the one that makes these isomorphisms continuous, and it does not depend on the choice of $V$.

## Remarks

Some authors use the dual line $\det \ker T_y \otimes (\det \operatorname{coker} T_y)^*$; the two conventions give dual line bundles.

Example: if every $T_y$ is invertible, then $\ker T_y = 0$ and $\operatorname{coker} T_y = 0$, so each fibre is $\C$ and $\det T$ is the trivial line bundle $Y \times \C$.

Non-example: the family $T_y = y \cdot \id$ on an infinite-dimensional Hilbert space, for $y \in [0, 1]$, is not a family of Fredholm operators, since $T_0 = 0$ has infinite-dimensional kernel.
So $\det T_0$ is not defined.
