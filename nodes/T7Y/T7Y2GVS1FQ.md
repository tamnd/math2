---
tag: T7Y2GVS1FQ
kind: concept
name: Linear program in standard form
msc: [90C05]
specializes: [VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_programming
    locator: Standard form
---

## Summary

A linear program in standard form maximizes a linear function $c^T x$ subject to linear inequalities $A x \le b$ and the sign conditions $x \ge 0$.
Every [[linear program|VNMXB0J2KA]] can be brought into this form, so theorems and algorithms need only treat one shape.
With [[slack variables|5VE5GVSNHK]] it becomes the equational form $A x + s = b$, $x, s \ge 0$, on which the [[simplex algorithm|MH272QHWPM]] works.
Some textbooks call the equational form itself the standard form.

## Explanations

### L1 human

Linear programs come in many shapes: some minimize, some maximize, some have equations, some have inequalities in both directions.
Standard form is an agreed shape: maximize, all constraints "$\le$", all variables nonnegative.
Any other shape can be rewritten into it with a few simple tricks, such as multiplying an inequality by $-1$.
For example, "minimize $x - y$ subject to $x + y \ge 1$, $x, y \ge 0$" becomes "maximize $-x + y$ subject to $-x - y \le -1$, $x, y \ge 0$".
