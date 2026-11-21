---
tag: RE5TFTDP4D
kind: definition
name: Quantifier elimination
msc: ["03C10"]
topics: [1A9JSC5YG8]
audience: grad
defines: 7FDDXV3JK7
uses: [92SWXST1ZM, HYJ10AF6RT, WDVVEYD6AT]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
    locator: lead section
  - book: isbn:9780387987606
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]] and let $T$ be an $L$-[[theory|92SWXST1ZM]].
The theory $T$ *has quantifier elimination* if, for every $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$, there is a quantifier-free $L$-formula $\psi(x_1, \dots, x_n)$ such that
$$T \models \forall x_1 \cdots \forall x_n \, \bigl(\varphi(x_1, \dots, x_n) \leftrightarrow \psi(x_1, \dots, x_n)\bigr).$$
For $n = 0$ the formula $\psi$ is a quantifier-free sentence, and the sentences $\top$ and $\bot$ count as quantifier-free.

An $L$-structure $M$ *has quantifier elimination* if its complete theory $\operatorname{Th}(M)$ has quantifier elimination.

## Notation

The formula $\psi$ is a *quantifier-free equivalent* of $\varphi$ modulo $T$.
The free variables of $\psi$ are among those of $\varphi$; this condition is part of the definition.
Many authors write QE for quantifier elimination.

## Remarks

The convention on $\top$ and $\bot$ matters when $L$ has no constant symbols, because then there are no atomic sentences.
It suffices to treat formulas of the form $\exists y \, \chi(x_1, \dots, x_n, y)$ with $\chi$ a conjunction of atomic and negated atomic formulas; see the [[tests for quantifier elimination|~e415d689]].

Example: the theory of dense linear orders without endpoints, in the signature $\set{<}$, has quantifier elimination; see [[this example|~f961c7a6]].
For instance, $\exists y \, (x_1 < y \wedge y < x_2)$ is equivalent to $x_1 < x_2$ by density, and $\exists y \, (x_1 < y)$ is equivalent to $x_1 = x_1$ since there is no greatest element.

Non-example: the theory of $(\R, +, \cdot, 0, 1)$, without the order symbol, does not have quantifier elimination; see [[this non-example|~5a627ec0]].
The formula $\exists y \, (x = y \cdot y)$ defines $[0, \infty)$, which is infinite and co-infinite.
A quantifier-free formula in $x$ is a Boolean combination of polynomial equations $p(x) = 0$, so it defines a finite or cofinite subset of $\R$.
With the order symbol added, the theory has quantifier elimination; this is [[Tarski's theorem|FSJ9NGRRPA]].

The requirement that $\psi$ have no new free variables excludes a cheat.
Without it, $\exists y \, \chi(\bar x, y)$ would be equivalent to $\chi(\bar x, y)$ with $y$ free, which is false in general.

## Explanations

### L1 human

A theory has quantifier elimination when each statement with "there is" or "for all" can be replaced by one without these words.
The replacement must say the same thing about the same objects, in every model of the theory.
For the fractions with their order, "there is a fraction between $a$ and $b$" becomes "$a$ is less than $b$".

### L2 human

We check the definition for one formula of the theory of dense linear orders.

1. Let $\varphi(x_1, x_2)$ be $\exists y \, (x_1 < y \wedge y < x_2)$, and let $\psi(x_1, x_2)$ be $x_1 < x_2$.
2. If $\varphi$ holds, then $x_1 < y < x_2$ for some $y$, so $x_1 < x_2$ by transitivity.
3. If $\psi$ holds, density gives $y$ with $x_1 < y < x_2$, so $\varphi$ holds.
4. So $T \models \forall x_1 \, \forall x_2 \, (\varphi \leftrightarrow \psi)$.

The typical use of the definition is in a proof by induction on formulas, where only the step for $\exists$ needs work.
A trap is to check the equivalence in one model only: the definition asks for it in every model of $T$, and for an incomplete $T$ one model is not enough.
