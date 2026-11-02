---
tag: BXVVXJQV8M
kind: definition
name: Regular summability method
msc: [40C99, 40D05]
defines: 29C7C41A52
uses: [X80DZEXQDQ, 0AZ3R52593]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Definition

Let $M \colon D_M \to \mathbb{K}$ be a [[summability method|X80DZEXQDQ]], where $\mathbb{K}$ is $\R$ or $\C$.
The method $M$ is *regular* if every [[convergent sequence|0AZ3R52593]] $s$ belongs to $D_M$ and
$$M(s) = \lim_{n \to \infty} s_n.$$
Equivalently, every convergent series is $M$-summable, and its $M$-sum is its ordinary sum.

## Remarks

Example: Cesàro summation is regular, because the [[Cesàro means of a convergent sequence converge to the same limit|0RDRPBMNAC]].
Non-example: the method with $D_M$ the convergent sequences and $M(s) = 2 \lim s_n$ is a summability method, but it is not regular, since it sends the constant sequence $1$ to $2$.
A method that sums every convergent sequence, but not necessarily to its ordinary limit, is called *conservative*.

## Explanations

### L1 human

A regular method extends the ordinary limit: it never changes the value of a convergent sequence.
