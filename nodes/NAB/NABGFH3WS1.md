---
tag: NABGFH3WS1
kind: definition
name: Minimax approximation
msc: [41A50, 41A10, 65D15]
defines: ASWF03X5AM
uses: [0X3WGX95FE, 0TK8Y3J5RW, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Minimax_approximation_algorithm
---

## Definition

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a [[continuous function|0X3WGX95FE]] on the [[interval|0TK8Y3J5RW]] $[a, b]$.
Let $n \ge 0$ be an integer and let $\mathcal{P}_n$ be the set of real polynomials of [[degree|0DPF6WRZW6]] at most $n$.
A *minimax approximation* of degree $n$ to $f$ is a polynomial $p^* \in \mathcal{P}_n$ such that
$$\max_{a \le x \le b} \abs{f(x) - p^*(x)} = \inf_{p \in \mathcal{P}_n} \max_{a \le x \le b} \abs{f(x) - p(x)}.$$
The common value is the *minimax error* $E_n(f)$.

## Remarks

Example: for $f(x) = x^2$ on $[-1, 1]$ and $n = 1$, the polynomial $p^*(x) = 1/2$ is the minimax approximation, with error $1/2$.
Check: $x^2 - 1/2$ takes the values $1/2, -1/2, 1/2$ at $x = -1, 0, 1$.
If a line $p$ had $\abs{x^2 - p(x)} < 1/2$ everywhere, then $p(-1) > 1/2$, $p(0) < 1/2$ and $p(1) > 1/2$, which no linear function can do, since $p(0)$ is the mean of $p(-1)$ and $p(1)$.

Non-example: the Taylor polynomial $1 + x$ of $e^x$ at $0$ is not the minimax approximation of degree $1$ on $[-1, 1]$.
Its error $e^x - 1 - x$ is never negative, so lowering the line a little makes the largest error smaller.

A minimax approximation exists and is unique for every continuous $f$.
It is characterised by equioscillation: the error $f - p^*$ attains its largest absolute value at $n + 2$ points with alternating signs.
In terms of norms, $p^*$ minimises $\norm{f - p}_\infty$ over $\mathcal{P}_n$, where $\norm{g}_\infty = \max_{[a, b]} \abs{g}$.
