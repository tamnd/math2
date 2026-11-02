---
tag: S966EZX3ZT
kind: statement
role: theorem
name: Fast Fourier transform
msc: [65T50, 65Y20]
uses: [TST0GH66A5, 0TGV80E6A4, 9N8D9E5TB2, RY3QGW87HX, BH3NNAYJT5, 9HYM2ZMS31]
about: [TST0GH66A5]
sources:
  - url: https://en.wikipedia.org/wiki/Fast_Fourier_transform
same_as:
  wikidata: Q623950
  wikipedia: Fast Fourier transform
---

## Statement

There is a constant $C$ with the following property.
For $x \in \C^N$ let $X$ be its [[discrete Fourier transform|TST0GH66A5]],
$$X_k = \sum_{n=0}^{N-1} x_n e^{-2\pi i nk/N}, \qquad 0 \le k < N.$$
For every integer $N \ge 2$ some algorithm computes $X$ from any $x \in \C^N$ and precomputed roots of unity.
It uses at most $C N \log_2 N$ complex additions and multiplications.
An algorithm of this kind is called a *fast Fourier transform* (FFT).

## Remarks

For $N = 2^m$ the radix-2 [[Cooley–Tukey algorithm|9N8D9E5TB2]] gives the bound: it uses $\frac{N}{2} \log_2 N$ complex multiplications and $N \log_2 N$ complex additions.
For general $N$, [[Bluestein's algorithm|RY3QGW87HX]] rewrites the transform as a cyclic convolution of a power-of-two length $M < 4N$, computed by three radix-2 FFTs plus $O(N)$ operations.
Evaluating the $N$ defining sums directly needs about $N^2$ multiplications, so the gain is a factor of order $N / \log N$.
The inverse transform has the same form with $e^{+2\pi i nk/N}$ and a factor $1/N$, so it is also computed by an FFT.
The bound counts arithmetic operations.
In floating-point arithmetic the FFT is also accurate: its normwise error bound grows like $\log_2 N$ times the unit roundoff, against about $N$ times for direct evaluation.
Whether $\Theta(N \log N)$ operations are necessary is not known in general; lower bounds are known only for restricted models of computation.

## Explanations

### L1 human

The discrete Fourier transform turns a list of $N$ samples into $N$ frequency coefficients.
Done naively, it needs $N^2$ multiplications, which is a trillion for a million samples.
A fast Fourier transform does the same job in a multiple of $N \log N$ steps, about twenty million for a million samples.
This speed-up is what makes digital audio, image compression and fast multiplication of large numbers practical.

### L2 human

"FFT" names a family of algorithms rather than one method: Cooley–Tukey for composite lengths, the [[prime-factor algorithm|BH3NNAYJT5]] for coprime factors, and [[Rader's|9HYM2ZMS31]] or Bluestein's algorithm for prime lengths.
All exploit the structure of the DFT matrix $(\omega^{nk})$, which factors into $O(\log N)$ sparse matrices.
Combined with the cyclic convolution property of the DFT, the FFT computes convolutions and polynomial products of length $N$ in $O(N \log N)$ operations.
Spectral methods for differential equations and fast polynomial interpolation at roots of unity rest on this.
