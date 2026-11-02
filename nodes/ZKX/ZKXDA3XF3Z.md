---
tag: ZKXDA3XF3Z
kind: definition
name: Cascade algorithm
msc: [65T60, 42C40]
defines: VZK6ZAXWJR
uses: [YH4BERB952, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Cascade_algorithm
---

## Definition

Let $(h_n)_{n \in \Z}$ be a finite sequence of real numbers with $\sum_n h_n = \sqrt{2}$.
Let $\varphi_0 \in L^2(\R)$ be a starting function, usually the indicator function of $[0, 1)$.
The *cascade algorithm* with filter $(h_n)$ is the iteration
$$\varphi_{i+1}(x) = \sqrt{2} \sum_{n} h_n \, \varphi_i(2x - n), \qquad i = 0, 1, 2, \dots$$
Suppose the sequence $(\varphi_i)$ converges in $L^2(\R)$ to a limit $\varphi$.
Then $\varphi$ satisfies the refinement equation $\varphi(x) = \sqrt{2}\sum_n h_n \varphi(2x - n)$.
So $\varphi$ is the [[scaling function|YH4BERB952]] of the filter.

## Remarks

The condition $\sum_n h_n = \sqrt{2}$ keeps the integral fixed: $\int \varphi_{i+1} = \sqrt{2}\sum_n h_n \cdot \frac{1}{2}\int\varphi_i = \int \varphi_i$.
The values of $\varphi_i$ at the points $k 2^{-i}$ can be computed by repeated upsampling by $2$ and convolution with $\sqrt{2}\,h$.
This is the inverse fast wavelet transform applied to a single coefficient.

Example: for the Haar filter $h_0 = h_1 = 1/\sqrt{2}$ and $\varphi_0 = \mathbf{1}_{[0,1)}$, one step gives $\varphi_1(x) = \mathbf{1}_{[0,1)}(2x) + \mathbf{1}_{[0,1)}(2x - 1) = \mathbf{1}_{[0,1)}(x)$.
So the iteration is constant and converges at once to the Haar scaling function.

Non-example: for the filter $h_0 = h_1 = 1$, the sum is $2 \ne \sqrt{2}$.
From $\varphi_0 = \mathbf{1}_{[0,1)}$ one gets $\varphi_i = 2^{i/2}\mathbf{1}_{[0,1)}$, which does not converge.

For the filters of the Daubechies wavelets, the iterates converge to the scaling function in $L^2(\R)$.
For some filters that satisfy the sum condition, the iteration still fails to converge, so convergence depends on further properties of the filter.

## Explanations

### L1 human

The cascade algorithm turns the self-similarity rule of a scaling function into a repeated computation.
Each round replaces the current shape by a weighted sum of half-size, shifted copies of it.
