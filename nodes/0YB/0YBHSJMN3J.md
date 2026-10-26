---
tag: 0YBHSJMN3J
kind: statement
role: theorem
name: Comparability of cardinals
aliases: [trichotomy-of-cardinals]
msc: ["03E10"]
uses: [01GTP8M5RG, 0HTGB13FE2]
sources:
  - url: https://en.wikipedia.org/wiki/Cardinal_number
    locator: Cardinal comparison
---

## Statement

Assume the [[axiom of choice|0HTGB13FE2]].
Let $A$ and $B$ be [[sets|0SJ3RX9TXA]].
Then there is an [[injective function|0PVG1CRAJN]] from $A$ to $B$ or an injective function from $B$ to $A$.
So $|A| \le |B|$ or $|B| \le |A|$.

## Remarks

With the [[Schröder–Bernstein theorem|0A9V6RKQG6]], it follows that the [[order of cardinals|01GTP8M5RG]] is a total order.
The statement is equivalent to the axiom of choice over ZF.
One proof uses [[Zorn's lemma|04RXTQA5ZA]] on the set of injective partial functions from $A$ to $B$.

## Explanations

### L1 human

Any two sets can be compared in size: one of them fits into the other.
Without the axiom of choice, two sets can exist such that neither fits into the other.
