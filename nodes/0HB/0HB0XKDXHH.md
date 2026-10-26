---
tag: 0HB0XKDXHH
kind: example
name: Binomial series
msc: [30B10]
instance_of: [0MZB06ST2B]
uses: [0VP56B4EMX, 0KX1MXJ5MR]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_series
    locator: lead section
same_as:
  wikidata: Q833480
  wikipedia: Binomial series
---

## Example

Let $\alpha$ be a real number.
For each natural number $k$, let
$$\binom{\alpha}{k} = \frac{\alpha (\alpha - 1) \cdots (\alpha - k + 1)}{k!}.$$
The binomial series is the [[power series|0VP56B4EMX]] $\sum_{k=0}^{\infty} \binom{\alpha}{k} x^k$.
For $|x| < 1$ its sum is $(1 + x)^{\alpha}$.

## Remarks

If $\alpha$ is a natural number, then $\binom{\alpha}{k} = 0$ for $k > \alpha$. The series is then the binomial formula for $(1 + x)^{\alpha}$.
Otherwise the [[radius of convergence is 1|0KX1MXJ5MR]].
For $\alpha = -1$ it is the geometric series $\sum (-1)^k x^k = 1/(1 + x)$.
For $\alpha = 1/2$ it gives $\sqrt{1 + x} = 1 + x/2 - x^2/8 + \cdots$.

## Explanations

### L1 human

The binomial series extends the binomial formula to exponents that are not natural numbers.
The expansion then has infinitely many terms, and it holds only for small $x$.
