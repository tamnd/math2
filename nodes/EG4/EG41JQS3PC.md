---
tag: EG41JQS3PC
kind: definition
name: WKB approximation
msc: ["34E20", "34E05"]
defines: YJEBN8N3G8
uses: [0NT64JV96A, Q26QN6GYZX]
sources:
  - url: https://en.wikipedia.org/wiki/WKB_approximation
---

## Definition

Let $I$ be an open interval, let $Q \colon I \to \R$ be smooth with $Q(x) \neq 0$ for all $x \in I$, and let $\varepsilon > 0$ be a small parameter.
Consider the linear [[ordinary differential equation|0NT64JV96A]]
$$\varepsilon^2 y''(x) = Q(x) \, y(x), \quad x \in I.$$
The *WKB ansatz* is $y = \exp\bigl(\frac{1}{\varepsilon} \sum_{n \ge 0} \varepsilon^n S_n(x)\bigr)$.
Inserting it and collecting powers of $\varepsilon$ gives $S_0'^2 = Q$ at order $\varepsilon^0$ and $2 S_0' S_1' + S_0'' = 0$ at order $\varepsilon^1$.
The *WKB approximation*, or *Liouville–Green approximation*, keeps these two orders.
It gives the two functions
$$y_\pm(x) = Q(x)^{-1/4} \exp\Bigl(\pm \frac{1}{\varepsilon} \int_{x_0}^{x} \sqrt{Q(s)} \, ds\Bigr),$$
where $x_0 \in I$ and the roots are taken with a fixed branch.
On compact subintervals of $I$, the equation has solutions $y = y_\pm \, (1 + O(\varepsilon))$ as $\varepsilon \to 0$.

## Remarks

Example: for constant $Q = q > 0$, the formula gives $q^{-1/4} e^{\pm \sqrt{q} (x - x_0) / \varepsilon}$, which solve the equation exactly.
Check of the first order: with $S_0' = \sqrt{Q}$, the second relation gives $S_1' = -S_0'' / (2 S_0') = -Q' / (4 Q)$, so $e^{S_1} = Q^{-1/4}$.

Non-example: the hypothesis $Q \neq 0$ fails for the Airy-type equation $\varepsilon^2 y'' = x y$ on an interval containing $0$.
The point $x = 0$ is a *turning point*, where $Q^{-1/4}$ blows up; there the WKB formulas are not valid, and solutions are matched through Airy functions.

The series $\sum \varepsilon^n S_n$ is in general only an [[asymptotic expansion|Q26QN6GYZX]], not a convergent series.
When $Q < 0$, one writes $Q = -k^2$, and the two solutions become $k^{-1/2} e^{\pm i \int k / \varepsilon}$, which oscillate.

## Explanations

### L1 human

The method guesses that the solution is an exponential with a slowly changing exponent.
The first equation fixes the phase, and the second fixes how the amplitude changes.
