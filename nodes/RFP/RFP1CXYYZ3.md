---
tag: RFP1CXYYZ3
kind: definition
name: View factor
msc: [80A21, 78A40]
defines: 8B0S4F70YA
uses: [S6XR2K4N8G, 5SAVDDA5P1]
sources:
  - url: https://en.wikipedia.org/wiki/View_factor
---

## Definition

Let $A_i$ and $A_j$ be two surfaces in space, with areas also written $A_i$ and $A_j$.
For points $p \in A_i$ and $q \in A_j$, let $S$ be the distance from $p$ to $q$.
Let $\theta_i$ and $\theta_j$ be the angles between the segment $pq$ and the normals of the surfaces at $p$ and at $q$.
The integrand below is set to $0$ when the segment $pq$ is blocked or when a surface faces away from the other point.
The *view factor* from $A_i$ to $A_j$ is
$$F_{i \to j} = \frac{1}{A_i} \int_{A_i} \int_{A_j} \frac{\cos\theta_i \cos\theta_j}{\pi S^2} \, dA_j \, dA_i.$$
If $A_i$ emits and reflects diffusely with uniform [[radiosity|5SAVDDA5P1]], then $F_{i \to j}$ is the fraction of the [[thermal radiation|S6XR2K4N8G]] leaving $A_i$ that strikes $A_j$ directly.

## Remarks

Reciprocity $A_i F_{i \to j} = A_j F_{j \to i}$ follows from the symmetry of the integrand.
If $A_1, \dots, A_n$ form a closed enclosure, then $\sum_{j=1}^n F_{i \to j} = 1$ for each $i$, and $F_{i \to i} = 0$ when $A_i$ is plane or convex.

Example: a hemispherical shell $A_1$ of radius $R$ closed by its base disk $A_2$.
The disk sees only the shell, so $F_{2 \to 1} = 1$.
Reciprocity gives $F_{1 \to 2} = (\pi R^2)(1) / (2\pi R^2) = 1/2$, and summation gives $F_{1 \to 1} = 1/2$: the concave shell sees itself.

Non-example: if $A_i$ is a mirror, reflecting specularly, the reflected part of the radiation leaving $A_i$ is not distributed according to $F_{i \to j}$, since the diffuse assumption fails.

Other names are configuration factor, angle factor and shape factor.
