---
tag: 0G4W89YJRK
kind: definition
name: Oriented angle
msc: [51M05]
defines: 03YN70NK0Z
uses: [0XW7V9ZZ05, 0ZEHZY85E6]
sources:
  - url: https://en.wikipedia.org/wiki/Angle
    locator: Signed angles
---

## Definition

Let $u = (u_1, u_2)$ and $v = (v_1, v_2)$ be nonzero vectors in the [[Euclidean plane|0XW7V9ZZ05]] $\mathbb{R}^2$. Let $u \cdot v = u_1 v_1 + u_2 v_2$ and $\det(u, v) = u_1 v_2 - u_2 v_1$.
The oriented angle from $u$ to $v$ is the class modulo $2\pi$ of each real number $\theta$ with
$$\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|} \quad \text{and} \quad \sin \theta = \frac{\det(u, v)}{\|u\| \, \|v\|}.$$
For points $A$, $B$ and $C$ of $\mathbb{R}^2$ with $A \neq B$ and $C \neq B$, the oriented angle $\measuredangle ABC$ is the oriented angle from $A - B$ to $C - B$.

## Remarks

Such a $\theta$ exists because $(u \cdot v)^2 + \det(u, v)^2 = \|u\|^2 \|v\|^2$. It is unique modulo $2\pi$.
Swapping the vectors changes the sign: the oriented angle from $v$ to $u$ is minus the oriented angle from $u$ to $v$.
The [[unoriented angle|0ZEHZY85E6]] between $u$ and $v$ is the absolute value of the representative of the oriented angle in $(-\pi, \pi]$.
Mathlib's `EuclideanGeometry.oangle` works in each oriented Euclidean plane, with values in $\mathbb{R} / 2\pi\mathbb{Z}$. It gives $0$ when a vector is zero.

## Explanations

### L1 human

The oriented angle remembers the direction of the turn. Turning from $(1, 0)$ to $(0, 1)$ is a quarter turn anticlockwise, so the oriented angle is $\pi / 2$. Turning back, from $(0, 1)$ to $(1, 0)$, gives $-\pi / 2$.
