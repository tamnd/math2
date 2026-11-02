---
tag: TJ9XPJ65YX
kind: definition
name: Discrete Fourier transform
msc: ["65T50", "42A38", "43A25"]
defines: TST0GH66A5
uses: [0YV2CKP2AV, 07GJV36896]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_Fourier_transform
---

## Definition

Let $N \ge 1$ be an integer and let $\omega_N = e^{-2\pi i / N}$, a primitive $N$-th [[root of unity|0YV2CKP2AV]], where $e^{z}$ is the [[complex exponential|07GJV36896]].
The *discrete Fourier transform* of a vector $x = (x_0, x_1, \dots, x_{N-1}) \in \C^N$ is the vector $X = (X_0, X_1, \dots, X_{N-1}) \in \C^N$ given by
$$X_k = \sum_{n=0}^{N-1} x_n\, \omega_N^{kn} = \sum_{n=0}^{N-1} x_n\, e^{-2\pi i k n / N}, \qquad k = 0, 1, \dots, N - 1.$$

## Remarks

The map $x \mapsto X$ is linear and invertible, with inverse
$$x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k\, e^{2\pi i k n / N}.$$
This follows from $\sum_{k=0}^{N-1} e^{2\pi i k m / N} = N$ if $N$ divides $m$ and $0$ otherwise.
It also gives the Parseval identity $\sum_k \abs{X_k}^2 = N \sum_n \abs{x_n}^2$, so $x \mapsto N^{-1/2} X$ is unitary.

Example: for $N = 2$, $X_0 = x_0 + x_1$ and $X_1 = x_0 - x_1$; so $(3, 1)$ has transform $(4, 2)$, and the inverse formula gives back $\frac12 (4 + 2, 4 - 2) = (3, 1)$.

Non-example: an infinite sequence $(x_n)_{n \in \Z}$ is not a vector of $\C^N$, so the definition does not apply; its analogue is the discrete-time Fourier transform, a function of a continuous frequency.

Indices are read modulo $N$, so the transform is the Fourier transform on the group $\Z / N\Z$.
It turns the cyclic convolution $(x * y)_n = \sum_{m} x_m y_{n - m}$ into the product $X_k Y_k$, and therefore diagonalizes every circulant matrix.
Some authors put the factor $\frac1N$ or $\frac{1}{\sqrt N}$ in the forward transform, or use $e^{+2\pi i k n/N}$.
