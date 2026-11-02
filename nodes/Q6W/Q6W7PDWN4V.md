---
tag: Q6W7PDWN4V
kind: definition
name: Cartesian closed category
msc: [18D15]
defines: BFBNQ36QS8
uses: [A2DE66937D, EK85VSSRMR, S5744QZV4N, RHWD8DY41R]
sources:
  - url: https://en.wikipedia.org/wiki/Cartesian_closed_category
---

## Definition

A [[category|A2DE66937D]] $\mathcal{C}$ is *Cartesian closed* if:

1. $\mathcal{C}$ has a [[terminal object|EK85VSSRMR]].
2. Any two objects $X$ and $Y$ of $\mathcal{C}$ have a [[product|S5744QZV4N]] $X \times Y$.
3. Any two objects $Y$ and $Z$ of $\mathcal{C}$ have an [[exponential object|RHWD8DY41R]] $Z^Y$.

## Remarks

Clauses 1 and 2 say that $\mathcal{C}$ has finite products.
Clause 3 then says that each functor $- \times Y$ has a right adjoint $(-)^Y$.
So there are bijections $\Hom(X \times Y, Z) \cong \Hom(X, Z^Y)$, natural in $X$ and $Z$.

Example: the category of sets is Cartesian closed.
A one-point set is terminal, $X \times Y$ is the Cartesian product, and $Z^Y$ is the set of maps $Y \to Z$ with evaluation.

Non-example: the category of abelian groups is not Cartesian closed, although clauses 1 and 2 hold.
In a Cartesian closed category, $- \times Y$ is a left adjoint, so it preserves the initial object $0$, and $0 \times Y \cong 0$.
In abelian groups $0 \times \Z \cong \Z$, which is not $0$, so clause 3 fails.
