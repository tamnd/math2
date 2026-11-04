---
tag: ~cd70cfd6
kind: statement
role: theorem
name: Builder strategy forcing many antichains in on-line poset partitioning
msc: [06A07]
uses: [0QV2JS9RJ3, 03HF498P1J, MPR6MH4YSQ, 072G59HW59]
about: [03HF498P1J, MPR6MH4YSQ]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_kitchensink_online.ptx#L84
    locator: source/s_kitchensink_online.ptx:84
---

## Statement

Two players build a [[partially ordered set|0QV2JS9RJ3]] $P$ in an on-line game.
The builder presents the points of $P$ one at a time, and states how each new point compares with the points shown before.
The assigner must put each new point at once into an [[antichain|03HF498P1J]], and cannot change this later.
The antichains together partition $P$.

Then for every integer $h \ge 1$, the builder has a strategy $S_h$ that produces a poset $P$ of [[height|MPR6MH4YSQ]] $h$ and forces the assigner to do both of the following.

1. The assigner uses at least $\binom{h+1}{2}$ antichains to partition $P$.
2. The assigner uses at least $h$ different antichains for the set of [[maximal elements|072G59HW59]] of $P$.

## Remarks

Off-line, a poset of height $h$ needs only $h$ antichains, by [[Mirsky's theorem|5VPXR3RDF1]].
The result shows that an on-line assigner can be forced to use about $h^2/2$ antichains.
