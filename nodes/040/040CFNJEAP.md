---
tag: 040CFNJEAP
kind: statement
role: lemma
name: Lebesgue number lemma
aliases: [lebesgues-number-lemma]
msc: ["54E45"]
uses: [0QPHW703PV, 0NVPNC12JY, 0692CGQF00]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%27s_number_lemma
    locator: lead section
same_as:
  wikidata: Q1049869
  wikipedia: Lebesgue's number lemma
---

## Statement

Let $(X, d)$ be a [[compact|0QPHW703PV]] [[metric space|063W5JMY85]] and let $(U_i)_{i \in I}$ be an [[open cover|0NVPNC12JY]] of $X$.
Then there is a real $\delta > 0$ such that each subset $A \subseteq X$ with [[diameter|0692CGQF00]] $\operatorname{diam}(A) < \delta$ is contained in $U_i$ for some $i \in I$.

## Remarks

Such a number $\delta$ is a Lebesgue number of the cover.
Equivalently, for each $x \in X$, the ball $B(x, \delta / 2)$ lies in one of the sets $U_i$.
Compactness is needed: the cover of $(0, 1)$ by the sets $(1/n, 1)$ has no Lebesgue number.

## Explanations

### L1 human

In a compact metric space, each open cover has a uniform size: each small enough set fits completely into one set of the cover.
You can think of $\delta$ as a safe size for a window that you move around the space.
