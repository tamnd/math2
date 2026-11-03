---
tag: 5VE5GVSNHK
kind: concept
name: Slack variable
msc: [90C05]
sources:
  - url: https://en.wikipedia.org/wiki/Slack_variable
same_as:
  wikidata: Q1765718
  wikipedia: Slack variable
---

## Summary

A slack variable is a new nonnegative variable that turns an inequality [[constraint|X3663P90AE]] into an equation.
The inequality $a^T x \le \beta$ becomes $a^T x + s = \beta$ with $s \ge 0$, and $s$ measures how far the constraint is from being tight.
Slack variables bring a [[linear program|VNMXB0J2KA]] into the equational form used by the [[simplex algorithm|MH272QHWPM]].

## Explanations

### L1 human

If a recipe allows at most $10$ eggs and you use $7$, then $3$ eggs are left over; that leftover amount is the slack.
Writing "eggs used plus eggs left over equals $10$" replaces an inequality with an equation and a sign condition.
When the slack is $0$, the constraint is tight: you used everything that was allowed.
For example, $x + 2y \le 4$ becomes $x + 2y + s = 4$ with $s \ge 0$, and at $(x, y) = (2, 1)$ the slack is $s = 0$.
