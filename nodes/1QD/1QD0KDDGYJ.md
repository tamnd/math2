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

The induction schema of first-order arithmetic is the infinite set of axioms $\mathrm{Ind}_\varphi$, one for each [[formula|HYJ10AF6RT]] $\varphi(x, \vec{y})$ of the [[language of arithmetic|D8SD54M5PN]].
The axiom $\mathrm{Ind}_\varphi$ says: if $\varphi$ holds at $0$, and passes from each $x$ to $S x$, then it holds at every $x$, for every value of the parameters $\vec{y}$.
It is the first-order form of [[mathematical induction|0ASJVEFA9J]].
The [[definition page|G55NMADJ6G]] gives the exact sentence.
Adding the schema to [[Robinson arithmetic|3K1AKGXF8A]] gives [[Peano arithmetic|HACXBCM7SS]], and restricting it to a class of formulas gives the [[fragments of PA|T70PYM1F36]].

## Motivation

The principle of induction says that every set of numbers that contains $0$ and is closed under successor contains all numbers.
That is a statement about all sets of numbers, and a first-order theory of numbers cannot quantify over sets.
The schema replaces "every set" by "every set defined by a formula".
This keeps the theory first-order, with a complete proof system and a decidable set of axioms.
The price is that the schema says nothing about sets that no formula defines.

## Notation

$\mathrm{Ind}_\varphi$ is the induction axiom for $\varphi$, with induction variable $x$ and parameters $\vec{y}$.
For a class $\Gamma$ of formulas, $\mathrm{I}\Gamma$ denotes the set of $\mathrm{Ind}_\varphi$ for $\varphi \in \Gamma$, or the theory $\mathsf{Q}$ plus this set; for example $\mathsf{I}\Sigma_1$ and $\mathsf{I}\Delta_0$.
Some books write the schema with the abbreviations $\varphi(0)$ and $\varphi(x')$, and some call it the induction scheme.

## Remarks

### Examples

- The instance for $\varphi(x, y) := x + y = y + x$, used three times in [[this example|DE8YZ5SDH3]], proves that addition is commutative in $\mathsf{PA}$.
- The instance for the open formula $\varphi(x) := S x \ne x$ proves $\forall x\,(S x \ne x)$; [[this example|855J8368AM]] gives the proof, and shows that $\mathsf{Q}$ without the schema cannot.
- For the $\Sigma_1$ formula $\varphi(x) := \exists y\,(x = y + y \lor x = S(y + y))$, the instance gives "every number is even or odd"; the [[Peano arithmetic|HACXBCM7SS]] page carries it out.

### Non-examples

- The second-order induction axiom $\forall X\,\bigl((X(0) \land \forall x\,(X(x) \to X(S x))) \to \forall x\, X(x)\bigr)$ is not an instance of the schema; [[this non-example|Y2S28SPR3R]] shows the difference in strength.
- The rule "from $\varphi(0)$ and $\varphi(x) \to \varphi(S x)$ infer $\varphi(x)$" is not the same as the schema in weak theories. For restricted classes $\Gamma$, such as $\Sigma_1$, the rule form is strictly weaker than $\mathrm{I}\Gamma$.

### Basic properties

- Each instance $\mathrm{Ind}_\varphi$ is true in $\mathfrak{N}$, since the set it talks about is a subset of $\N$.
- Over $\mathsf{Q}$, the schema for all formulas proves the least number principle and strong induction for all formulas.
- For each $n$, the theories $\mathsf{I}\Sigma_n$ and $\mathsf{I}\Pi_n$ have the same theorems.
- The schema has infinitely many instances, and no finite subset of it axiomatizes $\mathsf{PA}$ over $\mathsf{Q}$.
- The schema has non-standard models: in a non-standard model of $\mathsf{PA}$ the set of standard elements contains $0$ and is closed under $S$, but it is not definable, so no instance applies to it.

### History

Dedekind and Peano stated induction for arbitrary sets.
Skolem (1923) used induction on quantifier-free formulas in his [[primitive recursive arithmetic|WCXH72T8D8]].
Skolem (1934) also built a non-standard model of first-order arithmetic, which showed that the first-order schema cannot pin down $\N$.

### Common errors

- To think that the schema has one axiom. It has one axiom for each formula.
- To forget the parameters $\vec{y}$. Induction on $x$ for $x + y = y + x$ needs $y$ as a parameter.
- To think that a model of the schema is standard. Non-standard models satisfy every instance.

## Explanations

### L1 human

Induction is the domino principle: if the first domino falls, and each falling domino knocks over the next, then all dominoes fall.
In first-order arithmetic we cannot say "for every property".
So we write one induction rule for each property that we can express by a formula.
This infinite list of rules is the induction schema.

### L2 human

We write the instance of the schema that proves $\forall x\,(0 + x = x)$.

1. Let $\varphi(x)$ be $0 + x = x$. It has no parameters.
2. $\varphi(0)$ is $0 + 0 = 0$, an instance of $\mathsf{Q}4$.
3. $\varphi(x) \to \varphi(S x)$: from $0 + x = x$, $\mathsf{Q}5$ gives $0 + S x = S(0 + x) = S x$.
4. So $\mathrm{Ind}_\varphi$, which is $(\varphi(0) \land \forall x\,(\varphi(x) \to \varphi(S x))) \to \forall x\, \varphi(x)$, yields $\forall x\,(0 + x = x)$.

The typical use of the schema is exactly this: choose $\varphi$, check the base and the step, and apply $\mathrm{Ind}_\varphi$.
A trap is to choose $\varphi$ too weak, so that the step fails; the commutativity proof needs the parameter $y$ in $\varphi$.

### L3 human

Restricting the schema to classes $\Sigma_n$ gives the hierarchy $\mathsf{I}\Sigma_0 \subseteq \mathsf{I}\Sigma_1 \subseteq \mathsf{I}\Sigma_2 \subseteq \cdots$, whose union is $\mathsf{PA}$.
The inclusions are strict: $\mathsf{I}\Sigma_{n+1}$ proves the consistency of $\mathsf{I}\Sigma_n$.
Related schemas are collection $\mathsf{B}\Sigma_n$, the least number principle and the order induction principle.
Over a weak base they form a fine hierarchy: $\mathsf{I}\Sigma_{n+1} \vdash \mathsf{B}\Sigma_{n+1}$, and $\mathsf{B}\Sigma_{n+1} \vdash \mathsf{I}\Sigma_n$.
In second-order arithmetic the schema becomes a single axiom plus comprehension, and the strength moves into the comprehension schema.
