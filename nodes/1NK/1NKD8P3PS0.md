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

A formula is in prenex normal form when all its quantifiers come first and the rest has no quantifiers.

Let $\sigma$ be a signature.
A first-order [[formula|HYJ10AF6RT]] over $\sigma$ is in *prenex normal form* when it has the form
$$Q_1 x_1 \, Q_2 x_2 \cdots Q_n x_n \, \psi,$$
where $n \ge 0$, each $Q_i$ is $\forall$ or $\exists$, each $x_i$ is a variable, and $\psi$ is a formula with no quantifiers.
The string $Q_1 x_1 \cdots Q_n x_n$ is the *prefix*, and $\psi$ is the *matrix*.
A prenex formula is *universal* when every $Q_i$ is $\forall$, and *existential* when every $Q_i$ is $\exists$.

## Notation

Some books also require the variables $x_1, \dots, x_n$ to be distinct and to occur in the matrix.
Every prenex formula is equivalent to one of that kind.
Drop each quantifier whose variable is not free in what follows it; for a repeated variable this keeps only the innermost quantifier, which alone binds the occurrences in the matrix.

## Remarks

The conditions say two things.
The condition $n \ge 0$ allows an empty prefix, so every quantifier-free formula is prenex.
The condition that $\psi$ has no quantifiers is the real content: it rules out a quantifier hidden under a connective.

For example, $\forall x \, \exists y \, (R(x, y) \lor \neg P(x))$ is prenex, with prefix $\forall x \, \exists y$ and a matrix without quantifiers.
The formula $\neg \forall x \, P(x)$ is not: its first symbol is $\neg$, so its prefix is empty, and then the matrix $\neg \forall x \, P(x)$ contains a quantifier.
It is equivalent to $\exists x \, \neg P(x)$, which is prenex.

In classical first-order logic every formula is logically equivalent to a prenex formula, by the [[prenex normal form theorem|ME9J33BFNC]].
The proof moves quantifiers outward with rules such as $(\forall x \, \varphi) \to \chi \equiv \exists x \, (\varphi \to \chi)$ for $x$ not free in $\chi$, and some of these rules need a nonempty domain.
Worked conversions and the common slips are in the concept [[prenex normal form|CS82V969DE]].

## Explanations

### L1 human

A formula is in prenex form when it starts with all its quantifiers and the rest has none.
For example, "for every $x$ there is a $y$ such that $x < y$" is in prenex form.
"It is not true that every $x$ is positive" is not, because "not" comes before "every".

### L2 human

To test a formula, read it from the left and collect quantifiers with their variables until the first other symbol.
The formula is prenex exactly when no $\forall$ or $\exists$ occurs after that point.
For $\forall x \, (P(x) \to \exists y \, R(x, y))$ the collection stops at the bracket after $\forall x$, and then $\exists y$ appears, so the formula is not prenex.
For $\exists x \, \forall y \, (P(x) \to Q(y))$ the collection takes $\exists x \, \forall y$, and the rest has no quantifier, so the formula is prenex.
