---
tag: 0KH1N66QWW
kind: definition
name: Dirichlet convolution
aliases: [dirichlet-product]
msc: [11A25]
defines: 037F589D1D
uses: [0H2EPRZC0D, 0FCWA16FZE]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_convolution
    locator: Definition
---

## Definition

Let $f$ and $g$ be [[arithmetic functions|0H2EPRZC0D]].
Their Dirichlet convolution is the arithmetic function $f * g$ given by
$$(f * g)(n) = \sum_{d \mid n} f(d) \, g\!\left(\frac{n}{d}\right)$$
for each positive integer $n$, where $d$ runs over the [[positive divisors|0FCWA16FZE]] of $n$.

## Remarks

The convolution is commutative and associative, and it distributes over addition.
The identity element is $\varepsilon$, with $\varepsilon(1) = 1$ and $\varepsilon(n) = 0$ for $n > 1$.
An arithmetic function $f$ has an inverse for $*$ if and only if $f(1) \ne 0$.
For example, with the constant function $\mathbf{1}$, $(\mathbf{1} * \mathbf{1})(n)$ is the [[number of divisors|0BKJT6WG96]] of $n$.

## Explanations

### L1 human

The Dirichlet convolution combines two functions by a sum over the factorizations $n = d \cdot e$.
It is the natural product for functions defined by sums over divisors.
