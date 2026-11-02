---
tag: F2HHDD85EM
kind: statement
role: theorem
name: Hartman–Wintner theorem
msc: [34C10, 34D05]
uses: [ZH2S50NSZ6, 0QQRP17Z7S, 033RZ32T4Q, 0VT2QK6X6Q]
about: [ZH2S50NSZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillation_theory
  - book: isbn:9780898715101
---

## Statement

Let $t_0 \ge 0$ and let $q \colon [t_0, \infty) \to \R$ be continuous.
Consider the [[linear differential equation|0QQRP17Z7S]]
$$y'' + q(t) y = 0 \quad \text{on } [t_0, \infty).$$
For $t > t_0$ put
$$A(t) = \frac{1}{t} \int_{t_0}^{t} \int_{t_0}^{s} q(u) \, du \, ds.$$
Assume that the equation is nonoscillatory in the sense of [[oscillation theory|ZH2S50NSZ6]], and that $\liminf_{t \to \infty} A(t) > -\infty$, where $\liminf$ is the [[limit inferior|033RZ32T4Q]].
Then $\lim_{t \to \infty} A(t)$ exists and is a finite real number.

## Remarks

The proof goes through the [[Riccati equation|0VT2QK6X6Q]].
A nonoscillatory equation has a solution $y > 0$ on some interval $[T, \infty)$, and $w = y'/y$ satisfies $w' + w^2 + q = 0$ there.
Integrating gives $w(t) = w(T) - \int_T^t q - \int_T^t w^2$.
Averaging this identity and using the lower bound on $A$, one shows that $\int_T^\infty w^2 < \infty$, and then the average $A(t)$ converges.

Read as a test for oscillation, the theorem says: if $\liminf A(t) > -\infty$ and either $\liminf A(t) < \limsup A(t)$ or $A(t) \to \infty$, then the equation is oscillatory.
The case $A(t) \to \infty$ is Wintner's oscillation criterion.

Example: for $q = 1$ on $[0, \infty)$ one gets $A(t) = t/2 \to \infty$, so the equation is oscillatory; indeed $\sin t$ is a solution.
For $q(t) = 1/(4t^2)$ on $[1, \infty)$ the equation has the positive solution $\sqrt{t}$, so it is nonoscillatory.
Here $A(t) = (t - 1 - \ln t)/(4t)$, which tends to the finite limit $1/4$, as the theorem predicts.

## Explanations

### L1 human

The equation $y'' + q y = 0$ describes a spring whose stiffness $q(t)$ changes with time.
The solutions either keep crossing zero forever or eventually stay on one side.
The theorem looks at a double average of the stiffness.
If the solutions stop crossing zero and this average is bounded below, then the average must settle to a finite value.
So an average that grows without bound, or that keeps swinging, forces endless oscillation.

### L2 human

The Sturm comparison theorem compares $q$ with a constant or an Euler coefficient pointwise.
The Hartman–Wintner theorem uses only averages of $q$, so it also applies when $q$ changes sign.
It improves Wintner's criterion, which asks that $A(t) \to \infty$.
The key tool is the Riccati substitution $w = y'/y$, which turns a nonoscillatory linear equation into a first-order nonlinear one with a solution on a half-line.
Later criteria of Kamenev and Philos replace the weight $1/t$ by other weights in the same Riccati argument.
