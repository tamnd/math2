---
tag: YY6P3RSDWC
kind: definition
name: Local truncation error
msc: [65L70, 65L05, 65L06]
defines: T220HF0562
uses: [558XADG64M, 0FXDW992DS, 0AW1E6YTJY, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Truncation_error_(numerical_integration)
---

## Definition

Let $y$ be the exact solution of an [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$, and let $t_n = t_0 + nh$.
Consider a [[one-step method|558XADG64M]] $y_{n+1} = y_n + h \, \Phi(t_n, y_n, h)$ with increment function $\Phi$.
The *local truncation error* at step $n + 1$ is
$$\tau_{n+1} = y(t_{n+1}) - y(t_n) - h \, \Phi\big(t_n, y(t_n), h\big),$$
the error of one step started from the exact value $y(t_n)$.
The method is *consistent of order* $p$ if $\tau_{n+1} = O(h^{p+1})$ as $h \to 0$, uniformly in $n$, for every sufficiently smooth $f$.

## Remarks

For an implicit method or a linear multistep method $\sum_{j=0}^{k} \alpha_j y_{n+j} = h \sum_{j=0}^{k} \beta_j f(t_{n+j}, y_{n+j})$, one inserts the exact solution in the same way: $\tau_{n+k} = \sum_j \alpha_j y(t_{n+j}) - h \sum_j \beta_j y'(t_{n+j})$.
Some books divide by $h$ and call $\tau_{n+1}/h$ the truncation error; then order $p$ means $O(h^p)$.
Example: for the Euler method, $\Phi(t, y, h) = f(t, y)$, and Taylor's theorem gives $\tau_{n+1} = y(t_n + h) - y(t_n) - h y'(t_n) = \frac{h^2}{2} y''(\xi_n)$, so the method is consistent of order $1$.
Non-example: $\Phi(t, y, h) = 2 f(t, y)$ is not consistent, since $\tau_{n+1} = -h y'(t_n) + O(h^2)$ is not even $O(h^2)$.
If $\Phi$ is [[Lipschitz|0AW1E6YTJY]] in $y$ with constant $L > 0$ and $\abs{\tau_n} \le C h^{p+1}$ for all $n$, and if the method starts from $y_0 = y(t_0)$, then the global error satisfies $\abs{y(t_n) - y_n} \le \frac{C h^p}{L}\big(e^{L(t_n - t_0)} - 1\big)$.

## Explanations

### L1 human

The local truncation error asks: if the method starts a step at the exact answer, how wrong is it one step later?
A method of order $p$ makes an error of size about $h^{p+1}$ per step.
