---
tag: RY3QGW87HX
kind: statement
role: theorem
name: Bluestein's FFT algorithm
msc: [65T50, 65Y20]
uses: [TST0GH66A5, 2Z29JN3VES, 9N8D9E5TB2, 0TGV80E6A4]
about: [TST0GH66A5]
sources:
  - url: https://en.wikipedia.org/wiki/Chirp_Z-transform
    locator: Bluestein's algorithm
---

## Statement

Let $N \ge 1$, let $x \in \C^N$ and let $X$ be its [[discrete Fourier transform|TST0GH66A5]], $X_k = \sum_{n=0}^{N-1} x_n e^{-2\pi i nk/N}$.
For integers $m$ let $b_m = e^{\pi i m^2/N}$, and for $0 \le n < N$ let $a_n = x_n e^{-\pi i n^2/N}$.
Then for $0 \le k < N$,
$$X_k = \overline{b_k} \sum_{n=0}^{N-1} a_n\, b_{k-n}.$$
Let $M \ge 2N - 1$, let $\alpha \in \C^M$ be $a$ followed by zeros, and let $\beta \in \C^M$ have $\beta_j = b_j$ for $0 \le j < N$, $\beta_{M-j} = b_{-j}$ for $1 \le j < N$, and zeros elsewhere.
Then $X_k = \overline{b_k}\, (\alpha \circledast \beta)_k$ for $0 \le k < N$, where $(\alpha \circledast \beta)_k = \sum_{j=0}^{M-1} \alpha_j \beta_{(k-j) \bmod M}$ is the cyclic [[convolution|2Z29JN3VES]] of length $M$.
Take $M$ a power of $2$ and compute the cyclic convolution with three [[radix-2 FFTs|9N8D9E5TB2]] of length $M$.
Then the DFT of any length $N$ costs $O(N \log N)$ operations.

## Remarks

The key identity is $nk = \frac12 \bigl(n^2 + k^2 - (k-n)^2\bigr)$, which gives $e^{-2\pi i nk/N} = e^{-\pi i n^2/N} e^{-\pi i k^2/N} e^{\pi i (k-n)^2/N}$.
So the DFT is a pointwise product with a chirp, a convolution with the conjugate chirp, and another pointwise product.
The index $k - n$ runs from $-(N-1)$ to $N-1$, and the zero padding to $M \ge 2N-1$ makes the cyclic convolution agree with this linear convolution on $0 \le k < N$.
The cyclic convolution of length $M$ equals the inverse DFT of the product of the DFTs of $\alpha$ and $\beta$.
Since one can choose $M < 4N$, the constant in $O(N \log N)$ does not depend on the arithmetic of $N$; in particular prime $N$ is allowed.
The same identity with $e^{-2\pi i/N}$ replaced by any complex $z$ evaluates the chirp z-transform $\sum_n x_n z^{-nk}$, which is the subject of the source article.

## Explanations

### L1 human

The fast Fourier transform is easiest when the length is a power of two.
Bluestein's trick rewrites a transform of any length, even a prime length, as a convolution.
A convolution can be padded with zeros to a power-of-two length and computed with power-of-two FFTs.
So every length gets the speed $N \log N$, at the price of a larger constant.

### L2 human

The algorithm is the standard fallback in FFT libraries for lengths with large prime factors.
Compared with Rader's algorithm, it does not need a primitive root and works for every $N$, not only primes.
It needs about three FFTs of length $M \approx 2N$ to $4N$, so it is slower than a direct Cooley–Tukey FFT of a highly composite length.
The chirp $e^{\pi i m^2/N}$ is the same object as in the fractional Fourier transform and in radar signal processing.
