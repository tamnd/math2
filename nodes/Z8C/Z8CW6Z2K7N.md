---
tag: Z8CW6Z2K7N
kind: definition
name: Essentially self-adjoint operator
msc: [47B25]
defines: DT49GKR9AS
uses: [HM2HHE3J51, H971WGMV6C, 3TWMBFQJJ8, TRC892PJNN, 86B7HF79PQ, 0S23E6YE83]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $A$ be a [[symmetric operator|H971WGMV6C]] on $H$ with dense domain $D(A)$.
Then $A$ is [[closable|3TWMBFQJJ8]], with [[closure|TRC892PJNN]] $\overline{A}$.
The operator $A$ is *essentially self-adjoint* if $\overline{A}$ is self-adjoint, that is, $\overline{A} = (\overline{A})^*$, where ${}^*$ denotes the [[adjoint|86B7HF79PQ]].

## Remarks

The following conditions are equivalent for a symmetric operator $A$:

1. $A$ is essentially self-adjoint;
2. $A$ has exactly one self-adjoint extension;
3. $A^*$ is self-adjoint, and then $A^* = \overline{A}$;
4. the [[kernels|0S23E6YE83]] $\ker(A^* - iI)$ and $\ker(A^* + iI)$ are both $\set{0}$.

Example: on $L^2(\R)$, let $A = -i \, d/dx$ on the smooth functions with compact support.
Then $A^*$ is $-i \, d/dx$ on the Sobolev space $H^1(\R)$.
The equation $A^* u = \pm i u$ means $u' = \mp u$, with solutions $c e^{\mp x}$, which are not in $L^2(\R)$ unless $c = 0$; so condition 4 holds.
Non-example: on $L^2([0,1])$, let $B = -i \, d/dx$ on the smooth functions with compact support in $(0,1)$.
Now $e^{-x}$ and $e^{x}$ lie in $L^2([0,1])$ and solve $B^* u = i u$ and $B^* u = -i u$, so condition 4 fails, and $B$ has many self-adjoint extensions, one for each boundary condition $u(1) = e^{i \theta} u(0)$.
A self-adjoint operator is essentially self-adjoint; a core of a self-adjoint operator $T$ is a domain on which the restriction of $T$ is essentially self-adjoint.
