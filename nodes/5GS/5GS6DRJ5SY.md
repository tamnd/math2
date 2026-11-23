---
tag: 5GS6DRJ5SY
kind: statement
role: axiom
name: Comprehension schema
aliases: [comprehension-schema-second-order, comprehension-axiom]
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
audience: grad
about: [G6X7SZSNC5, KWEJFK5943]
uses: [G6X7SZSNC5, 47XHPD8XE2]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Deductive systems
  - url: https://en.wikipedia.org/wiki/Axiom_schema_of_specification
    locator: In higher-order settings
  - url: https://en.wikipedia.org/wiki/Impredicativity
    locator: History
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Arithmetical comprehension
---

## Statement

Let $L$ be a signature of [[second-order logic|G6X7SZSNC5]].
Let $n \ge 1$, let $X$ be an $n$-ary relation variable, and let $x_1, \ldots, x_n$ be distinct individual variables.
Let $\varphi$ be a formula in which $X$ is not free.
The comprehension axiom for $X$ and $\varphi$ is the universal closure of
$$\exists X \, \forall x_1 \cdots \forall x_n \, \big( X(x_1, \ldots, x_n) \leftrightarrow \varphi \big).$$
The universal closure quantifies the free variables of $\varphi$ other than $x_1, \ldots, x_n$.
These variables are the parameters, and they can be individual or relation variables.
The comprehension schema is the set of all comprehension axioms, for all $n$, $X$ and $\varphi$.
An instance is predicative when $\varphi$ contains no quantifier over relation variables, and impredicative otherwise.

## Remarks

### What the axiom says

The axiom says that the formula $\varphi$ defines an $n$-ary relation, and that this relation is a possible value of the variable $X$.
For example, over $\set{0, S}$, the instance for $\varphi(x) := \neg x = 0$ is
$$\exists X \, \forall x \, \big( X(x) \leftrightarrow \neg x = 0 \big),$$
and in $\mathbb{N}$ its witness is the set $\set{1, 2, 3, \ldots}$ of successors.

In the full semantics every instance is valid.
Fix a structure with domain $M$ and values of the parameters.
The set $A = \set{\bar{a} \in M^n : \varphi \text{ holds at } \bar{a}}$ is a subset of $M^n$, so $X = A$ is allowed.
Then $X(\bar{x}) \leftrightarrow \varphi$ holds for every $\bar{x}$, and the [[example on full structures|J5YH6PWPDX]] gives these steps in detail.
In the [[Henkin semantics|KWEJFK5943]] the schema is not automatic.
It is the condition that a general structure must satisfy to be a Henkin model.

### Why each condition is needed

The variable $X$ must not be free in $\varphi$.
For $\varphi := \neg X(x)$, the formula $\exists X \, \forall x \, (X(x) \leftrightarrow \neg X(x))$ is false in every structure, because the domain is not empty.

The parameters must be allowed.
Without them, [[a general structure on two points can satisfy all instances but omit the set $\set{0}$|PPTAB8J099]].
In that structure, $\forall X \, (X(x) \to X(y))$ no longer defines equality.

### Comprehension as an instantiation rule

A deductive system for second-order logic has the first-order rules for both kinds of quantifiers, and the comprehension schema as axioms.
The quantifier rules alone let us instantiate $\forall X \, \psi$ only by another relation variable.
With comprehension, we can instantiate by a formula: from $\forall X \, \psi$ we derive $\psi[\varphi / X]$.
In $\psi[\varphi / X]$, each atomic formula $X(t_1, \ldots, t_n)$ becomes $\varphi(t_1, \ldots, t_n)$.
The derivation takes three steps.

1. Comprehension gives a relation $X$ with $\forall \bar{x} \, (X(\bar{x}) \leftrightarrow \varphi)$.
2. The premise $\forall X \, \psi$ gives $\psi$ for this $X$.
3. Replacement of equivalents turns each $X(\bar{t})$ in $\psi$ into $\varphi(\bar{t})$, and this gives $\psi[\varphi / X]$.

So comprehension is the second-order form of the rule "a universal statement holds for each instance".

### What follows from it

The second-order induction axiom implies each instance of the first-order induction schema.
Instantiate $X$ by the formula of the instance, as the L2 explanation does.

The formula $\forall X \, (X(x) \to X(y))$ implies $x = y$.
Instantiate $X$ by the formula $z = x$, with the parameter $x$: then $x = x$ gives $y = x$.

In [[Frege's theorem|J36EHBHF6J]], the definitions of the number concepts, such as the concept "natural number", use impredicative instances.

### Predicative and impredicative instances

An impredicative instance defines a relation by a quantifier over all relations, and the new relation is one of them.
For example, this instance defines the least set that contains $0$ and is closed under $S$:
$$\exists N \, \forall x \, \Big( N(x) \leftrightarrow \forall X \, \big( (X(0) \land \forall y \, (X(y) \to X(S(y)))) \to X(x) \big) \Big).$$
Poincaré and Russell objected to such definitions as circular.
Weyl developed a part of analysis with [[predicative|AWWS4VDNQX]] definitions only.
In [[second-order arithmetic|DC60FYCSPM]], comprehension for formulas without set quantifiers gives the subsystem of arithmetical comprehension.
The full schema gives the full system.

### Comprehension and set-theoretic separation

In set theory, the unrestricted schema $\exists B \, \forall x \, (x \in B \leftrightarrow \varphi)$ is inconsistent.
The formula $x \notin x$ gives [[Russell's paradox|0HESMMSYEG]].
Zermelo's separation schema restricts it to the elements of a given set $A$: $\exists B \, \forall x \, (x \in B \leftrightarrow x \in A \land \varphi)$.
Second-order comprehension is close to separation with $A$ equal to the domain, because $X$ is always a relation on the domain.
It is consistent because $X$ is not an individual, so $X(X)$ is not a formula, and Russell's argument cannot start.
Frege's Basic Law V gave every concept an object as its extension, and this brought the paradox back.
In class theories, [[von Neumann-Bernays-Gödel set theory|JTPZ1HZ9KK]] has class comprehension for formulas that quantify only over sets.
Morse-Kelley set theory has it for all formulas.

## History

Frege's logic of 1879 used concepts defined by formulas.
Russell reported his paradox to Frege in a letter of 1902.
Zermelo introduced the separation schema in his axioms for set theory in 1908.
Weyl's predicative analysis appeared in his book "Das Kontinuum" in 1918.

## Explanations

### L1 human

The comprehension rule says that every property that we can write down describes a set.
For example, on the numbers $1$ to $10$, the property "is even" describes the set $\set{2, 4, 6, 8, 10}$.
So a statement about "every set" also applies to the set of even numbers.
The rule has one limit: the property must not mention the set that it describes.
A property such as "is not in this very set" would describe nothing, so the rule forbids it.

### L2 human

We derive one instance of the first-order induction schema from the second-order induction axiom (P3) and comprehension.
Let $\varphi(x) := x + 0 = x$, in the signature $\set{0, S, +}$.

1. (P3) is $\forall X \, \big( (X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x) \big)$.
2. Comprehension gives a set $X$ with $\forall x \, (X(x) \leftrightarrow x + 0 = x)$, since $X$ is not free in $\varphi$.
3. (P3) for this $X$ gives $(X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x)$.
4. Replace each $X(t)$ by $t + 0 = t$, using step 2.
   This gives the following sentence:
   $$\big(0 + 0 = 0 \land \forall x \, (x + 0 = x \to S(x) + 0 = S(x))\big) \to \forall x \, (x + 0 = x).$$
5. Step 4 is the instance of the first-order induction schema for $\varphi$.

Check: the base case of step 4 is $\varphi(0)$, and the step case is $\varphi(x) \to \varphi(S(x))$, as the schema requires.

The typical use of comprehension is exactly this: to apply a statement about all sets to a set given by a formula.
The trap is to apply it to a formula in which $X$ is free, as in "Why each condition is needed".

### L3 human

Comprehension is the logical core of second-order logic.
The quantifier rules are the first-order rules, and the schema decides which relations exist.
Its strength is graded by the complexity of the allowed formulas.
This grading is the backbone of the subsystems of second-order arithmetic in reverse mathematics.
In higher-order logic and type theory, the same schema appears at every type.
In Church's system it becomes $\lambda$-abstraction: the term $\lambda \bar{x} . \varphi$ names the relation directly.
In set theory, the same idea, cut down to separation, lets Zermelo's axioms avoid the known paradoxes.
