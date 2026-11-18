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

Let time be the [[partial order|0QV2JS9RJ3]] on four points $a, b, c, d$ with $a < b$ and $c < d$ as the only strict comparisons.
Take the intervals $X = [a, b]$ and $Y = [c, d]$.

1. Each of Allen's thirteen relations fixes the order between the left endpoints $a$ and $c$, by the table in [[the example|ET6CYR090M]].
2. For instance, "before" needs $b < c$, hence $a < c$ by transitivity, and "during" needs $c < a$.
3. In every row of that table, the condition implies $a < c$, $a = c$ or $c < a$.
4. Here $a$ and $c$ are distinct and incomparable. So no relation holds between $X$ and $Y$.

## Remarks

The proof that some relation always holds, in [[the example|ET6CYR090M]], uses linearity at every comparison.
Branching time, as in the frames of CTL, is partially ordered, so interval logics there need more than thirteen relations.
Interval logics over partial orders with linear intervals have been studied, with extra relations for incomparable intervals.

## Explanations

### L1 human

If time can branch, two events on different branches are neither before, after, nor at the same time as each other.
Then none of Allen's thirteen words fits.

### L2 human

1. Pick one row of Allen's table.
2. Check that its condition compares the two left endpoints, directly or by transitivity.
3. Find two intervals whose left endpoints are incomparable.

A trap: an incomparable pair is not the same as "before"; "before" requires $b < c$.
