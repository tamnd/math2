---
tag: JJ5XQEVBZ4
kind: definition
name: Microlocal analysis
msc: [35A27, 35S05, 58J40]
defines: 5B6WEQX7XK
uses: [DPVM34ADZV, 3T5Q9WVQX8, FF27N0BWTP]
sources:
  - url: https://en.wikipedia.org/wiki/Microlocal_analysis
---

## Definition

Let $X$ be an open subset of $\R^n$, or a smooth manifold, with cotangent bundle $T^*X$.
*Microlocal analysis* studies distributions and linear operators on $X$ through properties localized at points $(x, \xi) \in T^*X \setminus 0$.
Here $x$ is a position and $\xi \neq 0$ is a frequency direction.
A property holds *microlocally* near $(x_0, \xi_0)$ if it holds after cutting off near $x_0$ and keeping only frequencies in a conic neighbourhood of $\xi_0$.
The basic notions are:

1. The [[wave front set|3T5Q9WVQX8]] $\mathrm{WF}(u) \subset T^*X \setminus 0$ of a distribution $u$: the set of $(x_0, \xi_0)$ near which $u$ fails to be smooth microlocally.
2. Properly supported [[pseudo-differential operators|FF27N0BWTP]], which act microlocally and satisfy $\mathrm{WF}(Pu) \subseteq \mathrm{WF}(u)$.

## Remarks

Example: let $u = H(x_1)$ on $\R^2$, where $H$ is the Heaviside function.
Then $u$ is smooth off the line $x_1 = 0$, and $\mathrm{WF}(u) = \set{(x, \xi) : x_1 = 0, \ \xi = (\xi_1, 0), \ \xi_1 \neq 0}$.
The check: take a cutoff $\chi(x)$ near a point of the line.
The [[Fourier transform|DPVM34ADZV]] of $\chi u$ decays rapidly in every closed cone avoiding the $\xi_1$-axis, but only like $\abs{\xi_1}^{-1}$ along it.
Non-example: classical local regularity, such as "$u$ is smooth near $x_0$", is not a microlocal statement, since it does not distinguish frequency directions.
The projection of $\mathrm{WF}(u)$ to $X$ is the singular support: $\pi(\mathrm{WF}(u)) = \operatorname{sing\,supp} u$.
