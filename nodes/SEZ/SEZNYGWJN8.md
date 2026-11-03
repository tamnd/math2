---
tag: SEZNYGWJN8
kind: definition
name: Causal system
msc: [93A10, 93C05]
defines: NSR7N8A71M
uses: [21FN2KSTJZ, 6J9MPVHSMF]
sources:
  - url: https://en.wikipedia.org/wiki/Causal_system
---

## Definition

Let $\mathcal{T}$ be $\R$ or $\Z$, and let $\mathcal{U}$ and $\mathcal{Y}$ be sets of functions on $\mathcal{T}$.
A system $H \colon \mathcal{U} \to \mathcal{Y}$ is *causal* if for every $t \in \mathcal{T}$ and all inputs $u_1, u_2 \in \mathcal{U}$ the following holds:
if $u_1(s) = u_2(s)$ for all $s \le t$, then $(Hu_1)(t) = (Hu_2)(t)$.

## Remarks

Example: the delay $(Hu)(t) = u(t - 1)$ is causal, since $(Hu)(t)$ only uses the value of $u$ at the time $t - 1 \le t$.
Non-example: the advance $(Hu)(t) = u(t + 1)$ is not causal.
Take $u_1 = 0$ and $u_2$ equal to $0$ for $s \le 0$ and to $1$ for $s > 0$; they agree up to $t = 0$, but $(Hu_1)(0) = 0$ and $(Hu_2)(0) = 1$.
Let $H$ be a [[linear system|21FN2KSTJZ]] on a vector space of signals.
Then $H$ is causal if and only if every input that vanishes on $(-\infty, t]$ gives an output that vanishes at $t$.
A discrete-time [[LTI system|6J9MPVHSMF]] $y = h * u$ on finitely supported inputs is causal if and only if $h[n] = 0$ for all $n < 0$.
Some authors call a system *strictly causal* if $(Hu)(t)$ depends only on the values $u(s)$ with $s < t$.
