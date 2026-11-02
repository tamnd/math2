---
tag: 844NHRQQN3
kind: definition
name: Quasi-ergodicity
msc: [37A40, 37A25]
defines: F43HXQD0T6
uses: [P15VQS5DJ9, VQQM4Y550T, F608XX51KA, AZRPHS478B]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodicity
---

## Definition

Let $(X, \mathcal{A}, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $T \colon X \to X$ be a [[quasi-measure-preserving map|F608XX51KA]]: $T$ is measurable and $\mu(T^{-1}(A)) = 0$ for every $A \in \mathcal{A}$ with $\mu(A) = 0$.
The map $T$ is *quasi-ergodic* if every $A \in \mathcal{A}$ with $\mu(T^{-1}(A) \mathbin{\triangle} A) = 0$ satisfies $\mu(A) = 0$ or $\mu(X \setminus A) = 0$.

## Remarks

Here $\triangle$ is the symmetric difference, so the condition $\mu(T^{-1}(A) \mathbin{\triangle} A) = 0$ says that $A$ is invariant up to a [[null set|VQQM4Y550T]].
If $T$ preserves $\mu$ and $\mu$ is a probability measure, quasi-ergodicity is the same as being an [[ergodic transformation|AZRPHS478B]].
Example: let $\mu$ be a probability measure on $[0,1)$ with a strictly positive density $\rho$ with respect to Lebesgue measure $\lambda$, and let $T(x) = x + \alpha \bmod 1$ with $\alpha$ irrational.
The measures $\mu$ and $\lambda$ have the same null sets, and $T$ preserves $\lambda$, so $T$ is quasi-measure-preserving for $\mu$.
An almost invariant set for $\mu$ is almost invariant for $\lambda$, so it has $\lambda$-measure $0$ or $1$ by ergodicity of the rotation, hence $\mu$-measure $0$ or $1$.
Non-example: the identity map of $[0,1]$ with Lebesgue measure is quasi-measure-preserving, but $A = [0, 1/2]$ is invariant with $0 < \lambda(A) < 1$.
In older physics texts the "quasi-ergodic hypothesis" means something else: that a trajectory comes arbitrarily close to every point of its energy surface.

## Explanations

### L1 human

A quasi-ergodic map has no invariant pieces except the trivial ones, up to sets of measure zero.
The map is not asked to preserve the measure, only to respect which sets have measure zero.
