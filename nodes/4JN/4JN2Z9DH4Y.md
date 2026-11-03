---
tag: 4JN2Z9DH4Y
kind: concept
name: Rate–distortion function
msc: [94A34, 94A17]
sources:
  - url: https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory
---

## Summary

The rate–distortion function $R(D)$ of a source is the least number of bits per symbol that describe the source within average distortion $D$.
It is the least mutual information between the source and a reproduction, over all reproductions with average distortion at most $D$.
Shannon's rate–distortion theorem says that this formula equals the best rate achievable by actual codes.
It is a non-increasing convex function of $D$.

## Explanations

### L1 human

The more error one tolerates, the fewer bits one needs, and $R(D)$ makes this exact.
When the distortion counts wrong symbols, at $D = 0$ it is the entropy of the source, the cost of a perfect copy.
For large enough $D$ it is $0$, because then one can always output the same guess.
For a fair coin with error rate $D \le 1/2$ it equals $1 - h(D)$, where $h$ is the binary entropy function.
