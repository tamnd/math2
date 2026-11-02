---
tag: M03K2ZWNST
kind: definition
name: Pluricomplex Green function
msc: [32U35]
defines: 3MQVKVGYYY
uses: [FF2P7ER3QT]
sources:
  - url: https://en.wikipedia.org/wiki/Plurisubharmonic_function
---

## Definition

Let $\Omega \subseteq \C^n$ be a domain and let $w \in \Omega$.
Let $\mathcal{F}_w$ be the set of [[plurisubharmonic functions|FF2P7ER3QT]] $u$ on $\Omega$ such that:

1. $u < 0$ on $\Omega$;
2. there are a neighbourhood $U$ of $w$ and a constant $C$ with $u(\zeta) \le \log\abs{\zeta - w} + C$ for $\zeta \in U$.

The *pluricomplex Green function* of $\Omega$ with pole at $w$ is the function $g_\Omega(\cdot, w) \colon \Omega \to [-\infty, 0]$ given by
$$g_\Omega(z, w) = \sup\set{u(z) : u \in \mathcal{F}_w} .$$

## Remarks

Example: for the unit ball $\Omega = \set{\abs{z} < 1}$ and $w = 0$, $g_\Omega(z, 0) = \log\abs{z}$.
Check: $\log\abs{z}$ belongs to $\mathcal{F}_0$.
Conversely, let $u \in \mathcal{F}_0$ and let $\xi$ be a unit vector.
The function $\lambda \mapsto u(\lambda \xi) - \log\abs{\lambda}$ is subharmonic on $0 < \abs{\lambda} < 1$ and bounded above near $0$, so it extends across $0$.
Its boundary values are at most $0$, so $u(\lambda \xi) \le \log\abs{\lambda}$ by the maximum principle.
Non-example: $u(z) = \abs{z}^2 - 1$ is negative and plurisubharmonic on the ball but is bounded near $0$, so it fails clause 2.
For $n = 1$ and a bounded regular domain, $g_\Omega(z, w)$ is the classical Green function with the sign convention $g_\Omega(z, w) \sim \log\abs{z - w}$ near $w$.
Holomorphic maps decrease it: if $f \colon \Omega_1 \to \Omega_2$ is holomorphic, then $g_{\Omega_2}(f(z), f(w)) \le g_{\Omega_1}(z, w)$.
If $\Omega$ is bounded, then $g_\Omega(\cdot, w)$ is plurisubharmonic and belongs to $\mathcal{F}_w$.
