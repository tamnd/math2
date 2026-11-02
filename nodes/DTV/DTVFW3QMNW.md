---
tag: DTVFW3QMNW
kind: problem
name: Moser's worm problem
msc: [52C15, 52A40]
uses: [0TH78S7GBZ, 02HPP5VCZH, EWS4WFTA7W]
about: [EWS4WFTA7W]
sources:
  - url: https://en.wikipedia.org/wiki/Moser%27s_worm_problem
same_as:
  wikidata: Q15904307
  wikipedia: Moser's worm problem
history:
  posed_by: "Leo Moser"
  first_stated: "1966"
---

## Problem

Call a region $R$ in the plane a *worm cover* if it has the following property.
For every [[plane curve|EWS4WFTA7W]] $\gamma$ of [[length|0TH78S7GBZ]] $1$, some [[isometry|02HPP5VCZH]] $g$ of the plane satisfies $g(\gamma) \subseteq R$.
Find the smallest possible area of a worm cover.

## Remarks

The problem is open; most work concerns convex worm covers.
A disc of radius $1/2$ is such a region, so the answer is at most $\pi / 4$.
Indeed, let $m$ be the point of $\gamma$ at arc length $1/2$ from an end.
Every point of $\gamma$ is joined to $m$ by an arc of length at most $1/2$, so it lies within distance $1/2$ of $m$.
Much smaller convex worm covers are known.

## Explanations

### L1 human

Picture a worm of length one that can curl up in any way.
What is the smallest blanket that can always be placed over the worm, whatever its shape?
A round blanket of diameter one works, but smaller shapes also work, and the best one is not known.
