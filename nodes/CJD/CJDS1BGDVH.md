---
tag: CJDS1BGDVH
kind: definition
name: Lyapunov function for a difference equation
msc: [39A30, 93D05]
defines: E9G05M7CE6
uses: [D62PEKHRV5, 0X3WGX95FE, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_function
---

## Definition

Let $D \subseteq \R^k$, let $f \colon D \to D$ be [[continuous|0X3WGX95FE]], and consider the difference equation $x_{n+1} = f(x_n)$.
Let $x^* \in D$ be an [[equilibrium|D62PEKHRV5]], so $f(x^*) = x^*$.
Let $G \subseteq D$ be a [[neighbourhood|0ZCY0Z80B6]] of $x^*$ relative to $D$.
A *Lyapunov function* for the equation on $G$ is a continuous function $V \colon G \to \R$ such that:

1. $V(x^*) = 0$.
2. $V(x) > 0$ for every $x \in G$ with $x \ne x^*$.
3. $\Delta V(x) = V(f(x)) - V(x) \le 0$ for every $x \in G$ with $f(x) \in G$.

The function $V$ is a *strict* Lyapunov function if moreover $\Delta V(x) < 0$ for every $x \ne x^*$ in $G$ with $f(x) \in G$.

## Remarks

Example: for $f(x) = x / (1 + x^2)$ on $\R$ with $x^* = 0$, take $V(x) = x^2$.
Then $V(0) = 0$, $V(x) > 0$ for $x \ne 0$, and $\Delta V(x) = x^2 \left( (1 + x^2)^{-2} - 1 \right) < 0$ for $x \ne 0$, so $V$ is a strict Lyapunov function.

Non-example: for $f(x) = 2x$ and $V(x) = x^2$, clauses 1 and 2 hold but $\Delta V(x) = 3x^2 > 0$ for $x \ne 0$, so clause 3 fails.

The quantity $\Delta V$ is the forward difference of $V$ along solutions, the analogue of the derivative $\dot V$ along solutions of a differential equation.
If a Lyapunov function exists, the equilibrium is stable; if a strict one exists, it is asymptotically stable.
For a linear map $f(x) = Ax$ one often uses a quadratic form $V(x) = x^T P x$ with $P$ positive definite and $A^T P A - P$ negative definite.
