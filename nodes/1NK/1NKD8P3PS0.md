---
tag: 1NKD8P3PS0
kind: definition
name: Prenex normal form
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
defines: CS82V969DE
uses: [HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Definition

Let $\sigma$ be a signature.
A first-order [[formula|HYJ10AF6RT]] over $\sigma$ is in *prenex normal form* if it has the form
$$Q_1 x_1 \, Q_2 x_2 \cdots Q_n x_n \, \psi,$$
where $n \ge 0$ and each $Q_i$ is $\forall$ or $\exists$.
The $x_i$ are variables.
Here $\psi$ is a formula with no quantifiers.
The string $Q_1 x_1 \cdots Q_n x_n$ is the *prefix* and $\psi$ is the *matrix*.

## Notation

1. Some books also require that the variables $x_1, \dots, x_n$ are pairwise distinct and occur in the matrix. Every prenex formula is equivalent to one of this kind.
2. A prenex formula is *universal* when every $Q_i$ is $\forall$, and *existential* when every $Q_i$ is $\exists$.

## Remarks

The formula $\forall x \, \exists y \, (R(x, y) \lor \neg P(x))$ is in prenex normal form: its prefix is $\forall x \, \exists y$ and its matrix has no quantifiers.
The formula $\neg \forall x \, P(x)$ is not: the quantifier is inside a negation, so the formula is not a prefix followed by a quantifier-free matrix.
It is equivalent to $\exists x \, \neg P(x)$, which is in prenex normal form.
In classical first-order logic, every formula is logically equivalent to a formula in prenex normal form, by the [[prenex normal form theorem|~7674d52e]].
The proof moves quantifiers outwards with rules such as $(\forall x \, \varphi) \to \psi \equiv \exists x \, (\varphi \to \psi)$, when $x$ is not free in $\psi$.
This rule uses that structures have nonempty domains.

## Explanations

### L1 human

A formula is in prenex form when it starts with all its quantifiers, and the rest has none.
For example, "for every $x$ there is a $y$ such that $x < y$" is in prenex form.

### L2 human

To test a formula, read it from the left.
Collect the quantifiers with their variables until the first other symbol.
The formula is prenex exactly when no $\forall$ or $\exists$ occurs after that point.
For $\forall x \, (P(x) \to \exists y \, R(x, y))$ the test fails at $\exists y$, so the formula is not prenex.
