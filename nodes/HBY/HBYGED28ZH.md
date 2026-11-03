---
tag: HBYGED28ZH
kind: definition
name: Quaternions and spatial rotation
msc: [70B10, 15B10, "22E70"]
defines: EAK8KT5AMD
uses: [0GE4DVQKR8, 0CGYNDCWRR, 0XNZWJ96HK]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
---

## Definition

Let $\mathbb{H}$ be the [[quaternions|0GE4DVQKR8]], with conjugation $q \mapsto \bar q$ and norm $\abs{q} = \sqrt{q \bar q}$.
Identify $\R^3$ with the pure quaternions by $(v_1, v_2, v_3) \mapsto v_1 i + v_2 j + v_3 k$.
A *unit quaternion* is a $q \in \mathbb{H}$ with $\abs{q} = 1$.
The *rotation associated with* a unit quaternion $q$ is the map
$$R_q \colon \R^3 \to \R^3, \qquad R_q(v) = q\, v\, \bar q.$$

## Remarks

For each unit quaternion $q$, the map $R_q$ is an element of the [[special orthogonal group|0CGYNDCWRR]] $SO(3)$.
If $q = \cos(\theta/2) + \sin(\theta/2)(u_1 i + u_2 j + u_3 k)$ with $(u_1, u_2, u_3)$ a unit vector, then $R_q$ is the [[rotation|0XNZWJ96HK]] by $\theta$ about the axis $\R u$.
One has $R_{pq} = R_p \circ R_q$, and the map $q \mapsto R_q$ from the unit quaternions onto $SO(3)$ is a surjective group homomorphism with kernel $\set{1, -1}$.

Example: $q = (1 + k)/\sqrt{2}$ has $\abs{q} = 1$ and $\bar q = (1 - k)/\sqrt{2}$.
Then $R_q(i) = \tfrac12 (1 + k)\, i\, (1 - k) = \tfrac12 (i + j)(1 - k) = \tfrac12 (i + j + j - i) = j$, and $R_q(k) = k$.
So $R_q$ is the quarter turn about the $z$-axis, as the formula with $\theta = \pi/2$ predicts.

Non-example: $q = 2$ is not a unit quaternion, and $v \mapsto q v \bar q = 4 v$ is a scaling, not a rotation.
For any nonzero $q$ the map $v \mapsto q v q^{-1}$ equals $R_{q / \abs{q}}$, so one may also use non-unit quaternions in that form.
