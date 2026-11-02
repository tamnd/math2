---
tag: YGK9CD7SME
kind: definition
name: Reciprocal gamma function
msc: [33B15, 30D15]
defines: PY6K9AWR33
uses: [0V3FZMVB4K, 0419794R0T]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocal_gamma_function
---

## Definition

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], extended to a meromorphic function on $\C$ with poles at $0, -1, -2, \ldots$ and no zeros.
The *reciprocal gamma function* is the function $\C \to \C$ given by
$$\frac{1}{\Gamma}(z) = \begin{cases} 1/\Gamma(z) & \text{if } z \notin \set{0, -1, -2, \ldots}, \\ 0 & \text{if } z \in \set{0, -1, -2, \ldots}. \end{cases}$$

## Remarks

It is an [[entire function|0419794R0T]]: near a pole $-n$ of $\Gamma$, the quotient $1/\Gamma$ has a removable singularity with value $0$, because the pole is simple.
Its zeros are exactly $0, -1, -2, \ldots$, and they are simple, with derivative $(-1)^n n!$ at $-n$, the reciprocal of the residue of $\Gamma$.
Example: at $z = 3$ the value is $1/\Gamma(3) = 1/2! = \tfrac12$.
Non-example: $\Gamma$ itself is not entire, since it is not defined at $0$ and $\abs{\Gamma(z)} \to \infty$ as $z \to 0$.
It is an entire function of [[order|SHF8Z7GMFX]] $1$ and of maximal type.

## Explanations

### L1 human

The reciprocal gamma function is $1/\Gamma(z)$, with the value $0$ at the points where $\Gamma$ blows up.
These values make it smooth everywhere in the complex plane.
