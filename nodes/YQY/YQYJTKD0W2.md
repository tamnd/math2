---
tag: YQYJTKD0W2
kind: definition
name: Observability
msc: [93B07, 93C15]
defines: C4HN3EAQWM
uses: [ZPDTVZQN5K]
sources:
  - url: https://en.wikipedia.org/wiki/Observability
---

## Definition

Let $x' = f(x, u)$, $y = h(x)$ be a [[control system|ZPDTVZQN5K]] on $\R^n$ with output map $h \colon \R^n \to \R^p$.
Let $x_0, \tilde{x}_0 \in \R^n$.
For an admissible control $u$, let $x$ and $\tilde{x}$ be the trajectories with $x(0) = x_0$ and $\tilde{x}(0) = \tilde{x}_0$.
The states $x_0$ and $\tilde{x}_0$ are *indistinguishable* if, for every $u$, $h(x(t)) = h(\tilde{x}(t))$ for all $t \ge 0$ at which both trajectories are defined.
The system is *observable* if any two indistinguishable initial states are equal.

## Remarks

Consider a linear system $x' = A x + B u$, $y = C x$.
The output difference of two initial states does not depend on $u$.
The system is observable if and only if, for any $T > 0$, the output $y$ on $[0, T]$ determines $x(0)$.
Observability of the linear system is equivalent to $\rank \begin{pmatrix} C \\ CA \\ \vdots \\ CA^{n-1} \end{pmatrix} = n$.
Example: $x_1' = x_2$, $x_2' = 0$, $y = x_1$ is observable, since $y(t) = x_1(0) + t \, x_2(0)$ gives $x_1(0) = y(0)$ and $x_2(0) = y'(0)$.
Non-example: the same system with output $y = x_2$ is not observable, since $(0, 0)$ and $(1, 0)$ give the same output $y \equiv 0$.
