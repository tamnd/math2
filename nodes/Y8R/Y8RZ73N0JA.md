---
tag: Y8RZ73N0JA
kind: definition
name: Infinite compositions of functions
msc: [40A30, 30D05]
defines: B88PFYXWBK
uses: [07HF9YCWPP, 0VKD1TP7F3, 0XKWSSY8P2]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_compositions_of_analytic_functions
---

## Definition

Let $D$ be a subset of a [[metric space|0VKD1TP7F3]], for example of $\C$, and let $f_1, f_2, \dots$ be functions from $D$ to $D$.
The *forward* (or *inner*) compositions are $F_n = f_1 \circ f_2 \circ \cdots \circ f_n$.
The *backward* (or *outer*) compositions are $G_n = f_n \circ f_{n-1} \circ \cdots \circ f_1$.
The infinite forward composition converges at a point $z \in D$ if the sequence $(F_n(z))$ has a [[limit|0XKWSSY8P2]], and similarly for the backward composition.
When the limit exists for all $z$ in $D$, it defines the function $F(z) = \lim_{n \to \infty} F_n(z)$ (or $G(z) = \lim_{n \to \infty} G_n(z)$).

## Remarks

Example: on $D = \R$ let $f_n(x) = \frac{x}{2} + 1$ for all $n$.
Then $G_n(0) = 2 - 2^{1-n}$, so the backward composition converges at $0$ to the fixed point $2$ of $f_1$.
Non-example: with $f_n(x) = -x$ for all $n$, the sequence $F_n(1) = (-1)^n$ has no limit, so the infinite composition does not converge at $1$.
For a [[continued fraction|0BK6JBK58W]] with $f_n(w) = \frac{a_n}{b_n + w}$, the values $F_n(0)$ are the convergents; backward compositions do not have this interpretation.
When all $f_n$ equal a single map $f$, both $F_n$ and $G_n$ are the iterate $f^{\circ n}$.

## Explanations

### L1 human

Forward compositions add each new function on the inside, next to the starting value.
Backward compositions add it on the outside, so they describe a point moved step by step by a changing rule.
