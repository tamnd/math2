---
tag: AR52AWP2XE
kind: definition
name: Leray–Schauder method
msc: [47H11, 45G10, 47H10]
defines: QGRBR04JJN
uses: [06GZ956657, 3VJC5Q9MYA, 0R6EWFKRCF, 0X3WGX95FE, 7H3YSSDEBK]
sources:
  - url: https://en.wikipedia.org/wiki/Leray%E2%80%93Schauder_degree
---

## Definition

Let $X$ be a real [[Banach space|06GZ956657]].
A [[continuous|0X3WGX95FE]] map $T \colon [0, 1] \times X \to X$ is *compact* if it maps bounded sets to sets with [[compact|0R6EWFKRCF]] closure.
The *Leray–Schauder method* for an equation $u = F(u)$ in $X$ consists of the following steps.

1. Choose a compact map $T \colon [0, 1] \times X \to X$ with $T(1, \cdot) = F$ and $T(0, \cdot) = 0$.
2. Prove an a priori bound: there is $R > 0$ such that every solution of $u = T(\lambda, u)$ with $\lambda \in [0, 1]$ satisfies $\norm{u} < R$.
3. Conclude by the homotopy invariance of the [[Leray–Schauder degree|3VJC5Q9MYA]] on the ball $B_R = \set{u : \norm{u} < R}$:
$$\deg\bigl(I - T(1, \cdot), B_R, 0\bigr) = \deg\bigl(I - T(0, \cdot), B_R, 0\bigr) = \deg(I, B_R, 0) = 1,$$
so $u = F(u)$ has a solution in $B_R$.

## Remarks

Step 2 guarantees that no solution lies on the boundary of $B_R$ for any $\lambda$, which is what homotopy invariance needs.
The form with $T(\lambda, u) = \lambda F(u)$ is the Leray–Schauder alternative, also known as [[Schaefer's fixed point theorem|7H3YSSDEBK]]: either the set of solutions of $u = \lambda F(u)$, $0 \le \lambda \le 1$, is unbounded, or $u = F(u)$ has a solution.

Example: in $X = C[0, 1]$, let $F(u)(x) = \int_0^1 k(x, t)\, \arctan u(t)\, dt$ with $k$ continuous.
Then $F$ is compact by the Arzelà–Ascoli theorem.
Any solution of $u = \lambda F(u)$ with $0 \le \lambda \le 1$ satisfies $\norm{u}_\infty \le \frac{\pi}{2} \max \abs{k}$, since $\abs{\arctan} < \frac{\pi}{2}$.
So $R = \frac{\pi}{2} \max \abs{k} + 1$ works, and $u = F(u)$ has a continuous solution.

Non-example: in an infinite-dimensional space, without compactness, step 3 has no meaning.
For instance, $T(\lambda, u) = \lambda u$ on the unit ball of $\ell^2$ is not compact, and the Leray–Schauder degree of $I - T(\lambda, \cdot)$ is not defined.
