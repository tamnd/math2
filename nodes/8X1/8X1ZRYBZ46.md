---
tag: 8X1ZRYBZ46
kind: definition
name: Property (T)
msc: [22D55, 20F65]
defines: GTFZ277047
uses: [0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Kazhdan's_property_(T)
---

## Definition

Let $G$ be a locally compact group, and let $\pi$ be a unitary representation of $G$ on a Hilbert space $\mathcal{H}$.
For a [[compact|0TVJZYB6SH]] set $Q \subseteq G$ and $\varepsilon > 0$, a unit vector $\xi \in \mathcal{H}$ is *$(Q, \varepsilon)$-invariant* if $\norm{\pi(g) \xi - \xi} < \varepsilon$ for all $g \in Q$.
A vector $\xi$ is *invariant* if $\pi(g) \xi = \xi$ for all $g \in G$.
The group $G$ has *property (T)* if there exist a compact set $Q \subseteq G$ and $\varepsilon > 0$ with the following property.
Every unitary representation of $G$ with a $(Q, \varepsilon)$-invariant unit vector has a nonzero invariant vector.

## Remarks

Example: every compact group $G$ has property (T), with $Q = G$ and $\varepsilon = \sqrt{2}$.
If $\norm{\pi(g)\xi - \xi} < \sqrt{2}$ for all $g$, then $\mathrm{Re} \ip{\pi(g)\xi}{\xi} > 0$ for all $g$.
The average $\eta = \int_G \pi(g) \xi \, dg$ over the normalised Haar measure is invariant, and $\mathrm{Re} \ip{\eta}{\xi} > 0$, so $\eta \neq 0$.

Non-example: $\Z$ does not have property (T).
Here compact sets are finite.
In the regular representation on $\ell^2(\Z)$, let $\xi_N = N^{-1/2} \mathbf{1}_{\set{0, \ldots, N-1}}$.
Then $\norm{\pi(k)\xi_N - \xi_N} \le \sqrt{2\abs{k}/N}$, which is small on any finite $Q$ when $N$ is large.
But a nonzero vector of $\ell^2(\Z)$ invariant under all shifts would have constant coordinates and infinite norm.

Equivalently, the trivial representation is an isolated point of the unitary dual of $G$ in the Fell topology.
For a discrete group, $Q$ can be taken finite, and a discrete group with property (T) is finitely generated.
The groups $\mathrm{SL}_n(\R)$ and $\mathrm{SL}_n(\Z)$ have property (T) for $n \ge 3$, but not for $n = 2$.
