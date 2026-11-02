---
tag: GC9R87YZ6A
kind: definition
name: Action-angle coordinates
msc: [37J35, 70H06]
defines: M3T81YNSKC
uses: [CAN490EPRT, 0EDKGA2FAK, 0KZZ70ZHXP, 03NM7DZXXC]
sources:
  - url: https://en.wikipedia.org/wiki/Action-angle_coordinates
---

## Definition

Let $(M, \omega)$ be a [[symplectic manifold|CAN490EPRT]] of dimension $2n$, let $H \colon M \to \R$ be smooth, and let $U \subseteq M$ be open.
Let $\mathbb{T}^n = \R^n / 2\pi \Z^n$ be the $n$-[[torus|03NM7DZXXC]].
*Action-angle coordinates* for $H$ on $U$ are given by a [[diffeomorphism|0KZZ70ZHXP]] $\Psi \colon U \to D \times \mathbb{T}^n$, with $D \subseteq \R^n$ open, written $\Psi = (I_1, \ldots, I_n, \theta_1, \ldots, \theta_n)$, such that:

1. $\omega = \sum_{k=1}^n dI_k \wedge d\theta_k$ on $U$;
2. $H = K(I_1, \ldots, I_n)$ on $U$ for a smooth function $K \colon D \to \R$.

The $I_k$ are the *actions* and the $\theta_k$ are the *angles*.

## Remarks

Here the convention is $\omega = \sum_k dp_k \wedge dq_k$ on $\R^{2n}$, so that the actions play the role of momenta and the angles the role of positions.
In these coordinates the [[Hamiltonian system|0EDKGA2FAK]] reads $I_k' = 0$ and $\theta_k' = \partial K / \partial I_k (I)$, so $\theta(t) = \theta(0) + t \, \nabla K(I)$.

Example: the harmonic oscillator $H = \frac{1}{2}(p^2 + q^2)$ on $\R^2 \setminus \set{0}$.
Put $q = \sqrt{2I} \sin \theta$ and $p = \sqrt{2I} \cos \theta$ with $I > 0$.
A short computation gives $dp \wedge dq = dI \wedge d\theta$, and $H = I$, so both clauses hold with $K(I) = I$.

Non-example: polar coordinates $q = r \sin \theta$, $p = r \cos \theta$ with $r > 0$ give $H = r^2/2$, but $dp \wedge dq = r \, dr \wedge d\theta$, so clause 1 fails.

For an integrable system, the actions can be computed as $I_k = \frac{1}{2\pi} \oint_{\gamma_k} p \, dq$ over basic cycles $\gamma_k$ of an invariant torus, when $\omega = d(\sum_k p_k \, dq_k)$.
