---
tag: HTZZ8FW37W
kind: statement
role: theorem
name: Herglotz's theorem on positive definite sequences
msc: [42A82, 43A35]
uses: [3PRZ02APFA, 04EAFVFTF7, HZNEQQBCW4, 01MMVW8CKC, ZRHAG4NXHC]
about: [3PRZ02APFA]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%27s_theorem
---

## Statement

Let $(a_n)_{n \in \Z}$ be a sequence of complex numbers.
Call it *positive definite* if
$$\sum_{j, k = 1}^{N} c_j \overline{c_k} \, a_{n_j - n_k} \ge 0$$
for all $N \ge 1$, all integers $n_1, \dots, n_N$ and all $c_1, \dots, c_N \in \C$.
Then $(a_n)$ is positive definite if and only if there is a finite positive Borel measure $\mu$ on the [[circle group|04EAFVFTF7]] $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$ with
$$a_n = \int_{\mathbb{T}} z^n \, d\mu(z) \quad \text{for all } n \in \Z.$$
The measure $\mu$ is then unique, and $\mu(\mathbb{T}) = a_0$.

## Remarks

Positive definite means that $n \mapsto a_n$ is a [[positive-definite function|3PRZ02APFA]] on the group $\Z$, or that every Toeplitz matrix $(a_{j - k})_{j,k = 0}^{N}$ is [[positive semidefinite|01MMVW8CKC]].
The theorem is the case $G = \Z$ of [[Bochner's theorem|ZRHAG4NXHC]], with $\widehat{\Z} = \mathbb{T}$.

Proof idea: if $a_n = \int z^n\, d\mu$, then the sum in the definition is $\int \abs{\sum_j c_j z^{n_j}}^2 \, d\mu(z) \ge 0$.
Conversely, choosing $c_j = e^{-ij\theta}$ for $j = 0, \dots, N-1$ shows that $p_N(\theta) = \frac{1}{N}\sum_{j,k=0}^{N-1} a_{j-k} e^{-i(j-k)\theta}$ is nonnegative.
The measures $p_N(\theta)\, \frac{d\theta}{2\pi}$ have total mass $a_0$, and their $n$-th moments are $(1 - \abs{n}/N)\, a_n$ for $\abs{n} < N$.
A weak-* limit point of these measures is the required $\mu$, and uniqueness holds because trigonometric polynomials are dense in the continuous functions on $\mathbb{T}$.

Example: for $0 \le r < 1$, the sequence $a_n = r^{\abs{n}}$ is positive definite.
Its measure is $P_r(\theta)\, \frac{d\theta}{2\pi}$, where $P_r(\theta) = \sum_{n} r^{\abs{n}} e^{in\theta} = \frac{1 - r^2}{1 - 2r\cos\theta + r^2} > 0$ is the Poisson kernel.

Non-example: the sequence with $a_0 = a_1 = a_{-1} = 1$ and $a_n = 0$ otherwise is not positive definite.
The Toeplitz matrix $(a_{j-k})_{j,k=0}^{2}$ has determinant $-1$.

## Explanations

### L1 human

A sequence indexed by the integers is positive definite when all the square tables built from it behave like tables of inner products.
The theorem says that these are exactly the sequences of moments $\int z^n\, d\mu$ of a positive mass distribution on the unit circle.

### L2 human

Herglotz's theorem is the discrete forerunner of Bochner's theorem, and its proof by Fejér means and weak-* compactness is the model for the general case.
In the theory of stationary sequences, it says that the covariance sequence of a weakly stationary process has a spectral measure on the circle.
It is also equivalent to the representation of holomorphic functions on the unit disc with positive real part as Poisson–Stieltjes integrals.
