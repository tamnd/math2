---
tag: VGYXWXV5M4
kind: statement
role: proposition
name: Laplace transform of an integral
msc: [44A10]
uses: [05XT5AVJBK, TKZAV3KR86, 0K090GVHVN]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be piecewise continuous and of [[exponential order|TKZAV3KR86]] $a$, that is, $\abs{f(t)} \le M e^{a t}$ for all $t \ge 0$ and some constants $M$ and $a$.
Let $F$ be the [[Laplace transform|05XT5AVJBK]] of $f$, and let $g(t) = \int_0^t f(\tau) \, d\tau$.
Then for every complex $s$ with $\operatorname{Re} s > \max(a, 0)$,
$$\mathcal{L}\{g\}(s) = \frac{F(s)}{s}.$$

## Remarks

The function $g$ is continuous, $g(0) = 0$, and $g' = f$ at each point where $f$ is continuous.
The bound on $f$ gives a bound $\abs{g(t)} \le M' e^{b t}$ for every $b > \max(a, 0)$, so $\mathcal{L}\{g\}$ exists on $\operatorname{Re} s > \max(a, 0)$.
The [[rule for derivatives|0K090GVHVN]] then gives $F(s) = s \, \mathcal{L}\{g\}(s) - g(0) = s \, \mathcal{L}\{g\}(s)$.
Example: with $f = 1$, one gets $\mathcal{L}\{t\}(s) = 1 / s^2$; repeating gives $\mathcal{L}\{t^n / n!\}(s) = 1 / s^{n + 1}$.

## Explanations

### L1 human

Integrating in time corresponds to dividing by $s$ in the transform.
It is the opposite of differentiation, which corresponds to multiplying by $s$.

### L2 human

Read backwards, the rule inverts transforms of the form $F(s) / s$: the answer is the running integral of $\mathcal{L}^{-1}\{F\}$.
For example $1 / (s (s^2 + 1))$ inverts to $\int_0^t \sin \tau \, d\tau = 1 - \cos t$.
It is a special case of the [[convolution theorem|0JNMJEDD93]], since $g = f * 1$ and $\mathcal{L}\{1\} = 1/s$.
