---
tag: VWDS9PM9V9
kind: definition
name: Exponential type
msc: ["30D15"]
defines: 9P8D8YAHQS
uses: [0419794R0T, 0P8BA7T7S5, SHF8Z7GMFX]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_type
---

## Definition

Let $f$ be an [[entire function|0419794R0T]].
The function $f$ is of *exponential type* if there are constants $C > 0$ and $\tau \ge 0$ such that
$$\abs{f(z)} \le C e^{\tau \abs{z}} \quad \text{for all } z \in \C.$$
In that case the *type* of $f$ is
$$\sigma = \limsup_{r \to \infty} \frac{\log M(r)}{r}, \qquad M(r) = \max_{\abs{z} = r} \abs{f(z)},$$
with $\log 0 = -\infty$, and $f$ is said to be of exponential type $\sigma$.

## Remarks

Example: $\abs{\sin z} \le e^{\abs{z}}$ for all $z$, and $M(r) = \sinh r$ for $\sin z$, so $\sin z$ is of exponential type with type $1$.
Non-example: $f(z) = e^{z^2}$ has $\abs{f(x)} = e^{x^2}$ on the real line, and $e^{x^2} \le C e^{\tau \abs{x}}$ fails for large $x$ for every $C$ and $\tau$.
In terms of the [[order|SHF8Z7GMFX]], $f$ is of exponential type exactly when its order is less than $1$, or equal to $1$ with finite type.
For $f(z) = \sum_n a_n z^n$, the type is $\sigma = \frac{1}{e} \limsup_{n \to \infty} n \abs{a_n}^{1/n}$; for $e^z$ this gives $1$.
The notion is also used for functions holomorphic in a sector or a half-plane, with the bound required only there.
