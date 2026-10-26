---
tag: 0RKW2X63YR
kind: statement
role: theorem
name: Logarithm is the inverse of the exponential
msc: [33B10]
uses: [0044CPHJBV, 0KN2V7840E, 07BY47HG5S]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Statement

For every real $x > 0$, $e^{\ln x} = x$. For every real $y$, $\ln(e^y) = y$.
The function $\ln$ is continuous and strictly increasing on $(0, \infty)$, and its range is $\mathbb{R}$.

## Remarks

The two identities say that $\ln$ and $\exp$ are inverse bijections between $(0, \infty)$ and $\mathbb{R}$.
Continuity follows from the [[continuity of inverse functions|07BY47HG5S]], since $\exp$ is [[strictly increasing|0KN2V7840E]] and continuous.
Also $\ln x \to \infty$ as $x \to \infty$, and $\ln x \to -\infty$ as $x \to 0^+$. Mathlib states the first identity as `Real.exp_log`.

## Explanations

### L1 human

Taking $\ln$ undoes taking $\exp$, and the other way round.
The graph of $\ln$ is the mirror image of the graph of $e^x$ in the line $y = x$.
