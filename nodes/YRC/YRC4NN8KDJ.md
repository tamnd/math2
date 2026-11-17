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
Then there is a point $c$ in $(a, b)$ with $f'(c) = 0$.
We apply the theorem once, and then we drop one hypothesis at a time.

1. All hypotheses hold: let $f(x) = x^2 - 1$ on $[-1, 1]$. It is a polynomial, so (H1) and (H2) hold, and $f(-1) = 0 = f(1)$. The derivative $f'(x) = 2x$ is $0$ at $c = 0$.
2. Drop (H2): let $f(x) = |x|$ on $[-1, 1]$, the [[absolute value|0FFXKTKKQC]]. It is continuous, and $f(-1) = 1 = f(1)$.
3. For $x < 0$ we have $f'(x) = -1$, and for $x > 0$ we have $f'(x) = 1$. At $x = 0$ the derivative does not exist. So no point $c$ has $f'(c) = 0$.
4. Drop (H1): let $f(x) = x$ for $0 \leq x < 1$ and $f(1) = 0$. Then $f(0) = 0 = f(1)$, so (H3) holds.
5. On $(0, 1)$ we have $f'(x) = 1$, so (H2) holds and no point has $f'(c) = 0$. The function is not continuous at $1$, because $f(x) \to 1$ as $x \to 1$ but $f(1) = 0$.
6. Drop (H3): let $f(x) = x$ on $[0, 1]$. It is continuous and differentiable, and $f(0) = 0 \neq 1 = f(1)$.
7. On $(0, 1)$ we have $f'(x) = 1$, so no point has $f'(c) = 0$.
8. In steps 2 to 7, each function meets two of the three hypotheses and fails the conclusion. So each hypothesis is needed.

## Remarks

The example shows the three roles of the [[hypotheses|W48XN2MEM9]].
Continuity on the closed interval stops a jump at an end point, differentiability stops a corner, and the equal end values force the graph to turn.
Step 4 shows that continuity is needed also at the end points, not only inside the interval.

When we replace (H3) by nothing, the conclusion changes instead of failing: the mean value theorem gives a point $c$ with $f'(c) = \frac{f(b) - f(a)}{b - a}$.
Rolle's theorem is the case $f(a) = f(b)$ of the mean value theorem.

## Explanations

### L1 human

Rolle's theorem says that a smooth curve that starts and ends at the same height has a flat point somewhere in between.
A V-shaped graph, such as $|x|$ from $-1$ to $1$, starts and ends at the same height but has a sharp corner instead of a flat point.
A graph that climbs all the way and then jumps down at the very end also has no flat point.
A straight line that ends higher than it starts has no flat point either.
So each condition of the theorem is really needed.

### L2 human

We apply the theorem to $f(x) = x^3 - x$ on $[0, 1]$.

1. The function is a polynomial, so it is continuous on $[0, 1]$ and differentiable on $(0, 1)$.
2. We have $f(0) = 0$ and $f(1) = 1 - 1 = 0$, so $f(0) = f(1)$.
3. The theorem gives $c$ in $(0, 1)$ with $f'(c) = 0$.
4. We find it: $f'(x) = 3x^2 - 1 = 0$ gives $x = \pm \frac{1}{\sqrt{3}}$, and $c = \frac{1}{\sqrt{3}} \approx 0.577$ is in $(0, 1)$.

The typical use of Rolle's theorem is to prove the mean value theorem, and to show that an equation has at most a certain number of roots.
A trap is to check differentiability on $(a, b)$ and to forget continuity at $a$ and $b$, as step 4 of the example shows.
