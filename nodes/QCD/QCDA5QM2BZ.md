---
tag: QCDA5QM2BZ
kind: problem
name: Kuratowski's closure-complement problem
msc: [54A05]
uses: [0CQHFPGJ45, 0QEAJB91GZ, 0RKF1ZT5JJ, 0RZH6W98HK]
about: [0QEAJB91GZ, 0RKF1ZT5JJ]
sources:
  - url: https://en.wikipedia.org/wiki/Kuratowski%27s_closure-complement_problem
same_as:
  wikidata: Q6445654
  wikipedia: Kuratowski's closure-complement problem
history:
  posed_by: "Kazimierz Kuratowski"
  first_stated: "1922"
---

## Problem

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $A \subseteq X$.
Apply to $A$, again and again and in any order, the two operations of taking the [[closure|0QEAJB91GZ]] and taking the [[complement|0RKF1ZT5JJ]] in $X$.
How many distinct subsets of $X$ can arise in this way, at most?

## Remarks

The problem is solved: at most $14$ distinct sets arise, counting $A$ itself, and the bound $14$ is attained in $\R$.
The [[interior|0RZH6W98HK]] of $A$ is the complement of the closure of the complement of $A$.
With $k$ for closure and $i$ for interior, every set that arises is one of $A, kA, iA, ikA, kiA, kikA, ikiA$ or the complement of one of them.
The key identity is $kikik A = kik A$, which stops the list.

In $\R$, the set
$$A = (0, 1) \cup (1, 2) \cup \set{3} \cup ([4, 5] \cap \Q)$$
gives $14$ distinct sets.
For it, $kA = [0, 2] \cup \set{3} \cup [4, 5]$, $iA = (0, 1) \cup (1, 2)$, $ikA = (0, 2) \cup (4, 5)$, $kiA = [0, 2]$, $kikA = [0, 2] \cup [4, 5]$ and $ikiA = (0, 2)$.
These seven sets are distinct and bounded, and their seven complements are unbounded, so all $14$ are distinct.

## Explanations

### L1 human

Start with a set and keep pressing two buttons: "close it" and "take what is outside".
One might expect to get infinitely many different sets this way.
In fact the process always cycles back after a short while, and one can never get more than $14$ different sets.
A clever subset of the real line, made of intervals, a single point and some rational numbers, shows that all $14$ can really appear.
