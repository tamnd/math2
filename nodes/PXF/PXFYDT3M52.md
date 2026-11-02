---
tag: PXFYDT3M52
kind: concept
name: Pivotal quantity
msc: [62F25, "62E15"]
sources:
  - url: https://en.wikipedia.org/wiki/Pivotal_quantity
same_as:
  wikidata: Q7199665
  wikipedia: Pivotal quantity
---

## Summary

A pivotal quantity is a function of the data and the unknown parameter whose law does not depend on the parameter.
It is the standard tool to build a [[confidence interval|0S6T9KQNC0]]: one fixes an interval of probability $1 - \alpha$ for the pivot and solves for the parameter.
Many classical intervals, such as the Student t interval for a normal mean, come from a pivot.

## Explanations

### L1 human

A statistic cannot contain the unknown parameter, but a pivot may.
The point is that the pivot has a known law whatever the true parameter is.
For example, if $X$ is normal with unknown mean $\mu$ and variance $1$, then $X - \mu$ is standard normal for every $\mu$.
So $X - \mu$ lies in $[-1.96, 1.96]$ with probability about $0.95$, and this gives the interval $[X - 1.96, X + 1.96]$ for $\mu$.
