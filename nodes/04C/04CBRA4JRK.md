---
tag: 04CBRA4JRK
kind: statement
role: proposition
name: log x is at most x - 1
msc: [33B10, 26D15]
uses: [012C7GFF20, 0RKW2X63YR]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Statement

For every real $x > 0$,
$$\ln x \le x - 1,$$
with equality if and only if $x = 1$.

## Remarks

Put $\ln x$ into the inequality [[$1 + y \le e^y$|012C7GFF20]]. Then $1 + \ln x \le e^{\ln x} = x$.
The line $y = x - 1$ is the tangent to the graph of $\ln$ at $x = 1$.
Replacing $x$ by $1/x$ gives $\ln x \ge 1 - 1/x$. Mathlib states the main claim as `Real.log_le_sub_one_of_pos`.

## Explanations

### L1 human

The graph of $\ln$ lies below its tangent line at $x = 1$.
This follows from the concavity of the logarithm.
