---
tag: F05PSBZP8Z
kind: definition
name: Heteroclinic orbit
msc: [34C37, 37C29]
defines: N9GYM69ZWM
uses: [0G4X36AE0X, 02903SSA48, 0BVT6VSB3S]
sources:
  - url: https://en.wikipedia.org/wiki/Heteroclinic_orbit
---

## Definition

Let $U \subseteq \R^n$ be open, let $f \colon U \to \R^n$ be continuously differentiable, and let $\varphi$ be the [[flow|02903SSA48]] of the system $x' = f(x)$.
Let $p$ and $q$ be two distinct [[equilibrium points|0G4X36AE0X]] of the system.
A *heteroclinic orbit* from $p$ to $q$ is the [[trajectory|0BVT6VSB3S]] $\set{\varphi_t(x) : t \in \R}$ of a point $x \in U$ such that:

1. the solution through $x$ exists for all $t \in \R$;
2. $\varphi_t(x) \to p$ as $t \to -\infty$;
3. $\varphi_t(x) \to q$ as $t \to +\infty$.

## Remarks

Example: for $x' = 1 - x^2$ on $\R$, the equilibria are $-1$ and $1$.
The solution with $x(0) = 0$ is $x(t) = \tanh t$, since $(\tanh t)' = 1 - \tanh^2 t$.
It exists for all $t$, tends to $-1$ as $t \to -\infty$ and tends to $1$ as $t \to +\infty$.
So $(-1, 1)$ is a heteroclinic orbit from $-1$ to $1$.

Non-example: for the same equation, the solution with $x(0) = 2$ is $x(t) = \coth(t + c)$, where $c > 0$ and $\coth c = 2$.
It tends to $1$ as $t \to +\infty$, but it blows up at $t = -c$, so clause 1 fails.

A heteroclinic orbit from $p$ to $q$ lies in the unstable set of $p$ and in the stable set of $q$.
If $p = q$ in the same construction, the orbit is called a homoclinic orbit.
Some authors also allow $p$ and $q$ to be periodic orbits instead of equilibria.
