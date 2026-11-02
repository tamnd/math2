---
tag: ZPC2A2JMD8
kind: definition
name: Carathéodory's royal road
msc: [49K05, 49L12]
defines: 148S3XETT3
uses: [PQ25NHV0KS, 5TRXQKP7DY]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Definition

Let $a < b$, let $G \subseteq \R \times \R^n$ be open, and let $L \colon G \times \R^n \to \R$ be continuous, written $L(t, x, v)$.
For a $C^1$ curve $y \colon [a, b] \to \R^n$ with graph in $G$, let $J(y) = \int_a^b L(t, y(t), y'(t)) \, dt$, a functional of the [[calculus of variations|PQ25NHV0KS]].
Let $\bar x$ be a $C^1$ curve with graph in $G$.
*Carathéodory's royal road* is the following method to show that $\bar x$ minimises $J$ among such curves with the same endpoints.
One looks for a $C^1$ function $S \colon G \to \R$ and a continuous map $\psi \colon G \to \R^n$ such that:

1. $L(t, x, v) - S_t(t, x) - \nabla_x S(t, x) \cdot v \ge 0$ for all $(t, x) \in G$ and $v \in \R^n$;
2. $L(t, x, \psi(t, x)) - S_t(t, x) - \nabla_x S(t, x) \cdot \psi(t, x) = 0$ for all $(t, x) \in G$;
3. $\bar x'(t) = \psi(t, \bar x(t))$ for all $t \in [a, b]$.

The function $L^*(t, x, v) = L(t, x, v) - S_t(t, x) - \nabla_x S(t, x) \cdot v$ is the *equivalent Lagrangian* of $L$ with respect to $S$.

## Remarks

The method works because of this identity, valid for every admissible curve $y$:
$$J(y) = \int_a^b L^*(t, y(t), y'(t)) \, dt + S(b, y(b)) - S(a, y(a)).$$
The boundary terms depend only on the endpoints.
By clauses 1 to 3, the integral of $L^*$ is $\ge 0$ for every $y$ and $= 0$ for $\bar x$, so $J(y) \ge J(\bar x)$.

Clauses 1 and 2 say that $\min_v L^*(t, x, v) = 0$, with the minimum at $v = \psi(t, x)$.
With $H(t, x, p) = \sup_v (p \cdot v - L(t, x, v))$, this means $S_t + H(t, x, \nabla_x S) = 0$, the [[Hamilton–Jacobi equation|5TRXQKP7DY]].

Example: $n = 1$, $G = \R^2$, $L = \frac{1}{2} v^2$, and $\bar x(t) = t$ on $[0, 1]$.
Take $S(t, x) = x - t/2$ and $\psi = 1$.
Then $L^* = \frac{1}{2} v^2 + \frac{1}{2} - v = \frac{1}{2} (v - 1)^2$, which is $\ge 0$ and vanishes at $v = 1$, and $\bar x' = 1$.
So $\bar x(t) = t$ minimises $\int_0^1 \frac{1}{2} y'^2 \, dt$ among $C^1$ curves from $(0, 0)$ to $(1, 1)$.

Non-example: in the same problem, $S = 0$ with $\psi = 1$ fails clause 2, since $L(t, x, 1) = \frac{1}{2} \ne 0$.

## Explanations

### L1 human

The method changes the integrand by a total derivative, which changes the integral only by endpoint terms.
If the new integrand is never negative and is zero along the candidate curve, the candidate wins.
