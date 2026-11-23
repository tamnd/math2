---
tag: 1QD0KDDGYJ
kind: concept
name: Induction schema
aliases: [induction-scheme, first-order-induction-schema]
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
uses: [0ASJVEFA9J, D8SD54M5PN, HYJ10AF6RT, NCDZ969V7X]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section I
    note: adopted
    mention: wikipedia://en/76765067#90AD
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Peano arithmetic as first-order theory
  - book: isbn:9780521857840
inventory: [NXVCYWY1T9]
---

## Summary

The induction schema is the domino principle written in first-order logic, one axiom for each property that a formula can express.
Take the property "$x$ is even or odd", written as the $\Sigma_1$ formula
$$\varphi(x) := \exists y\,(y + y = x \lor S(y + y) = x).$$
Its induction axiom says that if $\varphi(0)$ holds, and $\varphi(x)$ implies $\varphi(S x)$ for every $x$, then $\varphi(x)$ holds for every $x$.
Both premises can be proved, so [[Peano arithmetic|HACXBCM7SS]] concludes that every number is even or odd.

In general, the induction schema of first-order arithmetic is the set of axioms $\mathrm{Ind}_\varphi$, one for each [[formula|HYJ10AF6RT]] $\varphi(x, \vec{y})$ of the [[language of arithmetic|D8SD54M5PN]]:
$$\mathrm{Ind}_\varphi := \forall \vec{y}\, \Bigl( \bigl( \varphi(0, \vec{y}) \land \forall x\,(\varphi(x, \vec{y}) \to \varphi(S x, \vec{y})) \bigr) \to \forall x\, \varphi(x, \vec{y}) \Bigr).$$
The [[definition|G55NMADJ6G]] fixes the details of substitution.

## Motivation

[[Mathematical induction|0ASJVEFA9J]] says that every set of numbers that contains $0$ and is closed under successor contains all numbers.
That is a statement about all sets of numbers, and a first-order theory of numbers cannot quantify over sets.
The schema replaces "every set" by "every set that a formula defines".
This keeps the theory first-order, with a complete proof system and a decidable set of axioms.

The price is that the schema says nothing about sets that no formula defines.
Adding the full schema to [[Robinson arithmetic|3K1AKGXF8A]] gives Peano arithmetic.
Restricting it to a class of formulas, such as $\Sigma_1$ or $\Delta_0$, gives the [[fragments of PA|T70PYM1F36]], and the strength of each fragment is measured by the formulas it may induct on.

## Notation

We write $\mathrm{Ind}_\varphi$ for the induction axiom of $\varphi$, with induction variable $x$ and parameters $\vec{y}$.
For a class $\Gamma$ of formulas, $\mathsf{I}\Gamma$ is $\mathsf{Q}$ plus $\mathrm{Ind}_\varphi$ for every $\varphi \in \Gamma$, as in $\mathsf{I}\Sigma_1$ and $\mathsf{I}\Delta_0$.
Some books write $\varphi(x')$ for $\varphi(S x)$, and some say "induction scheme".

## Remarks

### The even-or-odd instance worked out

We check the two premises for the formula $\varphi$ of the Summary.
For the base, the witness $y = 0$ works, since $\mathsf{Q}4$ gives
$$0 + 0 = 0.$$
For the step, assume $\varphi(x)$ with a witness $y$.
If $y + y = x$, then $S(y + y) = S x$, so the same $y$ is a witness for $\varphi(S x)$.
If $S(y + y) = x$, then the witness for $S x$ is $S y$, by $\mathsf{Q}5$ and the lemma $S y + y = S(y + y)$:
$$S y + S y = S(S y + y) = S(S(y + y)) = S x.$$
So $\mathrm{Ind}_\varphi$ gives $\forall x\, \varphi(x)$.
Check with $x = 7$: the witness is $y = 3$, since $S(3 + 3) = 7$, and the step gives $y = 4$ for $8$.

The formula has the form $\exists y\, \theta$ with $\theta$ quantifier-free, so this instance belongs already to the fragment $\mathsf{I}\Sigma_1$.

### More instances

The instance for $x + y = y + x$, with parameter $y$, proves that [[addition is commutative|DE8YZ5SDH3]] once two lemmas are in place.
The instance for the open formula $S x \ne x$ proves that [[no number is its own successor|855J8368AM]], a law that $\mathsf{Q}$ cannot prove.
In each case the work is the same: choose $\varphi$, prove the base, prove the step, and apply $\mathrm{Ind}_\varphi$.

### What it is not

The second-order induction axiom
$$\forall X\,\bigl((X(0) \land \forall x\,(X(x) \to X(S x))) \to \forall x\, X(x)\bigr)$$
is one sentence with a set variable, and it is not an instance of the schema.
It pins down $\mathbb{N}$ up to isomorphism, while the schema does not, as [[the compactness argument|Y2S28SPR3R]] shows.

The induction rule, "from $\varphi(0)$ and $\varphi(x) \to \varphi(S x)$ infer $\varphi(x)$", is not the schema either.
A rule applies only to premises that are already theorems, while the axiom can be used under hypotheses.
For restricted classes such as $\Sigma_1$, the rule gives a strictly weaker theory than the schema.

### The first properties

Each instance $\mathrm{Ind}_\varphi$ is true in the standard model, since $\varphi$ defines a subset of $\mathbb{N}$ and ordinary induction holds for every subset.
Over $\mathsf{Q}$, the full schema proves the least number principle and strong induction for every formula.
For each $n$, the theories $\mathsf{I}\Sigma_n$ and $\mathsf{I}\Pi_n$ prove the same sentences; [[this example|JZGV1EK4E9]] gives one direction.
No finite part of the schema axiomatizes $\mathsf{PA}$ over $\mathsf{Q}$, by [[Ryll-Nardzewski's theorem|M5WNB181T7]].

### Watch out

Do not forget the parameters.
To prove $x + y = y + x$ by induction on $x$, the formula must keep $y$ free.
If you first fix $y$ as the numeral $\overline{3}$, you prove only $x + \overline{3} = \overline{3} + x$, and generalizing over $y$ afterwards is not allowed, since $\overline{3}$ is a term, not a variable.

Do not think that a model of the schema is standard either.
In a non-standard model the set of standard elements contains $0$ and is closed under $S$, but no formula defines it, so no instance applies to it.

### History

Dedekind and Peano stated induction for arbitrary sets.
Skolem in 1923 used induction on quantifier-free formulas in his [[primitive recursive arithmetic|WCXH72T8D8]].
Skolem in 1934 built a non-standard model of first-order arithmetic, which showed that the schema cannot pin down $\mathbb{N}$.

### Try it

First, write the instance that proves $\forall x\,(0 \cdot x = 0)$.
It is $\mathrm{Ind}_\varphi$ for $\varphi(x) := 0 \cdot x = 0$, with base $\mathsf{Q}6$ and step $0 \cdot S x = 0 \cdot x + 0 = 0$ by $\mathsf{Q}7$, $\mathsf{Q}4$ and the hypothesis.

Second, in which class is the formula $S x \ne x$?
It has no quantifiers, so it is $\Delta_0$, and its instance is already in $\mathsf{I}\Delta_0$.

## Explanations

### L1 human

Induction is the domino principle: if the first domino falls, and each falling domino knocks over the next, then all dominoes fall.
In first-order arithmetic we cannot say "for every property".
So we write one induction rule for each property that a formula can express.
This infinite list of rules is the induction schema.

### L2 human

We write and use the instance with a parameter that proves $S x + y = S(x + y)$.
Keep $x$ free as a parameter and induct on $y$, with $\psi(y, x) := S x + y = S(x + y)$.
The base $\psi(0, x)$ holds, because $\mathsf{Q}4$ gives both $S x + 0 = S x$ and $x + 0 = x$.
For the step, assume $S x + y = S(x + y)$ and compute with $\mathsf{Q}5$ twice:
$$S x + S y = S(S x + y) = S(S(x + y)) = S(x + S y).$$
So $\mathrm{Ind}_\psi$ gives $\forall x\, \forall y\, \psi(y, x)$.
The typical use of the schema is exactly this: choose $\psi$, check the base and the step, and apply the axiom.
The trap is to induct on the wrong variable.
The axioms $\mathsf{Q}4$ and $\mathsf{Q}5$ only rewrite a sum by its right argument, so the induction must run on $y$.

### L3 human

Restricting the schema to the classes $\Sigma_n$ gives the hierarchy $\mathsf{I}\Delta_0 \subseteq \mathsf{I}\Sigma_1 \subseteq \mathsf{I}\Sigma_2 \subseteq \cdots$, whose union is $\mathsf{PA}$.
The inclusions are strict, because $\mathsf{I}\Sigma_{n+1}$ proves the consistency of $\mathsf{I}\Sigma_n$.
Related schemas are collection $\mathsf{B}\Sigma_n$, the least number principle and order induction.
Over a weak base they interleave: $\mathsf{I}\Sigma_{n+1}$ proves $\mathsf{B}\Sigma_{n+1}$, and $\mathsf{B}\Sigma_{n+1}$ proves $\mathsf{I}\Sigma_n$.
In second-order arithmetic the schema becomes one axiom plus comprehension, and the strength moves into the comprehension schema.
