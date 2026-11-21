---
tag: 2STE7K6ERM
kind: example
name: The existentially closed fields are the algebraically closed fields
aliases: [existentially-closed-fields-algebraically-closed]
msc: ["03C25", "12F05"]
topics: [1A9JSC5YG8]
audience: grad
instance_of: [6M98MCW575, 68GG7QKN7C]
uses: [60HQMM380F, 04C5ZBG1WT, 0PF6TM8TWT, 0EQWVHF3W5, 03FKX7Z5DC, 61VW0F3R83, 0X6AB5P3G1]
sources:
  - url: https://en.wikipedia.org/wiki/Existentially_closed_model
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $T$ be the theory of [[fields|04C5ZBG1WT]] in the signature $\set{+, -, \cdot, 0, 1}$.
We show that a field $K$ is an [[existentially closed model|60HQMM380F]] of $T$ if and only if $K$ is [[algebraically closed|0PF6TM8TWT]].

1. Let $K$ be e.c., and let $p \in K[x]$ have degree at least $1$. Let $q$ be an [[irreducible|03FKX7Z5DC]] factor of $p$.
2. The quotient $F = K[x]/(q)$ is a [[field extension|0EQWVHF3W5]] of $K$, since $(q)$ is a maximal ideal. The class of $x$ is a root of $q$, so of $p$.
3. The formula $\exists y \, (p(y) = 0)$, with the coefficients of $p$ as parameters, is existential and true in $F$. Since $K$ is e.c., it is true in $K$.
4. So every nonconstant polynomial over $K$ has a root in $K$, and $K$ is algebraically closed.
5. Conversely, let $K$ be algebraically closed and let $F \supseteq K$ be a field. Let $\varphi$ be an existential formula with parameters in $K$ that is true in $F$.
6. Let $\overline F$ be an [[algebraic closure|0X6AB5P3G1]] of $F$. Existential formulas go up to extensions, so $\varphi$ is true in $\overline F$.
7. The inclusion $K \subseteq \overline F$ is an inclusion of algebraically closed fields, so it is [[elementary|61VW0F3R83]]. So $\varphi$ is true in $K$.

So the e.c. fields are exactly the algebraically closed fields.

## Remarks

The example shows that the e.c. models of the theory of fields form an elementary class, the models of $\mathrm{ACF}$.
So $\mathrm{ACF}$ is the [[model companion|68GG7QKN7C]] of the theory of fields, and in fact its model completion.
The conditions are checked directly: every field embeds into its algebraic closure, every algebraically closed field is a field, and $\mathrm{ACF}$ is model complete by step 7.
Step 7 is a form of Hilbert's Nullstellensatz: a system of polynomial equations and inequations over $K$ with a solution in some extension field has a solution in $K$.

When the class changes, the result changes in this way.

- Among ordered fields, the e.c. models are the real closed fields. The field $\C$ is not an ordered field, so the argument of step 2 must use real closed extensions.
- Among fields of characteristic $p$, the e.c. models are the algebraically closed fields of characteristic $p$, by the same argument.
- Among integral domains, the e.c. models are again the algebraically closed fields: a domain that is not a field has an element without an inverse, and the fraction field supplies one.

## Explanations

### L1 human

A field is a number system where one can add, subtract, multiply and divide.
It is existentially closed when every system of equations that can be solved in a bigger field can already be solved in the field itself.
The complex numbers have this property, because every polynomial equation has a complex root.
The real numbers do not: $x^2 + 1 = 0$ has the solution $x = i$ only in the complex numbers.

### L2 human

We follow step 2 for $K = \Q$ and $p = x^2 - 2$.

1. The polynomial $x^2 - 2$ is irreducible over $\Q$, since $\sqrt 2$ is irrational.
2. The quotient $\Q[x]/(x^2 - 2)$ is a field, with elements $a + bx$ for rationals $a, b$.
3. In it, $x \cdot x = 2$, so the class of $x$ is a square root of $2$.
4. So $\exists y \, (y \cdot y = 2)$ holds in an extension of $\Q$ and fails in $\Q$, and $\Q$ is not e.c.

The typical use of the example is as the model for all later e.c. classes: closure under adding solutions of equations.
A trap is to think that the e.c. models of a theory always form an elementary class; for groups they do not.
