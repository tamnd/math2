---
tag: DJ6F3DZX42
kind: definition
name: Measurable space
msc: [28A05]
defines: N4KDT83V3S
uses: [0SJ3RX9TXA, 04WSW8T3SY, 0BVHZXWKCD]
sources:
  - url: https://en.wikipedia.org/wiki/Measurable_space
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]].
A *measurable space* is a pair $(X, \Sigma)$, where $\Sigma$ is a [[σ-algebra|04WSW8T3SY]] on $X$.
The elements of $\Sigma$ are the *measurable sets* of $(X, \Sigma)$.

## Remarks

The real line with its [[Borel σ-algebra|0BVHZXWKCD]] $\mathcal{B}(\R)$ is a measurable space, because $\mathcal{B}(\R)$ is a σ-algebra by its definition.
Any set $X$ with its power set is a measurable space, and so is $X$ with $\set{\varnothing, X}$.
For $X = \set{1, 2}$, the pair $(X, \set{\varnothing, \set{1}, X})$ is not a measurable space.
The family is not closed under complements, since $X \setminus \set{1} = \set{2}$ is missing.
A map $f \colon X \to Y$ between measurable spaces $(X, \Sigma)$ and $(Y, T)$ is called measurable when $f^{-1}(B) \in \Sigma$ for every $B \in T$.
Some authors call a measurable space a *Borel space*.
