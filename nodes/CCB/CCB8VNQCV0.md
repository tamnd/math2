---
tag: CCB8VNQCV0
kind: statement
role: theorem
name: Witt's theorem
aliases: [witt-extension-theorem]
msc: ["11E04", "15A63"]
topics: [DYAK7YMK7B]
audience: grad
uses: [0ZHWKQMVX5, 0AXZNE5XNH, 01NHFZF2SK, 00YC1D652K, 0F6ES3BRYP, MZHFGPV1YT, 43VKGAA2H7]
about: [0AXZNE5XNH, 0RBQS1JJCR]
sources:
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
    locator: Witt's cancellation theorem
  - book: isbn:9780387728285
    locator: Chapter 11
same_as:
  wikidata: Q8028529
  wikipedia: Witt's theorem
---

## Statement

Let $F$ be a field whose [[characteristic|0F6ES3BRYP]] is not $2$.
Let $V$ be a [[finite-dimensional vector space|0ZHWKQMVX5]] over $F$ with a [[nondegenerate|01NHFZF2SK]] [[symmetric bilinear form|0AXZNE5XNH]] $B$.

1. (Witt extension.) Let $U$ and $W$ be [[linear subspaces|00YC1D652K]] of $V$, and let $\sigma \colon U \to W$ be a linear bijection with $B(\sigma(x), \sigma(y)) = B(x, y)$ for all $x, y \in U$. Then there is a linear bijection $\tau \colon V \to V$ with $B(\tau(x), \tau(y)) = B(x, y)$ for all $x, y \in V$ and $\tau(x) = \sigma(x)$ for all $x \in U$.
2. Let $W_1, W_2$ be [[totally isotropic|MZHFGPV1YT]] subspaces of $V$ with $\dim W_1 = \dim W_2$. Then there is an isometry $\tau$ of $V$ with $\tau(W_1) = W_2$.

The subspaces $U$ and $W$ in part 1 may be degenerate.
The [[proof|XRXMHP9Z76]] enlarges $U$ until the form on it is nondegenerate, and then applies the [[reflection lemma|43VKGAA2H7]].

## Remarks

### Why each hypothesis is needed

The hypothesis on the characteristic is necessary for symmetric forms.
Over $\mathbb{F}_2$, take $V = \mathbb{F}_2^3$ with the dot product, $u = (1, 1, 1)$ and $e_1 = (1, 0, 0)$.
Both have $B(x, x) = 1$, so $e_1 \mapsto u$ is an isometry between lines.
An extension to $V$ would map the orthogonal complement of $e_1$ onto that of $u$.
But the complement of $e_1$ contains $(0, 1, 0)$ with $B(x, x) = 1$, while every $x$ in the complement of $u$ has $B(x, x) = x_1 + x_2 + x_3 = 0$.

Nondegeneracy of $B$ on $V$ is necessary.
Let $B(x, y) = x_1 y_1 - x_2 y_2$ on $F^3$, with radical $\operatorname{span}(e_3)$, and let $U = \operatorname{span}(e_3)$ and $W = \operatorname{span}(e_1 + e_2)$.
Both lines carry the zero form, so $e_3 \mapsto e_1 + e_2$ is an isometry.
But each isometry of $V$ maps the radical to itself, and $e_1 + e_2$ is not in the radical.

Finite dimension is used in the proof, in the dimension formula for orthogonal complements.

### Consequences

- Witt cancellation: if $V_1 \perp V_2$ and $V_1 \perp V_3$ are isometric and $V_1, V_2, V_3$ are nondegenerate, then $V_2$ and $V_3$ are isometric. The [[reflection lemma|43VKGAA2H7]] proves this directly.
- All maximal totally isotropic subspaces of $V$ have the same dimension, the Witt index, and by part 2 the isometry group acts transitively on them. The [[Witt decomposition|BPMRSPB6GD]] also gives the first claim.
- For example, in $\R^n$ with the dot product, any isometric map between two subspaces extends to an orthogonal map of $\R^n$.
- Two vectors $x, y$ with $B(x, x) = B(y, y)$, both nonzero, lie in one orbit of the isometry group. This holds also when $B(x, x) = 0$.

### Converse

The extension $\tau$ is an isometry of $V$, so its restriction to $U$ is an isometry onto $W$.
So part 1 describes exactly the maps $U \to W$ that come from isometries of $V$.
The extension is not unique.
For $U = \{0\}$, each isometry of $V$ extends $\sigma$.

### Generalizations

The theorem holds in every characteristic for nondegenerate [[alternating forms|0DGDS5XY84]].
It also holds for nondegenerate Hermitian forms.

## Explanations

### L1 human

A symmetric bilinear form measures something like lengths and angles, possibly with signs.
Witt's theorem says that if two configurations of vectors look the same for the form, then a symmetry of the whole space carries one onto the other.
So the symmetries of the form can carry any configuration onto any other configuration that the form cannot tell apart.

### L2 human

Witt's theorem is the foundation of the algebraic theory of [[quadratic forms|0RBQS1JJCR]].
We extend a map between degenerate lines in $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$ on $\Q^3$.

1. Let $U = \operatorname{span}(e_1 + e_3)$ and $W = \operatorname{span}(e_2 + e_3)$. Both lines are totally isotropic, so $\sigma(e_1 + e_3) = e_2 + e_3$ is an isometry.
2. The swap $\tau(x_1, x_2, x_3) = (x_2, x_1, x_3)$ keeps $B$, and $\tau(e_1 + e_3) = e_2 + e_3$. So $\tau$ extends $\sigma$.
3. A second extension is $\tau'(x_1, x_2, x_3) = (-x_2, x_1, x_3)$, a rotation in the $(x_1, x_2)$-plane, with $\tau'(e_1 + e_3) = e_2 + e_3$.

Cancellation reduces the classification of forms to anisotropic forms plus a number of hyperbolic planes, the Witt decomposition.
This decomposition leads to the [[Witt group|KFVY0RPGF2]] of a field.
For real forms, cancellation gives a short proof of Sylvester's law of inertia.
The theorem is named after Ernst Witt.
