---
tag: 4NJC7AGT5N
kind: statement
role: lemma
name: Kalman–Yakubovich–Popov lemma
msc: [93D10, 93C05, 15A39]
uses: [Y8ZT5NXZ7V, 86JKV3TRFD, A9WFM77Z4P, C4HN3EAQWM, 0KX66CZMBB, 0VR671PHE5]
about: [Y8ZT5NXZ7V]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman%E2%80%93Yakubovich%E2%80%93Popov_lemma
same_as:
  wikidata: Q6354030
  wikipedia: Kalman–Yakubovich–Popov lemma
---

## Statement

Let $A$ be a real $n \times n$ matrix, $b \in \R^{n \times 1}$, $c \in \R^{1 \times n}$ and $d \in \R$, and let $G(s) = c(sI - A)^{-1} b + d$ be the [[transfer function|86JKV3TRFD]] of the system $x' = Ax + bu$, $y = cx + du$.
Assume that $(A, b)$ is [[controllable|A9WFM77Z4P]] and $(A, c)$ is [[observable|C4HN3EAQWM]].
Then $G$ is [[positive real|Y8ZT5NXZ7V]] if and only if there are the following data.
These are a [[symmetric|0VR671PHE5]] [[positive definite|0KX66CZMBB]] $n \times n$ matrix $P$, an integer $k \ge 1$, a matrix $L \in \R^{k \times n}$ and a vector $w \in \R^{k}$.
They must satisfy
$$P A + A^T P = -L^T L, \qquad P b = c^T - L^T w, \qquad w^T w = 2d.$$

## Remarks

This is the positive real form of the lemma, also called the positive real lemma; the same holds for square multi-input multi-output systems with $D + D^T$ in place of $2d$.
For the "if" direction, $V(x) = \frac{1}{2} x^T P x$ satisfies $\frac{d}{dt} V = uy - \frac{1}{2}\abs{Lx + wu}^2 \le uy$ along solutions.
So the system is passive, and passivity of a linear system forces $G$ to be positive real.
The "only if" direction is the deep part: it builds $P$ from a spectral factorization of $G(s) + G(-s)$, and this uses controllability and observability.
A more general form of the lemma assumes only that $(A, b)$ is controllable.
It states that a frequency-domain inequality on the imaginary axis holds if and only if a related linear matrix inequality in a symmetric matrix $P$ has a solution.

Example: $A = -1$, $b = c = 1$, $d = 0$, so $G(s) = 1/(s + 1)$, which is positive real.
Take $P = 1$, $k = 1$, $L = \sqrt{2}$ and $w = 0$: then $PA + A^T P = -2 = -L^2$, $Pb = 1 = c - Lw$ and $w^2 = 0 = 2d$.

## Explanations

### L1 human

There are two ways to say that a linear system cannot create energy.
One looks at its frequency response and asks that its real part is never negative.
The other asks for a quadratic energy function of the state that never grows faster than the power put in.
The lemma says that the two are the same, for systems without hidden parts.

### L2 human

The lemma is the bridge between frequency-domain and state-space methods in nonlinear and robust control.
It is the key step in the proofs of the circle criterion and the Popov criterion.
There, a frequency inequality on the linear part gives a quadratic Lyapunov function for the whole loop.
A frequency-domain inequality must hold at infinitely many frequencies.
The general form of the lemma turns it into one linear matrix inequality, which can be checked by convex optimization.
