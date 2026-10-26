---
tag: ~a4ccb3ae
kind: definition
name: Open map
aliases: [open-mapping]
msc: [54C10]
defines: ~304128e6
uses: [~77bfcc55, ~159c5927, 0Q3F20XB0A]
sources:
  - url: https://en.wikipedia.org/wiki/Open_and_closed_maps
    locator: Definitions and characterizations
---

## Definition

Let $X$ and $Y$ be [[topological spaces|~77bfcc55]].
A function $f \colon X \to Y$ is an open map when for each [[open set|~159c5927]] $U$ of $X$, the [[image|0Q3F20XB0A]] $f(U)$ is open in $Y$.

## Remarks

The [[projections of a product|~d7bf67d8]] $X \times Y \to X$ are open maps.
A continuous bijection is a [[homeomorphism|~0e10d672]] if and only if it is an open map.
The map $\mathbb{R} \to \mathbb{R}$, $x \mapsto x^2$, is continuous but not open: the image of $(-1, 1)$ is $[0, 1)$.

## Explanations

### L1 human

An open map keeps open sets open when you push them forward.
Continuity is about pulling open sets back, so the two notions are different.
