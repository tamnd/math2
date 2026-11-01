---
tag: GGCHBSY4HK
kind: definition
name: Separable closure
msc: [12F10]
defines: JJ91A1V8NQ
uses: [09EYMKMSB9, 0N019F6RE9, 0MCXX29HWY, 0GK1WB9R98]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_extension
---

## Definition

Let $L/K$ be an [[algebraic extension|09EYMKMSB9]].
An element $\alpha \in L$ is separable over $K$ if its [[minimal polynomial|0GK1WB9R98]] over $K$ has no repeated root in an algebraic closure.
The *separable closure of $K$ in $L$* is the set $L_s$ of elements of $L$ that are separable over $K$.
Let $\overline{K}$ be an [[algebraic closure|0MCXX29HWY]] of $K$.
The *separable closure* of $K$ is the separable closure $K^{\mathrm{sep}}$ of $K$ in $\overline{K}$.

## Remarks

The set $L_s$ is a subfield of $L$ containing $K$, the extension $L_s/K$ is [[separable|0N019F6RE9]], and every separable subextension of $L/K$ lies in $L_s$.
The extension $L/L_s$ is purely inseparable.
The field $K^{\mathrm{sep}}$ is separably closed, and it is unique up to an isomorphism over $K$.

Example: let $K = \Q$ and $L = \overline{\Q}$.
Check: in characteristic $0$ every irreducible polynomial has distinct roots, so every element of $\overline{\Q}$ is separable and $\Q^{\mathrm{sep}} = \overline{\Q}$.

Non-example: let $K = \F_p(t)$ and $L = K(s)$ with $s^p = t$.
The element $s$ is not in the separable closure of $K$ in $L$, since its minimal polynomial $x^p - t = (x - s)^p$ has a repeated root; in fact $L_s = K$.
