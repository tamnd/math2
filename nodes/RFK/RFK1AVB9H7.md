---
tag: RFK1AVB9H7
kind: definition
name: Approximate derivative
msc: [26A24]
defines: 4W31MKE01V
uses: [0TXTSEMHR5, 0F1WR9C83K]
sources:
  - url: https://en.wikipedia.org/wiki/Approximate_limit
---

## Definition

Let $I \subseteq \R$ be an open interval, let $f \colon I \to \R$ be a function, and let $x \in I$.
Write $\lambda$ for Lebesgue measure.
A measurable set $E \subseteq \R$ has *density $1$* at $x$ if
$$\lim_{h \to 0^+} \frac{\lambda(E \cap [x - h, x + h])}{2h} = 1.$$
The function $f$ is *approximately differentiable* at $x$, with *approximate derivative* $c \in \R$, if the following holds.
There is a measurable set $E \subseteq I$ with $x \in E$ and density $1$ at $x$ such that
$$\lim_{\substack{y \to x \\ y \in E \setminus \set{x}}} \frac{f(y) - f(x)}{y - x} = c.$$
The approximate derivative is written $f'_{\mathrm{ap}}(x)$.

## Remarks

Example: let $f(1/n) = 1$ for $n \ge 2$ and $f(y) = 0$ at all other $y \in (-1, 1)$.
At $x = 0$ the ordinary [[derivative|0F1WR9C83K]] does not exist, since the quotient at $y = 1/n$ equals $n$.
The set $E = (-1, 1) \setminus \set{1/n : n \ge 2}$ has density $1$ at $0$, because the removed set is countable, and on $E$ the quotient is $0$; so $f'_{\mathrm{ap}}(0) = 0$.

Non-example: let $f(y) = 1$ for $y \ge 0$ and $f(y) = 0$ for $y < 0$, at $x = 0$.
For $y < 0$ the quotient is $-1/y$, which tends to $+\infty$ as $y \to 0^-$.
Every set of density $1$ at $0$ contains points $y < 0$ arbitrarily close to $0$.
So $f$ has no approximate derivative at $0$.

If $f'(x)$ exists, then $f'_{\mathrm{ap}}(x)$ exists and equals it, by taking $E = I$.
The approximate derivative is unique when it exists, because two sets of density $1$ at $x$ meet in a set of density $1$ at $x$.
