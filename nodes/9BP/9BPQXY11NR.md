---
tag: 9BPQXY11NR
kind: definition
name: Axiom schema of replacement
msc: ["03E30"]
defines: D96K8S8R61
uses: [0HE5WDQ9FJ, 0SJ3RX9TXA, 0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_schema_of_replacement
---

## Definition

Work in first-order logic with the relation symbol $\in$.
Let $\varphi(x, y, w_1, \dots, w_n)$ be a formula whose free variables are among $x, y, w_1, \dots, w_n$, and in which $A$ and $B$ do not occur.
The *instance of replacement* for $\varphi$ is the axiom
$$\forall w_1 \cdots \forall w_n\, \forall A\, \Bigl( \forall x \in A\, \exists! y\, \varphi(x, y, w) \to \exists B\, \forall y\, \bigl( y \in B \leftrightarrow \exists x \in A\, \varphi(x, y, w) \bigr) \Bigr).$$
The *axiom schema of replacement* is the set of these axioms, one for each formula $\varphi$.

In words: if $\varphi$ defines a [[function|0XHDTE5YMZ]] on the [[set|0SJ3RX9TXA]] $A$, then the image of $A$ under this function is a set.

## Remarks

Example: let $\varphi(x, y)$ say "$x$ is a natural number and $y$ is the set $\omega + x$".
For $A = \omega$ the hypothesis holds, so replacement gives the set $\set{\omega + n : n \in \omega}$, whose union is the ordinal $\omega + \omega$.
Non-example: the set $V_{\omega + \omega}$ of all sets of rank below $\omega + \omega$ satisfies all axioms of Zermelo set theory, but not replacement.
In it, the instance above fails: each $\omega + n$ lies in $V_{\omega + \omega}$, but the set $\set{\omega + n : n \in \omega}$ has rank $\omega + \omega$ and does not.
Replacement implies the separation scheme, given the other axioms of [[ZF|0HE5WDQ9FJ]].
It is used to justify definitions by transfinite recursion on the ordinals.
