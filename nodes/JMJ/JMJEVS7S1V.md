---
tag: JMJEVS7S1V
kind: definition
name: Characteristic variety
msc: [35A30, 35A27]
defines: CQJ2E2ARRF
uses: [F31T650DKY, 6DZETZ5T9G, 0WQJJCCTC8]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_variety
---

## Definition

Let $P$ be a [[linear differential operator|6DZETZ5T9G]] of order $m$ on an open set $\Omega \subseteq \R^n$, with [[principal symbol|F31T650DKY]] $\sigma_m(P)$.
The *characteristic variety* of $P$ is the set
$$\operatorname{Char}(P) = \set{(x, \xi) \in \Omega \times (\R^n \setminus \set{0}) : \sigma_m(P)(x, \xi) = 0}.$$
A nonzero vector $\xi$ is *characteristic* for $P$ at $x$ if $(x, \xi) \in \operatorname{Char}(P)$.
A $C^1$ hypersurface $S \subseteq \Omega$ is *noncharacteristic* at a point $x \in S$ if a [[normal vector|0WQJJCCTC8]] $\nu$ of $S$ at $x$ satisfies $\sigma_m(P)(x, \nu) \ne 0$.

## Remarks

Example: for the heat operator $P = \partial_t - \partial_x^2$ on $\R^2$ with variables $(t, x)$, the order is $2$ and $\sigma_2(P)((t, x), (\tau, \xi)) = -\xi^2$.
So $\operatorname{Char}(P)$ consists of the covectors with $\xi = 0$, that is, $(\tau, 0)$ with $\tau \ne 0$.
The lines $t = \text{const}$ have normal $(1, 0)$, so they are characteristic for the heat operator.
Non-example: for the same operator the lines $x = \text{const}$ have normal $(0, 1)$, and $\sigma_2 = -1 \ne 0$ there, so they are noncharacteristic.
The set $\operatorname{Char}(P)$ is conic: if $(x, \xi)$ lies in it, so does $(x, \lambda \xi)$ for every real $\lambda \ne 0$.
The operator is [[elliptic|B4TTNHSTRX]] exactly when $\operatorname{Char}(P)$ is empty.

## Explanations

### L1 human

The characteristic variety is the zero set of the principal symbol, with the zero covector removed.
