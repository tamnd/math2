---
tag: W6GV82MMQ7
kind: definition
name: Composition operator
msc: [47B33]
defines: CFASPSF7BB
uses: [07HF9YCWPP, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Composition_operator
---

## Definition

Let $\Omega$ be a set and let $X$ be a vector space of functions $\Omega \to \C$.
Let $\varphi \colon \Omega \to \Omega$ be a map such that $f \circ \varphi \in X$ for every $f \in X$.
The *composition operator* with symbol $\varphi$ is the [[linear map|0NRYHJPQG2]]
$$C_\varphi \colon X \to X, \qquad C_\varphi f = f \circ \varphi,$$
where $\circ$ is [[function composition|07HF9YCWPP]].

## Remarks

Linearity is automatic: $(af + bg) \circ \varphi = a (f \circ \varphi) + b (g \circ \varphi)$.

Example: let $X$ be the [[Hardy space|PNNNFJVF6W]] $H^2$ of the unit disc $\mathbb{D}$ and $\varphi(z) = z/2$.
For $f(z) = \sum_{n \ge 0} a_n z^n$ in $H^2$, $f \circ \varphi = \sum_{n \ge 0} 2^{-n} a_n z^n$, whose coefficients are again square-summable; so $C_\varphi$ is defined, and it is the diagonal operator with entries $2^{-n}$ on the basis $z^n$.

Non-example: $\varphi(z) = 2z$ does not map $\mathbb{D}$ into $\mathbb{D}$.
For $f(z) = \sum_{n \ge 0} z^n / (n + 1)$, which lies in $H^2$, the function $f(2z)$ is not defined on all of $\mathbb{D}$, since the series diverges for $\abs{z} > 1/2$.

When $X$ is a normed space one usually asks in addition that $C_\varphi$ be bounded.
