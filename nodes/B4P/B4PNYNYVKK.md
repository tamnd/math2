---
tag: B4PNYNYVKK
kind: concept
name: Differential entropy
msc: [94A17, 62B10]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_entropy
same_as:
  wikidata: Q3055345
  wikipedia: Differential entropy
---

## Summary

The differential entropy of a random vector $X$ with [[probability density function|0ZY9DX8FBF]] $f$ is $h(X) = -\int f(x) \log f(x) \, dx$.
It is the analogue of the [[Shannon entropy|Y86E072V0V]] for continuous random variables, introduced by Shannon.
Unlike Shannon entropy, it can be negative and it changes under a change of scale, so it is not an absolute measure of information.
Differences of differential entropies, such as mutual information, keep their meaning, and differential entropy is the basic quantity for Gaussian channels.

## Explanations

### L1 human

For a continuous quantity, such as a length, there are infinitely many possible values, and describing one exactly would need infinitely many bits.
Differential entropy measures instead how spread out the density is, on a logarithmic scale.
A uniform law on an interval of length $a$ has differential entropy $\log a$.
So an interval of length $1$ gives $0$, a longer interval gives a positive value, and a shorter one gives a negative value.
Measuring the same quantity in millimetres instead of metres adds $\log 1000$ to the result.
