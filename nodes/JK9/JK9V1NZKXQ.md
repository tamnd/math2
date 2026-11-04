---
about:
- 03HF498P1J
- MPR6MH4YSQ
kind: statement
msc:
- 06A07
- 05C15
name: On-line antichain partition of a poset of bounded height
role: theorem
sources:
- url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_kitchensink_online.ptx#L57
  locator: source/s_kitchensink_online.ptx:57
tag: JK9V1NZKXQ
uses:
- 0QV2JS9RJ3
- 03HF498P1J
- MPR6MH4YSQ
---

## Statement

Consider the on-line game in which the points of a [[partially ordered set|0QV2JS9RJ3]] $P$ are shown to Assigner one at a time.
When a point appears, Assigner sees how it compares with the points shown before it.
She must at once put it into a class, and she can never move it later.
Each class must end up as an [[antichain|03HF498P1J]].

Fix an integer $h \ge 1$.
Then Assigner has a strategy for this game that works for every poset $P$ whose [[height|MPR6MH4YSQ]] is at most $h$.
This strategy splits $P$ into at most $\binom{h+1}{2}$ antichains.

## Remarks

The off-line bound is only $h$ antichains, by [[Mirsky's theorem|5VPXR3RDF1]].
The theorem shows that the on-line setting costs a factor of about $(h+1)/2$ in the number of classes.
