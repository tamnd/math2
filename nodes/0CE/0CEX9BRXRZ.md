---
tag: 0CEX9BRXRZ
kind: statement
role: theorem
name: Classification of complex quadratic forms
msc: ["11E04", 15A63]
uses: [0Z3FEWZ8HA, 0EWQEYRVA8]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Statement

Let $V$ be a complex vector space of finite dimension $n$, and let $Q$ be a quadratic form on $V$.
Let $r$ be the [[rank|0ZC9YTXZRY]] of the symmetric matrix of $Q$ in a basis.
Then $V$ has a basis $(e_1, \dots, e_n)$ such that, for all $x_1, \dots, x_n \in \C$,
$$Q(x_1 e_1 + \cdots + x_n e_n) = x_1^2 + x_2^2 + \cdots + x_r^2.$$
So two quadratic forms on $V$ are equivalent if and only if their matrices have the same rank.

## Remarks

The proof starts from a [[diagonal form|0Z3FEWZ8HA]] $a_1 x_1^2 + \cdots + a_n x_n^2$ and replaces $e_i$ by $e_i / \sqrt{a_i}$ for each $a_i \ne 0$.
The same result holds over every algebraically closed field of characteristic not $2$.
Over $\R$, this fails: $x^2$ and $-x^2$ have the same rank but are not equivalent.

## Explanations

### L1 human

Over the complex numbers, every nonzero number is a square.
So all coefficients of a diagonal form can be made equal to $1$.
Only the number of squares remains, and it is the rank.
