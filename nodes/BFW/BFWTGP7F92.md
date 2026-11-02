---
tag: BFWTGP7F92
kind: definition
name: Nevanlinna theory of difference equations
msc: [39A45, 30D35]
defines: 9KAQ1REPE8
uses: [0ZZ7ZYDR8W, YT6Z0GWS0W]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna_theory
---

## Definition

Let $c \in \C \setminus \set{0}$ and let $n \ge 1$.
Let $F$ be a polynomial or a rational function in its last $n + 1$ arguments, with coefficients that are meromorphic functions of $z$.
A *complex difference equation* for an unknown [[meromorphic function|0ZZ7ZYDR8W]] $f$ on $\C$ is an equation
$$F\big(z, f(z), f(z + c), \dots, f(z + nc)\big) = 0.$$
For such a solution $f$, write $T(r, f)$ for its [[Nevanlinna characteristic|YT6Z0GWS0W]] and $m(r, f)$ for its proximity function.
A quantity $S(r, f)$ is *small* with respect to $f$ if $S(r, f) = o(T(r, f))$ as $r \to \infty$ outside a set of $r$ of finite logarithmic measure.
*Nevanlinna theory of difference equations* is the study of the meromorphic solutions of such difference equations through $T$, $m$ and the counting function $N$.
Its basic tools are estimates of the type $m\big(r, f(z + c)/f(z)\big) = S(r, f)$.

## Remarks

Example: $f(z) = e^{z}$ solves $f(z + 1) = e f(z)$.
Here $T(r, f) = r/\pi$ and $f(z + 1)/f(z) = e$ is constant, so $m\big(r, f(z+1)/f(z)\big) = 1$, which is small compared with $T(r, f)$.

Non-example: for $f(z) = e^{e^z}$, which has infinite order, the quotient $f(z + 1)/f(z) = e^{(e - 1)e^z}$ has proximity function comparable to $T(r, f)$, so the small-term estimate fails; this is why the difference lemma requires finite order.

The basic estimate holds for every meromorphic $f$ of finite order and every $c \in \C$, outside an exceptional set of finite logarithmic measure.
