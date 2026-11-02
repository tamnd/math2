---
tag: QEEZEDBZ50
kind: statement
role: lemma
name: Narasimhan lemma
msc: [32T15]
uses: [Z7RVXBA2KB, 80MTNXWW80, FX92PP3HZR, SKE8QTW3YM]
about: [Z7RVXBA2KB]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Statement

Let $\Omega \subseteq \C^n$ be a domain with $C^2$ boundary, and let $p \in \partial\Omega$ be a [[strongly pseudoconvex|Z7RVXBA2KB]] point.
Then there is a [[biholomorphic map|FX92PP3HZR]] $\Phi$ from an open neighbourhood $U$ of $p$ onto an open subset of $\C^n$ with this property.
The set $\Phi(U \cap \Omega)$ is strictly convex.
That is, the hypersurface $\Phi(U \cap \partial\Omega)$ has a defining function whose real Hessian is positive definite on the real tangent space at each of its points.

## Remarks

The proof is a computation with the second-order Taylor expansion of a defining function $\rho$ at $p$.
After a complex-linear change of coordinates, $p = 0$ and $\rho(z) = 2\operatorname{Re}\big(z_n + \sum_{j,k} a_{jk} z_j z_k\big) + \sum_{j,k} \rho_{j\bar k}\, z_j \bar z_k + o(\abs{z}^2)$, where $(\rho_{j \bar k})$ is the [[Levi form|80MTNXWW80]] matrix.
The holomorphic quadratic change of coordinates $z_n' = z_n + \sum_{j,k} a_{jk} z_j z_k$, $z_j' = z_j$ for $j < n$, removes the pure terms $z_j z_k$, so the new real Hessian at $0$ is given by the Levi form matrix.
Strong pseudoconvexity makes it positive definite on the complex tangent space $\set{z_n = 0}$.
The real tangent space at $0$ also contains the direction of $\operatorname{Im} z_n$.
A further change $z_n' = z_n + c z_n^2 + \sum_{j < n} b_j z_j z_n$, with suitable constants $c$ and $b_j$, makes the Hessian positive definite on the whole real tangent space.
Positive definiteness at $p$ then persists at nearby boundary points, by continuity.
Example of use: local holomorphic peak functions at $p$ are obtained from linear functions in the convex coordinates.
This is the first step towards the fact that every boundary point of a strongly pseudoconvex domain is a peak point.
Without strong pseudoconvexity the lemma fails.
If the boundary contains a complex disc, its image under a biholomorphic map is a complex disc in the new boundary, and a strictly convex hypersurface contains no such disc.

## Explanations

### L1 human

Strong pseudoconvexity is a complex form of strict convexity, and it is preserved by holomorphic changes of coordinates, whereas convexity is not.
The lemma says that the two notions agree locally: near each strongly pseudoconvex boundary point, one can bend the coordinates holomorphically so that the domain becomes strictly convex there.
So local problems at such points can be solved with the tools of convex geometry.

### L2 human

The lemma is used to build local [[peak functions|SKE8QTW3YM]] and local holomorphic support functions, and to construct integral kernels, such as the Henkin–Ramírez kernels, near strongly pseudoconvex boundaries.
It does not extend to weakly pseudoconvex points.
Kohn and Nirenberg gave a pseudoconvex domain in $\C^2$ with a boundary point near which no holomorphic coordinate change makes the domain convex.
Globally the lemma also fails: a strongly pseudoconvex domain need not be biholomorphic to a convex domain, for instance because it need not be contractible, while convex domains are.
