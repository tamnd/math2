---
tag: 0GPFKS96T7
kind: statement
role: proposition
name: Cardinality of the power set
msc: ["03E10"]
uses: [0BC7KX51Z8, 0VSB0XF4G7, 0JTGRV4WT4]
sources:
  - url: https://en.wikipedia.org/wiki/Power_set
    locator: Representing subsets as functions
---

## Statement

Let $A$ be a [[set|0SJ3RX9TXA]].
Then the [[power set|0BC7KX51Z8]] of $A$ is equinumerous with the set $\{0, 1\}^A$ of functions from $A$ to $\{0, 1\}$, so
$$|\mathcal{P}(A)| = 2^{|A|}.$$

## Remarks

The bijection sends a subset $S$ to its [[indicator function|0VSB0XF4G7]] $\mathbf{1}_S$.
For a finite set with $n$ elements, the power set has $2^n$ elements.
For $A = \mathbb{N}$, $|\mathcal{P}(\mathbb{N})| = 2^{\aleph_0}$, the [[cardinality of the continuum|0WC28W9DNM]].

## Explanations

### L1 human

A subset is a choice of "in" or "out" for each element.
With $n$ elements, there are $2 \cdot 2 \cdots 2 = 2^n$ such choices.
