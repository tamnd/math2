---
tag: 0KE6NBTVY8
kind: definition
name: Exponential generating function
msc: [05A15]
defines: 0JHXPVFKT0
uses: [072W67KFYK]
sources:
  - url: https://en.wikipedia.org/wiki/Generating_function
    locator: Exponential generating function (EGF)
inventory: [X6AGSJFM3Y]
---

## Definition

Let $K$ be a field of characteristic $0$, for example $\mathbb{Q}$ or $\mathbb{R}$, and let $(a_n)_{n \ge 0}$ be a sequence in $K$.
The exponential generating function of $(a_n)$ is the [[formal power series|072W67KFYK]]
$$\hat{A}(x) = \sum_{n \ge 0} a_n \frac{x^n}{n!} \in K[\![x]\!].$$

## Remarks

The constant sequence $1$ has the exponential generating function $e^x = \sum_n x^n / n!$.
For exponential generating functions, the product corresponds to the binomial convolution $c_n = \sum_{k=0}^{n} \binom{n}{k} a_k b_{n-k}$.
They suit labelled structures. For example, the [[derangement numbers|03WY4HHMT1]] have the exponential generating function $\frac{e^{-x}}{1 - x}$.

## Explanations

### L1 human

An exponential generating function divides the $n$-th term by $n!$ before it puts it in the series.
This makes the series of fast-growing sequences, such as $n!$, easy to handle: the sequence $n!$ gives $\frac{1}{1 - x}$.
