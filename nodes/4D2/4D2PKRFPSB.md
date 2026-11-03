---
tag: 4D2PKRFPSB
kind: statement
role: theorem
name: Water-filling for parallel Gaussian channels
msc: [94A40, 94A24, 90C25]
uses: [RYFPT7P01J, J7MZ2XQP9M, 0GCM7B6PBK]
about: [J7MZ2XQP9M]
sources:
  - url: https://en.wikipedia.org/wiki/Water-filling_algorithm
---

## Statement

Let $k \ge 1$, let $N_1, \dots, N_k > 0$ and let $P > 0$.
Consider $k$ parallel channels $Y_i = X_i + Z_i$, $i = 1, \dots, k$, where $Z_1, \dots, Z_k$ are independent, $Z_i$ has the normal distribution $N(0, N_i)$, and the noise is independent of the input.
The input must satisfy the total power constraint $\sum_{i=1}^k E[X_i^2] \le P$.
Then the [[capacity|J7MZ2XQP9M]] of this channel, in bits per use, is
$$C = \sum_{i=1}^k \frac12 \log_2\!\left(1 + \frac{P_i}{N_i}\right), \qquad P_i = \max(\nu - N_i, 0),$$
where the water level $\nu$ is the unique real number with $\sum_{i=1}^k \max(\nu - N_i, 0) = P$.
The capacity is achieved by independent inputs $X_i \sim N(0, P_i)$.

## Remarks

The idea of the proof: as for a single [[AWGN channel|RYFPT7P01J]], independent Gaussian inputs are optimal, and the mutual information becomes $\sum_i \frac12 \log_2(1 + P_i / N_i)$ for a power split $P_1, \dots, P_k \ge 0$ with $\sum_i P_i = P$.
This is a [[concave function|0GCM7B6PBK]] of $(P_1, \dots, P_k)$, so its maximum on the simplex is given by the Karush–Kuhn–Tucker conditions.
These conditions say that $P_i + N_i$ equals a common constant $\nu$ on every channel with $P_i > 0$, and that $N_i \ge \nu$ on every channel with $P_i = 0$.

Example: take $k = 2$, $N_1 = 1$ and $N_2 = 3$.
For $P = 1$ the level is $\nu = 2$, so $P_1 = 1$ and $P_2 = 0$, and $C = \frac12$ bit.
For $P = 4$ the level is $\nu = 4$, so $P_1 = 3$ and $P_2 = 1$, and $C = 1 + \frac12 \log_2 \frac43$ bits.

The name comes from a picture: pour a volume $P$ of water into a vessel whose floor has height $N_i$ above cell $i$.
The water settles at level $\nu$, and its depth above cell $i$ is $P_i$.

## Explanations

### L1 human

Suppose you can send over several noisy lines at once, with a fixed total budget of power.
Water-filling says how to split the budget: put more power into the quieter lines, and none into lines that are too noisy.
In the end, signal plus noise has the same level on every line that is used, like water finding a flat surface.

### L2 human

The same rule applies to a single Gaussian channel with coloured noise, after a change of basis that makes the noise components independent.
For a channel whose noise varies with frequency, the sum becomes an integral over frequency, and power is poured into the frequencies where the noise spectrum is low.
Consider a multiple-antenna channel $Y = HX + Z$ with white noise of variance $N$ and a transmitter that knows $H$.
The singular value decomposition of $H$ gives parallel channels with noise levels $N / \sigma_i^2$, one for each nonzero singular value $\sigma_i$.
Water-filling then applies to these channels.
A dual form, reverse water-filling, gives the rate–distortion function of parallel Gaussian sources.
