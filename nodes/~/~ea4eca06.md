---
tag: ~ea4eca06
kind: example
name: The scopes of nested quantifiers
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [~2fd0cd75]
uses: [~e71c5bb3, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Let $R$ and $S$ be binary relation symbols, and let
$$\varphi = \forall x \, (\exists y \, R(x, y) \land \exists x \, S(x, y)).$$
We find the scope of each quantifier and the status of each occurrence of a variable, by the [[definition|~e71c5bb3]].

1. The scope of $\forall x$ is $(\exists y \, R(x, y) \land \exists x \, S(x, y))$. The scope of $\exists y$ is $R(x, y)$. The scope of $\exists x$ is $S(x, y)$.
2. The $x$ in $R(x, y)$ lies in the scope of $\forall x$ only, so it is bound by $\forall x$.
3. The $y$ in $R(x, y)$ lies in the scope of $\exists y$, so it is bound by $\exists y$.
4. The $x$ in $S(x, y)$ lies in the scopes of $\forall x$ and of $\exists x$. It is bound by the innermost one, $\exists x$.
5. The $y$ in $S(x, y)$ lies in the scopes of $\forall x$ and $\exists x$, but in the scope of no quantifier on $y$. So it is free.
6. By the recursion: $\operatorname{FV}(\exists y \, R(x, y)) = \set{x}$ and $\operatorname{FV}(\exists x \, S(x, y)) = \set{y}$. The union is $\set{x, y}$, and $\forall x$ removes $x$, so $\operatorname{FV}(\varphi) = \set{y}$.
7. $\operatorname{BV}(\varphi) = \set{y} \cup \set{x} \cup \set{x} = \set{x, y}$.

## Remarks

Steps 5 and 6 agree, as they must: $y$ is the only variable with a free occurrence.
The outer $\forall x$ binds nothing in the right conjunct, because the inner $\exists x$ takes over the occurrence of $x$ there.
Renaming the bound variables gives the alpha-equivalent formula $\forall x \, (\exists w \, R(x, w) \land \exists u \, S(u, y))$.
In this form each quantifier binds its own variable and the free $y$ stands apart.
If we delete the inner quantifier and write $\forall x \, (\exists y \, R(x, y) \land S(x, y))$, the $x$ in $S(x, y)$ becomes bound by $\forall x$, and the free variables stay $\set{y}$.

## Explanations

### L1 human

Think of each quantifier as a fence around its part of the formula.
Inside its fence, a quantifier on $x$ owns every $x$.
When two fences on $x$ are nested, the inner fence wins.
The $y$ in $S(x, y)$ sits inside fences for $x$ only, so nobody owns it, and it is a free input.
So the claim depends on one value, the value of $y$.

### L2 human

We read $\varphi$ in the structure $(\mathbb{N}, <, >)$, with $R(x, y)$ meaning $x < y$ and $S(x, y)$ meaning $x > y$.

1. $\exists y \, (x < y)$ says that some number is above $x$. This is true for every $x$.
2. $\exists x \, (x > y)$ says that some number is above $y$. This is true for every $y$, and it does not mention the outer $x$.
3. So $\varphi$ is true for every value of $y$.

The typical use of scopes is the evaluation of a formula from the inside out, as in steps 1 and 2.
The trap is step 2: the $x$ of $S(x, y)$ is not the $x$ of the outer quantifier, so its value does not come from $\forall x$.
