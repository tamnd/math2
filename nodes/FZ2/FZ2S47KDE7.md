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
The goal is: for each $\varepsilon > 0$ there is $\delta > 0$ such that $0 < \lvert x - 2 \rvert < \delta$ implies $\lvert x^2 - 4 \rvert < \varepsilon$.

Scratch work, which is not part of the proof:

1. We factor: $\lvert x^2 - 4 \rvert = \lvert x - 2 \rvert \cdot \lvert x + 2 \rvert$. The first factor is the one that $\delta$ controls.
2. The second factor must be bounded. If $\lvert x - 2 \rvert < 1$, then $1 < x < 3$, so $3 < x + 2 < 5$ and $\lvert x + 2 \rvert < 5$.
3. Then $\lvert x^2 - 4 \rvert < 5 \lvert x - 2 \rvert$, and this is at most $\varepsilon$ when $\lvert x - 2 \rvert \le \varepsilon/5$.
4. Both restrictions hold when $\lvert x - 2 \rvert < \min(1, \varepsilon/5)$.

The proof:

1. Let $\varepsilon > 0$. Define $\delta = \min(1, \varepsilon/5)$. Then $\delta > 0$, since both numbers are positive.
2. Let $x$ be a real number with $0 < \lvert x - 2 \rvert < \delta$.
3. Since $\delta \le 1$, we have $\lvert x - 2 \rvert < 1$, so $1 < x < 3$ and $\lvert x + 2 \rvert = x + 2 < 5$.
4. Since $\delta \le \varepsilon/5$, we have $\lvert x - 2 \rvert < \varepsilon/5$.
5. So $\lvert x^2 - 4 \rvert = \lvert x - 2 \rvert \cdot \lvert x + 2 \rvert < \frac{\varepsilon}{5} \cdot 5 = \varepsilon$. In this step both factors are non-negative, and each is less than its bound.
6. Since $\varepsilon > 0$ was arbitrary, $\lim_{x \to 2} x^2 = 4$.

A check with numbers: for $\varepsilon = 0.1$ the proof gives $\delta = 0.02$.
For $x = 2.019$ we get $x^2 = 4.076361$, and $\lvert x^2 - 4 \rvert = 0.076361 < 0.1$.

## Remarks

1. The number $1$ in $\min(1, \varepsilon/5)$ is a choice. Any fixed positive number works, but it changes the bound: with $\lvert x - 2 \rvert < \frac12$ we get $\lvert x + 2 \rvert < 4.5$ and $\delta = \min(\frac12, \varepsilon/4.5)$.
2. For large $\varepsilon$ the restriction $\delta \le 1$ is the active one. For $\varepsilon = 10$ we get $\delta = 1$, not $2$.
3. The proof shows more: $x^2$ is continuous at $2$, because the estimate also holds at $x = 2$.
4. The same method shows $\lim_{x \to a} x^2 = a^2$ for each real $a$, with $\delta = \min(1, \varepsilon / (2\lvert a \rvert + 1))$. Here $\lvert x + a \rvert \le \lvert x - a \rvert + 2 \lvert a \rvert < 1 + 2\lvert a \rvert$, by the [[triangle inequality|03HF5PMY5T]].
5. The value of $\delta$ in remark 4 depends on $a$, and it tends to $0$ as $\lvert a \rvert$ grows. This is why $x^2$ is not uniformly continuous on $\mathbb{R}$.

## Explanations

### L1 human

We want to show that $x^2$ is as close to $4$ as we wish, once $x$ is close enough to $2$.
The difference $x^2 - 4$ is $(x - 2)$ times $(x + 2)$.
Near $2$, the factor $x + 2$ is less than $5$.
So if $x$ is within one fifth of the tolerance from $2$, then $x^2$ is within the tolerance from $4$.
For a tolerance of $0.1$, a distance of $0.02$ is enough.

### L2 human

We repeat the method for $\lim_{x \to -1} (x^2 + x) = 0$.

1. Scratch work: $\lvert x^2 + x \rvert = \lvert x + 1 \rvert \cdot \lvert x \rvert$. If $\lvert x + 1 \rvert < 1$, then $-2 < x < 0$, so $\lvert x \rvert < 2$.
2. Proof: let $\varepsilon > 0$, and let $\delta = \min(1, \varepsilon/2)$.
3. Let $0 < \lvert x + 1 \rvert < \delta$. Then $\lvert x + 1 \rvert < 1$, so $\lvert x \rvert < 2$ by step 1.
4. Also $\lvert x + 1 \rvert < \varepsilon/2$. So $\lvert x^2 + x \rvert = \lvert x + 1 \rvert \cdot \lvert x \rvert < \frac{\varepsilon}{2} \cdot 2 = \varepsilon$.

The pattern "factor, bound the second factor on a fixed interval, take a minimum" is typical for the limit of a polynomial or a rational function at a point.
A trap is to bound the second factor with the wrong interval: with $\lvert x + 1 \rvert < 1$ the bound for $\lvert x \rvert$ is $2$, not $1$.
