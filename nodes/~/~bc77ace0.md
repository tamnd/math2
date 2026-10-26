---
tag: ~bc77ace0
kind: concept
name: Multi-index notation
aliases: [multi-index]
msc: [26B99]
uses: [~ff1fb7d0]
sources:
  - url: https://en.wikipedia.org/wiki/Multi-index_notation
    locator: Definition and basic properties
same_as:
  wikidata: Q780239
  wikipedia: Multi-index notation
---

## Summary

A multi-index of dimension $n$ is an $n$-tuple $\alpha = (\alpha_1, \dots, \alpha_n)$ of non-negative integers.
With $|\alpha| = \alpha_1 + \dots + \alpha_n$, $\alpha! = \alpha_1! \cdots \alpha_n!$, $x^\alpha = x_1^{\alpha_1} \cdots x_n^{\alpha_n}$ and $\partial^\alpha = \partial_1^{\alpha_1} \cdots \partial_n^{\alpha_n}$, formulas of several variables take the short form of their one-variable versions.

## Remarks

Here $\partial_i$ is the [[partial derivative|~ff1fb7d0]] with respect to $x_i$, and $\partial^\alpha f$ is a partial derivative of order $|\alpha|$.
For $\alpha = (2, 0, 1)$, $|\alpha| = 3$, $\alpha! = 2$, $x^\alpha = x_1^2 x_3$ and $\partial^\alpha f = \partial^3 f / \partial x_1^2 \, \partial x_3$.
The notation $\partial^\alpha f$ does not show the order of differentiation. It is unambiguous when $f$ is of class $C^{|\alpha|}$, by [[Schwarz's theorem|~08d2c32d]].
Examples of use are [[Taylor's theorem in several variables|~3353d047]] and the multinomial theorem $(x_1 + \dots + x_n)^k = \sum_{|\alpha| = k} \frac{k!}{\alpha!} x^\alpha$.

## Explanations

### L1 human

Multi-index notation is a bookkeeping device.
One symbol $\alpha$ records how many times each variable appears, so one formula covers all mixed derivatives or monomials of a given order.
