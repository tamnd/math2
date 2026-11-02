---
tag: SZ9X10ATEK
kind: definition
name: Bounded poset
msc: [06A06]
defines: B0QT3SM5DT
uses: [011C29Q1S1, 0Z7HDDXX3X, 0T2NTJCV83]
sources:
  - url: https://en.wikipedia.org/wiki/Greatest_element_and_least_element
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]].
The poset $P$ is *bounded* when it has a [[greatest element|0Z7HDDXX3X]] $\top$ and a [[least element|0T2NTJCV83]] $\bot$, that is, $\bot \le x \le \top$ for all $x \in P$.

## Remarks

The positive divisors of $12$, ordered by divisibility, form a bounded poset with $\bot = 1$ and $\top = 12$, since $1 \mid d$ and $d \mid 12$ for each divisor $d$.
The poset $(\Z, \le)$ is not bounded: it has neither a greatest nor a least element.
The interval $(0, 1]$ in $\R$ has the top $1$ but no bottom, so it is not bounded.
For a subset of $P$, being bounded usually means something weaker: having an [[upper bound|0H5J02P8S9]] and a lower bound in $P$.
The elements $\top$ and $\bot$ are unique when they exist, by antisymmetry.
A bounded poset with one element has $\top = \bot$.

## Explanations

### L1 human

A bounded poset has a top and a bottom.
Every element lies between the two.
