---
tag: K6MCP56ETX
kind: concept
name: Cross-entropy
msc: [94A17, 68T05]
sources:
  - url: https://en.wikipedia.org/wiki/Cross-entropy
same_as:
  wikidata: Q1685498
  wikipedia: Cross-entropy
---

## Summary

The cross-entropy of a law $q$ relative to a law $p$ is $H(p, q) = -\sum_x p(x) \log q(x)$.
It is the average number of bits needed to encode outcomes drawn from $p$ with a code designed for $q$.
It splits as $H(p, q) = H(p) + D(p \,\|\, q)$, the [[Shannon entropy|Y86E072V0V]] of $p$ plus the [[Kullback–Leibler divergence|PQBW43X5RE]].
So by [[Gibbs' inequality|55WNT5655E]] it is smallest when $q = p$.
In statistics and machine learning, minimizing cross-entropy with respect to a model $q$ is the same as maximizing the likelihood of the data.

## Explanations

### L1 human

Imagine you compress a text with a code built for English, while the text is in French.
The code still works, but the files are longer than with a code built for French.
The cross-entropy is the average length you get; the extra length beyond the true entropy is the price of the wrong model.
For example, coding a fair coin with a code built for a coin with heads probability $\frac14$ costs on average $\frac12 \cdot 2 + \frac12 \log_2 \frac43 \approx 1.21$ bits instead of $1$ bit.
