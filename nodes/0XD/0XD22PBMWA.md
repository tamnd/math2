---
tag: 0XD22PBMWA
kind: statement
role: proposition
name: Monotonicity of the cumulative distribution function
msc: ["60E05"]
uses: [0MXMS3AE13, 0464Z0JP2E]
sources:
  - url: https://en.wikipedia.org/wiki/Cumulative_distribution_function
    locator: Properties
---

## Statement

Let $X$ be a real random variable with [[cumulative distribution function|0MXMS3AE13]] $F_X$.
Then $F_X$ is nondecreasing: if $x \le y$, then $F_X(x) \le F_X(y)$.

## Remarks

The proof: $\{X \le x\} \subseteq \{X \le y\}$, so the claim follows from the [[monotonicity of probability|0464Z0JP2E]].
More precisely, $F_X(y) - F_X(x) = P(x < X \le y) \ge 0$.
A nondecreasing function has at most countably many points of discontinuity. So $P(X = x) > 0$ for at most countably many $x$.

## Explanations

### L1 human

As $x$ moves to the right, the event "$X \le x$" contains more outcomes, so its probability cannot go down.
