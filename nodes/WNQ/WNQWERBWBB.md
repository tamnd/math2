---
tag: WNQWERBWBB
kind: problem
name: Hilbert's thirteenth problem
msc: [26B40, 41A30, 01A60]
uses: [0THBK9V825, 0X3WGX95FE]
about: [0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_thirteenth_problem
same_as:
  wikidata: Q838094
  wikipedia: Hilbert's thirteenth problem
history:
  posed_by: "David Hilbert"
  first_stated: "1900"
---

## Problem

Consider the equation of degree seven
$$x^7 + a x^3 + b x^2 + c x + 1 = 0,$$
and its solution $x$ as a function of the three coefficients $a, b, c$.
Can this function be written as a finite [[composition|0THBK9V825]] of [[continuous functions|0X3WGX95FE]] of two variables?

## Remarks

Hilbert expected the answer to be negative.
Every equation of degree seven can be brought to the form above by Tschirnhaus transformations, so the question asks whether the general septic is solvable by functions of two variables.

In 1957 Andrey Kolmogorov and Vladimir Arnold showed that the answer is positive for continuous functions, in a strong form.
Arnold proved that every continuous function of three variables is a composition of continuous functions of two variables.
Kolmogorov's superposition theorem goes further: every continuous $f \colon [0, 1]^n \to \R$ can be written as
$$f(x_1, \dots, x_n) = \sum_{q=0}^{2n} \Phi_q\Big( \sum_{p=1}^{n} \varphi_{q, p}(x_p) \Big)$$
with continuous functions $\Phi_q$ and $\varphi_{q, p}$ of one variable.
So addition is the only function of two variables that is needed.

Many authors read Hilbert's question as being about algebraic functions instead of continuous ones; in that form the problem is still open.

## Explanations

### L1 human

Some functions of several variables secretly need only one or two variables at a time, such as $\sin(x + y z)$, built from multiplication, addition and the sine.
Hilbert asked whether the solution of a particular seventh-degree equation, which depends on three numbers, can be built in this way from continuous functions of two variables.
Kolmogorov and Arnold showed that, surprisingly, every continuous function of any number of variables can be built from continuous functions of one variable and addition.
