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

Let $\varphi$ be a first-order [[formula|HYJ10AF6RT]] and let $x$ be a variable.
An occurrence of $x$ in $\varphi$ is *bound* when it lies inside a subformula $\forall x \, \psi$ or $\exists x \, \psi$ of $\varphi$, and *free* otherwise.
The set $\operatorname{FV}(\varphi)$ of *free variables* of $\varphi$ contains the variables with at least one free occurrence.
The set $\operatorname{BV}(\varphi)$ of *bound variables* contains the variables $x$ for which $\varphi$ contains a quantifier $\forall x$ or $\exists x$.
Both sets have a [[recursive definition|Y3FZTH5158]] that follows the formation rules of formulas.
The free variables are the parameters of a formula: the truth of $\varphi$ in a structure depends on the values of its free variables and on nothing else.

## Motivation

In the formula $\exists y \, (x = y + y)$ the two variables play different roles.
The formula says that $x$ is even, so its truth depends on the value of $x$.
The variable $y$ is only a placeholder inside the quantifier: the formula $\exists z \, (x = z + z)$ says the same thing.
The same pattern appears in the sum $\sum_{i=1}^{n} i^2$, which depends on $n$ but not on $i$, and in the integral $\int_0^1 t x \, dt$, which depends on $x$ but not on $t$.
Logic needs to tell the two roles apart for three reasons.
First, a [[sentence|DKFGQTRYZE]] is a formula without free variables, and only sentences are true or false in a structure without further data.
Second, [[substitution|NCDZ969V7X]] may replace free occurrences only.
Third, renaming a bound variable must not change the meaning of a formula.

## Notation

1. $\operatorname{FV}(\varphi)$ and $\operatorname{BV}(\varphi)$ are the sets of free and bound variables. Some books write $\operatorname{Free}(\varphi)$, or say "$x$ occurs free in $\varphi$".
2. $\operatorname{Var}(t)$ is the set of variables of a [[term|6D3WA7N2W4]] $t$. A term has no quantifiers, so all its variables are free.
3. The notation $\varphi(x_1, \ldots, x_n)$ means that $\operatorname{FV}(\varphi) \subseteq \set{x_1, \ldots, x_n}$. It does not say that each $x_i$ occurs in $\varphi$.
4. In a subformula $\forall x \, \psi$ or $\exists x \, \psi$, the formula $\psi$ is the *scope* of the quantifier.
5. Formulas that differ only in the names of bound variables are *alpha-equivalent*, written $\varphi \equiv_\alpha \psi$ in some texts. The name comes from the alpha conversion of the [[lambda calculus|BD756KR8FM]].
6. In Mathlib, `FirstOrder.Language.BoundedFormula L α n` keeps the two kinds apart by type: free variables come from the type `α`, and bound variables are numbers in `Fin n`.

## Remarks

### Examples

1. In $\exists y \, (x = y + y)$ we have $\operatorname{FV} = \set{x}$ and $\operatorname{BV} = \set{y}$. The occurrence of $x$ is free, and the occurrence of $y$ in $y + y$ is bound by $\exists y$.
2. In $P(x) \land \forall x \, Q(x)$ the variable $x$ is [[both free and bound|FSM1P7XHE3]]. Its first occurrence is free, and its second occurrence is bound.
3. In $\forall x \, (\exists y \, R(x, y) \land \exists x \, S(x, y))$ the quantifier $\exists x$ lies in the [[scope|MC39PJBSVQ]] of $\forall x$. The occurrence of $x$ in $S(x, y)$ is bound by the inner quantifier $\exists x$.
4. In $\forall x \, \exists y \, (x < y)$ both variables are bound, so $\operatorname{FV} = \emptyset$ and the formula is a sentence.
5. In $\forall x \, (y = y)$ we have $\operatorname{BV} = \set{x}$ although $x$ has no occurrence in the scope. Such a quantifier is called vacuous.

### Non-examples

1. In $\forall y \, (x < y)$ the occurrence of $x$ lies in the scope of $\forall y$, but it is [[free|AN4VTVRMTA]]. A quantifier binds only its own variable.
2. In the term $f(x, y)$ no variable is bound, because a term contains no quantifier.
3. The constant symbol $0$ in $\forall x \, (x + 0 = x)$ is neither free nor bound. Only variables can be free or bound.

### Basic properties

1. $\operatorname{FV}(\varphi)$ and $\operatorname{BV}(\varphi)$ are finite, because $\varphi$ is a finite string.
2. A variable $x$ is in $\operatorname{FV}(\varphi)$ exactly when $x$ has a free occurrence in $\varphi$. This follows by induction on formulas, as shown on the [[definition|Y3FZTH5158]] page.
3. The truth of $\varphi$ in a structure under an assignment $s$ depends only on the values $s(x)$ for $x \in \operatorname{FV}(\varphi)$. This is the coincidence lemma of [[structures and satisfaction|NJDME6F845]].
4. Alpha-equivalent formulas are [[logically equivalent|0JMR2HM2N2]]. So a bound variable can be renamed to any variable that does not appear anywhere in its scope.
5. Every formula is alpha-equivalent to a formula in which no variable is both free and bound and no two quantifiers bind the same variable. Such formulas are sometimes called rectified. The reason is that $\mathrm{Var}$ is infinite, so fresh names always exist.

### History

In the Begriffsschrift of 1879, Frege used German letters for bound variables and Latin letters for variables whose generality extends over the whole judgement.
The same distinction appears in older mathematics as the index of a sum and the variable of integration.
Church's lambda calculus of the 1930s had a rule for renaming bound variables, later called alpha conversion.

### Common errors

1. Students treat "bound" as "inside some quantifier". In $\forall y \, (x < y)$ the occurrence of $x$ is inside $\forall y$ but free.
2. Students think that $\operatorname{FV}(\varphi)$ and $\operatorname{BV}(\varphi)$ are disjoint. In $P(x) \land \forall x \, Q(x)$ the variable $x$ lies in both sets.
3. Students rename a bound variable to a name that is already free in the scope. Renaming $y$ to $x$ in $\exists y \, (x = y + y)$ gives $\exists x \, (x = x + x)$, a sentence with another meaning.

## Explanations

### L1 human

In the sentence "some number $y$ doubles to $x$" the letter $x$ is an input: we must know $x$ to decide whether the claim is true.
The letter $y$ is not an input.
It only names the number that the word "some" talks about.
For $x = 6$ the claim is true, with $y = 3$, and for $x = 7$ it is false.
We call $x$ free and $y$ bound.
We can change $y$ to $z$ without changing the claim, but changing $x$ changes the question.

### L2 human

We compute the free and bound variables of $\varphi = \forall y \, (x < y) \lor \exists x \, (x = y)$.

1. $\operatorname{FV}(x < y) = \set{x, y}$, and the quantifier $\forall y$ removes $y$. So $\operatorname{FV}(\forall y \, (x < y)) = \set{x}$.
2. $\operatorname{FV}(x = y) = \set{x, y}$, and the quantifier $\exists x$ removes $x$. So $\operatorname{FV}(\exists x \, (x = y)) = \set{y}$.
3. The disjunction takes the union, so $\operatorname{FV}(\varphi) = \set{x, y}$.
4. The two quantifiers bind $y$ and $x$, so $\operatorname{BV}(\varphi) = \set{x, y}$.
5. Renaming the bound variables gives the alpha-equivalent formula $\forall u \, (x < u) \lor \exists w \, (w = y)$, with $\operatorname{FV} = \set{x, y}$ and $\operatorname{BV} = \set{u, w}$.

The typical use is a check before a substitution or a quantifier rule: a term may replace $x$ only where $x$ is free, and it must not contain a variable that a quantifier then binds.
The trap is step 3: both $x$ and $y$ are free, although each of them is also bound in one disjunct.

### L3 human

Binding is the syntactic shape of a function of a variable.
The formula $\varphi$ with $\operatorname{FV}(\varphi) = \set{x}$ defines a subset of the domain of a structure, and the quantifier $\exists x$ turns this subset into a truth value.
The same binding structure appears in the lambda terms $\lambda x . t$, in sums, products and integrals, and in set-builder notation $\set{x \mid \varphi}$.
Alpha-equivalence is the fact that bound names carry no meaning, and the operations of logic are defined on alpha-equivalence classes.
Nameless encodings make the classes concrete: with [[de Bruijn indices|1TC37YHZPE]], or with the numbered bound variables of Mathlib, alpha-equivalent formulas are equal.
Nominal techniques and higher-order abstract syntax are other ways to handle binding in proof assistants.
In proof theory, the eigenvariable conditions of the quantifier rules are conditions on free variables.
In model theory, a formula with $n$ free variables defines an $n$-ary relation in each structure, and the definable sets are the objects of study.
