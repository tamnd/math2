---
tag: HC3T4EY6WZ
kind: statement
role: theorem
name: Riemann localization principle
msc: [42A20, 42A63]
uses: [G12KXDHPPS, WVKDC011KP, 3JY4BVE4DW, 0ATF6Q0633]
about: [G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
---

## Statement

Let $f, g \colon \R \to \C$ be [[periodic functions|0ATF6Q0633]] of period $2\pi$ that are integrable on $[-\pi, \pi]$.
Let $S_N f$ and $S_N g$ be the partial sums of their [[Fourier series|G12KXDHPPS]].
Let $x_0 \in \R$ and $\delta > 0$, and suppose that $f(x) = g(x)$ for almost every $x$ in $(x_0 - \delta, x_0 + \delta)$.
Then
$$\lim_{N \to \infty} \big(S_N f(x_0) - S_N g(x_0)\big) = 0.$$
In particular the Fourier series of $f$ converges at $x_0$ if and only if that of $g$ does, and then to the same limit.

## Remarks

Put $h = f - g$; then $h$ vanishes near $x_0$, and $S_N h(x_0) = \frac{1}{2\pi} \int_{\delta \le \abs{t} \le \pi} h(x_0 - t) D_N(t) \, dt$ with the [[Dirichlet kernel|3JY4BVE4DW]] $D_N$.
On $\delta \le \abs{t} \le \pi$ the factor $\frac{1}{\sin(t/2)}$ is bounded, so $t \mapsto \frac{h(x_0 - t)}{\sin(t/2)}$ is integrable there.
The [[Riemann–Lebesgue lemma|WVKDC011KP]] applied to $\sin((N + \frac{1}{2}) t)$ gives $S_N h(x_0) \to 0$.
The same argument shows that $S_N h \to 0$ uniformly on every closed interval inside the interval where $h$ vanishes.
Example: a function equal to $x^2$ near $x_0 = 1$ has a Fourier series converging to $1$ at $x_0$, whatever its values far from $x_0$.
By contrast, each Fourier coefficient depends on the values of $f$ on the whole period.

## Explanations

### L1 human

Whether a Fourier series converges at a point depends only on the function near that point.
Changing the function far away changes every coefficient, but these changes cancel in the limit at the point.

### L2 human

Localization reduces convergence questions to local behaviour, which is why the Dini and Dirichlet–Jordan tests involve only values of $f$ near $x$.
It contrasts with the global nature of the coefficients.
