---
tag: BQXB8H365P
kind: definition
name: Fano variety
msc: [14J45]
defines: FMHA649HJ9
uses: [A4H4CZ2V35, W05VYY4HBR, RRK8P6TXG2]
sources:
  - url: https://en.wikipedia.org/wiki/Fano_variety
---

## Definition

Let $k$ be a field and let $X$ be a smooth [[projective variety|A4H4CZ2V35]] over $k$ with [[canonical bundle|W05VYY4HBR]] $\omega_X$.
The variety $X$ is a *Fano variety* if the anticanonical bundle $\omega_X^{-1}$ is [[ample|RRK8P6TXG2]].

## Remarks

In divisor notation, $X$ is Fano when $-K_X$ is ample.
Example: on $\mathbb{P}^n$ one has $\omega = \mathcal{O}(-n-1)$, so $\omega^{-1} = \mathcal{O}(n+1)$ is ample and $\mathbb{P}^n$ is Fano.
More generally, a smooth hypersurface $X \subset \mathbb{P}^n$ of degree $d \ge 1$, with $n \ge 2$, has $\omega_X = \mathcal{O}_X(d - n - 1)$ by the adjunction formula, so it is Fano exactly when $d \le n$.
Non-example: a smooth plane cubic curve has $\omega = \mathcal{O}(3 - 3) = \mathcal{O}$, and the trivial bundle on a curve is not ample.
Many authors also allow mild singularities, such as terminal or log terminal ones, and then ask that $-K_X$ be an ample $\Q$-Cartier divisor.
Over $\C$, smooth Fano varieties are simply connected and rationally connected, and in each dimension they form finitely many deformation families.
