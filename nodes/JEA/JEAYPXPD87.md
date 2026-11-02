---
tag: JEAYPXPD87
kind: definition
name: Akaike information criterion
msc: [62B10]
defines: CMAX3KF9H0
uses: [05FSTXM92W, 0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Akaike_information_criterion
---

## Definition

Let $M$ be a parametric statistical model with $k$ free real parameters, and let $x$ be data.
Let $\hat L$ be the maximum over the parameters of the [[likelihood function|05FSTXM92W]] of $M$ at $x$, the value at the [[maximum likelihood estimate|0FREPFKNS7]].
The *Akaike information criterion* of $M$ at $x$ is
$$\mathrm{AIC} = 2k - 2 \ln \hat L.$$
Among several candidate models for the same data, the AIC rule selects a model with the smallest AIC.

## Remarks

Only differences of AIC between models fitted to the same data have a meaning.
Example: a model with $k = 2$ and $\ln \hat L = -100$ has $\mathrm{AIC} = 204$.
A larger model with $k = 3$ and $\ln \hat L = -99.5$ has $\mathrm{AIC} = 205$, so the AIC rule keeps the smaller model.
Non-example: $-2 \ln \hat L$ alone, without the term $2k$, is not the AIC; it always favours the larger of two nested models.
For small samples a corrected version, AICc, adds a further penalty.
The [[Bayesian information criterion|GXP6H9VGRB]] uses the penalty $k \ln n$ in place of $2k$.
