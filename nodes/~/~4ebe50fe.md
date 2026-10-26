---
tag: ~4ebe50fe
kind: statement
role: theorem
name: Global existence for globally Lipschitz vector fields
msc: [34A12]
uses: [~d8e88376, ~375aa480, ~3f3a6157, ~40f94cf8]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Global existence of solution
---

## Statement

Let $J$ be an interval, let $K \ge 0$, and let $f : J \times \mathbb{R}^n \to \mathbb{R}^n$ be continuous.
Assume that $\|f(t, x) - f(t, y)\| \le K \|x - y\|$ for all $t \in J$ and $x, y \in \mathbb{R}^n$.
Then for each $t_0 \in J$ and $x_0 \in \mathbb{R}^n$, the [[initial value problem|~40f94cf8]] $x' = f(t, x)$, $x(t_0) = x_0$ has exactly one solution defined on all of $J$.

## Remarks

The point is that the solution does not blow up: the Lipschitz bound gives $\|f(t, x)\| \le \|f(t, 0)\| + K \|x\|$, so $\|x(t)\|$ grows at most exponentially.
A linear system $x' = A(t) x + b(t)$ with continuous $A$ and $b$ on $J$ satisfies the hypothesis on each compact subinterval. So its solutions exist on all of $J$.
A field that is only locally Lipschitz can give [[blow-up in finite time|~28ca1207]].

## Explanations

### L1 human

If the field grows at most linearly in the state, solutions cannot run away to infinity in finite time.
So the solution exists as long as the field is defined.
