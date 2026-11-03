---
tag: K615PRVSME
kind: definition
name: Linear time-invariant system
msc: [93C05, 93C80]
defines: 6J9MPVHSMF
uses: [21FN2KSTJZ, S4THJVE1AJ, 2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_time-invariant_system
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $\mathcal{T}$ be $\R$ or $\Z$.
Let $\mathcal{U}$ and $\mathcal{Y}$ be vector spaces over $\mathbb{K}$ of functions on $\mathcal{T}$ that are closed under the shifts $(S_\tau v)(t) = v(t - \tau)$ for $\tau \in \mathcal{T}$.
A system $H \colon \mathcal{U} \to \mathcal{Y}$ is a *linear time-invariant system* (LTI system) if:

1. $H$ is [[linear|21FN2KSTJZ]]: $H(a u_1 + b u_2) = a \, Hu_1 + b \, Hu_2$ for all $u_1, u_2 \in \mathcal{U}$ and $a, b \in \mathbb{K}$.
2. $H$ is [[time-invariant|S4THJVE1AJ]]: $H(S_\tau u) = S_\tau(Hu)$ for all $u \in \mathcal{U}$ and $\tau \in \mathcal{T}$.

## Remarks

Discrete time shows the structure in a simple way.
Let $\mathcal{U}$ be the finitely supported sequences on $\Z$, let $\delta$ be the sequence with $\delta[0] = 1$ and $\delta[n] = 0$ for $n \ne 0$, and put $h = H\delta$.
Every $u \in \mathcal{U}$ is the finite sum $u = \sum_k u[k] \, S_k \delta$, so the two clauses give $(Hu)[n] = \sum_k u[k] \, h[n - k]$, the discrete [[convolution|2Z29JN3VES]] $h * u$.
Example: $(Hu)[n] = \tfrac12 (u[n] + u[n - 1])$ is LTI, and $h[0] = h[1] = \tfrac12$, $h[n] = 0$ otherwise.
Non-example: $(Hu)[n] = n \, u[n]$ is linear but fails clause 2, since for $u = \delta$ and $\tau = 1$ one gets $H(S_1 \delta) = S_1 \delta$ but $S_1(H\delta) = 0$.
In continuous time, the state-space system $x' = Ax + Bu$, $y = Cx + Du$ with constant matrices and zero initial state in the far past is LTI.
