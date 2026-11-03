---
about:
- H96HXG6CA0
- W8ZWXC2HQS
kind: statement
msc:
- '34A25'
- '34B30'
name: Existence of a Frobenius-type solution at a regular singular point
role: theorem
sources:
- url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-power-ser.tex#L1619
  locator: ch-power-ser.tex:1619
tag: 6NCSVZY8MA
uses:
- H96HXG6CA0
- W8ZWXC2HQS
- 0MZB06ST2B
---

## Statement

Consider the second order linear equation $P(x) y'' + Q(x) y' + R(x) y = 0$.
Assume that $x = 0$ is a [[regular singular point|H96HXG6CA0]] of this equation.
Then the equation has at least one solution of the form $y = x^r \sum_{k \ge 0} a_k x^k$, where $r$ is a constant and the sum is a [[power series|0MZB06ST2B]] in $x$.

A solution of this form is called a Frobenius-type solution.

## Remarks

The constant $r$ is a root of the indicial equation, and the coefficients $a_k$ come from a recurrence. This is the basis of the [[Frobenius method|W8ZWXC2HQS]].

The result gives only one solution. A second independent solution may need a logarithmic term.
