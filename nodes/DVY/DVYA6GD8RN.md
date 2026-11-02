---
tag: DVYA6GD8RN
kind: problem
name: Plateau's problem
msc: [49Q05, 53A10, "58E12"]
uses: [41X0YW2R9N, 0DEB0JMN0W, 0YYT36R4YD]
about: [41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Plateau%27s_problem
same_as:
  wikidata: Q1972021
  wikipedia: Plateau's problem
history:
  posed_by: "Joseph-Louis Lagrange"
  first_stated: "1760"
---

## Problem

Let $\Gamma$ be a Jordan curve in $\R^3$, that is, a subset homeomorphic to a circle.
Is there a surface of least area among all surfaces with boundary $\Gamma$?

## Remarks

The problem is named after Joseph Plateau, who studied soap films spanning wire frames by experiment.
Jesse Douglas and Tibor Radó solved it independently for surfaces of the type of a disc, around 1930.
Their result applies to a rectifiable $\Gamma$ and gives a continuous map $X$ from the closed unit disc $\overline{D}$ to $\R^3$.
The map sends the boundary circle homeomorphically onto $\Gamma$.
It is [[harmonic|0DEB0JMN0W]] in the open disc and [[conformal|0YYT36R4YD]] away from isolated branch points.
It has least area among all such disc-type surfaces spanning $\Gamma$.
The image of $X$ is then a [[minimal surface|41X0YW2R9N]], possibly with branch points.
Douglas received one of the first two Fields Medals in 1936, in part for this work.
Later, geometric measure theory treated the problem in higher dimensions and without a fixed topological type, with solutions such as integral currents.
The least-area surface need not be unique, and it need not be a disc: some curves are spanned by surfaces of other types with smaller area.

## Explanations

### L1 human

Bend a wire into a closed loop, dip it in soapy water, and a film appears that spans the loop with as little area as it can.
Plateau's problem asks whether such a least-area surface always exists, as a mathematical object, for every loop.
The answer is yes for disc-shaped surfaces, and the proof was one of the great successes of analysis in the twentieth century.
