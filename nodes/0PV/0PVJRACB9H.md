---
tag: 0PVJRACB9H
kind: statement
role: proposition
name: The exponential series has infinite radius of convergence
msc: [30B10, 33B10]
uses: [0JBMYAA9QH, 0660QX1VPR]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Power series
---

## Statement

The [[radius of convergence|0660QX1VPR]] of the power series $\sum_{n=0}^{\infty} \frac{x^n}{n!}$ is $\infty$.
So the series converges absolutely for every real $x$.

## Remarks

The ratio of consecutive coefficients is $\frac{1/(n+1)!}{1/n!} = \frac{1}{n + 1} \to 0$. The [[ratio formula|0JBMYAA9QH]] then gives radius $\infty$.
The same holds for the series of sine, cosine, $\sinh$ and $\cosh$.
Mathlib states it as `NormedSpace.expSeries_radius_eq_top`.

## Explanations

### L1 human

The factorials in the denominators grow faster than every power $x^n$.
So the terms of the series go to $0$ fast, for each fixed $x$.
