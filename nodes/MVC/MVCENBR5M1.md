---
tag: MVCENBR5M1
kind: definition
name: Mellin transform method
msc: [45H05, 44A15]
defines: HWHNY5854A
uses: [N5PVGRJE1T, A2PMJG7J68, R3SG1SN7JQ]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Definition

For a function $g$ on $(0, \infty)$ write $\mathcal{M}g(s) = \int_0^\infty x^{s - 1} g(x) \, dx$ for its [[Mellin transform|N5PVGRJE1T]].
Let $k$ and $f$ be given functions on $(0, \infty)$, let $\lambda \in \C$, and consider the [[integral equation|R3SG1SN7JQ]]
$$\varphi(x) - \lambda \int_0^\infty k\!\left(\frac{x}{t}\right) \varphi(t) \, \frac{dt}{t} = f(x), \quad x > 0,$$
or its first-kind form without the term $\varphi(x)$.
Assume that $\mathcal{M}k$ and $\mathcal{M}f$ converge absolutely in a common strip $a < \operatorname{Re} s < b$.
The *Mellin transform method* consists of the following steps.

1. Apply $\mathcal{M}$; since the integral is the [[Mellin convolution|A2PMJG7J68]] of $k$ and $\varphi$, the equation becomes $(1 - \lambda \mathcal{M}k(s)) \, \mathcal{M}\varphi(s) = \mathcal{M}f(s)$ in the strip.
2. Solve for $\mathcal{M}\varphi(s) = \mathcal{M}f(s) / (1 - \lambda \mathcal{M}k(s))$ (for the first kind, $\mathcal{M}\varphi = \mathcal{M}f / \mathcal{M}k$).
3. Recover $\varphi$ by the [[Mellin inversion formula|XJWC13NY9E]] $\varphi(x) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} x^{-s} \, \mathcal{M}\varphi(s) \, ds$ with $a < c < b$.

## Remarks

Step 1 rests on the identity $\mathcal{M}\left[\int_0^\infty k(x/t) \varphi(t) \, dt/t\right](s) = \mathcal{M}k(s) \, \mathcal{M}\varphi(s)$, which follows from the substitution $x = t u$.

Example: the first-kind equation $\int_0^\infty e^{-x/t} \varphi(t) \, \frac{dt}{t} = f(x)$ with $f(x) = \int_0^\infty e^{-x/t - t} \, \frac{dt}{t}$.
Here $k(u) = e^{-u}$ and $\mathcal{M}k(s) = \Gamma(s)$ for $\operatorname{Re} s > 0$.
By step 1 applied to $e^{-t}$, $\mathcal{M}f(s) = \Gamma(s)^2$, so step 2 gives $\mathcal{M}\varphi(s) = \Gamma(s)$ and step 3 gives $\varphi(t) = e^{-t}$.

A kernel $h(x, t)$ that is homogeneous of degree $-1$, that is $h(cx, ct) = c^{-1} h(x, t)$ for all $c > 0$, can be written $h(x, t) = \frac{1}{t} h\!\left(\frac{x}{t}, 1\right)$, so the method applies to $\int_0^\infty h(x, t) \varphi(t) \, dt$.
For $h(x, t) = \frac{1}{x + t}$ one gets $k(u) = \frac{1}{1 + u}$ and $\mathcal{M}k(s) = \frac{\pi}{\sin \pi s}$ for $0 < \operatorname{Re} s < 1$.

Non-example: the kernel $e^{-(x - t)^2}$ on $(0, \infty)$ is not a function of $x / t$ times $\frac{1}{t}$, so the Mellin transform does not turn the equation into a product.

The substitution $x = e^{u}$, $t = e^{v}$ turns the equation into a [[convolution integral equation|EY75YD988Z]] on $\R$, and the method into the [[Fourier transform method|NRG03YP2PW]].
