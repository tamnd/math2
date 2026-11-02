---
tag: DEHZAQ1N92
kind: definition
name: c-cyclical monotonicity
msc: [49Q22, 49N15]
defines: RPN59B2XSR
uses: [HTR7J0W66V]
sources:
  - url: https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
---

## Definition

Let $X$ and $Y$ be sets and let $c \colon X \times Y \to (-\infty, \infty]$ be a function, the cost.
A set $\Gamma \subseteq X \times Y$ is *$c$-cyclically monotone* if for every integer $N \ge 1$ and all pairs $(x_1, y_1), \dots, (x_N, y_N) \in \Gamma$,
$$\sum_{i=1}^{N} c(x_i, y_i) \le \sum_{i=1}^{N} c(x_i, y_{i+1}),$$
where $y_{N+1} = y_1$.
Let $X$ and $Y$ be topological spaces, and let $\pi$ be a Borel measure on $X \times Y$, such as a [[coupling|HTR7J0W66V]].
Then $\pi$ is *$c$-cyclically monotone* if it is concentrated on a $c$-cyclically monotone Borel set.

## Remarks

Example: let $X = Y = \R$, $c(x, y) = (x - y)^2$ and $\Gamma = \set{(x, x) : x \in \R}$, the diagonal.
The left side of the inequality is $0$ and the right side is a sum of squares, so the inequality holds and $\Gamma$ is $c$-cyclically monotone.

Non-example: with the same cost, $\Gamma = \set{(0, 1), (1, 0)}$ fails for $N = 2$: the left side is $1 + 1 = 2$ and the right side is $c(0, 0) + c(1, 1) = 0$.

Equivalently, the inequality may be required for every permutation $\sigma$ of $\set{1, \dots, N}$, with $y_{\sigma(i)}$ in place of $y_{i+1}$, since every permutation is a product of disjoint cycles.
For $X = Y = \R^n$ and $c(x, y) = \frac12 \abs{x - y}^2$, a set is $c$-cyclically monotone exactly when it is cyclically monotone in the sense of Rockafellar, that is, $\sum_i \ip{y_i}{x_{i+1} - x_i} \le 0$ with $x_{N+1} = x_1$.
