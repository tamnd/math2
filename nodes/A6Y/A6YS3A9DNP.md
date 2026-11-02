---
tag: A6YS3A9DNP
kind: definition
name: Trigonometric polynomial
msc: [42A05, 42A10]
defines: J3NJQ5FZJ5
uses: [07GJV36896, 08WFZP6P89]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_polynomial
---

## Definition

Let $N \ge 0$ be an integer.
A *trigonometric polynomial* of degree at most $N$ is a function $T \colon \R \to \C$ with
$$T(x) = \sum_{n=-N}^{N} c_n e^{inx},$$
for complex numbers $c_{-N}, \dots, c_N$, where $e^{inx}$ is the [[complex exponential|07GJV36896]].
Its *degree* is the largest $\abs{n}$ with $c_n \ne 0$.

## Remarks

By Euler's formula the same functions are the sums $a_0 + \sum_{n=1}^{N} (a_n \cos nx + b_n \sin nx)$ with complex $a_n, b_n$, built from [[sine and cosine|08WFZP6P89]].
The two forms are related by $a_0 = c_0$, $a_n = c_n + c_{-n}$ and $b_n = i(c_n - c_{-n})$ for $n \ge 1$.
$T$ is real-valued exactly when $c_{-n} = \overline{c_n}$ for all $n$, that is, when all $a_n$ and $b_n$ are real.
Example: $\cos^2 x = \frac{1}{4} e^{-2ix} + \frac{1}{2} + \frac{1}{4} e^{2ix}$, so $\cos^2 x$ is a trigonometric polynomial of degree $2$.
Non-example: $\sin(x/2)$ is not a trigonometric polynomial, since it has period $4\pi$ and not $2\pi$, while every trigonometric polynomial is $2\pi$-periodic.
The coefficients are unique: $c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} T(x) e^{-inx} \, dx$.
