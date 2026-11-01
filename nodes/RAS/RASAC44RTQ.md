---
tag: RASAC44RTQ
kind: definition
name: Unramified morphism of rings
msc: [13B40, 14B25, 13N05]
defines: GY3QA6NH0E
uses: [0310REJJY8, DPBJ04JMH8, AC5TFFQT9M, 7HCFARHG7D, 00MHHZ9SNE, 4C1AE84N5N, NJ3APQ8BHH, 0WCX7NB4N7, 764GZHTGV8]
sources:
  - url: https://en.wikipedia.org/wiki/Unramified_morphism
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $A$ be a commutative [[$R$-algebra|DPBJ04JMH8]].
Then $A$ is *unramified* over $R$, and the structure map $R \to A$ is an *unramified morphism*, if both conditions hold:

1. $A$ is an $R$-algebra of [[finite type|AC5TFFQT9M]].
2. The module of [[Kähler differentials|7HCFARHG7D]] $\Omega_{A/R}$ is zero.

## Remarks

Some authors, following Grothendieck, require $A$ to be [[finitely presented|764GZHTGV8]] rather than only of finite type; the two agree when $R$ is Noetherian.
Condition 2 alone is called *formally unramified*.
An equivalent form, for $A$ of finite type, is a condition on each [[prime ideal|00MHHZ9SNE]] $\mathfrak q$ of $A$, with $\mathfrak p = \mathfrak q \cap R$.
One needs $\mathfrak p A_{\mathfrak q} = \mathfrak q A_{\mathfrak q}$ in the [[localization|4C1AE84N5N]].
One also needs the [[residue field|NJ3APQ8BHH]] of $\mathfrak q$ to be a finite [[separable extension|0WCX7NB4N7]] of that of $\mathfrak p$.

Example: let $R = \Z[\frac12]$ and $A = R[x]/(x^2 + 1) = \Z[\frac12][i]$.
It is of finite type, and $\Omega_{A/R} = A \, dx / (2x \, dx) \cong A/(2i) = 0$, since $2i$ is a unit in $A$.

Non-example for clause 2: for $A = \Z[i]$ over $\Z$, one gets $\Omega_{A/\Z} \cong \Z[i]/(2) \ne 0$; the prime $2$ ramifies.
Non-example for clause 1: the algebraic closure $\overline{\Q}$ of $\Q$ has $\Omega_{\overline{\Q}/\Q} = 0$, because every element is separable algebraic over $\Q$, but it is not of finite type over $\Q$.
