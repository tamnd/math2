---
tag: BFQBHBN5F5
kind: concept
name: Empirical likelihood
msc: [62G10, 62G15, 62G20]
sources:
  - url: https://en.wikipedia.org/wiki/Empirical_likelihood
same_as:
  wikidata: Q5374245
  wikipedia: Empirical likelihood
---

## Summary

Empirical likelihood is a method of inference that uses a [[likelihood|0VW9E4QXR6]] ratio without assuming a parametric family.
It assigns unknown weights to the observed data points and maximises the product of the weights under a constraint given by the parameter value.
It then compares the result with the unconstrained maximum.
Art Owen developed it in the late 1980s.
Like a parametric likelihood ratio, it yields tests and confidence regions with chi-squared calibration, and its confidence regions take their shape from the data.

## Explanations

### L1 human

A parametric likelihood asks how probable the data are under a formula for the distribution.
Empirical likelihood avoids the formula: it only allows distributions that put weight on the observed points.
To judge a proposed mean $\mu$, it tilts the weights as little as possible so that the weighted average of the data equals $\mu$.
The more the weights must be tilted, the less plausible $\mu$ is.
If $\mu$ is the sample mean, no tilting is needed and the ratio is $1$.
