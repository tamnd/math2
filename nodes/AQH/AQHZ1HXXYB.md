---
tag: AQHZ1HXXYB
kind: concept
name: Rényi entropy
msc: [94A17]
sources:
  - url: https://en.wikipedia.org/wiki/R%C3%A9nyi_entropy
same_as:
  wikidata: Q1433083
  wikipedia: Rényi entropy
---

## Summary

The Rényi entropies $H_\alpha(X) = \frac{1}{1 - \alpha} \log \sum_x p(x)^\alpha$ form a family of measures of uncertainty indexed by an order $\alpha \ge 0$, $\alpha \ne 1$.
They were introduced by Alfréd Rényi in 1961 as generalizations of the [[Shannon entropy|Y86E072V0V]], which is the limit as $\alpha \to 1$.
Other members are the Hartley entropy ($\alpha = 0$), the collision entropy ($\alpha = 2$) and the [[min-entropy|G47K6AJT8N]] ($\alpha \to \infty$).
They are used in cryptography, in the study of randomness extraction, in statistics and in quantum information theory.

## Explanations

### L1 human

Shannon entropy averages the surprise of the outcomes in one particular way.
Rényi entropies average it in other ways, with a parameter $\alpha$ that decides how much weight the likely outcomes get.
Small $\alpha$ treats all possible outcomes almost alike, and large $\alpha$ looks mostly at the most likely outcome.
For a uniform law on $n$ outcomes all Rényi entropies agree and equal $\log n$.
For other laws they differ, and they decrease as $\alpha$ grows.
