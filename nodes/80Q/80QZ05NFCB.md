---
tag: 80QZ05NFCB
kind: definition
name: Invariant set
msc: [34C45, 37C10]
defines: WWZTW11664
uses: [07BNRFQ0PJ, 02903SSA48, 07TZ2Q4C1M]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_(mathematics)
---

## Definition

Let $U$ be an open subset of $\R^n$, let $f \colon U \to \R^n$ be locally Lipschitz, and let $\varphi$ be the [[flow|02903SSA48]] of the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$.
For $x \in U$ let $I(x)$ be the maximal interval of existence of the solution through $x$.
A set $M \subseteq U$ is invariant if $\varphi_t(x) \in M$ for every $x \in M$ and every $t \in I(x)$.
It is positively invariant if $\varphi_t(x) \in M$ for every $x \in M$ and every $t \in I(x)$ with $t \ge 0$, and negatively invariant if the same holds for $t \le 0$.

## Remarks

A set is invariant exactly when it is a union of [[trajectories|07TZ2Q4C1M]].
Example: for $x' = -y$, $y' = x$ on $\R^2$, the flow is rotation by the angle $t$, so it preserves $x^2 + y^2$; hence each disc $\set{x^2 + y^2 \le r^2}$ is invariant.
Non-example: for $x' = -x$ on $\R$, the interval $[0, 1]$ is positively invariant, since $\varphi_t(x) = e^{-t} x$ stays in $[0, 1]$ for $t \ge 0$.
It is not invariant, since $\varphi_{-1}(1) = e > 1$.
An equilibrium point and a periodic orbit are invariant sets.
For a continuously differentiable function $V \colon U \to \R$ with $\nabla V \cdot f \le 0$ on $U$, each sublevel set $\set{x \in U : V(x) \le c}$ is positively invariant.
For a general flow $\varphi$ on a set $X$ the same definition reads $\varphi_t(M) \subseteq M$ for all $t$.

## Explanations

### L1 human

An invariant set is a trap with no way out in either direction of time.
A positively invariant set is a trap that solutions can enter but never leave.
