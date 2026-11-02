---
tag: FFR8NPWG64
kind: statement
role: theorem
name: Convolution property of the Z-transform
msc: [44A55, 44A35]
uses: [3DBAMXA80B, EPG6JPVJE7, 1P8WX3EGHF, 2Z29JN3VES, 0RVD9R2V99]
about: [5FY0JQGHYZ, 2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Properties
---

## Statement

Let $x = (x_n)_{n \in \Z}$ and $y = (y_n)_{n \in \Z}$ be sequences of complex numbers with [[bilateral Z-transforms|3DBAMXA80B]] $X$ and $Y$.
Let $z$ be a point of both [[regions of convergence|1P8WX3EGHF]].
Then for every $n \in \Z$ the series $(x * y)_n = \sum_{k \in \Z} x_k \, y_{n-k}$ converges absolutely, $z$ lies in the region of convergence of $x * y$, and
$$\mathcal{Z}\{x * y\}(z) = X(z) \, Y(z).$$
If moreover $x_n = y_n = 0$ for all $n < 0$, then $(x * y)_n = \sum_{k=0}^{n} x_k y_{n-k}$ for $n \ge 0$, and the same identity holds for the [[unilateral Z-transforms|EPG6JPVJE7]].

## Remarks

The double series $\sum_{n} \sum_{k} \abs{x_k} \abs{y_{n-k}} \abs{z}^{-n}$ equals $\left(\sum_k \abs{x_k} \abs{z}^{-k}\right)\left(\sum_m \abs{y_m} \abs{z}^{-m}\right)$, which is finite.
So each inner sum converges absolutely, and the terms can be regrouped, which gives the product formula.
In the one-sided case this is the [[Cauchy product|0RVD9R2V99]] of two absolutely convergent series in $z^{-1}$.
Example: for $x_n = y_n = 1$ ($n \ge 0$), $(x * y)_n = n + 1$, and $\left(z/(z-1)\right)^2 = \sum_{n \ge 0} (n+1) z^{-n}$ for $\abs{z} > 1$.
If the two regions do not meet, the [[convolution|2Z29JN3VES]] may fail to exist: for $x_n = y_n = 1$ for all $n \in \Z$, each sum $\sum_k x_k y_{n-k}$ diverges.

## Explanations

### L1 human

Convolution of sequences is the operation that a linear time-invariant filter performs on its input.
The Z-transform turns this operation into ordinary multiplication of functions.
So passing a signal through a filter amounts to multiplying its transform by the transform of the filter.

### L2 human

The transform of the impulse response of a system is its transfer function, and the theorem says that the output transform is the input transform times the transfer function.
It is the discrete counterpart of the convolution theorem for the Laplace transform.
Together with the shift property, it reduces linear constant-coefficient difference equations to algebra.
