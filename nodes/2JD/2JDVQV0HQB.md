---
tag: 2JDVQV0HQB
kind: definition
name: Bland's rule
msc: [90C05, 90C49]
defines: YM58206VR1
uses: [MH272QHWPM, PJVT97Z7EN, 957S7V3JW8]
sources:
  - url: https://en.wikipedia.org/wiki/Bland's_rule
---

## Definition

Consider the [[simplex algorithm|MH272QHWPM]] for "maximize $c^T x$ subject to $A x = b$, $x \ge 0$", with variables indexed by $1, \dots, n$.
At a [[basic feasible solution|957S7V3JW8]] with basis $B$, let $\bar c_j$ be the reduced costs and $d$ the column of the entering variable.
*Bland's rule* (the *smallest subscript rule*) makes both choices of a pivot as follows.

1. Entering variable: among the indices $j \notin B$ with $\bar c_j > 0$, choose the smallest $j$.
2. Leaving variable: among the indices $i \in B$ with $d_i > 0$ that attain the minimum ratio $x_i / d_i$, choose the smallest $i$.

## Remarks

Bland's theorem: the simplex algorithm with Bland's rule does not [[cycle|PJVT97Z7EN]], so it stops after finitely many pivots at an optimal basis or with a proof of unboundedness.
The proof considers a cycle and the largest index that enters and leaves during it, and derives a sign contradiction from the reduced costs.
The rule can still need exponentially many steps on some programs.

Example: suppose $B = \set{3, 4}$ and the reduced costs are $\bar c_1 = 2$, $\bar c_2 = 5$.
The largest-coefficient rule takes $j = 2$, but Bland's rule takes $j = 1$.
If then $x_3 / d_3 = x_4 / d_4 = 0$ with $d_3, d_4 > 0$, Bland's rule removes $i = 3$.

Non-example: the rule "among the $j$ with $\bar c_j > 0$, take the largest $\bar c_j$" is Dantzig's rule, not Bland's rule, and it can cycle.
