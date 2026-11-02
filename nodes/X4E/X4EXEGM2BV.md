---
tag: X4EXEGM2BV
kind: statement
role: proposition
name: Tanh-sinh quadrature
msc: [65D32, 65D30]
uses: [7HYF6YG0RS, FH0538XCZR]
about: [7HYF6YG0RS]
sources:
  - url: https://en.wikipedia.org/wiki/Tanh-sinh_quadrature
same_as:
  wikidata: Q7683194
  wikipedia: Tanh-sinh quadrature
---

## Statement

Let $\varphi \colon \R \to (-1, 1)$ be $\varphi(t) = \tanh\big(\tfrac{\pi}{2} \sinh t\big)$, so that
$$\varphi'(t) = \frac{\frac{\pi}{2} \cosh t}{\cosh^2\big(\frac{\pi}{2} \sinh t\big)}.$$
Then:

1. $\varphi$ is a smooth increasing bijection of $\R$ onto $(-1, 1)$, and for every Lebesgue integrable $f$ on $(-1, 1)$,
$$\int_{-1}^{1} f(x) \, dx = \int_{-\infty}^{\infty} f(\varphi(t)) \, \varphi'(t) \, dt;$$
2. if moreover $\abs{f(x)} \le M$ for all $x \in (-1, 1)$, then for all real $t$,
$$\abs{f(\varphi(t)) \, \varphi'(t)} \le 2 \pi M \cosh t \; e^{-\pi \sinh \abs{t}}.$$

The *tanh-sinh rule* with step $h > 0$ and $2N + 1$ points is $T_{h,N}(f) = h \sum_{k=-N}^{N} \varphi'(kh) \, f(\varphi(kh))$, the [[trapezoidal rule|FH0538XCZR]] for the transformed integral, cut off at $\abs{t} \le Nh$.

## Remarks

Clause 1 is the change of variables formula, since $\varphi' > 0$ and $\varphi(t) \to \pm 1$ as $t \to \pm\infty$.
Clause 2 follows from $\cosh u \ge \frac12 e^{\abs{u}}$, which gives $\cosh^{-2}\big(\frac{\pi}{2}\sinh t\big) \le 4 e^{-\pi \sinh\abs{t}}$.
So the transformed integrand decays double exponentially, and the cut-off at $\abs{t} \le Nh$ loses almost nothing; this is why the method is also called double exponential quadrature.
The trapezoidal rule on $\R$ is extremely accurate for functions analytic in a strip around the real axis.
For integrands analytic in a suitable region around $(-1, 1)$, the error of $T_{h,N}$ with a good choice of $h$ decreases roughly like $e^{-cN/\log N}$ for some $c > 0$.
Example: for $f(x) = (1 - x^2)^{-1/2}$, which is unbounded, the transformed integrand is $\frac{\pi}{2} \cosh t / \cosh\big(\frac{\pi}{2} \sinh t\big)$, still double exponentially decaying, and its integral is $\pi$.
The method was introduced by Hidetosi Takahashi and Masatake Mori in 1974.

## Explanations

### L1 human

Tanh-sinh quadrature stretches the interval $(-1, 1)$ to the whole real line with a clever change of variable.
After the change, the function to be integrated dies off extremely fast at both ends, even if the original one blew up at an endpoint.
Then the simplest rule, adding equally spaced samples, gives an excellent answer.

### L2 human

The method is robust against endpoint singularities, which defeat Gaussian rules, and it reuses all old samples when the step $h$ is halved.
For these reasons it is a standard choice in arbitrary-precision computation, where hundreds of correct digits are needed.
It needs care near the endpoints in floating-point arithmetic, since $\varphi(kh)$ is extremely close to $\pm 1$ and $1 \mp \varphi(kh)$ should be computed directly.
Related double exponential substitutions treat integrals over $[0, \infty)$ and $\R$.
