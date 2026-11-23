---
tag: 9CNGDRAMGC
kind: concept
name: Free and bound variables
aliases: [free-variable, bound-variable]
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
uses: [HYJ10AF6RT, 6D3WA7N2W4, 0GHS47PDAQ, 0MSRQHCNN9, 8BS13NDRE8]
sources:
  - url: https://en.wikipedia.org/wiki/Free_variables_and_bound_variables
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Summary

A variable in a formula plays one of two roles: it is an input that the formula talks about, or it is a placeholder that a quantifier uses up.
In
$$\forall y \, (x < y) \land \exists x \, (x = 0)$$
the $x$ in $x < y$ is an input, since the truth of the formula depends on its value, and it is called free.
The $y$ in $x < y$ and the $x$ in $x = 0$ belong to the quantifiers $\forall y$ and $\exists x$, and they are called bound.
So the same letter $x$ is free at one place and bound at another.

Let $\varphi$ be a first-order [[formula|HYJ10AF6RT]] and $x$ a variable.
An occurrence of $x$ in $\varphi$ is *bound* when it lies inside a subformula $\forall x \, \psi$ or $\exists x \, \psi$ of $\varphi$, and *free* otherwise.
The set $\operatorname{FV}(\varphi)$ of *free variables* contains the variables with at least one free occurrence.
The set $\operatorname{BV}(\varphi)$ of *bound variables* contains the variables $x$ such that $\forall x$ or $\exists x$ occurs in $\varphi$.
Both sets have a [[recursive definition|Y3FZTH5158]], and in the example $\operatorname{FV} = \{ x \}$ and $\operatorname{BV} = \{ x, y \}$.

## Motivation

The formula $\exists y \, (x = y + y)$ says that $x$ is even.
Its truth depends on the value of $x$, but not on any value of $y$: the formula $\exists z \, (x = z + z)$ says the same thing.
You know this pattern already.
The sum $\sum_{i=1}^{n} i^2$ depends on $n$ and not on $i$, and the integral $\int_0^1 t x \, dt$ depends on $x$ and not on $t$.

Logic must keep the two roles apart for three reasons.
A [[sentence|DKFGQTRYZE]] is a formula with no free variables, and only a sentence is true or false in a structure without further data.
[[Substitution|NCDZ969V7X]] may replace free occurrences only.
And renaming a bound variable must not change the meaning, so we need to know which variables are bound.

## Notation

We write $\operatorname{FV}(\varphi)$ and $\operatorname{BV}(\varphi)$; some books write $\operatorname{Free}(\varphi)$, or say "$x$ occurs free in $\varphi$".
For a [[term|6D3WA7N2W4]] $t$, $\operatorname{Var}(t)$ is its set of variables, and all of them are free, since a term has no quantifiers.
In $\forall x \, \psi$ or $\exists x \, \psi$, the formula $\psi$ is the *scope* of the quantifier.
The notation $\varphi(x_1, \ldots, x_n)$ means $\operatorname{FV}(\varphi) \subseteq \{ x_1, \ldots, x_n \}$, and it does not promise that each $x_i$ occurs.
Formulas that differ only in the names of bound variables are *alpha-equivalent*, a name taken from the [[lambda calculus|BD756KR8FM]].
In Mathlib, `FirstOrder.Language.BoundedFormula L α n` keeps the roles apart by type: free variables come from `α`, and bound variables are numbers in `Fin n`.

## Remarks

### Working the opening example

Compute the free variables from the inside out.
The atomic formula $x < y$ has $\operatorname{FV} = \{ x, y \}$, and $\forall y$ removes $y$, leaving $\{ x \}$.
The atomic formula $x = 0$ has $\operatorname{FV} = \{ x \}$, and $\exists x$ removes $x$, leaving $\emptyset$.
A conjunction takes the union:
$$\operatorname{FV}(\forall y \, (x < y) \land \exists x \, (x = 0)) = \{ x \} \cup \emptyset = \{ x \}.$$
The quantifiers are $\forall y$ and $\exists x$, so $\operatorname{BV} = \{ x, y \}$.
Check: in $(\mathbb{N}, <, 0)$ the formula is false for every value of $x$, since $y = x$ fails $x < y$; in $(\mathbb{N}, \le, 0)$, reading $<$ as $\le$, it is true exactly for $x = 0$.

### More examples

In $P(x) \land \forall x \, Q(x)$ the variable $x$ is [[both free and bound|FSM1P7XHE3]]: the first occurrence is free and the second is bound.
In $\forall x \, (\exists y \, R(x, y) \land \exists x \, S(x, y))$ the inner $\exists x$ takes over the $x$ in $S(x, y)$, and the $y$ there is free; the [[scopes of nested quantifiers|MC39PJBSVQ]] work this out.
In $\forall x \, \exists y \, (x < y)$ both variables are bound, so $\operatorname{FV} = \emptyset$ and the formula is a sentence.
In $\forall x \, (y = y)$ the quantifier is vacuous: $\operatorname{BV} = \{ x \}$ although $x$ does not occur in the scope.

### What does not count as bound

In $\forall y \, (x < y)$ the occurrence of $x$ lies in the scope of $\forall y$, yet it is [[free|AN4VTVRMTA]].
A quantifier binds only its own variable.
In the term $f(x, y)$ nothing is bound, since a term has no quantifier.
The constant symbol $0$ in $\forall x \, (x + 0 = x)$ is neither free nor bound, because only variables have these roles.

### The rules you can use

Both sets are finite, since a formula is a finite string.
A variable lies in $\operatorname{FV}(\varphi)$ exactly when it has a free occurrence; the [[definition|Y3FZTH5158]] proves this by induction on formulas.
The truth of $\varphi$ in a structure under an assignment depends only on the values of the variables in $\operatorname{FV}(\varphi)$; this is the coincidence lemma of [[structures and satisfaction|NJDME6F845]].
Alpha-equivalent formulas are [[logically equivalent|0JMR2HM2N2]], so a bound variable may be renamed to any variable that does not appear in its scope.
Since there are infinitely many variables, every formula is alpha-equivalent to one in which no variable is both free and bound and no two quantifiers bind the same variable.

### Watch out

"Bound" does not mean "inside some quantifier".
In $\forall y \, (x < y)$ the $x$ is inside $\forall y$, but it is free.

$\operatorname{FV}(\varphi)$ and $\operatorname{BV}(\varphi)$ can overlap, as $x$ does in the opening example.

A renaming must use a fresh name.
Renaming $y$ to $x$ in $\exists y \, (x = y + y)$ gives $\exists x \, (x = x + x)$.
This is a sentence, true in $\mathbb{N}$ because $0 = 0 + 0$, so the free $x$ has been captured and the meaning has changed.

### History

In the Begriffsschrift of 1879, Frege used German letters for bound variables and Latin letters for variables whose generality covers the whole judgement.
Church's lambda calculus of the 1930s had a rule for renaming bound variables, later called alpha conversion.

### Try it

Find $\operatorname{FV}$ of $\exists x \, (P(x) \to \forall y \, R(x, y, z))$.
The answer is $\{ z \}$: $\forall y$ removes $y$ from $\{ x, y, z \}$, the implication adds nothing new, and $\exists x$ removes $x$.

Is the $y$ in $\exists x \, (x < y) \lor \forall y \, (y = y)$ free?
The first $y$ is free and the other two are bound, so $y \in \operatorname{FV} \cap \operatorname{BV}$.

## Explanations

### L1 human

In the sentence "some number $y$ doubles to $x$", the letter $x$ is an input: we must know $x$ to decide whether the claim is true.
The letter $y$ is not an input; it only names the number that the word "some" talks about.
For $x = 6$ the claim is true, with $y = 3$, and for $x = 7$ it is false.
We call $x$ free and $y$ bound.
We can change $y$ to $z$ without changing the claim, but changing $x$ changes the question.

### L2 human

Take $\varphi = \forall y \, (x < y) \lor \exists x \, (x = y)$, a formula where each letter plays both roles.
The left disjunct has $\operatorname{FV} = \{ x, y \} \setminus \{ y \} = \{ x \}$.
The right disjunct has $\operatorname{FV} = \{ x, y \} \setminus \{ x \} = \{ y \}$.
The disjunction takes the union, so $\operatorname{FV}(\varphi) = \{ x, y \}$, and the two quantifiers give $\operatorname{BV}(\varphi) = \{ x, y \}$.
Renaming the bound variables gives the alpha-equivalent formula $\forall u \, (x < u) \lor \exists w \, (w = y)$, where the free $x$ and $y$ now stand apart from the bound $u$ and $w$.
This renamed form is the safe starting point for a substitution or a quantifier rule, because no letter has two roles.

### L3 human

Binding is the syntax of a function of a variable.
A formula with $\operatorname{FV}(\varphi) = \{ x \}$ defines a subset of the domain of a structure, and $\exists x$ turns that subset into a truth value.
The same binding structure appears in the lambda term $\lambda x . t$, in sums and integrals, and in set-builder notation $\{ x \mid \varphi \}$.
Alpha-equivalence says that bound names carry no meaning, and the operations of logic really act on alpha-equivalence classes.
Nameless encodings make the classes concrete: with [[de Bruijn indices|1TC37YHZPE]], or with the numbered bound variables of Mathlib, alpha-equivalent formulas are equal.
In proof theory, the eigenvariable conditions of the quantifier rules are conditions on free variables, and in model theory a formula with $n$ free variables defines an $n$-ary relation.
