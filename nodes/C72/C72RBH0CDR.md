---
tag: C72RBH0CDR
kind: concept
name: Proof-theoretic ordinal
msc: ["03F15", "03F30"]
topics: [XTTKZTYDSD]
audience: grad
specializes: [0YSCSX5YZC]
uses: [0YSCSX5YZC, 0QFT7Z76N5, 0ZHQMQ2C1N, KT50SMH3EC, C19Z3B6V4P, 6GD30FGYDZ, 01CGSJ0GNQ, QQQRJA90EP]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
---

## Summary

Peano arithmetic can prove that the order on pairs of numbers, "compare the first entries, then the second", has no infinite descending sequence.
That order has type $\omega^2$, and in the same way PA handles $\omega^\omega$, $\omega^{\omega^\omega}$ and every longer tower, but never $\varepsilon_0$ itself.
The proof-theoretic ordinal of a theory records exactly this: how long a [[well-order|01CGSJ0GNQ]] the theory can still recognize as a well-order.

We use the following definition, the $\Pi^1_1$ ordinal.
Let $T$ be a recursively axiomatized theory that contains enough arithmetic, and add a new unary predicate $X$.
For a [[primitive recursive|QQQRJA90EP]] linear order $\prec$ on $\mathbb{N}$, the formula $\operatorname{TI}(\prec, X)$ says that if $X$ is progressive along $\prec$, then $X$ holds of every number.
The proof-theoretic ordinal of $T$ is
$$\lvert T \rvert = \sup \{ \operatorname{otyp}(\prec) : \prec \text{ is a primitive recursive well-order and } T \vdash \operatorname{TI}(\prec, X) \}.$$
The [[precise definition|C19Z3B6V4P]] spells out each part.
So $\lvert T \rvert$ is the supremum of the order types of the primitive recursive well-orders whose well-foundedness $T$ proves.

## Motivation

Gödel's second incompleteness theorem says that a consistent theory such as PA cannot prove its own consistency.
Gentzen found what is missing.
In 1936 he proved the consistency of PA from [[transfinite induction|0ZHQMQ2C1N]] up to [[epsilon nought|KT50SMH3EC]], and in 1943 he showed that PA proves this induction below each $\alpha < \varepsilon_0$ but not up to $\varepsilon_0$.
So one ordinal marks the exact point where the theory stops.

This suggests attaching an ordinal to every theory, and the proof-theoretic ordinal is that ordinal.
It puts theories of very different kinds on one scale: arithmetic, subsystems of second-order arithmetic, set theories such as Kripke-Platek, and theories of inductive definitions.
Computing it is the aim of an [[ordinal analysis|57PTMS2ADY]], and the later pages on $\Gamma_0$, the Bachmann-Howard ordinal and collapsing functions are all about naming the values.

## Notation

Most books write $\lvert T \rvert$, and some write $\lvert T \rvert_{\Pi^1_1}$ or $\lvert T \rvert_{\sup}$ to separate it from other ordinals of $T$.
The $\Pi^0_2$ ordinal $\lvert T \rvert_{\Pi^0_2}$ is defined from the provably total functions of $T$ instead of from well-orders.
Some books take computable instead of primitive recursive orders, or orders on a primitive recursive subset of $\mathbb{N}$; for the standard theories this gives the same value.

## Remarks

### A first lower bound

Let us check that PA proves induction along the order of type $\omega^2$ from the Summary.
Code the pair $(a, b)$ by one number, and put $(a, b) \prec (c, d)$ if $a < c$, or $a = c$ and $b < d$.
Assume that $X$ is progressive: $X(a, b)$ holds as soon as $X$ holds at every pair below $(a, b)$.

We prove $\forall b \, X(a, b)$ by strong induction on $a$.
Fix $a$ and assume $\forall b \, X(a', b)$ for every $a' < a$.
Now use strong induction on $b$.
The pairs below $(a, b)$ are the pairs $(a', b')$ with $a' < a$, which satisfy $X$ by the outer hypothesis, and the pairs $(a, b')$ with $b' < b$, which satisfy $X$ by the inner hypothesis.
So progressiveness gives $X(a, b)$.
Both inductions are on formulas with the parameter $X$, which PA allows, so PA proves $\operatorname{TI}(\prec, X)$ and $\omega^2 \le \lvert \mathrm{PA} \rvert$.

### The values for the standard theories

The table lists the values that the later pages explain.

| Theory | Proof-theoretic ordinal |
|---|---|
| [[primitive recursive arithmetic|WCXH72T8D8]], $\mathrm{I\Sigma}_1$ | $\omega^\omega$ |
| PA, $\mathrm{ACA}_0$ | $\varepsilon_0$ |
| ACA | $\varepsilon_{\varepsilon_0}$ |
| [[ATR0|MKB74TX3Z8]] | $\Gamma_0$ |
| ATR | $\Gamma_{\varepsilon_0}$ |
| $\mathrm{ID}_1$, KP | Bachmann-Howard ordinal |
| $\Pi^1_1\text{-}\mathrm{CA}_0$ | $\psi_0(\Omega_\omega)$, in Buchholz's notation |

The worked cases are [[IΣ1|8KPSC3GE1B]], [[PA|7ANX5PDRDM]], [[ACA0|GXZZW7G54P]] and [[ACA|JHYZ2A3VPJ]].
The ordinal $\Gamma_0$ is the [[Feferman-Schütte ordinal|CNN7BK5YAW]], and the [[Bachmann-Howard ordinal|QH3ENXFRSV]] is the first value that needs a collapsing function.

### What the definition leaves out

The first uncountable ordinal $\omega_1$ is never a proof-theoretic ordinal.
Each order in the supremum is an order on $\mathbb{N}$, so it has countable type, and $T$ has only countably many proofs.

An unsound theory can prove induction along an order that is not well-founded.
[[PA plus the negation of Con(PA)|FWY2SE83Q4]] does this, and that is why the supremum runs only over true well-orders.

One order is not enough to read off $\lvert T \rvert$.
By [[the artificial notation system|PXMATF6B16]], PA fails to prove induction along a certain primitive recursive order of type only $\omega$.

### First properties

If $T \subseteq T'$, then every order counted for $T$ is counted for $T'$, so $\lvert T \rvert \le \lvert T' \rvert$.
If $T$ proves only true $\Pi^1_1$ sentences, then $\lvert T \rvert < \omega_1^{\mathrm{CK}}$, the least ordinal that is not the type of a computable well-order.
The argument, in [[the definition|C19Z3B6V4P]], puts all the orders that $T$ proves well-founded side by side in one computable well-founded relation.

### Watch out: the value depends on the definition

The $\Pi^1_1$ ordinal and the $\Pi^0_2$ ordinal are different notions, and the second depends on a choice of function hierarchy.
The provably total functions of PRA are the primitive recursive functions.
Measured by the fast-growing functions $F_\alpha$, they are those below $F_\omega$, so the answer is $\omega$.
Measured by the Hardy functions $H_\alpha$, where $H_{\omega^\alpha} = F_\alpha$, the answer is $\omega^\omega$.
So always say which definition you use.
For PA both hierarchies give $\varepsilon_0$, since $\omega^\alpha < \varepsilon_0$ for every $\alpha < \varepsilon_0$.

### History

Gentzen's papers of 1936 and 1943 give the first value, $\varepsilon_0$ for PA.
Feferman in 1964 and Schütte in 1965, independently, identified $\Gamma_0$ as the limit of predicative analysis.
Bachmann introduced the notation behind the Bachmann-Howard ordinal in 1950, and Howard used it in 1972 for the theory $\mathrm{ID}_1$ of one inductive definition.

### Try it

Why is $\lvert T \rvert \ge \omega$ for every $T$ that contains PA?
The usual order $<$ on $\mathbb{N}$ has type $\omega$, and $\operatorname{TI}(<, X)$ is the strong induction schema for $X$.

Which is larger, $\lvert \mathrm{I\Sigma}_1 \rvert$ or $\lvert \mathrm{ACA} \rvert$?
$\lvert \mathrm{ACA} \rvert = \varepsilon_{\varepsilon_0}$ is larger, since $\omega^\omega < \varepsilon_0 < \varepsilon_{\varepsilon_0}$.

## Explanations

### L1 human

Some orderings of the natural numbers have the property that every walk downward stops after finitely many steps.
A theory can prove this for some orderings and not for others.
Each such ordering has a length, which is an ordinal, and the theory reaches up to a certain length and no further.
That length is the proof-theoretic ordinal.
For Peano arithmetic it is $\varepsilon_0$, the limit of $\omega$, $\omega^\omega$, $\omega^{\omega^\omega}$, and so on.

### L2 human

We show $\varepsilon_0 \le \lvert \mathrm{PA} \rvert$ from one theorem.
Let $\prec$ be the order on the [[Cantor normal forms|6GD30FGYDZ]] below $\varepsilon_0$, which is primitive recursive and has type $\varepsilon_0$.
For each tower $\omega_n$, defined by
$$\omega_0 = 1, \qquad \omega_{n+1} = \omega^{\omega_n},$$
[[transfinite induction in arithmetic|ZE54ABPMJ0]] gives a PA-proof of induction along $\prec$ restricted to the notations below $\omega_n$.
The restricted order is still primitive recursive, and its type is $\omega_n$.
So $\omega_n \le \lvert \mathrm{PA} \rvert$ for every $n$, and the supremum of the towers is $\varepsilon_0$.

The upper bound is the hard half: Gentzen showed that PA does not prove induction along the full order, and cut elimination shows that no other primitive recursive well-order of type $\varepsilon_0$ or more is provable either.
This is the typical shape of an analysis: a natural notation system for the lower bound and a proof-theoretic argument about all orders for the upper bound.

### L3 human

The proof-theoretic ordinal measures the $\Pi^1_1$ part of a theory, the sentences "$\prec$ is well-founded" that it proves.
Other measures look at other parts: the $\Pi^0_2$ ordinal at the provably total functions, and $\Pi^1_2$ ordinals at stronger consequences.
Beyond the [[Bachmann-Howard ordinal|QH3ENXFRSV]] the values are written with [[collapsing functions|8S6CT4TMB7]], up to theories such as [[Π¹₁-comprehension|2MGJJTSRFD]].
The ordinal analysis of full second-order arithmetic is an open problem.
