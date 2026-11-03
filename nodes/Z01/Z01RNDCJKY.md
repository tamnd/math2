---
tag: Z01RNDCJKY
kind: definition
name: Self-concordant function
msc: [90C25, 90C51]
defines: N4Q5T33P33
uses: [07Q7CNM5WF, 02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Self-concordant_function
---

## Definition

Let $U \subseteq \R^n$ be a nonempty open [[convex set|02AS45T3H9]].
A function $f \colon U \to \R$ is *self-concordant* if:

1. $f$ is [[convex|07Q7CNM5WF]] and three times continuously differentiable on $U$.
2. For every $x \in U$ and every $h \in \R^n$,
$$\abs{D^3 f(x)[h, h, h]} \le 2 \left( D^2 f(x)[h, h] \right)^{3/2}.$$

Here $D^k f(x)[h, \dots, h]$ is the $k$-th derivative of $t \mapsto f(x + th)$ at $t = 0$.

## Remarks

Equivalently, for every $x \in U$ and $h \in \R^n$, the function $\phi(t) = f(x + th)$ satisfies $\abs{\phi'''(t)} \le 2 \phi''(t)^{3/2}$ wherever it is defined.
Many authors, following Nesterov and Nemirovski, also ask that $f$ be closed: $f(x_k) \to +\infty$ whenever $x_k$ tends to a boundary point of $U$.
The condition is invariant under affine changes of variables, and sums of self-concordant functions are self-concordant.
Some authors allow a constant other than $2$; scaling $f$ by a positive factor moves between these versions.

Example: $f(x) = -\log x$ on $U = (0, \infty)$.
Here $f''(x) = 1/x^2$ and $f'''(x) = -2/x^3$, so $\abs{f'''(x)} = 2/x^3 = 2 (f''(x))^{3/2}$, with equality.
Quadratic and affine functions are self-concordant, since their third derivative is $0$.

Non-example: $f(x) = e^x$ on $\R$ is convex but not self-concordant.
Clause 2 reads $e^x \le 2 e^{3x/2}$, that is $e^{-x/2} \le 2$, which fails for $x < -2 \log 2$.
