---
tag: Q9VG3EGT74
kind: definition
name: Morse theory on Hilbert manifolds
msc: ["58E05", 58B20, 57R70]
defines: T9H6PT9FHE
uses: [R8DMMW0E9M, 4724KRNHAT, MGPPCDFQDG, MAX2ZYG6H9, 9ZQC7ARWTT]
sources:
  - url: https://en.wikipedia.org/wiki/Palais–Smale_compactness_condition
---

## Definition

Let $M$ be a $C^\infty$ [[Hilbert manifold|R8DMMW0E9M]] with a complete Riemannian metric $g$, and let $f \colon M \to \R$ be a $C^2$ function.
The gradient $\nabla f$ is defined by $g(\nabla f, v) = df(v)$.
The function $f$ satisfies *condition (C)* if every sequence $(p_n)$ in $M$ on which $f$ is bounded and $\norm{\nabla f(p_n)} \to 0$ has a convergent subsequence.
This is the [[Palais–Smale condition|4724KRNHAT]] on $M$.
Through $g$, the Hessian of $f$ at a critical point $p$ is a bounded self-adjoint operator on $T_p M$.
The point $p$ is *nondegenerate* if this operator is invertible.
Its *index* is the supremum of the dimensions of subspaces of $T_p M$ on which the Hessian is negative definite.

*Morse theory on Hilbert manifolds* is the [[critical point theory|9ZQC7ARWTT]] of $C^2$ functions $f$ on such $M$ with three properties.
The function is bounded below, it satisfies condition (C), and its critical points are [[nondegenerate|MGPPCDFQDG]] of finite [[index|MAX2ZYG6H9]].

## Remarks

For such $f$ the two basic theorems of Morse theory hold.
If $a < b$ and $f^{-1}[a, b]$ contains no critical point, then the sublevel set $M^a = \set{f \le a}$ is a deformation retract of $M^b$.
If $f^{-1}[a, b]$ contains exactly one critical point, of index $\lambda$, in its interior, then $M^b$ has the homotopy type of $M^a$ with a $\lambda$-cell attached.

Example: let $(N, h)$ be a compact Riemannian manifold, let $p, q \in N$, and let $M$ be the Hilbert manifold of paths $\omega \colon [0, 1] \to N$ of Sobolev class $H^1$ with $\omega(0) = p$ and $\omega(1) = q$.
The [[energy|Q12AB1MJ64]] $E(\omega) = \frac{1}{2} \int_0^1 \abs{\omega'}^2 \, dt$ is bounded below and satisfies condition (C).
Its critical points are the geodesics from $p$ to $q$, of finite index, and they are nondegenerate when $q$ is not conjugate to $p$ along any geodesic.

Non-example: on $M = \R$ the function $f(x) = \arctan x$ is bounded below and has no critical points, but condition (C) fails along $x_n = -n$, since $f(x_n)$ is bounded and $f'(x_n) \to 0$.
Accordingly $f$ does not attain its infimum $-\pi/2$, while a function that is bounded below and satisfies condition (C) attains its infimum at a critical point.
