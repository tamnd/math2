---
tag: 0HESMMSYEG
kind: statement
role: theorem
name: Russell's paradox
aliases: [russell-paradox]
msc: ["03E30"]
uses: [0SJ3RX9TXA, 0EZ758XE73, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Russell's_paradox
    locator: lead section
same_as:
  wikidata: Q33401
  wikipedia: Russell's paradox
---

## Statement

There is no [[set|0SJ3RX9TXA]] $R$ such that, for each set $x$, $x \in R$ if and only if $x \notin x$.

## Remarks

Proof: if such an $R$ exists, apply the condition to $x = R$. Then $R \in R$ if and only if $R \notin R$, which is a contradiction.
So the collection $\{x \mid x \notin x\}$ is not a set. Unrestricted comprehension, which makes a set from each property, is inconsistent.
It follows that there is no set of all sets. Otherwise, separation would give $R$ as a subset of it.

## History

Bertrand Russell found the paradox in May 1901.
Ernst Zermelo found it independently, by 1902 and possibly in 1899, but he did not publish it.
In a 1902 letter, Russell told Gottlob Frege that the paradox arises in the logical system of Frege.
Axiomatic set theories, such as [[Zermelo–Fraenkel set theory|0HE5WDQ9FJ]], avoid it with a restricted form of comprehension.

## Explanations

### L1 human

Try to form "the set of all sets that do not contain themselves".
Ask whether this set contains itself: both answers lead to a contradiction.
So some collections are too large to be sets.
