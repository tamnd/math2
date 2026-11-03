---
tag: 47AADZ5XJE
kind: definition
name: Constant elasticity of substitution
msc: [91B38, 91B16]
defines: MYBPAD9TGZ
uses: [09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Constant_elasticity_of_substitution
---

## Definition

Let $f \colon (0, \infty)^2 \to (0, \infty)$ be a production function of capital $K$ and labour $L$ with positive [[partial derivatives|09EGC6F8PT]] $f_K$ and $f_L$.
The *elasticity of substitution* of $f$ at $(K, L)$ is
$$\sigma(K, L) = \frac{d \ln (K / L)}{d \ln (f_L / f_K)},$$
the derivative being taken along an isoquant of $f$.
The function $f$ has *constant elasticity of substitution* if $\sigma$ is the same constant at every point.

The *CES production function* with parameters $A > 0$, $a \in (0, 1)$ and $\rho < 1$, $\rho \ne 0$, is
$$f(K, L) = A \left( a K^{\rho} + (1 - a) L^{\rho} \right)^{1/\rho}.$$

## Remarks

Check for the CES function: $f_L / f_K = \frac{1 - a}{a} (K / L)^{1 - \rho}$.
So $\ln(f_L / f_K) = \ln \frac{1 - a}{a} + (1 - \rho) \ln (K / L)$, and $\sigma = 1 / (1 - \rho)$ at every point.
For example, $\rho = 1/2$ gives $\sigma = 2$.

Non-example: $f(K, L) = K + \sqrt{L}$ has $f_L / f_K = 1 / (2 \sqrt{L})$.
Along an isoquant $K + \sqrt{L} = c$, a short computation gives $\sigma(K, L) = 2 + \sqrt{L} / K$, which changes from point to point, so $f$ fails the constancy condition.

As $\rho \to 0$, the CES function tends to the [[Cobb–Douglas function|XWMZSDDKTZ]] $A K^{a} L^{1 - a}$, with $\sigma = 1$.
As $\rho \to -\infty$, it tends to $A \min(K, L)$, a [[Leontief function|KTTZ1J9SPZ]], with $\sigma = 0$.
The value $\rho = 1$, excluded above, gives the linear function $A(aK + (1 - a)L)$, in which the inputs are perfect substitutes and $\sigma = \infty$.
The general form with $n$ inputs is $A \left( \sum_i a_i x_i^{\rho} \right)^{\nu / \rho}$, where $\nu > 0$ is the degree of homogeneity.
