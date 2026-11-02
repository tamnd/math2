---
tag: KCV4BDWZ87
kind: statement
role: theorem
name: Contraction mapping principle for integral equations
msc: [45G10, 47H10, 45B05]
uses: [0VK6VEH345, BSCYBP6AS6, 0AW1E6YTJY, 0QN69YA357, 09GRCZVR5E, K6ZF91051B]
about: [BSCYBP6AS6]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_fixed-point_theorem
---

## Statement

Let $a < b$, let $f \colon [a, b] \to \R$ be continuous, and let $H \colon [a, b] \times [a, b] \times \R \to \R$ be continuous.
Assume that $H$ satisfies a [[Lipschitz condition|0AW1E6YTJY]] in its third variable: there is $L \ge 0$ with
$$\abs{H(x, s, u) - H(x, s, v)} \le L \abs{u - v} \quad \text{for all } x, s \in [a, b] \text{ and } u, v \in \R.$$
Let $\lambda \in \R$ with $\abs{\lambda} L (b - a) < 1$.
Then the [[nonlinear integral equation|BSCYBP6AS6]]
$$\varphi(x) = f(x) + \lambda \int_a^b H\left(x, s, \varphi(s)\right) ds, \quad x \in [a, b],$$
has exactly one continuous solution $\varphi \colon [a, b] \to \R$.
For every continuous $\varphi_0$, the functions $\varphi_{k+1}(x) = f(x) + \lambda \int_a^b H(x, s, \varphi_k(s)) \, ds$ converge to $\varphi$ uniformly on $[a, b]$.

## Remarks

Proof idea: let $T$ be the right side, viewed as a map of $C[a, b]$ with the maximum norm.
This space is a complete metric space, by the [[completeness of the space of bounded continuous functions|09GRCZVR5E]].
The map $T$ sends continuous functions to continuous functions, since $H$ is uniformly continuous on compact sets.
The Lipschitz condition gives $\max \abs{T \varphi - T \psi} \le \abs{\lambda} L (b - a) \max \abs{\varphi - \psi}$, so $T$ is a [[contraction|0QN69YA357]].
The [[Banach fixed point theorem|0VK6VEH345]] gives the unique fixed point and the convergence of the [[fixed-point iteration|K6ZF91051B]].

Example: the linear case $H(x, s, u) = K(x, s) u$ with a continuous kernel $K$ has $L = \max \abs{K}$, and the theorem gives unique solvability of $\varphi = f + \lambda \int_a^b K \varphi$ for $\abs{\lambda} \max \abs{K} (b - a) < 1$.

The smallness condition matters: for $H(x, s, u) = u$ on $[0, 1]$ and $\lambda = 1$, so $\abs{\lambda} L (b - a) = 1$, the equation $\varphi = f + \int_0^1 \varphi$ has no solution when $\int_0^1 f \ne 0$.
For the Volterra form, with $\int_a^x$ in place of $\int_a^b$, the conclusion holds for every $\lambda$, because some power of $T$ is a contraction.
The same proof works for complex-valued functions.

## Explanations

### L1 human

If the integral term reacts only weakly to changes of the unknown, the equation has exactly one solution.
One finds it by guessing any function and feeding it into the right side again and again.
The guesses get closer to each other at a fixed rate and converge to the solution.

### L2 human

This is the standard first existence theorem for nonlinear Fredholm-type equations of Urysohn form.
The error after $k$ steps is at most $q^k (1 - q)^{-1} \max \abs{\varphi_1 - \varphi_0}$ with $q = \abs{\lambda} L (b - a)$, so the method also gives numerical bounds.
The same argument, applied on a short time interval, proves the Picard–Lindelöf theorem for ordinary differential equations through their integral form.
For larger $\lambda$ one needs other tools, such as Schauder's fixed point theorem or Fredholm theory in the linear case.
