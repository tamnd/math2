---
tag: BEEJJA60BX
kind: definition
name: Kernel density estimation
msc: [62G07]
defines: ZV65XMJ9A4
uses: [04YG690N5V, 0AJN7WHBJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_density_estimation
---

## Definition

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with an unknown [[probability density function|04YG690N5V]] $f$.
Let $K \colon \R \to \R$ be an integrable function with $\int_{\R} K(u) \, du = 1$, called the kernel, and let $h > 0$, called the bandwidth.
The *kernel density estimator* of $f$ is
$$\hat f_h(x) = \frac{1}{n h} \sum_{i=1}^{n} K\Big(\frac{x - X_i}{h}\Big), \quad x \in \R.$$

## Remarks

The substitution $u = (x - X_i)/h$ gives $\int_{\R} \hat f_h(x) \, dx = 1$; if moreover $K \ge 0$, then $\hat f_h$ is a probability density.
Common kernels are the Gaussian kernel $K(u) = e^{-u^2/2}/\sqrt{2\pi}$ and the Epanechnikov kernel $K(u) = \frac{3}{4}(1 - u^2)$ for $\abs{u} \le 1$, $0$ otherwise.
Example: with $K = \frac{1}{2} \mathbf{1}_{[-1, 1]}$, $\hat f_h(x)$ is the fraction of data in $[x - h, x + h]$ divided by $2h$.
Non-example: $K = \mathbf{1}_{[-1, 1]}$ has integral $2$, so the resulting $\hat f_h$ integrates to $2$ and is not a density estimate.
If $f$ is twice continuously differentiable and $K$ is a bounded symmetric density with finite variance, the mean integrated squared error is smallest for $h$ of order $n^{-1/5}$.
In $\R^d$, one uses $\frac{1}{n h^d} \sum_i K((x - X_i)/h)$ with a kernel on $\R^d$.
