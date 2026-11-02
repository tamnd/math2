---
tag: MBMHS6FQF6
kind: statement
role: theorem
name: Łojasiewicz inequality
msc: [32B20, "26E05", 14P15]
uses: [081WKEDK6C, 0R6EWFKRCF]
about: [081WKEDK6C]
sources:
  - url: https://en.wikipedia.org/wiki/%C5%81ojasiewicz_inequality
same_as:
  wikidata: Q8080668
  wikipedia: Łojasiewicz inequality
---

## Statement

Let $U \subseteq \R^n$ be open and let $f \colon U \to \R$ be a real [[analytic function|081WKEDK6C]].

1. Let $Z = f^{-1}(0)$, assume $Z \neq \emptyset$, and let $K \subseteq U$ be [[compact|0R6EWFKRCF]].
Then there are constants $C > 0$ and $\alpha > 0$ such that $\abs{f(x)} \ge C \operatorname{dist}(x, Z)^{\alpha}$ for all $x \in K$.
2. Let $a \in U$.
Then there are a neighbourhood $W \subseteq U$ of $a$ and constants $C > 0$ and $\theta \in (0, 1)$ such that $\abs{f(x) - f(a)}^{\theta} \le C \norm{\nabla f(x)}$ for all $x \in W$.

## Remarks

Part 1 is the distance inequality and part 2 is the gradient inequality.
Łojasiewicz proved them with his theory of semianalytic sets.
A later route uses resolution of singularities to make $f$ locally a monomial times a unit, where both inequalities are direct.

Analyticity is necessary.
The smooth function with $f(x) = e^{-1/x^2}$ for $x \neq 0$ and $f(0) = 0$ has $Z = \set{0}$.
But $\abs{f(x)} / \abs{x}^{\alpha} \to 0$ as $x \to 0$ for every $\alpha > 0$, so part 1 fails on $K = [-1, 1]$.

For $f(x) = x^2$ on $\R$ and $a = 0$, part 2 holds with $\theta = 1/2$ and $C = 1/2$, since $\abs{x^2}^{1/2} = \abs{x} = \tfrac12 \abs{f'(x)}$.

## Explanations

### L1 human

An analytic function cannot become small without being close to its zero set: it is at least a power of the distance to its zeros.
In the same spirit, near a critical point the gradient cannot be much smaller than the change in the value of the function.
Both say that analytic functions are never infinitely flat.

### L2 human

The gradient inequality is the key to the convergence of gradient flows.
If $f$ is real analytic and $x(t)$ is a bounded trajectory of $x' = -\nabla f(x)$, the inequality bounds the length of the trajectory, so $x(t)$ converges to a single critical point.
For merely smooth functions a bounded gradient trajectory can accumulate on a whole circle of critical points.
The distance inequality is used to divide distributions by real analytic functions.
