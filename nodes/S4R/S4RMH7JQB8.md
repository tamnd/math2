---
tag: S4RMH7JQB8
kind: concept
name: Quasiconvex function
msc: [26B25, 26A51, 90C26]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiconvex_function
same_as:
  wikidata: Q1126412
  wikipedia: Quasiconvex function
---

## Summary

A quasiconvex function is a real function on a convex set whose sublevel sets are all [[convex|02AS45T3H9]].
Every [[convex function|07Q7CNM5WF]] is quasiconvex, but many quasiconvex functions are not convex.
The notion is used in optimization and economics, where only the shape of the sublevel sets matters, not the exact values.
The [[definition|393PNMXBFJ]] gives the precise condition.

## Explanations

### L1 human

A function is quasiconvex if, on each segment, its value never rises above the larger of the two values at the ends.
Picture a valley whose sides may be steep or flat but never have a bump in the middle.
Every increasing function on the real line is quasiconvex, even if its graph bends downward.
For example $\sqrt{\abs{x}}$ is quasiconvex on $\R$ but not convex.
