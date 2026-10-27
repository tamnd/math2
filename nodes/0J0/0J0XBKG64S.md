---
tag: 0J0XBKG64S
kind: concept
name: Proof by contradiction
aliases: [reductio-ad-absurdum, indirect-proof]
msc: [00A35]
topics: [G9JFJGY4TQ]
uses: [0B94TKFQJX, 0XR7A7RSXB, 0NFAGWH84K]
sources:
  - url: https://en.wikipedia.org/wiki/Reductio_ad_absurdum
    locator: lead section
same_as:
  wikidata: Q14402006
  wikipedia: Reductio ad absurdum
---

## Summary

A proof by contradiction proves a [[proposition|0ZGC7ZESYN]] $p$ in two steps.
It assumes $\neg p$, and it gets a contradiction from this assumption, that is, a statement $q$ together with $\neg q$.
Then $\neg p$ is false, so $p$ is true by the [[double negation law|0NFAGWH84K]].

## Remarks

Another name is reductio ad absurdum.
A classical example: $\sqrt{2}$ is irrational. Assume $\sqrt{2} = a/b$ in lowest terms. Then $a$ and $b$ are both even, which is a contradiction.
The last step uses classical logic. A proof of $\neg p$ from a contradiction with $p$ is valid also in intuitionistic logic.

## Explanations

### L1 human

To show that something is true, suppose that it is false and follow the consequences.
If you reach an impossible situation, the supposition was wrong.
So the statement must be true.
