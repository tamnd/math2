---
tag: 9E4PCEXSJ3
kind: example
name: The limit of 1/x at 3 by epsilon and delta
msc: ["00A35", "26A03"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [RXG5JTZ2PZ]
uses: [RXG5JTZ2PZ, 0GBZDAFPX8, 0FFXKTKKQC]
sources:
  - url: https://en.wikipedia.org/wiki/(%CE%B5,_%CE%B4)-definition_of_limit
    locator: lead section
---

## Example

Let $f(x) = \frac1x$ on the domain $D = \mathbb{R} \setminus \{0\}$.
We prove $\lim_{x \to 3} \frac1x = \frac13$ by an [[epsilon-delta proof|RXG5JTZ2PZ]].
The new feature is that the troublesome factor needs a bound from below, not from above.

The scratch work starts from the goal.
Over a common denominator, $\left\lvert \frac1x - \frac13 \right\rvert = \frac{\lvert x - 3 \rvert}{3 \lvert x \rvert}$.
The factor $\frac{1}{3\lvert x \rvert}$ is large when $x$ is near $0$, so we keep $x$ away from $0$.
If $\lvert x - 3 \rvert < 1$, then $2 < x < 4$, so $3\lvert x \rvert > 6$.
Then the difference is less than $\frac{\lvert x - 3 \rvert}{6}$, which is at most $\varepsilon$ when $\lvert x - 3 \rvert \le 6\varepsilon$.

The proof runs forward.

1. Let $\varepsilon > 0$ and define $\delta = \min(1, 6\varepsilon)$, which is positive.
2. Let $x \in D$ with $0 < \lvert x - 3 \rvert < \delta$.
3. Since $\delta \le 1$, we have $2 < x < 4$, so $x > 0$ and $3 \lvert x \rvert = 3x > 6$.
4. So $\left\lvert \frac1x - \frac13 \right\rvert = \frac{\lvert x - 3 \rvert}{3x} < \frac{\lvert x - 3 \rvert}{6}$.
5. Since $\delta \le 6\varepsilon$, we have $\lvert x - 3 \rvert < 6\varepsilon$, so the difference is less than $\frac{6\varepsilon}{6} = \varepsilon$.
6. Since $\varepsilon > 0$ was arbitrary, $\lim_{x \to 3} \frac1x = \frac13$.

Check: for $\varepsilon = 0.1$ the proof gives $\delta = \min(1, 0.6) = 0.6$, and $x = 2.5$ gives $\left\lvert 0.4 - \frac13 \right\rvert = \frac{1}{15} \approx 0.067 < 0.1$.

## Remarks

Step 3 is where the restriction $\delta \le 1$ does its work.
Without it, $x$ could come close to $0$, and no bound $\frac{1}{3\lvert x \rvert} < M$ would hold.
The restriction must keep $x$ away from the bad point: $\delta \le 3$ fails, because then $x$ can be any number in $(0, 6)$ other than $3$, and $\frac{1}{3x}$ is unbounded there.

The same proof works at each point $a > 0$.
Restrict to $\delta \le a/2$, so that $x > a/2$ and
$$\left\lvert \frac1x - \frac1a \right\rvert = \frac{\lvert x - a \rvert}{a x} < \frac{2 \lvert x - a \rvert}{a^2}.$$
So $\delta = \min(a/2, a^2 \varepsilon/2)$ works.
This $\delta$ tends to $0$ as $a \to 0$, which reflects that $\frac1x$ is not uniformly continuous on $(0, \infty)$.

## Explanations

### L1 human

The fraction $\frac1x$ is close to $\frac13$ when $x$ is close to $3$, but $x$ must stay away from $0$, where $\frac1x$ becomes huge.
If $x$ is between $2$ and $4$, the difference $\frac1x - \frac13$ is at most one sixth of the distance from $x$ to $3$.
So to get within $0.1$ of $\frac13$, it is enough that $x$ is within $0.6$ of $3$.
For $x = 2.5$, the value $\frac{1}{2.5} = 0.4$ differs from $\frac13$ by about $0.067$.

### L2 human

We use the same idea for $\lim_{x \to 1} \frac{x}{x + 1} = \frac12$, on the domain $x \neq -1$.

1. Scratch work: $\left\lvert \frac{x}{x + 1} - \frac12 \right\rvert = \frac{\lvert 2x - (x + 1) \rvert}{2 \lvert x + 1 \rvert} = \frac{\lvert x - 1 \rvert}{2 \lvert x + 1 \rvert}$.
2. If $\lvert x - 1 \rvert < 1$, then $0 < x < 2$, so $x + 1 > 1$ and $2 \lvert x + 1 \rvert > 2$.
3. Proof: let $\varepsilon > 0$ and $\delta = \min(1, 2\varepsilon)$, and let $0 < \lvert x - 1 \rvert < \delta$.
4. By step 2, $\left\lvert \frac{x}{x + 1} - \frac12 \right\rvert < \frac{\lvert x - 1 \rvert}{2} < \frac{2\varepsilon}{2} = \varepsilon$.

A lower bound for a denominator is the core of every limit of a quotient, including the proof of the limit law for quotients.
Watch out: the interval must keep the denominator away from $0$, so it cannot contain the zero of the denominator.
