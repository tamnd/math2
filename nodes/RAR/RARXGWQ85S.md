---
tag: RARXGWQ85S
kind: counterexample
name: Volterra's function
msc: [26A27, 26A24]
uses: [0F1WR9C83K, 0N1JQXZXHC, 0565EGK6XP, 0NHGY0N0JB, 0BW9N5CDSB]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra%27s_function
same_as:
  wikidata: Q3075214
  wikipedia: Volterra's function
---

## Counterexample

Let $S \subseteq [0, 1]$ be the Smith–Volterra–Cantor set.
It is closed, contains no interval, and has positive Lebesgue measure.
Let $g(t) = t^2 \sin(1/t)$ for $t \ne 0$ and $g(0) = 0$.
Then $g$ is differentiable on $\R$, with $g'(t) = 2t \sin(1/t) - \cos(1/t)$ for $t \ne 0$ and $g'(0) = 0$.

The complement $[0, 1] \setminus S$ is a union of disjoint open intervals.
On each such interval $(a, b)$, let $t_0$ be the largest $t \in (0, (b - a)/2]$ with $g'(t) = 0$.
Define $V(x) = g(x - a)$ for $a < x \le a + t_0$, $V(x) = g(t_0)$ for $a + t_0 \le x \le b - t_0$, and $V(x) = g(b - x)$ for $b - t_0 \le x < b$.
Set $V(x) = 0$ for $x \in S$.

Then $V$ is differentiable at every point of $[0, 1]$, and its derivative $V'$ is bounded.
At each point of $S$, one has $V'(x) = 0$, but $V'$ is not continuous there.
So $V'$ is discontinuous on a set of positive measure, and by [[Lebesgue's criterion|0565EGK6XP]] it is not [[Riemann integrable|0N1JQXZXHC]].

## Remarks

The number $t_0$ exists because $g'$ has zeros at points of $(0, \varepsilon)$ for every $\varepsilon > 0$.
Near an endpoint $a$, the derivative $V'(x) = g'(x - a)$ keeps taking values close to $1$ and close to $-1$.
Every point of $S$ is a limit of such endpoints, which gives the discontinuity of $V'$ on $S$.
The example shows that a function can have a bounded [[derivative|0F1WR9C83K]] that has no Riemann integral.
So the [[fundamental theorem of calculus|0NHGY0N0JB]] in the Riemann form $\int_a^b f' = f(b) - f(a)$ needs the hypothesis that $f'$ is Riemann integrable.
The Lebesgue integral repairs this: a bounded derivative is Lebesgue integrable, and the formula holds.

## Explanations

### L1 human

Volterra's function is differentiable everywhere, and its slope stays bounded.
Yet the slope jumps around wildly on a fat Cantor set, a set with no intervals but with positive length.
Because the bad set is so large, the Riemann integral cannot handle the derivative.
The function shows that the Riemann integral is too weak to undo every differentiation.
