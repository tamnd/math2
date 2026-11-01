---
tag: 8G5ABXRK85
kind: object
name: Unit disc
msc: [30J99, 30C20]
instance_of: [0QW64ARSHB, 0EWMDD6C14]
sources:
  - url: https://en.wikipedia.org/wiki/Unit_disk
same_as:
  wikidata: Q2390323
  wikipedia: Unit disk
---

## Description

The *open unit disc* is $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$, and the *closed unit disc* is $\overline{\mathbb{D}} = \set{z \in \C : \abs{z} \le 1}$.
The open disc is open, since it is the preimage of $(-\infty, 1)$ under the continuous map $z \mapsto \abs{z}$, and it is connected, since it is convex.
So it is a [[domain in the complex plane|0EWMDD6C14]].
It is star-shaped about $0$, so every closed curve in it contracts to $0$ along straight segments, and it is a [[simply connected domain|0QW64ARSHB]].
Its boundary is the unit circle $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$.

## Remarks

By the [[Riemann mapping theorem|02WHMEG5ZR]], every simply connected domain other than $\C$ is conformally equivalent to $\mathbb{D}$.
The Cayley map $z \mapsto (z - i)/(z + i)$ is a conformal map of the upper half-plane onto $\mathbb{D}$.
The conformal automorphisms of $\mathbb{D}$ are the [[Möbius transformations|0SG74WBFA2]] $z \mapsto e^{i\theta}(z - a)/(1 - \bar a z)$ with $\abs{a} < 1$ and real $\theta$.
With the hyperbolic metric it becomes the [[Poincaré disk model|85MM2EA0TK]] of the hyperbolic plane.

## Explanations

### L1 human

The unit disc is the set of complex numbers at distance less than $1$ from $0$: a round region without its rim.
It is the standard domain of complex analysis, because by the Riemann mapping theorem many other regions can be turned into it without distorting small angles.
Function spaces such as the [[Hardy spaces|PNNNFJVF6W]] and the [[Bergman spaces|2D619WTPYC]] are usually first defined on the unit disc.
