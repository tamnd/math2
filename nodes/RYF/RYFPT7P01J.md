---
tag: RYFPT7P01J
kind: example
name: Additive white Gaussian noise channel
msc: [94A40, 94A24, 60G15]
instance_of: [B9C5RBFATB]
uses: [J7MZ2XQP9M, A83CYGDXFG, B4PNYNYVKK, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Additive_white_Gaussian_noise
---

## Example

Fix a power limit $P > 0$ and a noise variance $N > 0$.
The discrete-time *additive white Gaussian noise channel* (AWGN channel) is the [[channel|B9C5RBFATB]] with real input $X_i$ and output $Y_i = X_i + Z_i$ for $i = 1, 2, \dots$.
The noise terms $Z_1, Z_2, \dots$ are independent random variables with the [[normal distribution|05AQE0QR0D]] $N(0, N)$, independent of the input.
A codeword $(x_1, \dots, x_n)$ must satisfy the power constraint $\frac{1}{n} \sum_{i=1}^n x_i^2 \le P$.

Check of the capacity: for an input $X$ with $E[X^2] \le P$, the output has variance at most $P + N$.
With $h$ the [[differential entropy|B4PNYNYVKK]], the [[mutual information|A83CYGDXFG]] is
$$I(X; Y) = h(Y) - h(Y \mid X) = h(Y) - h(Z) \le \tfrac12 \log_2\big(2\pi e (P + N)\big) - \tfrac12 \log_2(2 \pi e N),$$
because the normal distribution has the largest differential entropy among distributions with a given variance.
Equality holds for $X \sim N(0, P)$.
So the [[capacity|J7MZ2XQP9M]] is
$$C = \frac12 \log_2\!\left(1 + \frac{P}{N}\right)$$
bits per channel use.
The ratio $P/N$ is the signal-to-noise ratio.
For $P = N$ the capacity is $1/2$ bit per use.

## Explanations

### L1 human

The AWGN channel is the standard model of a noisy analogue link.
The sender transmits a real number, and the receiver gets that number plus a random Gaussian error.
The errors at different times are independent and all have the same spread, which is what "white" means here.
Without a power limit the sender could shout over the noise, so the capacity depends on the ratio of signal power to noise power.
When that ratio is large, doubling it adds only about half a bit per use.
