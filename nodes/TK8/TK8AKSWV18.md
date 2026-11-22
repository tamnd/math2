---
tag: TK8AKSWV18
kind: example
name: Each hypothesis of the extreme value theorem is needed
msc: ["00A35", "26A15"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [W48XN2MEM9]
uses: [W48XN2MEM9, 0WS1A8E2P9, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Extreme_value_theorem
    locator: Functions to which the theorem does not apply
  - url: https://en.wikipedia.org/wiki/Extreme_value_theorem
    locator: lead section
---

## Example

The [[extreme value theorem|0WS1A8E2P9]] says: if $f$ is a [[continuous|0X3WGX95FE]] real function on a closed and bounded interval $[a, b]$, then $f$ takes a largest value and a smallest value on $[a, b]$.
Its [[hypotheses|W48XN2MEM9]] are (H1) $f$ is continuous, (H2) the domain is closed, and (H3) the domain is bounded.
We apply the theorem, and then we drop one hypothesis at a time.

1. All three hold.
   Take $f(x) = x(1 - x)$ on $[0, 1]$, a polynomial and so continuous.
   Complete the square:
   $$f(x) = \tfrac14 - \left(x - \tfrac12\right)^2,$$
   so the largest value is $f(\tfrac12) = \tfrac14$, and the smallest is $f(0) = f(1) = 0$.
2. Drop (H1).
   Take $g(x) = x$ for $0 \le x < 1$ and $g(1) = 0$ on the closed, bounded interval $[0, 1]$; it is not continuous at $1$.
   The values of $g$ fill $[0, 1)$, and every value $x < 1$ is beaten by $g\left(\tfrac{1 + x}{2}\right) = \tfrac{1 + x}{2}$.
   So $g$ has no largest value.
3. Drop (H2).
   Take $h(x) = x$ on the open interval $(0, 1)$, which is continuous on a bounded domain that is not closed.
   For each $x$ in $(0, 1)$ the point $\tfrac{1 + x}{2}$ lies in $(0, 1)$ and gives a larger value, so $h$ has no largest value.
   In the same way the point $\tfrac{x}{2}$ shows that $h$ has no smallest value.
4. Drop (H3).
   Take $k(x) = x$ on $[0, \infty)$, which is continuous on a closed domain that is not bounded.
   For each $x \ge 0$ we have $k(x + 1) > k(x)$, so $k$ has no largest value.
5. In steps 2 to 4 each function meets two of the three hypotheses and fails the conclusion.
   So each hypothesis is needed.

## Remarks

The test has a fixed shape: keep the other hypotheses, drop one, and find a function for which the conclusion fails.
A failure can be worse than in the steps above.
The function $1/x$ on $(0, 1]$ is continuous but not even bounded above, so it has no largest value for a more drastic reason.

The theorem says nothing about functions that fail a hypothesis.
Some of them still have both extreme values, for example $\sin x$ on $[0, \infty)$, with largest value $1$ and smallest value $-1$.
A failed hypothesis removes the guarantee, not the possibility.

## Explanations

### L1 human

The extreme value theorem says that an unbroken curve over a closed stretch of the number line has a highest point and a lowest point.
Take away any one condition and the promise can fail.
A curve with a jump can approach a height of $1$ without ever reaching it.
On a stretch with its end point removed, the line $y = x$ climbs toward the missing end and never gets there.
On a stretch that goes on forever, the line $y = x$ keeps climbing.

### L2 human

Does the theorem apply to $f(x) = 1/x$ on $[1, 2]$, and what are the extreme values?
The domain $[1, 2]$ is closed and bounded, and $f$ is continuous there because $x \ne 0$, so the theorem applies.
The function decreases on $[1, 2]$, so
$$\max f = f(1) = 1, \qquad \min f = f(2) = \tfrac12.$$
On $(0, 2]$ the same function is still continuous, but the domain is not closed, and $1/x$ grows without bound as $x \to 0$.
So the theorem no longer applies, and indeed there is no largest value.
The typical use of the theorem is to know that an optimum exists before you search for it, for example before you set a derivative equal to zero.
