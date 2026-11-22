---
tag: YRC4NN8KDJ
kind: example
name: Each hypothesis of Rolle's theorem is needed
msc: ["00A35", "26A24"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [W48XN2MEM9]
uses: [W48XN2MEM9, 0194DY35BG, 0X3WGX95FE, 0K57YG3BB8, 0FFXKTKKQC]
sources:
  - url: https://en.wikipedia.org/wiki/Rolle%27s_theorem
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Rolle%27s_theorem
    locator: lead section
---

## Example

[[Rolle's theorem|0194DY35BG]] says: let $a < b$, and let $f$ be a real function such that (H1) $f$ is [[continuous|0X3WGX95FE]] on $[a, b]$, (H2) $f$ is [[differentiable|0K57YG3BB8]] on $(a, b)$, and (H3) $f(a) = f(b)$.
Then some point $c$ in $(a, b)$ has $f'(c) = 0$.
We apply the theorem once, and then we drop one [[hypothesis|W48XN2MEM9]] at a time.

1. All three hold.
   Take $f(x) = x^2 - 1$ on $[-1, 1]$, a polynomial, so (H1) and (H2) hold, and $f(-1) = 0 = f(1)$.
   The derivative $f'(x) = 2x$ is $0$ at $c = 0$.
2. Drop (H2).
   Take the [[absolute value|0FFXKTKKQC]] $f(x) = |x|$ on $[-1, 1]$, which is continuous with $f(-1) = 1 = f(1)$.
   For $x < 0$ we have $f'(x) = -1$, for $x > 0$ we have $f'(x) = 1$, and at $0$ there is no derivative.
   So no $c$ has $f'(c) = 0$.
3. Drop (H1).
   Take $f(x) = x$ for $0 \le x < 1$ and $f(1) = 0$, so that $f(0) = 0 = f(1)$ and (H3) holds.
   On $(0, 1)$ we have $f'(x) = 1$, so (H2) holds and no point has $f'(c) = 0$.
   The function is not continuous at $1$, because $f(x) \to 1$ as $x \to 1$ from the left, while $f(1) = 0$.
4. Drop (H3).
   Take $f(x) = x$ on $[0, 1]$, which is continuous and differentiable, with $f(0) = 0 \ne 1 = f(1)$.
   On $(0, 1)$ we have $f'(x) = 1$, so no point has $f'(c) = 0$.
5. In steps 2 to 4 each function meets two of the three hypotheses and fails the conclusion.
   So each hypothesis is needed.

## Remarks

Each hypothesis blocks one way for the conclusion to fail.
Continuity on the closed interval blocks a jump at an end point, differentiability blocks a corner, and equal end values force the graph to turn back.
Step 3 shows that continuity is needed at the end points too, not only inside the interval.

If we drop (H3) and change the conclusion, the theorem survives in a new form.
The mean value theorem gives a point $c$ with
$$f'(c) = \frac{f(b) - f(a)}{b - a},$$
and Rolle's theorem is its special case $f(a) = f(b)$.
For $f(x) = x$ on $[0, 1]$, step 4, the mean value theorem gives $f'(c) = 1$, which holds at every point.

## Explanations

### L1 human

Rolle's theorem says that a smooth curve that starts and ends at the same height has a flat point somewhere in between.
A V-shaped graph, such as $|x|$ from $-1$ to $1$, starts and ends at the same height but has a sharp corner instead of a flat point.
A graph that climbs all the way and then jumps down at the very end has no flat point either.
A straight line that ends higher than it starts has none.
So each condition of the theorem is really needed.

### L2 human

Apply the theorem to $f(x) = x^3 - x$ on $[0, 1]$.
It is a polynomial, so it is continuous on $[0, 1]$ and differentiable on $(0, 1)$.
Its end values are $f(0) = 0$ and $f(1) = 1 - 1 = 0$, so all three hypotheses hold, and some $c$ in $(0, 1)$ has $f'(c) = 0$.
Find it:
$$f'(x) = 3x^2 - 1 = 0 \quad \Longrightarrow \quad x = \pm \frac{1}{\sqrt{3}},$$
and $c = 1/\sqrt{3} \approx 0.577$ lies in $(0, 1)$.
Check: $f'(0.577) = 3 \cdot 0.333 - 1 \approx 0$.
The typical uses of Rolle's theorem are to prove the mean value theorem and to bound the number of roots of an equation.
Watch out: it is easy to check differentiability on $(a, b)$ and forget continuity at $a$ and $b$, which is exactly what step 3 punishes.
