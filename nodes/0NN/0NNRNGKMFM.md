---
tag: 0NNRNGKMFM
kind: definition
name: Moment-generating function
msc: ["60E10"]
defines: 0WQVXP7PDB
uses: [0DCT0QZVQ1, 0PH0VHTQS0]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_generating_function
    locator: Definition
---

## Definition

Let $X$ be a real random variable.
The moment-generating function of $X$ is the function
$$M_X(t) = E\left[e^{tX}\right], \quad t \in \mathbb{R},$$
with values in $(0, \infty]$.

## Remarks

Always $M_X(0) = 1$. The set of $t$ with $M_X(t) < \infty$ is an interval that contains $0$.
If $M_X$ is finite on an open interval around $0$, then all [[moments|0PH0VHTQS0]] of $X$ are finite and $M_X$ determines the law of $X$.
Some random variables have $M_X(t) = \infty$ for all $t \ne 0$. An example is a Cauchy random variable.
For $X \sim \operatorname{Exp}(\lambda)$, $M_X(t) = \lambda / (\lambda - t)$ for $t < \lambda$, and $M_X(t) = \infty$ for $t \ge \lambda$.

## Explanations

### L1 human

The moment-generating function is a tool that turns a distribution into a function of one real variable.
It is useful because sums of independent variables become products, and moments become derivatives.
