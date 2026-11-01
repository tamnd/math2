---
tag: 6D10WYZR4F
kind: definition
name: Rough path
msc: [60L20]
defines: X6KCW4X5JA
uses: [012PBA0FMD, 0BF2DE2SYK, 22735FGJV6, JA95NH206E]
sources:
  - url: https://en.wikipedia.org/wiki/Rough_path
---

## Definition

Let $T > 0$, let $d \ge 1$, and let $\alpha \in (1/3, 1/2]$.
For a path $X \colon [0, T] \to \R^d$ write $X_{s,t} = X_t - X_s$.
An *$\alpha$-Hölder rough path* on $[0, T]$ with values in $\R^d$ is a pair $(X, \mathbb{X})$ of a path $X \colon [0, T] \to \R^d$ and a map $\mathbb{X} \colon [0, T]^2 \to \R^d \otimes \R^d$ such that:

1. (Chen's relation) $\mathbb{X}_{s,t} - \mathbb{X}_{s,u} - \mathbb{X}_{u,t} = X_{s,u} \otimes X_{u,t}$ for all $s, u, t \in [0, T]$;
2. $\sup_{s \ne t} \abs{X_{s,t}} / \abs{t - s}^{\alpha} < \infty$;
3. $\sup_{s \ne t} \abs{\mathbb{X}_{s,t}} / \abs{t - s}^{2\alpha} < \infty$.

Here $\otimes$ is the [[tensor product|0BF2DE2SYK]], and $\R^d \otimes \R^d$ is identified with the $d \times d$ matrices.

## Remarks

The map $\mathbb{X}_{s,t}$ stands for the iterated integral $\int_s^t X_{s,r} \otimes dX_r$.
Clause 2 says that $X$ is [[Hölder continuous|012PBA0FMD]] with exponent $\alpha$.
Example: for a continuously differentiable path $X$, set $\mathbb{X}_{s,t} = \int_s^t X_{s,r} \otimes \dot{X}_r \, dr$.
Splitting $\int_s^t$ at $u$ and writing $X_{s,r} = X_{s,u} + X_{u,r}$ for $r \ge u$ gives Chen's relation, and clauses 2 and 3 hold with exponents $1$ and $2$.
Example: for a [[Brownian motion|22735FGJV6]] $B$, the [[Itô integrals|JA95NH206E]] $\mathbb{B}_{s,t} = \int_s^t B_{s,r} \otimes dB_r$ give a rough path almost surely, for each $\alpha \in (1/3, 1/2)$.
Non-example: a smooth path $X$ with $\mathbb{X} = 0$ fails Chen's relation when $X_{s,u} \otimes X_{u,t} \ne 0$.
The second level is not determined by $X$: if $g \colon [0, T] \to \R^d \otimes \R^d$ is $2\alpha$-Hölder, then $\mathbb{X}_{s,t} + g_t - g_s$ also satisfies the three clauses.
