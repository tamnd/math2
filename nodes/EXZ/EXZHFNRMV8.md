---
tag: EXZHFNRMV8
kind: definition
name: Non-uniform discrete Fourier transform
msc: [65T50, 65T40]
defines: NY851TZ24X
uses: [TST0GH66A5]
sources:
  - url: https://en.wikipedia.org/wiki/Non-uniform_discrete_Fourier_transform
---

## Definition

Let $N \ge 1$ and $K \ge 1$ be integers.
Let $p_0, \ldots, p_{N-1}$ be real numbers, the sample points, and let $f_0, \ldots, f_{K-1}$ be real numbers, the frequencies.
The *non-uniform discrete Fourier transform* of a vector $x = (x_0, \ldots, x_{N-1}) \in \C^N$ is the vector $X \in \C^K$ given by
$$X_k = \sum_{n=0}^{N-1} x_n\, e^{-2\pi i\, p_n f_k}, \qquad k = 0, \ldots, K-1.$$
It is of *type I* if $f_k = k$ for all $k$, with arbitrary $p_n$.
It is of *type II* if $p_n = n/N$ for all $n$, with arbitrary $f_k$.
It is of *type III* if both families are arbitrary.
The numbering of types I and II varies between authors; some, including the cited source, swap the two names.

## Remarks

Example: with $K = N$, $p_n = n/N$ and $f_k = k$, the sum is $\sum_n x_n e^{-2\pi i nk/N}$, the ordinary [[discrete Fourier transform|TST0GH66A5]]; it is both of type I and of type II.
Non-example: the sum $\sum_{n \in \Z} x_n e^{-2\pi i n f}$ over all integers is not a non-uniform DFT, because the definition requires finitely many sample points.
The map $x \mapsto X$ is linear, with the $K \times N$ matrix $A_{kn} = e^{-2\pi i p_n f_k}$.
Unlike the DFT matrix, $A$ is in general not a multiple of a unitary matrix, and it can be badly conditioned or singular, for example when two sample points coincide.
The adjoint transform, with $e^{+2\pi i p_n f_k}$, is used in place of an inverse.
Some authors use multidimensional points $p_n, f_k \in \R^d$ with the dot product $p_n \cdot f_k$ in the exponent.

## Explanations

### L1 human

The definition keeps the formula of the discrete Fourier transform but lets the positions $p_n$ and frequencies $f_k$ be any real numbers.
The three types say which of the two sides is still on a regular grid.
Computing it directly costs about $NK$ operations.
Fast algorithms, called non-uniform FFTs, approximate it to a chosen accuracy with far fewer operations when $N$ and $K$ are large.
