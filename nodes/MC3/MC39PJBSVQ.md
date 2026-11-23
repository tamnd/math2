---
tag: MC39PJBSVQ
kind: example
name: The scopes of nested quantifiers
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [9CNGDRAMGC]
uses: [Y3FZTH5158, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Let $R$ and $S$ be binary relation symbols, and let
$$\varphi = \forall x \, (\exists y \, R(x, y) \land \exists x \, S(x, y)).$$
We find the scope of each quantifier and the status of each occurrence of a variable, by the [[definition|Y3FZTH5158]].

1. The scope of $\forall x$ is $(\exists y \, R(x, y) \land \exists x \, S(x, y))$, the scope of $\exists y$ is $R(x, y)$, and the scope of $\exists x$ is $S(x, y)$.
2. The $x$ in $R(x, y)$ lies in the scope of $\forall x$ only, so $\forall x$ binds it.
3. The $y$ in $R(x, y)$ lies in the scope of $\exists y$, so $\exists y$ binds it.
4. The $x$ in $S(x, y)$ lies in the scopes of $\forall x$ and of $\exists x$, and the innermost one, $\exists x$, binds it.
5. The $y$ in $S(x, y)$ lies in the scopes of $\forall x$ and $\exists x$, but of no quantifier on $y$, so it is free.
6. By the recursion, $\operatorname{FV}(\exists y \, R(x, y)) = \{ x \}$ and $\operatorname{FV}(\exists x \, S(x, y)) = \{ y \}$.
   The union is $\{ x, y \}$, and $\forall x$ removes $x$, so $\operatorname{FV}(\varphi) = \{ y \}$.
7. The three quantifiers give $\operatorname{BV}(\varphi) = \{ x, y \}$.

## Remarks

Steps 5 and 6 agree, as they must: $y$ is the only variable with a free occurrence.
The outer $\forall x$ binds nothing in the right conjunct, because the inner $\exists x$ takes over the $x$ there.

Renaming the bound variables gives the alpha-equivalent formula $\forall x \, (\exists w \, R(x, w) \land \exists u \, S(u, y))$.
Now each quantifier has its own variable, and the free $y$ stands apart.

If we delete the inner quantifier and write $\forall x \, (\exists y \, R(x, y) \land S(x, y))$, the $x$ in $S(x, y)$ becomes bound by $\forall x$.
The free variables stay $\{ y \}$, but the meaning changes, since the outer $x$ now reaches into $S$.

## Explanations

### L1 human

Think of each quantifier as a fence around its part of the formula.
Inside its fence, a quantifier on $x$ owns every $x$.
When two fences on $x$ are nested, the inner fence wins.
The $y$ in $S(x, y)$ sits inside fences for $x$ only, so nobody owns it, and it is a free input.

### L2 human

We read $\varphi$ in $\mathbb{N}$ with $R(x, y)$ meaning $x < y$ and $S(x, y)$ meaning $x > y$, and we evaluate it from the inside out.
The formula $\exists y \, (x < y)$ says that some number is above $x$, which holds for every $x$.
The formula $\exists x \, (x > y)$ says that some number is above $y$, which holds for every $y$, and it does not mention the outer $x$.
So $\varphi$ is true for every value of its free variable $y$.
The $x$ of $S(x, y)$ gets its value from $\exists x$, not from $\forall x$; reading it as the outer $x$ is the usual slip.
