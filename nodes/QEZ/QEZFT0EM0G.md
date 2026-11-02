---
tag: QEZFT0EM0G
kind: definition
name: Vanishing cycle
msc: [32S30, 14D05, 32S50]
defines: M5EK9AKXNR
uses: [507C34W0ZT, 0YTCMFB4HC, M0Q5CFJ7ZH, P9CM4GQ2T0]
sources:
  - url: https://en.wikipedia.org/wiki/Vanishing_cycle
---

## Definition

Let $U$ be an open subset of $\C^{n+1}$ and let $f \colon U \to \C$ be a [[holomorphic function|507C34W0ZT]].
Let $p \in U$ be a nondegenerate [[critical point|0YTCMFB4HC]] of $f$ with $f(p) = 0$.
This means that the partial derivatives of $f$ vanish at $p$ and the Hessian matrix $\left( \partial^2 f / \partial z_j \partial z_k (p) \right)$ is invertible.
By the holomorphic Morse lemma there are holomorphic coordinates $w_0, \dots, w_n$ centred at $p$, on a ball $B$ about $p$, in which $f = w_0^2 + \cdots + w_n^2$.
For small real $t > 0$, the set
$$\Sigma_t = \set{w \in B : w_0, \dots, w_n \in \R, \ w_0^2 + \cdots + w_n^2 = t}$$
is an $n$-dimensional [[sphere|P9CM4GQ2T0]] in the fibre $f^{-1}(t) \cap B$.
The *vanishing cycle* at $p$ is the class $\delta = [\Sigma_t]$ in the [[homology group|M0Q5CFJ7ZH]] $H_n(f^{-1}(t) \cap B; \Z)$, defined up to the sign fixed by an orientation of $\Sigma_t$.

## Remarks

When $B$ is a ball in the coordinates $w$, the class $\delta$ generates the reduced homology $\tilde H_n(f^{-1}(t) \cap B; \Z) \cong \Z$, and $\Sigma_t$ shrinks to the point $p$ as $t \to 0$.
Let $f^{-1}(c)$ be a fibre further away, joined to $t$ by a path $\gamma$ of regular values.
Transporting $\delta$ along $\gamma$ gives a vanishing cycle in $H_n(f^{-1}(c); \Z)$, which depends on the homotopy class of $\gamma$.

Example: $n = 0$ and $f(w) = w^2$.
The fibre $f^{-1}(t)$ is the two points $\pm\sqrt{t}$, and $\delta = [\sqrt{t}] - [-\sqrt{t}]$ in $H_0$.

Example: $n = 1$ and $f(w) = w_0^2 + w_1^2$.
The local fibre is an annulus, and $\delta$ is the class of its core circle.

Non-example: the critical point $0$ of $f(w) = w^3$ is degenerate, since the Hessian is $0$.
Its local fibre is three points, with reduced $H_0$ of rank $2$, so it is not described by one vanishing cycle.
After a small perturbation $w^3 - sw$ with $s \ne 0$, it splits into two nondegenerate critical points, each with its own vanishing cycle.
