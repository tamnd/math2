---
tag: YKSA8SJ81V
kind: statement
role: theorem
name: Theorema Egregium
msc: [53A05]
uses: [SQVQ5DQT6W, MAJ3DH7MZS, 6080X3FAD4, 68TVVHCQ3Z]
about: [SQVQ5DQT6W]
sources:
  - url: https://en.wikipedia.org/wiki/Theorema_Egregium
same_as:
  wikidata: Q1048874
  wikipedia: Theorema Egregium
---

## Statement

Let $S$ and $\bar S$ be [[regular surfaces|6080X3FAD4]] in $\R^3$, and let $\varphi \colon S \to \bar S$ be a smooth map.
Assume that $\varphi$ is a local isometry: for each $p \in S$ and $v, w \in T_p S$, $\ip{d\varphi_p(v)}{d\varphi_p(w)} = \ip{v}{w}$.
Let $K$ and $\bar K$ be the [[Gaussian curvatures|SQVQ5DQT6W]] of $S$ and $\bar S$.
Then $\bar K(\varphi(p)) = K(p)$ for each $p \in S$.

## Remarks

The key step is that $K$ can be written, in any local parametrisation, through $E, F, G$ of the [[first fundamental form|MAJ3DH7MZS]] and their partial derivatives of order at most $2$.
This follows from the Gauss equation among the [[Gauss–Codazzi equations|68TVVHCQ3Z]], which expresses $eg - f^2$ through the Christoffel symbols, and these depend only on $E, F, G$.
A local isometry has, in suitable parametrisations, the same functions $E, F, G$, hence the same $K$.
Example: the map $(u, v) \mapsto (\cos u, \sin u, v)$ wraps the plane onto the unit cylinder as a local isometry, and indeed both have $K = 0$.
Consequence: no open piece of a sphere, where $K > 0$, is isometric to a piece of the plane, so every flat map of a region of the Earth distorts some distances.
The converse fails: a map that preserves $K$ need not be a local isometry.
For example, the map $(x, y, 0) \mapsto (2x, y, 0)$ of the plane keeps $K = 0$ but doubles some lengths.

## Explanations

### L1 human

Gaussian curvature can be measured by someone who lives on the surface and only measures lengths on it.
Bending a surface without stretching it, like rolling a sheet of paper, never changes its Gaussian curvature.
This is why you cannot flatten an orange peel without tearing it, and why every flat map of the Earth is distorted.

### L2 human

Gauss called this result remarkable because $K$ was defined through the normal and the second fundamental form, which depend on how the surface sits in space.
The theorem shows that $K$ is intrinsic, and it is the starting point of Riemannian geometry, where curvature is defined from the metric alone.
In orthogonal coordinates, where $F = 0$, one has
$$K = -\frac{1}{2\sqrt{EG}} \left( \frac{\partial}{\partial u} \frac{G_u}{\sqrt{EG}} + \frac{\partial}{\partial v} \frac{E_v}{\sqrt{EG}} \right).$$
The mean curvature is not intrinsic: the plane and the cylinder are locally isometric but have $H = 0$ and $H \ne 0$.
