---
tag: ~ac09da6e
kind: statement
role: theorem
name: Logarithm is the inverse of the exponential
msc: [33B10]
uses: [~317c1d19, ~865c5f29, ~3bd5368b]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Statement

For every real $x > 0$, $e^{\ln x} = x$. For every real $y$, $\ln(e^y) = y$.
The function $\ln$ is continuous and strictly increasing on $(0, \infty)$, and its range is $\mathbb{R}$.

## Remarks

The two identities say that $\ln$ and $\exp$ are inverse bijections between $(0, \infty)$ and $\mathbb{R}$.
Continuity follows from the [[continuity of inverse functions|~3bd5368b]], since $\exp$ is [[strictly increasing|~865c5f29]] and continuous.
Also $\ln x \to \infty$ as $x \to \infty$, and $\ln x \to -\infty$ as $x \to 0^+$. Mathlib states the first identity as `Real.exp_log`.

## Explanations

### L1 human

Taking $\ln$ undoes taking $\exp$, and the other way round.
The graph of $\ln$ is the mirror image of the graph of $e^x$ in the line $y = x$.
