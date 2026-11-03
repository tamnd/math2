---
tag: MMSZK6CYRX
kind: example
name: Sherrington–Kirkpatrick model
msc: [82B44, 60K35, 82D30]
instance_of: [EHPA4B5S5W]
uses: [05AQE0QR0D, R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Spin_glass
---

## Example

Let $N \ge 2$ and let $(g_{ij})_{1 \le i < j \le N}$ be independent standard [[Gaussian|05AQE0QR0D]] random variables.
The *Sherrington–Kirkpatrick model* is the random Hamiltonian
$$H_N(\sigma) = -\frac{1}{\sqrt{N}} \sum_{1 \le i < j \le N} g_{ij} \sigma_i \sigma_j, \qquad \sigma \in \set{-1, +1}^N,$$
with partition function $Z_N(\beta) = \sum_{\sigma} e^{-\beta H_N(\sigma)}$ for the inverse temperature $\beta \ge 0$.

Check: the couplings $J_{ij} = g_{ij} / \sqrt{N}$ are independent and symmetric, so each takes both signs with probability $1/2$.
So it is a [[spin glass|EHPA4B5S5W]] in which every spin interacts with every other spin.
For each fixed $\sigma$, $H_N(\sigma)$ is a centred Gaussian variable of variance $\frac{1}{N} \binom{N}{2} = \frac{N-1}{2}$, so the energy grows like $N$, as it should.

## Remarks

By Jensen's inequality, $\mathbb{E} \log Z_N \le \log \mathbb{E} Z_N = N \log 2 + \beta^2 (N-1)/4$.
This annealed bound gives the correct free energy only at high temperature.
The exact limit of $\frac{1}{N} \mathbb{E} \log Z_N$ for all $\beta$ is the [[Parisi formula|32S4Y36QNK]].
The model is the mean-field version of the [[Edwards–Anderson model|S5F9QX7YSP]], in the same way as the [[Curie–Weiss model|A6GX2K5YFB]] is the mean-field version of the [[Ising model|R0KGM32QN6]].

## Explanations

### L1 human

Take $N$ magnets and connect every pair, not only neighbours.
Give each pair a random strength from a bell curve, positive or negative, and scale it down by $\sqrt{N}$ so that the total energy stays of size $N$.
Sherrington and Kirkpatrick proposed this model in 1975 as a version of a spin glass that should be easy to solve.
It turned out to be very hard, and its solution by Parisi became a landmark of the field.
