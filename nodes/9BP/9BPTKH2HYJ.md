---
tag: 9BPTKH2HYJ
kind: definition
name: Stability of a difference equation
msc: [39A30]
defines: CHEQ235HW9
uses: [D62PEKHRV5, 0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_stability
---

## Definition

Let $D \subseteq \R^m$, let $\norm{\cdot}$ be a [[norm|0V2WP9B1MF]] on $\R^m$, and let $f \colon D \to D$ be a map.
Let $x^* \in D$ be an [[equilibrium|D62PEKHRV5]] of $x_{n+1} = f(x_n)$, so $f(x^*) = x^*$.
Write $f^n$ for the $n$-th iterate of $f$.

1. The equilibrium $x^*$ is *stable* if for every $\varepsilon > 0$ there is $\delta > 0$ such that $\norm{x_0 - x^*} < \delta$ and $x_0 \in D$ imply $\norm{f^n(x_0) - x^*} < \varepsilon$ for all $n \ge 0$.
2. It is *attracting* if there is $\eta > 0$ such that $\norm{x_0 - x^*} < \eta$ and $x_0 \in D$ imply $f^n(x_0) \to x^*$ as $n \to \infty$.
3. It is *asymptotically stable* if it is stable and attracting.
4. It is *unstable* if it is not stable.

## Remarks

Example: for $f(x) = x/2$ on $\R$, the equilibrium $0$ is asymptotically stable: take $\delta = \varepsilon$, since $\abs{f^n(x_0)} = \abs{x_0}/2^n \le \abs{x_0}$, and $f^n(x_0) \to 0$ for every $x_0$.
Non-example: for $f(x) = 2x$, the equilibrium $0$ is not stable, since $\abs{f^n(x_0)} = 2^n \abs{x_0}$ exceeds any $\varepsilon$ for $x_0 \ne 0$.
For $f(x) = -x$, the equilibrium $0$ is stable but not attracting, as solutions jump between $x_0$ and $-x_0$.
Since all norms on $\R^m$ are equivalent, the notions do not depend on the choice of norm.
For a higher-order equation, the same definitions apply to the equivalent first-order system on $\R^{mk}$.
They are the discrete analogues of the definitions of [[Lyapunov stability|092S6VBECQ]] and [[asymptotic stability|05Y1JAM3Y5]] for flows.
