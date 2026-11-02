---
tag: KZPVHDKV9E
kind: statement
role: theorem
name: Initial value theorem
msc: [44A10, "40E05"]
uses: [05XT5AVJBK, 0TXTSEMHR5]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Initial_value_theorem
same_as:
  wikidata: Q4272300
  wikipedia: Initial value theorem
---

## Statement

Let $f \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$.
Assume that the Laplace integral of $f$ converges at some real number $s_0$, and let $F$ be the [[Laplace transform|05XT5AVJBK]] of $f$.
Assume that the one-sided [[limit|0TXTSEMHR5]] $f(0^+) = \lim_{t \to 0^+} f(t)$ exists and is finite.
Then
$$\lim_{s \to +\infty} s F(s) = f(0^+),$$
where $s$ tends to $+\infty$ through real values.

## Remarks

Since $s \int_0^\infty e^{-s t} \, dt = 1$, the difference $s F(s) - f(0^+)$ is $s \int_0^\infty e^{-s t} (f(t) - f(0^+)) \, dt$.
The weight $s e^{-s t}$ has total mass $1$ and concentrates near $t = 0$ as $s \to \infty$.
On $[0, \delta]$ the integrand is small by the existence of $f(0^+)$; on $[\delta, \infty)$ the contribution tends to $0$ by the convergence at $s_0$.
Example: for $f(t) = \cos t$, $s F(s) = s^2 / (s^2 + 1) \to 1 = f(0)$.
The finiteness of $f(0^+)$ matters: for $f(t) = t^{-1/2}$ one has $F(s) = \sqrt{\pi / s}$, so $s F(s) = \sqrt{\pi s} \to +\infty$.

## Explanations

### L1 human

The behaviour of the transform for very large $s$ tells the starting value of the function.
One can read $f(0^+)$ from $F$ without inverting the transform.

### L2 human

In control and circuit theory one uses it to check the value of a response just after a switch is closed.
It is the simplest Abelian theorem for the Laplace transform: behaviour of $f$ near $0$ gives behaviour of $F$ near $\infty$.
Its companion is the [[final value theorem|BDHADVMJ8G]], which links $f$ near $\infty$ with $F$ near $0$.
