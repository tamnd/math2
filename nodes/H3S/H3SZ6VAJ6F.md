---
tag: H3SZ6VAJ6F
kind: definition
name: Ergodic transformation
msc: [37A25, 28D05]
defines: AZRPHS478B
uses: [0NFPJVJJHX, 556WBDAHNP]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodicity
---

## Definition

Let $(X, \mathcal{A}, \mu)$ be a [[probability space|0NFPJVJJHX]], and let $T \colon X \to X$ be a [[measure-preserving transformation|556WBDAHNP]].
A set $A \in \mathcal{A}$ is *$T$-invariant* if $T^{-1}(A) = A$.
The map $T$ is *ergodic* if every $T$-invariant set $A \in \mathcal{A}$ satisfies $\mu(A) = 0$ or $\mu(A) = 1$.

## Remarks

Equivalent forms: every measurable $f \colon X \to \R$ with $f \circ T = f$ almost everywhere is constant almost everywhere.
One can also require $\mu(T^{-1}(A) \mathbin{\triangle} A) = 0$ instead of $T^{-1}(A) = A$; this gives the same class of maps.
Example: the rotation $T(x) = x + \alpha \bmod 1$ on $[0,1)$ with Lebesgue measure and $\alpha$ irrational.
If $A$ is invariant, the Fourier coefficients of $f = 1_A$ satisfy $\hat f(k) e^{2 \pi i k \alpha} = \hat f(k)$.
Since $k \alpha \notin \Z$ for $k \ne 0$, all $\hat f(k)$ with $k \ne 0$ vanish, so $f$ is constant almost everywhere and $\mu(A) \in \set{0, 1}$.
Non-example: for $\alpha = 1/2$ the set $A = [0, 1/4) \cup [1/2, 3/4)$ is invariant with $\mu(A) = 1/2$.
The identity map is not ergodic on $[0,1]$ either, since every measurable set is invariant.
The definition extends to $\sigma$-finite measures: then an invariant set must be null or have null complement.
