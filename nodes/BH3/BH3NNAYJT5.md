---
tag: BH3NNAYJT5
kind: statement
role: theorem
name: Prime-factor FFT algorithm
msc: [65T50]
uses: [TST0GH66A5, 0FNN9B4W64, 9N8D9E5TB2]
about: [TST0GH66A5]
sources:
  - url: https://en.wikipedia.org/wiki/Prime-factor_FFT_algorithm
same_as:
  wikidata: Q7243214
  wikipedia: Prime-factor FFT algorithm
---

## Statement

For $M \ge 1$ let $\omega_M = e^{-2\pi i/M}$.
Let $N = N_1 N_2$ where $N_1, N_2 \ge 1$ are coprime integers.
Let $x \in \C^N$ and let $X$ be its [[discrete Fourier transform|TST0GH66A5]], $X_k = \sum_{n=0}^{N-1} x_n \omega_N^{nk}$.
For $0 \le n_1 < N_1$ and $0 \le n_2 < N_2$ let $n(n_1, n_2) = (N_2 n_1 + N_1 n_2) \bmod N$.
For $0 \le k_1 < N_1$ and $0 \le k_2 < N_2$ let $k(k_1, k_2)$ be the unique $k \in \set{0, \ldots, N-1}$ with $k \equiv k_1 \pmod{N_1}$ and $k \equiv k_2 \pmod{N_2}$.
Then both index maps are bijections onto $\set{0, \ldots, N-1}$, and
$$X_{k(k_1, k_2)} = \sum_{n_1=0}^{N_1-1} \sum_{n_2=0}^{N_2-1} x_{n(n_1, n_2)}\, \omega_{N_1}^{n_1 k_1}\, \omega_{N_2}^{n_2 k_2}.$$
So a DFT of length $N$ is a two-dimensional DFT of size $N_1 \times N_2$, with no twiddle factors.

## Remarks

The output map is a bijection by the [[Chinese remainder theorem|0FNN9B4W64]].
The input map is a bijection because $n(n_1, n_2) \equiv N_2 n_1 \pmod{N_1}$ and $N_2$ is invertible modulo $N_1$, and similarly modulo $N_2$.
For the formula, $\omega_N^{N_2 n_1 k} = \omega_{N_1}^{n_1 k} = \omega_{N_1}^{n_1 k_1}$ since $k \equiv k_1 \pmod{N_1}$, and in the same way $\omega_N^{N_1 n_2 k} = \omega_{N_2}^{n_2 k_2}$.
Example: $N = 6 = 2 \cdot 3$; the input order $n(n_1, n_2) = (3n_1 + 2n_2) \bmod 6$ lists $0, 2, 4$ for $n_1 = 0$ and $3, 5, 1$ for $n_1 = 1$.
Coprimality is necessary: for $N_1 = N_2 = 2$ the input map gives $2n_1 + 2n_2 \bmod 4$, which takes only the values $0$ and $2$.
For non-coprime factors one uses the [[Cooley–Tukey algorithm|9N8D9E5TB2]], which pays with twiddle factors.

## Explanations

### L1 human

Suppose the length of a Fourier transform is a product of two coprime numbers, such as $6 = 2 \cdot 3$ or $15 = 3 \cdot 5$.
Then the input and output can be reordered so that the transform becomes a grid of small transforms.
The reordering is the Chinese remainder theorem in action.
Unlike the Cooley–Tukey split, no extra multiplications are needed between the two stages.

### L2 human

The algorithm is due to Good and to Thomas, and is often called the Good–Thomas algorithm.
It is used for lengths with several coprime factors, with each small length done by a hand-optimised module, for example Winograd's.
The price is the more complicated index arithmetic.
A prime-power length such as $8$ or $9$ cannot be split this way, and a Cooley–Tukey or another FFT is used for such factors.
