---
tag: BQ441SGBBA
kind: definition
name: Holographic principle
msc: ["83E05", 81T35]
defines: XVZZF47Z3Q
uses: [ANNJ7JR36T, 7C2CSSHPKA, YHJ0PDNY8T]
sources:
  - url: https://en.wikipedia.org/wiki/Holographic_principle
---

## Definition

Let $\ell_P = \sqrt{\hbar G / c^3}$ be the Planck length and let $k_B$ be Boltzmann's constant.
Let $\mathcal{V}$ be a spatial region whose boundary has area $A$.
The *holographic principle* is the postulate that, in quantum gravity, the physics of $\mathcal{V}$ is described by degrees of freedom on its boundary.
In particular the entropy $S$ of $\mathcal{V}$ satisfies
$$S \le \frac{k_B A}{4 \ell_P^2}.$$
In other words, the number of independent quantum states of the region is at most $e^{A / 4\ell_P^2}$.

## Remarks

The bound is saturated by a [[black hole|YHJ0PDNY8T]] whose horizon has area $A$, by the [[Bekenstein–Hawking entropy|ANNJ7JR36T]] $S = k_B A / 4\ell_P^2$.
The usual argument goes as follows.
If a region held more entropy, adding matter until it collapses into a black hole of area at most $A$ would decrease the entropy, against the second law.
Example: for a sphere of radius $1$ m, $A \approx 12.6$ m$^2$ and $\ell_P^2 \approx 2.6 \times 10^{-70}$ m$^2$, so the bound is about $1.2 \times 10^{70} k_B$.
Non-example: a local quantum field theory without gravity in the region, cut off at the Planck length, has about $V / \ell_P^3$ degrees of freedom.
This grows with the volume and violates the bound for large regions.
The naive spacelike bound fails in some cosmological and collapsing situations; Bousso's covariant entropy bound (1999) states the principle on light sheets instead of volumes.
It is related to the [[Bekenstein bound|7C2CSSHPKA]] on the entropy of a system of given size and energy.
