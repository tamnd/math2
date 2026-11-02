---
tag: R1QBNFTHFP
kind: statement
role: theorem
name: Rejection sampling
msc: [65C10, 65C05]
uses: [0ZY9DX8FBF, 0AREFQ9Z65, 0990W5PN13, 04P2SR252N]
about: [0ZY9DX8FBF]
sources:
  - url: https://en.wikipedia.org/wiki/Rejection_sampling
same_as:
  wikidata: Q381699
  wikipedia: Rejection sampling
---

## Statement

Let $f$ and $g$ be [[probability density functions|0ZY9DX8FBF]] on $\R^d$, and let $M \ge 1$ be a constant with $f(x) \le M g(x)$ for all $x$.
Let $(Y_1, V_1), (Y_2, V_2), \ldots$ be independent pairs, where $Y_j$ has density $g$, $V_j$ has the [[uniform distribution|0AREFQ9Z65]] on $(0, 1)$, and $Y_j$ and $V_j$ are independent.
Call trial $j$ *accepted* if $g(Y_j) > 0$ and $V_j \le f(Y_j) / (M g(Y_j))$.
Let $\tau$ be the index of the first accepted trial and $X = Y_\tau$.
Then:

1. each trial is accepted with probability $1/M$;
2. the [[conditional distribution|0990W5PN13]] of $Y_j$ given that trial $j$ is accepted has density $f$;
3. $\tau$ is finite almost surely, has the [[geometric distribution|04P2SR252N]] with success probability $1/M$, so $\mathbb E\tau = M$, and $X$ has density $f$.

## Remarks

For a measurable set $A$, $P(Y_j \in A,\ \text{accepted}) = \int_A g(y) \frac{f(y)}{M g(y)}\, dy = \frac{1}{M} \int_A f(y)\, dy$, where the integral runs over the points with $g > 0$, which carry all the mass of $f$ since $f \le M g$.
Taking $A = \R^d$ gives clause 1, and dividing by $1/M$ gives clause 2.
Clause 3 follows because the trials are independent and $X$ is the value of the first success.
Example: to sample the density $f(x) = 2x$ on $[0, 1]$, take $g = 1$ on $[0, 1]$ and $M = 2$; a uniform $Y$ is accepted when $V \le Y$, which happens half the time.
The bound $f \le M g$ is necessary: if $f > M g$ on a set of positive measure, the accepted values follow the density proportional to $\min(f, M g)$, not $f$.
The method needs $f$ only up to a constant factor: if $f = c \tilde f$ with unknown $c$, one uses $\tilde f \le \tilde M g$ and the acceptance test $V \le \tilde f(Y)/(\tilde M g(Y))$.

## Explanations

### L1 human

To sample from a difficult distribution, sample from an easier one that sits above it after scaling, and throw away some of the samples.
Picture the graph of $f$ under the graph of $M g$: pick a random point under $M g$, and keep it only if it also lies under $f$.
The kept points are uniform under the graph of $f$, so their horizontal positions have density $f$.
On average $M$ tries are needed per kept sample, so the envelope $M g$ should fit $f$ closely.

### L2 human

Rejection sampling, due to von Neumann, is exact, needs no inverse distribution function, and works in any dimension.
Its weakness is the acceptance rate $1/M$, which typically decays exponentially with the dimension, so in high dimension Markov chain Monte Carlo is used instead.
Many fast samplers are refinements of it.
The ziggurat algorithm uses a cheap envelope made of rectangles.
Adaptive rejection sampling builds the envelope from tangent lines of $\log f$ when $f$ is log-concave.
The number of trials before acceptance is geometric, so the cost per sample is random but with all moments finite.
