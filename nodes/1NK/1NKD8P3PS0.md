---
tag: 1NKD8P3PS0
kind: definition
name: Prenex normal form
msc: [03B10]
defines: CS82V969DE
uses: [HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
---

## Definition

Let $\sigma$ be a signature.
A first-order [[formula|HYJ10AF6RT]] over $\sigma$ is in *prenex normal form* if it has the form
$$Q_1 x_1 \, Q_2 x_2 \cdots Q_n x_n \, \psi,$$
where $n \ge 0$ and each $Q_i$ is $\forall$ or $\exists$.
The $x_i$ are variables.
Here $\psi$ is a formula with no quantifiers.
The string $Q_1 x_1 \cdots Q_n x_n$ is the *prefix* and $\psi$ is the *matrix*.

## Remarks

The formula $\forall x \, \exists y \, (R(x, y) \lor \neg P(x))$ is in prenex normal form: its prefix is $\forall x \, \exists y$ and its matrix has no quantifiers.
The formula $\neg \forall x \, P(x)$ is not: the quantifier is inside a negation, so the formula is not a prefix followed by a quantifier-free matrix.
It is equivalent to $\exists x \, \neg P(x)$, which is in prenex normal form.
In classical first-order logic, every formula is logically equivalent to a formula in prenex normal form.
The proof moves quantifiers outwards with rules such as $(\forall x \, \varphi) \to \psi \equiv \exists x \, (\varphi \to \psi)$, when $x$ is not free in $\psi$.
This rule uses that structures have nonempty domains.
