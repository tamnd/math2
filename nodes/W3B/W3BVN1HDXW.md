---
tag: W3BVN1HDXW
kind: concept
name: Consistency of summability methods
msc: ["40D25", "40C05"]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Summary

Two [[summability methods|8X25Q4XYMN]] are consistent when they never give different values to the same series.
If a series is summable by both methods, the two values must agree.
Consistency is what makes it reasonable to speak of "the" generalized sum of a divergent series.
The [[Mazur–Orlicz theorem|YE5439NH1T]] gives a condition under which two regular matrix methods are consistent on bounded sequences.

## Explanations

### L1 human

There are many ways to give a value to a divergent series, such as averaging the partial sums or plugging $x \to 1$ into a power series.
One wants these ways to agree whenever they both work.
For the series $1 - 1 + 1 - 1 + \cdots$, both [[Cesàro summation|N8ZGG7EW6J]] and [[Abel summation|EZXPY4A19C]] give $1/2$.
In fact, every series that Cesàro summation sums is summed by Abel summation to the same value, so the two methods are consistent.
