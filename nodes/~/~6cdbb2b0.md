---
tag: ~6cdbb2b0
kind: statement
role: theorem
name: Expectation of a product of independent random variables
aliases: [multiplicativity-of-expectation]
msc: [60A05]
uses: [~cd613feb, ~296c063d, ~05dccacd]
sources:
  - url: https://en.wikipedia.org/wiki/Expected_value
    locator: Properties
---

## Statement

Let $X$ and $Y$ be [[independent|~296c063d]] integrable real random variables.
Then $XY$ is integrable and
$$E[XY] = E[X] \, E[Y].$$

## Remarks

The proof uses that the joint law of $(X, Y)$ is the [[product of the marginal laws|~05dccacd]], and then Fubini's theorem.
For nonnegative independent $X$ and $Y$, the equality holds in $[0, \infty]$ without integrability.
The converse is false: $E[XY] = E[X] \, E[Y]$ means only that $X$ and $Y$ are uncorrelated.
More generally, $E[g(X) \, h(Y)] = E[g(X)] \, E[h(Y)]$ for measurable $g$ and $h$ with $g(X)$ and $h(Y)$ integrable.

## Explanations

### L1 human

For independent variables, the average of a product is the product of the averages.
For two fair dice, the expected product of the two results is $3.5 \cdot 3.5 = 12.25$.
