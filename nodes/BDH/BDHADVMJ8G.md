---
tag: BDHADVMJ8G
kind: statement
role: theorem
name: Final value theorem
msc: [44A10, "40E05"]
uses: [05XT5AVJBK, 0TXTSEMHR5]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Final_value_theorem
same_as:
  wikidata: Q4272645
  wikipedia: Final value theorem
---

## Statement

Let $f \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$.
Assume that the [[limit|0TXTSEMHR5]] $f(\infty) = \lim_{t \to \infty} f(t)$ exists and is finite.
Then the Laplace integral $F(s)$ of $f$ converges for every real $s > 0$, and
$$\lim_{s \to 0^+} s F(s) = f(\infty),$$
where $s$ tends to $0$ through positive real values.

## Remarks

Since $f$ has a finite limit, it is bounded for large $t$, so $F(s)$ converges for $s > 0$.
Since $s \int_0^\infty e^{-s t} \, dt = 1$, the difference $s F(s) - f(\infty)$ equals $s \int_0^\infty e^{-s t} (f(t) - f(\infty)) \, dt$.
As $s \to 0^+$ the weight $s e^{-s t}$ spreads its mass over large $t$, where $f(t) - f(\infty)$ is small, and the part over a fixed interval $[0, T]$ tends to $0$.
Example: for $f(t) = 1 - e^{-t}$, $s F(s) = 1 - s/(s + 1) \to 1 = f(\infty)$.
The hypothesis that $f(\infty)$ exists is needed: for $f(t) = \sin t$, $s F(s) = s / (s^2 + 1) \to 0$, but $\sin t$ has no limit.

## Explanations

### L1 human

The behaviour of the transform for small $s$ tells the long-run value of the function, if that value exists.
One can read the steady state from $F$ without inverting the transform.

### L2 human

In control theory one uses it to find the steady-state error of a stable system.
For a rational $F$, the limit $f(\infty)$ exists when all poles of $s F(s)$ lie in the open left half-plane; then the theorem applies.
If $s F(s)$ has a pole on the imaginary axis or to its right, the formula can give a wrong answer, as the example $\sin t$ shows.
The converse direction, from $F$ to $f$, needs extra hypotheses and belongs to the [[Tauberian theorems|NV54MWKT6T]].
Its companion is the [[initial value theorem|KZPVHDKV9E]].
