---
tag: XBCYFDPS2F
kind: concept
name: Accessibility relation
sources:
  - wikipedia: en:3708585@r1320635173
    locator: Accessibility relation
    note: adopted
    mention: wikipedia://en/3708585
    sections: [Summary]
same_as:
  wikidata: Q2663311
  wikipedia: Accessibility relation
inventory: [BRP65H8828]
---

## Summary

An **accessibility relation** is a relation which plays a key role in assigning truth values to sentences in the relational semantics for modal logic. In relational semantics, a modal formula's truth value at a *possible world* $w$ can depend on what is true at another possible world $v$, but only if the accessibility relation $R$ relates $w$ to $v$. For instance, if $P$ holds at some world $v$ such that $wRv$, the formula $\Diamond P$ will be true at $w$. The fact $wRv$ is crucial. If $R$ did not relate $w$ to $v$, then $\Diamond P$ would be false at $w$ unless $P$ also held at some other world $u$ such that $wRu$.
