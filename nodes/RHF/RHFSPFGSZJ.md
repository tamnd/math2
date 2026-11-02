---
tag: RHFSPFGSZJ
kind: example
name: Steiner chain
msc: [51M04, 51B10]
illustrates: [YXST7NGMTC]
uses: [060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Steiner_chain
same_as:
  wikidata: Q1368121
  wikipedia: Steiner chain
---

## Example

Let $\alpha$ and $\beta$ be two [[circles|060W5CBZP6]] in the plane with $\beta$ inside $\alpha$ and no common point.
A *Steiner chain* for $\alpha$ and $\beta$ is a cyclic sequence of $n \ge 3$ circles $\gamma_1, \ldots, \gamma_n$ with two properties.
Each $\gamma_i$ is tangent to $\alpha$ from inside and to $\beta$ from outside.
Each $\gamma_i$ is tangent to $\gamma_{i+1}$, where $\gamma_{n+1} = \gamma_1$.

Take $\alpha$ of radius $3$ and $\beta$ of radius $1$, both centred at the origin.
Let $\gamma_k$ be the circle of radius $1$ centred at $2(\cos(k\pi/3), \sin(k\pi/3))$ for $k = 1, \ldots, 6$.
The centre of $\gamma_k$ is at distance $2 = 3 - 1$ from the origin, so $\gamma_k$ touches $\alpha$ from inside.
It is also at distance $2 = 1 + 1$, so $\gamma_k$ touches $\beta$ from outside.
Two consecutive centres are at distance $2 \cdot 2 \sin(\pi/6) = 2$, the sum of the radii, so $\gamma_k$ and $\gamma_{k+1}$ touch.
So these six circles form a Steiner chain.

## Remarks

For concentric circles of radii $R > r$, a chain of $n$ circles that goes once around $\beta$ exists exactly when $\sin(\pi/n) = (R - r)/(R + r)$.
Steiner's porism says that if one chain closes up for $\alpha$ and $\beta$, then a chain closes up starting from any first circle tangent to both.
The proof uses an [[inversion in a circle|YXST7NGMTC]] that sends $\alpha$ and $\beta$ to concentric circles, where rotation moves one chain to any other.

## Explanations

### L1 human

Put a small coin inside a large ring, and fill the space between them with coins that touch both and touch their neighbours.
For the right sizes, the coins close up into a full necklace.
Then the necklace can be rolled around: start it from any position and it still closes up.
