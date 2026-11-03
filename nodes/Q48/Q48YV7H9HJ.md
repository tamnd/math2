---
tag: Q48YV7H9HJ
kind: definition
name: Binary entropy function
msc: [94A17]
defines: GW25TGD33J
uses: [Y86E072V0V, 04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_entropy_function
---

## Definition

The *binary entropy function* is the function $H_b \colon [0, 1] \to [0, 1]$ given by
$$H_b(p) = -p \log_2 p - (1 - p) \log_2 (1 - p),$$
with the convention $0 \log_2 0 = 0$, so that $H_b(0) = H_b(1) = 0$.

## Remarks

$H_b(p)$ is the [[Shannon entropy|Y86E072V0V]] in bits of a random variable that takes two values with probabilities $p$ and $1 - p$.

Example: $H_b(\frac12) = -\frac12 \log_2 \frac12 - \frac12 \log_2 \frac12 = 1$, and $H_b(\frac14) = \frac14 \cdot 2 + \frac34 \log_2 \frac43 \approx 0.811$.

Non-example: the formula has no meaning at $p = 2$ as an entropy, because $1 - p < 0$ is not a probability; $H_b$ is defined only on $[0, 1]$.

The function is symmetric, $H_b(p) = H_b(1 - p)$, continuous, and strictly concave on $[0, 1]$.
Its derivative on $(0, 1)$ is $H_b'(p) = \log_2 \frac{1 - p}{p}$.
Some authors use the [[natural logarithm|04DXAFN2ES]] instead; this gives $H_b(p) \ln 2$, measured in nats.
In Mathlib, the natural-logarithm version is `Real.binEntropy`.

## Explanations

### L1 human

It is the entropy of a single biased coin, as a function of its bias.
