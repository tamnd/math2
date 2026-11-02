---
tag: R7SH3ECJRN
kind: definition
name: Ordered semigroup
msc: ["06F05"]
defines: HA79YFZAQR
uses: [0V3CFG1KK9, 011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Ordered_semigroup
---

## Definition

Let $(S, \cdot)$ be a [[semigroup|0V3CFG1KK9]] and let $\le$ be a [[partial order|011C29Q1S1]] on $S$.
The triple $(S, \cdot, \le)$ is an *ordered semigroup* if for all $a, b, c \in S$,
$$a \le b \implies ca \le cb \text{ and } ac \le bc.$$

## Remarks

Example: $(\N, +)$ with the usual order is an ordered semigroup, since $a \le b$ gives $c + a \le c + b$ and $a + c \le b + c$.
Non-example: $(\Z, \cdot)$ with the usual order is not an ordered semigroup.
Indeed $1 \le 2$, but $(-1) \cdot 1 = -1 > -2 = (-1) \cdot 2$.
An ordered semigroup with an identity element is an *ordered monoid*.
Some authors require the order to be total and call the general case a partially ordered semigroup.
