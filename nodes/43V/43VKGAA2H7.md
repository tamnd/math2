---
tag: 43VKGAA2H7
kind: statement
role: lemma
name: Reflections and Witt cancellation
aliases: [witt-cancellation, witt-cancellation-theorem, reflection-in-an-anisotropic-vector]
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
about: [0AXZNE5XNH, 01NHFZF2SK]
uses: [0AXZNE5XNH, 0KAN330PAH, 0F6ES3BRYP, MZHFGPV1YT, 05Q4JD6XEH, M2JH84VEY9]
sources:
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
    locator: Witt's cancellation theorem
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Statement

Reflections move any vector to any other vector with the same nonzero value $B(v, v)$, and from this, equal nondegenerate pieces can be cancelled from both sides of an isometry.

Let $F$ be a field with [[characteristic|0F6ES3BRYP]] not $2$.
Let $V$ be a finite-dimensional vector space over $F$ with a [[nondegenerate|0KAN330PAH]] [[symmetric bilinear form|0AXZNE5XNH]] $B$.
An *isometry* of $V$ is a linear bijection $\tau \colon V \to V$ with $B(\tau x, \tau y) = B(x, y)$ for all $x, y$.
For $w \in V$ with $B(w, w) \neq 0$, the *reflection* in $w$ is
$$\tau_w(x) = x - \frac{2 B(x, w)}{B(w, w)} \, w.$$
Write $\langle a \rangle$ for the line $F$ with the form $B(x, y) = a x y$, and $V_1 \perp V_2$ for the orthogonal direct sum of two spaces with forms.

1. Each reflection $\tau_w$ is an isometry of $V$, with $\tau_w(w) = -w$ and $\tau_w(x) = x$ for every $x \in w^\perp$.
2. If $x, y \in V$ and $B(x, x) = B(y, y) \neq 0$, then there is an isometry $\tau$ of $V$ with $\tau(x) = y$, and $\tau$ is one reflection or a product of two reflections.
3. Let $U, U'$ be subspaces of $V$ on which $B$ is nondegenerate, and let $\sigma \colon U \to U'$ be a linear bijection with $B(\sigma x, \sigma y) = B(x, y)$ for all $x, y \in U$. Then $\sigma$ extends to an isometry of $V$.
4. (Witt cancellation.) Let $V_1, V_2, V_3$ be finite-dimensional spaces over $F$ with nondegenerate symmetric forms. If $V_1 \perp V_2$ is isometric to $V_1 \perp V_3$, then $V_2$ is isometric to $V_3$.

The [[proof|WMK89ZW2WZ]] checks part 1 by expansion, reduces part 2 to a choice between $x - y$ and $x + y$, and proves part 3 by induction on $\dim U$.

## Remarks

### A reflection with numbers

On $\mathbb{Q}^2$ take $B(x, y) = x_1 y_1 - x_2 y_2$, and move $x = (1, 0)$ onto $y = (\tfrac{5}{3}, \tfrac{4}{3})$.
Both have value $1$, since $B(y, y) = \tfrac{25}{9} - \tfrac{16}{9} = 1$.
Reflect in $w = x - y = (-\tfrac{2}{3}, -\tfrac{4}{3})$, which has $B(w, w) = \tfrac{4}{9} - \tfrac{16}{9} = -\tfrac{4}{3} \neq 0$.
Since $B(x, w) = -\tfrac{2}{3}$, the coefficient is
$$\frac{2 B(x, w)}{B(w, w)} = \frac{-4/3}{-4/3} = 1, \qquad \text{so} \qquad \tau_w(x) = x - w = y.$$
Check: $B(y, w) = -\tfrac{10}{9} + \tfrac{16}{9} = \tfrac{2}{3}$, so the coefficient for $y$ is $-1$ and $\tau_w(y) = y + w = x$; the reflection swaps the two vectors.

### Why each hypothesis is needed

The characteristic must not be $2$.
In characteristic $2$ the coefficient $2 B(x, w) / B(w, w)$ is $0$, so $\tau_w$ is the identity and moves nothing.
Part 4 also fails in characteristic $2$.
Over $\mathbb{F}_2$, the form $\langle 1 \rangle \perp \langle 1 \rangle \perp \langle 1 \rangle$ is isometric to $\langle 1 \rangle \perp H$, where $H$ has the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
To see it, take $e_1 + e_2 + e_3$, with value $1$, and the vectors $e_1 + e_2$ and $e_2 + e_3$ of its complement, which have values $0$, $0$ and mutual value $1$.
But $\langle 1 \rangle \perp \langle 1 \rangle$ is not isometric to $H$, because $B(v, v) = 0$ for every $v$ in $H$ and $B(e_1, e_1) = 1$ in $\langle 1 \rangle \perp \langle 1 \rangle$.

The condition $B(w, w) \neq 0$ is needed, since the formula divides by it, so there is no reflection in an [[isotropic vector|MZHFGPV1YT]].
In part 3, nondegeneracy on $U$ is a hypothesis of this lemma only, and [[Witt's theorem|CCB8VNQCV0]] removes it.

### What it gives you

Cancellation gives the uniqueness of the anisotropic part in the [[Witt decomposition|BPMRSPB6GD]].
It also gives the uniqueness part of [[Sylvester's law of inertia|0WFED3K3DQ]] over $\mathbb{R}$.
Suppose that $p \langle 1 \rangle \perp q \langle -1 \rangle \cong p' \langle 1 \rangle \perp q' \langle -1 \rangle$ with $p + q = p' + q'$ and $p \leq p'$.
Cancel $p$ copies of $\langle 1 \rangle$ to get $q \langle -1 \rangle \cong (p' - p) \langle 1 \rangle \perp q' \langle -1 \rangle$.
The left side is negative definite, and the right side has a vector with value $1$ unless $p' = p$, so $p = p'$.

### The converse

Part 2 has a converse: if an isometry $\tau$ has $\tau(x) = y$, then $B(y, y) = B(\tau x, \tau x) = B(x, x)$.
So for a single anisotropic vector, its value $B(x, x)$ is the only invariant under isometries.

### Generalizations

The [[Cartan-Dieudonné theorem|0VMWGYY35Q]] says that every isometry of $V$ is a product of at most $\dim V$ reflections.
[[Witt's theorem|CCB8VNQCV0]] extends part 3 to all subspaces $U$, degenerate or not.

### Watch out

The reflection in $x - y$ does not always exist, since $x - y$ can be isotropic.
On $\mathbb{Q}^3$ with $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$, take $x = e_1$ and $y = e_1 + e_2 + e_3$, both of value $1$.
Then $x - y = -(e_2 + e_3)$ has value $1 - 1 = 0$, so $\tau_{x - y}$ is not defined.
Use $x + y = (2, 1, 1)$ instead, with value $4 + 1 - 1 = 4$ and $B(x, x + y) = 2$.
So $\tau_{x + y}(x) = x - \tfrac{2 \cdot 2}{4}(x + y) = -y$, and then $\tau_y(-y) = y$.
Check: the two reflections $\tau_y \circ \tau_{x + y}$ send $x$ to $y$, as part 2 promises.

### Try it

On $\mathbb{Q}^2$ with the dot product, find a reflection that sends $(1, 0)$ to $(\tfrac{3}{5}, \tfrac{4}{5})$.
Answer: $w = (\tfrac{2}{5}, -\tfrac{4}{5})$ has $B(w, w) = \tfrac{4}{5}$ and $B((1, 0), w) = \tfrac{2}{5}$, so the coefficient is $1$ and $\tau_w(1, 0) = (1, 0) - w = (\tfrac{3}{5}, \tfrac{4}{5})$.

## Explanations

### L1 human

A reflection flips one direction and keeps every direction that is orthogonal to it.
In the plane with the dot product, the reflection in $w = (1, -1)$ fixes the line $x_1 = x_2$ and swaps $(1, 0)$ and $(0, 1)$.
For any symmetric form, two vectors with the same nonzero value $B(v, v)$ can be moved onto each other by one or two reflections.
From this, a matching between two nondegenerate subspaces extends to the whole space, and equal pieces can be cancelled.

### L2 human

Here is a typical use: the induction step in the proof of Witt's theorem.
Given an isometry $\sigma$ from a nondegenerate subspace $U$ onto $U'$, pick $u \in U$ with $B(u, u) \neq 0$.
Part 2 gives an isometry $\rho$ of $V$ with $\rho(u) = \sigma(u)$.
Then $\rho^{-1} \sigma$ fixes $u$, and the problem moves into the orthogonal complement of $u$, which has smaller dimension.
In the example above, with $u = (1, 0)$ and $\sigma(u) = (\tfrac{5}{3}, \tfrac{4}{3})$, the single reflection $\tau_w$ is the $\rho$ you need.

### L3 human

The reflections generate the orthogonal group $O(V)$, by the Cartan-Dieudonné theorem, and the spinor norm and the determinant of an isometry are read off a product of reflections.
Witt cancellation makes the isometry classes of nondegenerate forms a cancellative monoid under $\perp$.
Its group of differences, divided by the subgroup generated by the hyperbolic plane, is the [[Witt group|KFVY0RPGF2]] of $F$.
