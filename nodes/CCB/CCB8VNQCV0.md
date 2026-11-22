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

Outside characteristic $2$, every isometry between two subspaces of a nondegenerate symmetric space extends to an isometry of the whole space, even when the subspaces are degenerate.

Let $F$ be a field whose [[characteristic|0F6ES3BRYP]] is not $2$.
Let $V$ be a [[finite-dimensional vector space|0ZHWKQMVX5]] over $F$ with a [[nondegenerate|01NHFZF2SK]] [[symmetric bilinear form|0AXZNE5XNH]] $B$.

1. (Witt extension.) Let $U$ and $W$ be [[linear subspaces|00YC1D652K]] of $V$, and let $\sigma \colon U \to W$ be a linear bijection with $B(\sigma(x), \sigma(y)) = B(x, y)$ for all $x, y \in U$. Then there is a linear bijection $\tau \colon V \to V$ with $B(\tau(x), \tau(y)) = B(x, y)$ for all $x, y \in V$ and $\tau(x) = \sigma(x)$ for all $x \in U$.
2. Let $W_1, W_2$ be [[totally isotropic|MZHFGPV1YT]] subspaces of $V$ with $\dim W_1 = \dim W_2$. Then there is an isometry $\tau$ of $V$ with $\tau(W_1) = W_2$.

The subspaces $U$ and $W$ in part 1 may be degenerate.
The [[proof|XRXMHP9Z76]] enlarges $U$ until the form on it is nondegenerate, and then applies the [[reflection lemma|43VKGAA2H7]].

## Remarks

### A first extension

On $\mathbb{Q}^3$ take $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$.
Let $U = \operatorname{span}(e_1 + e_3)$ and $W = \operatorname{span}(e_2 + e_3)$.
Both lines are totally isotropic, since $1 - 1 = 0$, so $\sigma(e_1 + e_3) = e_2 + e_3$ is an isometry, although $U$ and $W$ are degenerate.
The swap $\tau(x_1, x_2, x_3) = (x_2, x_1, x_3)$ keeps $B$ and sends $e_1 + e_3$ to $e_2 + e_3$, so it extends $\sigma$.
Check: $B(\tau x, \tau y) = x_2 y_2 + x_1 y_1 - x_3 y_3 = B(x, y)$.

### Why each hypothesis is needed

The characteristic must not be $2$.
Over $\mathbb{F}_2$, take $V = \mathbb{F}_2^3$ with the dot product, $e_1 = (1, 0, 0)$ and $u = (1, 1, 1)$.
Both have $B(x, x) = 1$, so $e_1 \mapsto u$ is an isometry between lines.
An extension to $V$ would map the orthogonal complement of $e_1$ onto that of $u$.
But the complement of $e_1$ contains $e_2$ with $B(e_2, e_2) = 1$, while every $x$ in the complement of $u$ has $B(x, x) = x_1 + x_2 + x_3 = 0$.

Nondegeneracy of $B$ on $V$ is needed.
Let $B(x, y) = x_1 y_1 - x_2 y_2$ on $F^3$, with radical $\operatorname{span}(e_3)$, and let $U = \operatorname{span}(e_3)$ and $W = \operatorname{span}(e_1 + e_2)$.
Both lines carry the zero form, so $e_3 \mapsto e_1 + e_2$ is an isometry.
But each isometry of $V$ maps the radical to itself, and $e_1 + e_2$ is not in the radical.

Finite dimension is used in the proof, through the dimension formula for orthogonal complements.

### What it gives you

Witt cancellation follows: if $V_1 \perp V_2 \cong V_1 \perp V_3$ with all three nondegenerate, then $V_2 \cong V_3$, and the [[reflection lemma|43VKGAA2H7]] already proves this case.
All maximal totally isotropic subspaces have the same dimension, the Witt index of the [[Witt decomposition|BPMRSPB6GD]].
To see this, take maximal $W_1, W_2$ with $\dim W_1 \leq \dim W_2$, and extend a linear injection $W_1 \to W_2$, which is an isometry because both forms are zero, to an isometry $\tau$ of $V$ by part 1.
Then $\tau^{-1}(W_2)$ is totally isotropic and contains $W_1$, so it equals $W_1$ by maximality, and $\dim W_1 = \dim W_2$.
By part 2, the isometry group then acts transitively on these subspaces.
Two nonzero vectors $x, y$ with $B(x, x) = B(y, y)$ lie in one orbit of the isometry group, and this includes the isotropic case $B(x, x) = 0$.
For $\mathbb{R}^n$ with the dot product, every map between two subspaces that keeps the dot product extends to an orthogonal map of $\mathbb{R}^n$.

### The converse

An isometry $\tau$ of $V$ restricts to an isometry from $U$ onto $\tau(U)$.
So part 1 describes exactly the maps between subspaces that come from isometries of $V$.

### Generalizations

The theorem holds in every characteristic for nondegenerate [[alternating forms|0DGDS5XY84]].
It also holds for nondegenerate Hermitian forms.

### Watch out

The extension is not unique.
In the first example, $\tau'(x_1, x_2, x_3) = (-x_2, x_1, x_3)$ also keeps $B$ and sends $(1, 0, 1)$ to $(0, 1, 1)$.
For $U = \{0\}$, every isometry of $V$ extends $\sigma$.

### Try it

In the first example, find a reflection that sends the isotropic vector $x = (1, 0, 1)$ to the isotropic vector $y = (3, 4, 5)$.
Answer: $w = x - y = (-2, -4, -4)$ has $B(w, w) = 4 + 16 - 16 = 4$ and $B(x, w) = -2 + 4 = 2$.
So the coefficient $2 B(x, w) / B(w, w)$ is $1$, and $\tau_w(x) = x - w = y$.

## History

Ernst Witt proved the extension theorem and the cancellation theorem in 1937, in his paper "Theorie der quadratischen Formen in beliebigen Körpern".

## Explanations

### L1 human

A symmetric bilinear form measures something like lengths and angles, possibly with signs.
Witt's theorem says that if two configurations of vectors look the same to the form, then a symmetry of the whole space carries one onto the other.
In other words, the only thing that can stop you from moving one configuration onto another is a difference that the form itself detects.

### L2 human

Here is a typical use: the orbit of an isotropic vector.
In $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$ on $\mathbb{Q}^3$, the vectors $(1, 0, 1)$ and $(3, 4, 5)$ are both isotropic and nonzero.
The map $\operatorname{span}(1, 0, 1) \to \operatorname{span}(3, 4, 5)$ with $(1, 0, 1) \mapsto (3, 4, 5)$ is an isometry, since both lines carry the zero form.
Part 1 extends it to an isometry of $\mathbb{Q}^3$.
So all nonzero isotropic vectors of this form lie in one orbit, and the cone $x_1^2 + x_2^2 = x_3^2$ minus the origin is a single orbit of the isometry group.

### L3 human

Witt's theorem is the foundation of the algebraic theory of [[quadratic forms|0RBQS1JJCR]].
Cancellation reduces the classification of forms to anisotropic forms plus a number of hyperbolic planes, which leads to the [[Witt group|KFVY0RPGF2]] of a field.
For real forms, cancellation gives a short proof of [[Sylvester's law of inertia|0WFED3K3DQ]].
By part 2, the stabilizers in the orthogonal group of any two maximal totally isotropic subspaces are conjugate.
