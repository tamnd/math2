---
tag: KSC0K8GGCG
kind: example
name: The complex field has no definable Skolem function for square roots
msc: ["03C07", "03C60"]
topics: [2RE7GWWXM5]
audience: ug2
not_instance_of:
  - target: NKQY9NB955
    note: no function defined by a formula without parameters is a Skolem function for y·y = x in the complex field, because complex conjugation would have to fix its value at -1
uses: [NKQY9NB955, CY1TXHF6KQ, XY6CJMDY5M, NDTJ2E895C]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: Skolem theories
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $L = \set{+, -, \cdot, 0, 1}$ and $\mathcal{C} = (\C, +, -, \cdot, 0, 1)$.
Let $\varphi(x, y)$ be the formula $y \cdot y = x$.
We check that no $L$-formula $\psi(x, y)$ without parameters defines a [[Skolem function|NKQY9NB955]] for $\varphi$ in $\mathcal{C}$.

1. Assume that $\psi(x, y)$ defines a function $f \colon \C \to \C$, and that $f$ is a Skolem function for $\varphi$.
2. $\mathcal{C} \models \exists y \, \varphi(-1, y)$, with $y = i$. So $c = f(-1)$ satisfies $c^2 = -1$, and $c = i$ or $c = -i$.
3. Complex conjugation $\sigma(a + bi) = a - bi$ preserves sums, products, $0$ and $1$, and it is a bijection. So it is an [[automorphism|XY6CJMDY5M]] of $\mathcal{C}$.
4. $\mathcal{C} \models \psi(-1, c)$. [[Automorphisms preserve formulas|NDTJ2E895C]], so $\mathcal{C} \models \psi(\sigma(-1), \sigma(c))$, that is, $\mathcal{C} \models \psi(-1, \sigma(c))$.
5. $\psi$ defines a function, so $\sigma(c) = f(-1) = c$.
6. But $\sigma(i) = -i \ne i$ and $\sigma(-i) = i \ne -i$. So $\sigma(c) \ne c$, a contradiction.
7. So no Skolem function for $\varphi$ in $\mathcal{C}$ is [[definable|CY1TXHF6KQ]] without parameters.

## Remarks

The example shows that Skolem functions exist, by the axiom of choice, but in general they are not definable.
In $\R$ the order separates the two square roots and gives a [[definable Skolem function|117B3EEJD8]]; in $\C$ an automorphism exchanges them.
Parameters do not help.
For finitely many parameters $\bar a$, choose $x$ transcendental over $\Q(\bar a)$.
Then $x$ is not a square in $\Q(\bar a, x)$, so some automorphism of $\C$ fixes $\Q(\bar a, x)$ and exchanges the two square roots of $x$; the argument of steps 4 to 6 then applies at $x$.
So adding Skolem functions to the field $\C$ adds new structure: the expansion has fewer automorphisms, and its definable sets are not those of the field.
The theory of algebraically closed fields is not a Skolem theory, and its Skolemization is a different theory.

## Explanations

### L1 human

The number $-1$ has two complex square roots, $i$ and $-i$.
Nothing in addition and multiplication tells them apart: exchanging $i$ and $-i$ everywhere, which is complex conjugation, keeps all equations true.
So a rule written only with addition and multiplication cannot pick one of them.
Any rule that picks a square root has to make an arbitrary choice.

### L2 human

We check step 3 on a product, to see that conjugation preserves the operations.

1. Let $z = 1 + 2i$ and $w = 3 - i$. Then $z w = 3 - i + 6i - 2i^2 = 5 + 5i$.
2. $\sigma(z) \sigma(w) = (1 - 2i)(3 + i) = 3 + i - 6i - 2i^2 = 5 - 5i$.
3. $\sigma(z w) = 5 - 5i$, so $\sigma(z w) = \sigma(z) \sigma(w)$ in this case.

The typical use of the argument is to prove non-definability: a set or function that is not fixed by some automorphism is not definable without parameters.
A trap is to apply the argument with parameters that the automorphism moves; an automorphism proves non-definability over $A$ only if it fixes $A$ pointwise.
