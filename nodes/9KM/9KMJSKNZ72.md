---
tag: 9KMJSKNZ72
kind: statement
role: lemma
name: Bihari–LaSalle inequality
msc: [26D10, 34A40]
uses: [07EJHQYR9A]
about: [07EJHQYR9A]
sources:
  - url: https://en.wikipedia.org/wiki/Bihari%E2%80%93LaSalle_inequality
same_as:
  wikidata: Q4907094
  wikipedia: Bihari–LaSalle inequality
---

## Statement

Let $a < b$, let $u, f : [a, b] \to [0, \infty)$ be continuous, and let $c > 0$.
Let $w : [0, \infty) \to [0, \infty)$ be continuous and non-decreasing, with $w(r) > 0$ for $r > 0$.
Define $G(r) = \int_c^r \frac{ds}{w(s)}$ for $r > 0$, and let $G(\infty) = \lim_{r \to \infty} G(r) \in (0, \infty]$.
Assume that
$$u(t) \le c + \int_a^t f(s)\, w(u(s))\, ds \quad \text{for each } t \in [a, b].$$
Then for each $t \in [a, b]$ with $\int_a^t f(s)\, ds < G(\infty)$,
$$u(t) \le G^{-1}\left( \int_a^t f(s)\, ds \right).$$

## Remarks

The function $G$ is continuous and strictly increasing with $G(c) = 0$, so $G^{-1}$ is defined on $[0, G(\infty))$.
Proof idea: let $v(t) = c + \int_a^t f(s)\, w(u(s))\, ds$.
Then $v \ge c > 0$, $u \le v$, and $v' = f\, w(u) \le f\, w(v)$ since $w$ is non-decreasing.
So $\frac{d}{dt} G(v(t)) = v'(t) / w(v(t)) \le f(t)$, and integration gives $G(v(t)) \le \int_a^t f$.
For $w(r) = r$ one gets $G(r) = \ln(r/c)$ and the bound $u(t) \le c\, \exp\left(\int_a^t f\right)$, which is [[Grönwall's inequality|07EJHQYR9A]] with constant $\alpha = c$.
For $w(r) = r^2$ and $f = 1$ one gets $u(t) \le c / (1 - c(t - a))$ while $c(t - a) < 1$; the restriction on $t$ matches the blow-up of the solution of $u' = u^2$.

## Explanations

### L1 human

Grönwall's inequality controls a quantity whose growth rate is at most proportional to its size.
The Bihari–LaSalle inequality does the same when the growth rate is a more general increasing function of the size.
The bound is the solution of the comparison equation $v' = f\, w(v)$, $v(a) = c$.

### L2 human

The inequality is the nonlinear version of the integral form of [[Grönwall's inequality|07EJHQYR9A]].
It gives a priori bounds for solutions of nonlinear equations and estimates of the time of existence.
With $c \to 0$ it gives the [[Osgood uniqueness criterion|2AHNVSH76M]], which relaxes the Lipschitz condition in uniqueness theorems.
