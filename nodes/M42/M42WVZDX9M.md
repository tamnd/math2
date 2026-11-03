---
tag: M42WVZDX9M
kind: definition
name: Least mean squares filter
msc: ["93E24", 94A12, "93E35"]
defines: 17RASDZEBS
uses: [MBQSZ6VYFC, 05NZ1HHQMV]
sources:
  - url: https://en.wikipedia.org/wiki/Least_mean_squares_filter
---

## Definition

Let $x_0, x_1, \dots \in \R^n$ be input vectors and $d_0, d_1, \dots \in \R$ be desired outputs.
In the tapped delay line case, $x_k = (u_k, u_{k-1}, \dots, u_{k-n+1})^{T}$ for a scalar input signal $u$.
Fix a step size $\mu > 0$ and an initial weight vector $w_0 \in \R^n$.
The *least mean squares filter* is the sequence $w_k \in \R^n$ given by
$$e_k = d_k - w_k^{T} x_k, \qquad w_{k+1} = w_k + \mu \, e_k \, x_k.$$
Its output at time $k$ is $w_k^{T} x_k$ and $e_k$ is its error.

## Remarks

The gradient of $\frac{1}{2} e_k^2 = \frac{1}{2}(d_k - w^{T} x_k)^2$ with respect to $w$ is $-e_k x_k$, so each step is a step of [[stochastic gradient descent|MBQSZ6VYFC]] on the [[mean squared error|05NZ1HHQMV]] $E[(d - w^{T} x)^2]$.
If $(x_k, d_k)$ is jointly wide-sense stationary with $R = E[x_k x_k^{T}]$ positive definite and $p = E[d_k x_k]$, the minimizer of the mean squared error is the Wiener solution $w^* = R^{-1} p$.
Let $\lambda_{\max}(R)$ be the largest eigenvalue of $R$.
Under the independence assumption, which treats $x_k$ as independent of $w_k$, the mean $E[w_k]$ converges to $w^*$ for every $w_0$ if and only if $0 < \mu < 2/\lambda_{\max}(R)$.
Example: $n = 1$, $x_k = 1$ and $d_k = c$ for all $k$.
Then $w_{k+1} - c = (1 - \mu)(w_k - c)$, so $w_k \to c$ exactly when $0 < \mu < 2$, in agreement with $\lambda_{\max}(R) = 1$.
Non-example: the normalized LMS filter $w_{k+1} = w_k + \mu \, e_k x_k / (\varepsilon + \norm{x_k}^2)$, with $\varepsilon > 0$, divides the step by the input power.
Its step is not the fixed multiple $\mu e_k x_k$, so it is a variant and not the LMS filter itself.
The [[recursive least squares filter|GJ21825GA8]] replaces $\mu$ by a matrix gain and converges faster.
