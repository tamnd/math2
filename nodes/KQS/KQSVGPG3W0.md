---
tag: KQSVGPG3W0
kind: definition
name: Monodromy of the hypergeometric equation
msc: ["33C05", "34M35"]
defines: T8SBE28DM1
uses: [W8VE25R5A7, S1XK3HXHFX, 0M3YQJ81NB, WYGRXCG2RN, C8HD62AB6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Definition

Let $a, b, c \in \C$, let $X = \C \setminus \set{0, 1}$, and fix a base point $z_0 \in X$.
Let $V$ be the two-dimensional complex vector space of solutions of the [[hypergeometric differential equation|W8VE25R5A7]] on a small disc around $z_0$.
For a loop $\gamma$ in $X$ based at $z_0$, [[analytic continuation|0M3YQJ81NB]] of each solution along $\gamma$ gives a solution near $z_0$ again.
This defines a linear map $M_\gamma \colon V \to V$ that depends only on the homotopy class of $\gamma$.
The *monodromy representation* of the equation is the [[group representation|WYGRXCG2RN]]
$$\rho \colon \pi_1(X, z_0) \to \mathrm{GL}(V), \qquad [\gamma] \mapsto M_\gamma,$$
of the [[fundamental group|S1XK3HXHFX]], with the convention that makes $\rho$ a homomorphism.
Its image is the *monodromy group* of the equation, defined up to conjugation in $\mathrm{GL}_2(\C)$.

## Remarks

The group $\pi_1(X, z_0)$ is free on the classes $\gamma_0$, $\gamma_1$ of simple loops around $0$ and $1$, so $\rho$ is determined by the two matrices $M_{\gamma_0}$ and $M_{\gamma_1}$.
The eigenvalues of $M_{\gamma_0}$ are $1$ and $e^{2\pi i(1 - c)}$, and those of $M_{\gamma_1}$ are $1$ and $e^{2\pi i(c - a - b)}$.
A loop around $\infty$, positively oriented in the coordinate $1/z$, has eigenvalues $e^{2\pi i a}$ and $e^{2\pi i b}$.

Example: for $a = b = 1$, $c = 2$, the solutions near $z_0$ are spanned by $w_1 = 1/z$ and $w_2 = \log(1 - z)/z$, as a direct check in the equation shows.
Both are single-valued near $0$, so $M_{\gamma_0}$ is the identity.
Around $1$, $\log(1 - z)$ changes by $\pm 2\pi i$, so in the basis $(w_1, w_2)$ the matrix $M_{\gamma_1}$ is $\begin{pmatrix} 1 & \pm 2\pi i \\ 0 & 1 \end{pmatrix}$, with the sign fixed by the orientation.
Here the monodromy group is infinite cyclic.

Non-example: continuation along a path from $z_0$ to a different point $z_1$ does not give an element of the monodromy group.
It maps solutions near $z_0$ to solutions near $z_1$, which is a different space.

This is a special case of the general notion of [[monodromy|C8HD62AB6Q]] of a linear differential equation.
