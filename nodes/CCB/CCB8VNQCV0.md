---
tag: CCB8VNQCV0
kind: statement
role: theorem
name: Witt's theorem
msc: ["11E04", 15A63]
uses: [0ZHWKQMVX5, 0AXZNE5XNH, 01NHFZF2SK, 00YC1D652K, 0F6ES3BRYP]
about: [0AXZNE5XNH, 0RBQS1JJCR]
sources:
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
same_as:
  wikidata: Q8028529
  wikipedia: Witt's theorem
---

## Statement

Let $F$ be a field whose [[characteristic|0F6ES3BRYP]] is not $2$.
Let $V$ be a [[finite-dimensional vector space|0ZHWKQMVX5]] over $F$ with a [[nondegenerate|01NHFZF2SK]] [[symmetric bilinear form|0AXZNE5XNH]] $B$.
Let $U$ and $W$ be [[linear subspaces|00YC1D652K]] of $V$, and let $\sigma \colon U \to W$ be a linear bijection with $B(\sigma(x), \sigma(y)) = B(x, y)$ for all $x, y \in U$.
Then there is a linear bijection $\tau \colon V \to V$ with $B(\tau(x), \tau(y)) = B(x, y)$ for all $x, y \in V$ and $\tau(x) = \sigma(x)$ for all $x \in U$.

## Remarks

The usual proof is by induction on $\dim U$, and it builds $\tau$ as a product of reflections in non-isotropic vectors; dividing by $2$ is needed to write these reflections.
A consequence is Witt cancellation: if $V_1 \perp V_2$ and $V_1 \perp V_3$ are isometric and $V_1, V_2, V_3$ are nondegenerate, then $V_2$ and $V_3$ are isometric.
Another consequence: all maximal totally isotropic subspaces of $V$ have the same dimension, the Witt index.
For example, in $\R^n$ with the dot product, any isometric map between two subspaces extends to an orthogonal map of $\R^n$.

The hypothesis on the characteristic is necessary for symmetric forms.
Over $\F_2$, take $V = \F_2^3$ with the dot product, $u = (1,1,1)$ and $e_1 = (1,0,0)$; both have $B(x,x) = 1$, so $e_1 \mapsto u$ is an isometry between lines.
An extension to $V$ would map the orthogonal complement of $e_1$ onto that of $u$.
But the complement of $e_1$ contains $(0,1,0)$ with $B(x,x) = 1$, while every $x$ in the complement of $u$ has $B(x,x) = x_1 + x_2 + x_3 = 0$.
The theorem holds in every characteristic for nondegenerate [[alternating forms|0DGDS5XY84]] and for quadratic forms with nondegenerate polar form.

## Explanations

### L1 human

A symmetric bilinear form measures something like lengths and angles, possibly with signs.
Witt's theorem says that if two configurations of vectors look the same for the form, then a symmetry of the whole space carries one onto the other.
So the symmetries of the form can carry any configuration onto any other configuration that the form cannot tell apart.

### L2 human

Witt's theorem is the foundation of the algebraic theory of [[quadratic forms|0RBQS1JJCR]].
Cancellation reduces the classification of forms to anisotropic forms plus a number of hyperbolic planes, the Witt decomposition.
This decomposition leads to the [[Witt group|KFVY0RPGF2]] of a field.
For real forms, cancellation gives a short proof of Sylvester's law of inertia.
