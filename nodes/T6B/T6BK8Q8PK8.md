---
tag: T6BK8Q8PK8
kind: statement
role: theorem
name: Mather's stability theorem
msc: [58K25, 57R45]
uses: [1991WETZF9, C3TFCVE2YK, F45VQ47GPV, 2A5HZZRGFT]
about: [1991WETZF9, C3TFCVE2YK]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Statement

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]] and let $f \colon M \to N$ be a proper smooth map.
Then $f$ is [[stable|1991WETZF9]] if and only if $f$ is [[infinitesimally stable|C3TFCVE2YK]].

## Remarks

Mather proved the theorem in a series of papers on the stability of smooth mappings.
The proof that infinitesimal stability implies stability joins $f$ to a nearby map $g$ by a smooth path $f_t$ and seeks families of diffeomorphisms $\varphi_t$, $\psi_t$ with $f_t = \psi_t \circ f \circ \varphi_t^{-1}$.
Differentiating in $t$ gives an equation of the same form as in the definition of infinitesimal stability.
The [[Malgrange preparation theorem|2A5HZZRGFT]] is used to solve it for all $t$, not only for $t = 0$.
Example: for a compact $M$, a function $f \colon M \to \R$ is infinitesimally stable exactly when its critical points are nondegenerate with distinct critical values, so these functions are the stable ones.
When $M$ is compact every smooth map $M \to N$ is proper, so the theorem applies to all of them.
Mather also showed that infinitesimal stability can be checked on finite jets at finite sets of points.
He determined the pairs of dimensions for which stable maps are dense in $C^\infty(M, N)$; they are not dense in general.

## Explanations

### L1 human

Stability asks that every nearby map be the same map in new coordinates, which is hard to check directly.
Infinitesimal stability asks only that every tiny push of the map be undone by tiny changes of coordinates, which is a linear equation.
Mather's theorem says that, for proper maps, the easy linear test decides the hard question.

### L2 human

The theorem is the foundation of the modern theory of stable maps.
It reduces stability to the local algebra of germs, where finite determinacy and the preparation theorem make computations finite.
With it, one shows that the fold and cusp of maps of the plane, the cross-cap of maps from the plane to space, and the [[Morin singularities|DF8CJ1A9MF]] are stable.
