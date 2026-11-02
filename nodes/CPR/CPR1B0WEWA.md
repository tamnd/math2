---
tag: CPR1B0WEWA
kind: definition
name: Plurisubharmonic function
msc: [32U05, 31C10]
defines: FF2P7ER3QT
uses: [Z1MHMGFNFW, RN4G8SGP6P]
sources:
  - url: https://en.wikipedia.org/wiki/Plurisubharmonic_function
---

## Definition

Let $\Omega \subseteq \C^n$ be an open set.
A function $u \colon \Omega \to [-\infty, \infty)$ is *plurisubharmonic* if:

1. $u$ is [[upper semicontinuous|RN4G8SGP6P]];
2. for every $a \in \Omega$ and $b \in \C^n$ such that the set $\set{a + \lambda b : \lambda \in \C, \abs{\lambda} \le 1}$ lies in $\Omega$,
$$u(a) \le \frac{1}{2\pi} \int_0^{2\pi} u(a + e^{i\theta} b) \, d\theta .$$

## Remarks

Clause 2 says that for all $a, b$ the function $\lambda \mapsto u(a + \lambda b)$ is [[subharmonic|Z1MHMGFNFW]] or identically $-\infty$ on each component of its domain.
Many authors also require that $u$ is not identically $-\infty$ on any connected component of $\Omega$.
A function $u$ of class $C^2$ is plurisubharmonic if and only if
$$\sum_{j,k=1}^n \frac{\partial^2 u}{\partial z_j \partial \bar z_k}(z) \, w_j \bar w_k \ge 0 \quad \text{for all } z \in \Omega,\ w \in \C^n .$$
Example: $u(z) = \abs{z_1}^2 + \cdots + \abs{z_n}^2$ has complex Hessian equal to the identity matrix, which is positive definite, so $u$ is plurisubharmonic.
Non-example: $u(z_1, z_2) = \abs{z_1}^2 - \abs{z_2}^2$ is smooth, but on the line $\lambda \mapsto (0, \lambda)$ it is $-\abs{\lambda}^2$, which is not subharmonic, so clause 2 fails at $a = 0$, $b = (0, 1)$.
Plurisubharmonic functions are subharmonic as functions on $\R^{2n}$, but the converse fails, as the non-example shows.
The abbreviation "psh" is common.
