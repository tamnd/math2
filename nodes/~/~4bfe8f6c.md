---
tag: ~4bfe8f6c
kind: example
name: Embeddings between algebraically closed fields are elementary
msc: ["03C07", "03C60"]
topics: [2RE7GWWXM5]
audience: ug2
instance_of: [CGH8C8EA9N]
uses: [CGH8C8EA9N, MT8TDVPBXB, 7FDDXV3JK7, C9494XYEMN, 0PF6TM8TWT]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraically_closed_field
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $L = \set{+, -, \cdot, 0, 1}$ be the signature of rings.
Let $K$ and $F$ be [[algebraically closed fields|0PF6TM8TWT]], and let $h \colon K \to F$ be an embedding of $L$-structures.
We check that $h$ is an [[elementary embedding|CGH8C8EA9N]].

1. Let $\varphi(x_1, \dots, x_n)$ be an $L$-formula and let $\bar a = (a_1, \dots, a_n)$ be a tuple of $K$.
2. The theory $\mathrm{ACF}$ of algebraically closed fields has [[quantifier elimination|7FDDXV3JK7]]; see [[the model theory of algebraically closed fields|MT8TDVPBXB]]. So there is a quantifier-free formula $\psi(\bar x)$ with $\mathrm{ACF} \models \forall \bar x \, (\varphi(\bar x) \leftrightarrow \psi(\bar x))$.
3. $K$ is a model of $\mathrm{ACF}$, so $K \models \varphi(\bar a)$ if and only if $K \models \psi(\bar a)$.
4. [[Embeddings preserve quantifier-free formulas|C9494XYEMN]], so $K \models \psi(\bar a)$ if and only if $F \models \psi(h(\bar a))$.
5. $F$ is a model of $\mathrm{ACF}$, so $F \models \psi(h(\bar a))$ if and only if $F \models \varphi(h(\bar a))$.
6. Joining steps 3 to 5 gives $K \models \varphi(\bar a) \iff F \models \varphi(h(\bar a))$, so $h$ is elementary.

The standard instance is the inclusion of the field $\overline{\Q}$ of algebraic numbers into $\C$, so $\overline{\Q} \preceq \C$.

## Remarks

The example shows that $\mathrm{ACF}$ is a [[model complete theory|YR6HCMABTE]]: every embedding between its models is elementary.
A consequence: a finite system of polynomial equations and inequations with coefficients in $\overline{\Q}$ that has a solution in $\C$ also has a solution in $\overline{\Q}$.
To see this, write "the system has a solution" as an existential formula with the coefficients as parameters, and apply the elementarity of $\overline{\Q} \subseteq \C$.
The proof does not need $K$ and $F$ to have the same characteristic, because an embedding of fields keeps the characteristic.
If $K$ is not algebraically closed, the conclusion fails: the inclusion $\Q \subseteq \C$ is an embedding, but $\exists y \, (y \cdot y = 1 + 1)$ is false in $\Q$ and true in $\C$.
In the same way, quantifier elimination for real closed fields shows that embeddings of real closed ordered fields are elementary; see [[this example|~76723848]].

## Explanations

### L1 human

The algebraic numbers are the complex numbers that solve some polynomial equation with whole-number coefficients, such as $\sqrt{2}$ or $i$.
Any question about the arithmetic of algebraic numbers, written with "for all" and "there exists", has the same answer in the algebraic numbers and in all the complex numbers.
For example, "is there a number whose square is $\sqrt{2}$" has the answer yes in both places, since $\sqrt[4]{2}$ is algebraic.
So the small field of algebraic numbers cannot be told apart from the complex numbers by such questions.

### L2 human

We check one consequence directly: the system $x^2 + y^2 = 1$, $x - y = \sqrt{2}$ has a solution in $\C$, so it has one in $\overline{\Q}$.

1. Substitute $x = y + \sqrt{2}$: we get $2y^2 + 2\sqrt{2}\, y + 1 = 0$.
2. The discriminant is $8 - 8 = 0$, so $y = -\sqrt{2}/2$ is the only root.
3. Then $x = \sqrt{2}/2$, and $x^2 + y^2 = \tfrac12 + \tfrac12 = 1$.
4. Both numbers are algebraic, so the solution lies in $\overline{\Q}$, as the example predicts.

The typical use is to move a solution of an algebraic problem from $\C$, where analysis is available, to a smaller algebraically closed field.
A trap is to use a subfield that is not algebraically closed: the equation $y^2 = 2$ has a solution in $\C$ and none in $\Q$.
