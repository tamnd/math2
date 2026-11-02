---
tag: KR4KX354JN
kind: definition
name: Symmetric operator
msc: [47B25, 47B02]
defines: H971WGMV6C
uses: [HM2HHE3J51, BCJHNHKQFG]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]].
Let $T \colon D(T) \to H$ be a [[densely defined|BCJHNHKQFG]] linear operator, where the domain $D(T)$ is a dense linear subspace of $H$.
The operator $T$ is *symmetric* when
$$\ip{Tx}{y} = \ip{x}{Ty} \quad \text{for all } x, y \in D(T).$$

## Remarks

Example: on $H = L^2(0, 1)$ let $D(T)$ be the smooth functions with compact support in $(0, 1)$ and $Tf = -i f'$.
For $f, g \in D(T)$, integration by parts with vanishing boundary terms gives $\int_0^1 -i f' \bar g = \int_0^1 f \, \overline{-i g'}$, so $T$ is symmetric.

Non-example: on the same domain, $Sf = f'$ satisfies $\ip{Sf}{g} = -\ip{f}{Sg}$, so $\ip{Sf}{g} \ne \ip{f}{Sg}$ whenever $\ip{f}{Sg} \ne 0$; it is skew-symmetric, not symmetric.

An equivalent form: $T$ is symmetric if and only if its [[adjoint|86B7HF79PQ]] $T^*$ extends $T$, written $T \subseteq T^*$.
$T$ is self-adjoint when moreover $T^* = T$, including equality of domains.
By the [[Hellinger–Toeplitz theorem|ZXJ7FJ3WCE]], a symmetric operator with $D(T) = H$ is bounded, and then it is self-adjoint.
Some authors, and Mathlib, call a linear map $T \colon E \to E$ on an inner product space symmetric when the identity holds on all of $E$, without a domain.
