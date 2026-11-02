---
tag: SBF5C86E3Z
kind: definition
name: Koenigs function
msc: [30D05, 37F10, 39B32]
defines: 529D1C4W9H
uses: [0NAHXR1FRH, R6QVS6P21N, AYVTR2ES5B, VTJV7JVJEA]
sources:
  - url: https://en.wikipedia.org/wiki/Koenigs_function
---

## Definition

Let $U \subseteq \C$ be an open set containing $0$, and let $f \colon U \to \C$ be [[holomorphic|0NAHXR1FRH]] with $f(0) = 0$.
Let $\lambda = f'(0)$ and assume $0 < \abs{\lambda} < 1$.
Let $V$ be a neighbourhood of $0$ on which the iterates $f^n$ of $f$ are defined and tend to $0$.
The *Koenigs function* of $f$ is the function $\varphi \colon V \to \C$ given by
$$\varphi(z) = \lim_{n \to \infty} \frac{f^n(z)}{\lambda^n},$$
where $f^n$ is the $n$-th [[iterate|AYVTR2ES5B]] of $f$.

## Remarks

The limit exists, uniformly near $0$, and $\varphi$ is holomorphic with $\varphi(0) = 0$ and $\varphi'(0) = 1$.
It solves [[Schröder's equation|VTJV7JVJEA]] $\varphi \circ f = \lambda \varphi$, since replacing $z$ by $f(z)$ shifts the index $n$ by one.
It is the unique solution with these normalisations, by the [[Koenigs linearization theorem|G02NBNN6CJ]].

Example: $f(z) = z / (2 - z)$ on the unit disc, with $\lambda = f'(0) = 1/2$.
For $\varphi(z) = z / (1 - z)$ one has $\varphi(f(z)) = \frac{z/(2-z)}{(2 - 2z)/(2 - z)} = \frac{z}{2(1 - z)} = \frac{1}{2} \varphi(z)$.
So $\varphi(f^n(z)) = 2^{-n} \varphi(z)$, and since $f^n(z) \to 0$ and $\varphi(w) / w \to 1$ as $w \to 0$, the limit of $2^n f^n(z)$ is $\varphi(z)$.

Non-example: for $f(z) = z^2$ one has $\lambda = 0$, so the quotient $f^n(z) / \lambda^n$ is not defined, and $f$ has no Koenigs function.

When $f$ is a univalent holomorphic map of the unit disc into itself with $f(0) = 0$ and $0 < \abs{f'(0)} < 1$, the limit exists on the whole disc and $\varphi$ is univalent there.
