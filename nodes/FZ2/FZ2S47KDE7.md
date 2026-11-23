---
tag: FZ2S47KDE7
kind: example
name: The limit of x^2 at 2 by epsilon and delta
msc: ["00A35", "26A03"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [RXG5JTZ2PZ]
uses: [RXG5JTZ2PZ, 0GBZDAFPX8, 03HF5PMY5T, 0FFXKTKKQC]
sources:
  - url: https://en.wikipedia.org/wiki/(%CE%B5,_%CE%B4)-definition_of_limit
    locator: lead section
---

## Example

We prove $\lim_{x \to 2} x^2 = 4$ from the [[epsilon-delta definition of a limit|0GBZDAFPX8]], by the method of [[writing epsilon-delta proofs|RXG5JTZ2PZ]].
The goal: for each $\varepsilon > 0$ there is $\delta > 0$ such that $0 < \lvert x - 2 \rvert < \delta$ implies $\lvert x^2 - 4 \rvert < \varepsilon$.

The scratch work, which is not part of the proof, runs backward from the goal.
Factor $\lvert x^2 - 4 \rvert = \lvert x - 2 \rvert \cdot \lvert x + 2 \rvert$; the first factor is the one that $\delta$ controls.
The second factor needs a bound: if $\lvert x - 2 \rvert < 1$, then $1 < x < 3$, so $3 < x + 2 < 5$.
Then $\lvert x^2 - 4 \rvert < 5 \lvert x - 2 \rvert$, which is at most $\varepsilon$ when $\lvert x - 2 \rvert \le \varepsilon/5$.
Both demands hold when $\lvert x - 2 \rvert < \min(1, \varepsilon/5)$.

The proof runs forward.

1. Let $\varepsilon > 0$ and define $\delta = \min(1, \varepsilon/5)$.
   Then $\delta > 0$, since both numbers are positive.
2. Let $x$ be a real number with $0 < \lvert x - 2 \rvert < \delta$.
3. Since $\delta \le 1$, we have $\lvert x - 2 \rvert < 1$, so $1 < x < 3$ and $\lvert x + 2 \rvert = x + 2 < 5$.
4. Since $\delta \le \varepsilon/5$, we have $\lvert x - 2 \rvert < \varepsilon/5$.
5. Both factors are non-negative and each is below its bound, so
   $$\lvert x^2 - 4 \rvert = \lvert x - 2 \rvert \cdot \lvert x + 2 \rvert < \frac{\varepsilon}{5} \cdot 5 = \varepsilon.$$
6. Since $\varepsilon > 0$ was arbitrary, $\lim_{x \to 2} x^2 = 4$.

Check: for $\varepsilon = 0.1$ the proof gives $\delta = 0.02$, and $x = 2.019$ gives $x^2 = 4.076361$, so $\lvert x^2 - 4 \rvert = 0.076361 < 0.1$.

## Remarks

The number $1$ in $\min(1, \varepsilon/5)$ is a choice, and any fixed positive number works with a different bound.
With $\lvert x - 2 \rvert < \tfrac12$ we get $\lvert x + 2 \rvert < 4.5$ and $\delta = \min(\tfrac12, \varepsilon/4.5)$.
For large $\varepsilon$ the restriction $\delta \le 1$ is the active one: $\varepsilon = 10$ gives $\delta = 1$, not $2$.
The estimate also holds at $x = 2$, so the same proof shows that $x^2$ is continuous at $2$.

The method works at every point $a$.
By the [[triangle inequality|03HF5PMY5T]], $\lvert x - a \rvert < 1$ gives $\lvert x + a \rvert \le \lvert x - a \rvert + 2\lvert a \rvert < 1 + 2\lvert a \rvert$, so $\delta = \min\big(1, \varepsilon/(2\lvert a \rvert + 1)\big)$ proves $\lim_{x \to a} x^2 = a^2$.
At $a = 2$ this gives $\varepsilon/5$ again.
This $\delta$ tends to $0$ as $\lvert a \rvert$ grows, and no single $\delta$ serves every $a$: that is why $x^2$ is not uniformly continuous on $\mathbb{R}$.

## Explanations

### L1 human

We want $x^2$ as close to $4$ as we wish, once $x$ is close enough to $2$.
The difference $x^2 - 4$ is $(x - 2)$ times $(x + 2)$.
Near $2$, the factor $x + 2$ is less than $5$.
So if $x$ is within one fifth of the tolerance from $2$, then $x^2$ is within the tolerance from $4$.
For a tolerance of $0.1$, a distance of $0.02$ is enough.

### L2 human

We repeat the method for $\lim_{x \to -1} (x^2 + x) = 0$.

1. Scratch work: $\lvert x^2 + x \rvert = \lvert x + 1 \rvert \cdot \lvert x \rvert$.
   If $\lvert x + 1 \rvert < 1$, then $-2 < x < 0$, so $\lvert x \rvert < 2$.
2. Proof: let $\varepsilon > 0$, and let $\delta = \min(1, \varepsilon/2)$.
3. Let $0 < \lvert x + 1 \rvert < \delta$.
   Then $\lvert x + 1 \rvert < 1$, so $\lvert x \rvert < 2$ by step 1.
4. Also $\lvert x + 1 \rvert < \varepsilon/2$, so $\lvert x^2 + x \rvert = \lvert x + 1 \rvert \cdot \lvert x \rvert < \frac{\varepsilon}{2} \cdot 2 = \varepsilon$.

"Factor, bound the second factor on a fixed interval, take a minimum" is the usual route to the limit of a polynomial or a rational function at a point.
Watch out for the interval: with $\lvert x + 1 \rvert < 1$ the bound for $\lvert x \rvert$ is $2$, not $1$.
