---
tag: TPK0GPTJAW
kind: example
name: Intervals in a partial order with no Allen relation
msc: ["03B44", "06A06"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: 991B5RR6X4
    note: over a partially ordered time, two intervals can stand in none of Allen's thirteen relations, so the interval logics over linear time do not apply unchanged
uses: [991B5RR6X4, ET6CYR090M, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Allen%27s_interval_algebra
    locator: section Relations
---

## Example

Let time be the [[partial order|0QV2JS9RJ3]] on four points $a, b, c, d$ in which $a < b$ and $c < d$ are the only strict comparisons.
Take the intervals $X = [a, b]$ and $Y = [c, d]$.

1. Each of the thirteen relations of Allen fixes the order between the left endpoints $a$ and $c$, by the table in [[the example of Allen's relations|ET6CYR090M]].
2. For instance, "before" needs $b < c$, hence $a < c$ by transitivity, and "during" needs $c < a$.
3. Row by row, the condition implies $a < c$, $a = c$ or $c < a$.
   For "after", $d < a$ gives $c < d < a$, and for "met by", $d = a$ gives $c < a$.
4. Here $a$ and $c$ are distinct and incomparable.
   So no relation holds between $X$ and $Y$.

## Remarks

The proof that some relation always holds, in [[the example of Allen's relations|ET6CYR090M]], uses linearity at every comparison.
Branching time, as in the frames of CTL, is partially ordered, so interval logics there need more than thirteen relations.
Interval logics over partial orders with linear intervals have been studied, with extra relations for incomparable intervals.
Adding the comparison $a < c$ alone, with $a < d$ by transitivity, does not help.
Every relation with $a < c$ also compares $b$ with $c$ or with $d$, and $b$ is still incomparable with both.

## Explanations

### L1 human

If time can branch, two events on different branches are neither before, after, nor at the same time as each other.
Then none of the thirteen words of Allen fits.

### L2 human

Pick one row of the table of Allen, and check that its condition compares the two left endpoints, directly or by transitivity.
Then find two intervals whose left endpoints are incomparable.
Watch out: an incomparable pair is not the same as "before", since "before" requires $b < c$.
