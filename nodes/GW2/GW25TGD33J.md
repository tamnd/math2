---
tag: GW25TGD33J
kind: concept
name: Binary entropy function
msc: [94A17]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_entropy_function
same_as:
  wikidata: Q4913893
  wikipedia: Binary entropy function
---

## Summary

The binary entropy function $H_b(p) = -p \log_2 p - (1 - p) \log_2 (1 - p)$ is the [[Shannon entropy|Y86E072V0V]] of a coin that shows heads with probability $p$.
It is a concave function on $[0, 1]$, with value $0$ at the ends and maximum $1$ at $p = \frac12$.
It appears in the capacity $1 - H_b(p)$ of the [[binary symmetric channel|W773330RK7]] and in estimates of binomial coefficients, such as $\binom{n}{k} \le 2^{n H_b(k/n)}$.

## Explanations

### L1 human

Take a biased coin and ask how much information one toss gives.
If the coin is fair, one toss gives a full bit.
If the coin always lands heads, it gives nothing.
The binary entropy function draws the curve between these cases: it is a hump over $[0, 1]$, highest in the middle.
For example, a coin with heads probability $0.1$ gives about $0.47$ bits per toss.
