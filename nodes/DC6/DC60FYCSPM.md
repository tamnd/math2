---
tag: DC60FYCSPM
kind: concept
name: Second-order arithmetic
msc: ["03F35", "03B30"]
topics: [BY8AAFN7C5]
audience: grad
uses: [D8SD54M5PN, 3K1AKGXF8A, 1QD0KDDGYJ, 5GS6DRJ5SY, G6X7SZSNC5, P0H5NYX8Z0, HACXBCM7SS]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Models
same_as:
  wikidata: Q7442973
  wikipedia: Second-order arithmetic
---

## Summary

Second-order arithmetic $\mathsf{Z}_2$ is a first-order theory with two sorts of variables: number variables, which range over natural numbers, and set variables, which range over sets of natural numbers.
Its language has $0$, $1$, $+$, $\cdot$, $<$ on numbers and the membership relation $n \in X$.
Its axioms are the basic axioms for $0$, $1$, $+$, $\cdot$ and $<$ in the style of [[Robinson arithmetic|3K1AKGXF8A]], the induction axiom for sets, and the [[comprehension schema|5GS6DRJ5SY]] $\exists X\, \forall n\, (n \in X \leftrightarrow \varphi(n))$ for every formula $\varphi$ of the language in which $X$ is not free.
The [[definition page|Y92NXGEQBD]] states the axioms in full.
A model is a pair of a structure for the numbers and a family of subsets of its domain; an $\omega$-model is a model whose numbers are the standard natural numbers.
Real numbers, functions and countable structures can be coded as sets of numbers, so $\mathsf{Z}_2$ and its subsystems can state and prove most theorems of ordinary analysis and countable algebra.
This makes $\mathsf{Z}_2$ the common frame of [[reverse mathematics|7SQS69T17R]].

## Motivation

[[Peano arithmetic|HACXBCM7SS]] speaks only about single numbers, and a real number is an infinite object.
To speak about real numbers, continuous functions and countable groups, a theory must quantify over infinite sets of numbers.
Full set theory can do this, but it assumes far more than analysis uses.
Hilbert and Bernays observed that most of analysis needs only sets of natural numbers.
A real number is a sequence of rationals, a sequence is a set of pairs, and a continuous function on the reals is determined by countably many rational data.
Second-order arithmetic is the smallest natural theory with sets of numbers and with comprehension for all its formulas.
Its subsystems, with comprehension and induction for restricted classes of formulas, measure how much of this set existence a given theorem uses.

## Notation

The language is written $L_2$.
Lower-case letters $i, j, k, m, n, x, y$ are number variables, and upper-case letters $X, Y, Z$ are set variables.
A formula is arithmetical when it has no set quantifiers; free set variables are allowed as parameters.
The classes $\Sigma^0_n$ and $\Pi^0_n$ are the [[classes of arithmetical formulas|GE43CSZTS9]] by number quantifiers, now with atomic formulas $t \in X$.
The classes $\Sigma^1_n$ and $\Pi^1_n$ count alternations of set quantifiers in front of an arithmetical formula.
A structure for $L_2$ is written $(M, \mathcal{S})$, where $M$ interprets the number sort and $\mathcal{S}$ is a family of subsets of the domain of $M$.
An $\omega$-model is written $(\N, \mathcal{S})$, or only $\mathcal{S}$, with $\mathcal{S} \subseteq \mathcal{P}(\N)$.
Some books write $\mathsf{Z}_2$ as $\mathsf{PA}_2$ or as "analysis", and some use a function sort in place of a set sort.
A subscript $0$, as in $\mathsf{ACA}_0$, means that induction is the single set induction axiom, not the schema for all formulas.

## Remarks

### Examples

- The full structure $(\N, \mathcal{P}(\N))$ is a model of $\mathsf{Z}_2$; [[this example|~9a3df793]] checks the axioms.
- The square root of $2$ is coded by the set of its binary truncations, and the coding takes place inside $\mathsf{Z}_2$; [[this example|~aa7e8c21]] gives the numbers.
- For each $\omega$-model $\mathcal{S}$ of $\mathsf{Z}_2$, every set definable in $(\N, \mathcal{S})$ with parameters from $\mathcal{S}$ lies in $\mathcal{S}$, by comprehension. So the arithmetical sets lie in every $\omega$-model.
- The theory $\mathsf{ACA}_0$ of [[arithmetical comprehension|~08f6623a]] is a subsystem: it keeps the basic axioms and set induction, and it restricts comprehension to arithmetical formulas.

### Non-examples

- The family of [[computable sets|PPGD5KW8JC]] does not give a model of $\mathsf{Z}_2$: the comprehension instance for the halting set fails; [[this non-example|~a21f55cb]] gives the details.
- [[Peano arithmetic|HACXBCM7SS]] is not second-order arithmetic: its language has no set variables, so it cannot state comprehension. Its theorems are exactly the theorems of $\mathsf{ACA}_0$ without set variables, by [[this example|HPA6HX3114]].
- Full [[second-order logic|G6X7SZSNC5]] with the second-order Peano axioms is not the theory $\mathsf{Z}_2$. The theory $\mathsf{Z}_2$ is read with [[Henkin semantics|P0H5NYX8Z0]], so it has models $(M, \mathcal{S})$ with $\mathcal{S} \ne \mathcal{P}(M)$.

### Basic properties

- Full induction. With comprehension, the induction axiom gives the induction scheme for every $L_2$ formula: take the set defined by the formula and apply the axiom.
- Peano arithmetic. So every axiom of [[Peano arithmetic|HACXBCM7SS]] is a theorem of $\mathsf{Z}_2$, and $\mathsf{Z}_2$ proves the consistency of $\mathsf{PA}$.
- Incompleteness. $\mathsf{Z}_2$ has a computable set of axioms and contains $\mathsf{PA}$, so the [[first incompleteness theorem|X9WYNYE29C]] applies: if $\mathsf{Z}_2$ is consistent, some arithmetical sentence is undecided by it.
- Non-standard models. Since $\mathsf{Z}_2$ is a first-order theory, the [[compactness theorem|1NR3HAWG9D]] gives models whose numbers are not the standard natural numbers.
- Countable models. By the downward Löwenheim-Skolem theorem, $\mathsf{Z}_2$ has countable $\omega$-models; in them $\mathcal{S}$ is a countable family of sets.
- Five subsystems. The subsystems $\mathsf{RCA}_0$, $\mathsf{WKL}_0$, $\mathsf{ACA}_0$, $\mathsf{ATR}_0$ and $\Pi^1_1\text{-}\mathsf{CA}_0$ are listed on the page on [[reverse mathematics|7SQS69T17R]].

### History

Hilbert and Bernays developed a large part of analysis in a system of this kind in the second volume of *Grundlagen der Mathematik* (1939).
Harvey Friedman introduced the study of its subsystems with restricted comprehension and induction in the 1970s.
Stephen Simpson's book *Subsystems of Second Order Arithmetic* (first edition 1999) became the standard reference.

### Common errors

- The name suggests second-order logic, but $\mathsf{Z}_2$ is a two-sorted first-order theory, and the completeness theorem holds for it.
- An $\omega$-model fixes the numbers, not the sets: $(\N, \mathcal{S})$ with $\mathcal{S} \ne \mathcal{P}(\N)$ is still an $\omega$-model.
- A subsystem with subscript $0$ has only the set induction axiom. It proves induction only for the formulas whose sets it can form.

## Explanations

### L1 human

Ordinary arithmetic talks about whole numbers, such as $3$ and $17$.
Second-order arithmetic also talks about sets of whole numbers, such as the set of all even numbers.
A real number such as $\sqrt 2$ can be stored as a set of whole numbers: we store its decimal or binary digits.
In this way the theory can talk about real numbers, sequences and functions.
Its main axiom says: for each property that the language can state, the numbers with that property form a set.
Most of calculus can be done inside this theory.

### L2 human

We use comprehension and induction to prove one fact.

1. Claim: $\mathsf{Z}_2$ proves that every nonempty set $X$ has a least element.
2. Suppose $X$ has no least element. By comprehension, the set $Y = \set{n : \forall m \le n\, (m \notin X)}$ exists.
3. $0 \in Y$: if $0 \in X$, then $0$ is the least element of $X$, a contradiction.
4. If $n \in Y$, then $n + 1 \in Y$: else $n + 1 \in X$, all smaller numbers are outside $X$, and $n + 1$ is least.
5. By the induction axiom for $Y$, every $n$ lies in $Y$, so no $n$ lies in $X$, and $X$ is empty.

The typical use of $\mathsf{Z}_2$ is as a frame: we fix a subsystem, and we ask which theorems of analysis it proves.
A trap is to use comprehension for a formula with set quantifiers inside a subsystem that allows only arithmetical formulas.
In step 2 the formula has no set quantifiers, so the same proof works in $\mathsf{ACA}_0$; in $\mathsf{RCA}_0$ the formula $\forall m \le n\,(m \notin X)$ is bounded, so it works there too.

### L3 human

Second-order arithmetic sits between first-order arithmetic and set theory.
Its standard model $(\N, \mathcal{P}(\N))$ carries the same information as the level $V_{\omega+1}$ of the cumulative hierarchy, because $\N$ codes $V_\omega$.
The sets definable in the full model form the [[analytical hierarchy|M6JGF4TPM6]], the lightface version of the projective sets of descriptive set theory.
The subsystems of $\mathsf{Z}_2$ form the measuring scale of [[reverse mathematics|7SQS69T17R]], and their $\omega$-models are families of sets closed under computability-theoretic operations, such as Turing ideals for $\mathsf{RCA}_0$ and jump ideals for $\mathsf{ACA}_0$.
The [[proof-theoretic ordinals|C72RBH0CDR]] of many subsystems are known, including $\Pi^1_1\text{-}\mathsf{CA}_0$, and an ordinal analysis of full $\mathsf{Z}_2$ is an open problem.
