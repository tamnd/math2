---
tag: K40YJX8K1G
kind: definition
name: Higher-order logic
msc: ["03B16", "03B15"]
topics: [MDHDYV8QZW]
audience: grad
defines: P1ABGYRQXH
uses: [086QKPF0A6, 983GZBQYT4, 00E0YZCERH, 09CEDJYBKP, G6X7SZSNC5, ~abb2cff1]
sources:
  - url: https://en.wikipedia.org/wiki/Higher-order_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Higher-order_logic
    locator: Semantics
  - url: https://en.wikipedia.org/wiki/Higher-order_logic
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Type_theory
    locator: lead section
---

## Definition

The relational types are defined inductively.

1. $\iota$ is a type, the type of individuals.
2. If $\tau_1, \dots, \tau_n$ are types with $n \ge 1$, then $(\tau_1, \dots, \tau_n)$ is a type, the type of $n$-ary relations between objects of types $\tau_1, \dots, \tau_n$.

Higher-order logic over a signature $L$ has, for each type $\tau$, variables of type $\tau$ and quantifiers $\forall$ and $\exists$ over them.
The symbols of $L$ and the terms are as in [[first-order logic|086QKPF0A6]], and every term has type $\iota$.
Its formulas are built as in first-order logic, with one more kind of atomic formula: $X(t_1, \dots, t_n)$, whenever $X$ has type $(\tau_1, \dots, \tau_n)$ and each $t_i$ is a variable of type $\tau_i$, or a term when $\tau_i = \iota$.

In the standard semantics over an $L$-[[structure|983GZBQYT4]] with domain $M$, the domains $D_\tau$ are given by $D_\iota = M$ and $D_{(\tau_1, \dots, \tau_n)} = \mathcal{P}(D_{\tau_1} \times \dots \times D_{\tau_n})$.
Here $\mathcal{P}$ is the [[power set|00E0YZCERH]] and $\times$ the [[Cartesian product|09CEDJYBKP]].
A variable of type $\tau$ ranges over $D_\tau$, and $X(t_1, \dots, t_n)$ is true when the tuple of the values of $t_1, \ldots, t_n$ belongs to the value of $X$.

In the Henkin semantics, a model gives a domain $D_\tau \subseteq \mathcal{P}(D_{\tau_1} \times \dots \times D_{\tau_n})$ for each relational type $\tau = (\tau_1, \ldots, \tau_n)$, and these domains must satisfy every instance of the comprehension schema, as in the [[Henkin semantics|~abb2cff1]] of second-order logic.

The order of a type is $1$ for $\iota$, and one more than the largest order of $\tau_1, \dots, \tau_n$ for $(\tau_1, \dots, \tau_n)$.
The logic of order $k$ allows variables only of types whose order is at most $k$.

## Notation

Variables of type $\iota$ are written $x, y, z$, variables of type $(\iota, \ldots, \iota)$ are written $X, Y, Z$, and variables of higher types are often written in script letters such as $\mathcal{X}$.
Some books write $0$ for the type $\iota$ and $(\tau_1, \ldots, \tau_n)$ as $\langle \tau_1, \ldots, \tau_n \rangle$.
Church's simple theory of types uses function types $\sigma \to \tau$ and a type $o$ of truth values instead, and a relation of type $(\tau)$ there is a function of type $\tau \to o$.
The abbreviation HOL is common, and it also names proof assistants that implement Church's system.

## Remarks

### Orders

[[First-order logic|086QKPF0A6]] is the logic of order $1$, and [[second-order logic|G6X7SZSNC5]] is the logic of order $2$.
The type $((\iota))$ has order $3$, so its variables range over sets of subsets of the domain, and they belong to third-order logic.
The type $(\iota, (\iota))$ also has order $3$: its variables range over relations between individuals and sets of individuals.

### Examples

- The sentence $\forall \mathcal{X} \, \exists Y \, \forall x \, (Y(x) \leftrightarrow \exists Z \, (\mathcal{X}(Z) \land Z(x)))$, with $\mathcal{X}$ of type $((\iota))$, says that [[every family of sets has a union|~646a5193]]. It is valid in the standard semantics.
- In third-order logic, [[equality of sets is definable|~89fbded5]] by $\forall \mathcal{Z} \, (\mathcal{Z}(X) \to \mathcal{Z}(Y))$, one order above the second-order definition $\forall X \, (X(x) \to X(y))$ of equality of individuals.
- Every second-order sentence is a higher-order sentence, with the same meaning in each semantics.

### Non-examples

- [[The expression $X(X)$ is not a formula|~a334b103]], because no type $\tau$ equals the type $(\tau)$.
- A formula with a variable that ranges over all objects of all types at once is not a formula of higher-order logic; each variable has exactly one type.

### No complete proof system for the standard semantics

Second-order logic is a part of higher-order logic, and a second-order sentence has the same meaning in both.
In the standard semantics, the valid second-order sentences do not form a computably enumerable set, as the page on [[second-order logic|G6X7SZSNC5]] shows.
So the valid higher-order sentences do not form a computably enumerable set either, and no effective proof system is sound and complete for them.
With the Henkin semantics there is a sound and complete proof system, as Henkin proved in 1950.

### Reduction to second order

Hintikka showed in 1955 that each higher-order sentence $\varphi$ has a second-order sentence $\varphi^*$ that is satisfiable exactly when $\varphi$ is satisfiable, in the standard semantics.
Then $\varphi$ is valid exactly when $\neg (\neg \varphi)^*$ is valid.
The idea is that second-order logic can describe the power set of a set up to isomorphism.
A second-order sentence can say that a part $B$ of the domain, with a binary relation $E$, is extensional and contains, for each subset $X$ of a part $A$, an element $b$ with $\set{a : E(a, b)} = X$.
Then $B$ is a copy of $\mathcal{P}(A)$, and quantifiers over $\mathcal{P}(A)$ become quantifiers over elements of $B$.
Repeating this step codes every finite type by individuals and second-order quantifiers.
So, for the standard semantics, second-order logic already has the full strength of higher-order logic.

### Type theory

Higher-order logic with function types is Church's simple theory of types of 1940, based on the [[simply typed lambda calculus|2DP940895E]].
It was a simplification of the ramified type theory of Whitehead and Russell, and the simplification was proposed by Chwistek and by Ramsey.
This form belongs to [[type theory|Q48KGV33AH]]; this page treats higher-order logic as an extension of first-order logic.

## Explanations

### L1 human

Higher-order logic sorts all objects into levels.
The bottom level holds the individuals, for example the numbers $1, 2, 3$.
The next level holds sets of individuals, for example $\set{1, 2}$, and the level above holds collections of such sets, for example $\set{\set{1}, \set{1, 2}}$.
A variable lives on one level, and a statement may only say that an object belongs to an object one level up.
This rule blocks paradoxes such as a set that belongs to itself.

### L2 human

We compute the orders of some types and the domains of the standard semantics over $M = \set{1, 2}$.

1. The type $\iota$ has order $1$, and $D_\iota = \set{1, 2}$ has $2$ elements.
2. The type $(\iota)$ has order $2$, and $D_{(\iota)} = \mathcal{P}(\set{1, 2})$ has $2^2 = 4$ elements.
3. The type $(\iota, \iota)$ has order $2$, and $D_{(\iota, \iota)} = \mathcal{P}(M \times M)$ has $2^4 = 16$ elements.
4. The type $((\iota))$ has order $3$, and $D_{((\iota))} = \mathcal{P}(D_{(\iota)})$ has $2^4 = 16$ elements.
5. The type $(\iota, (\iota))$ has order $3$, and $D_{(\iota, (\iota))} = \mathcal{P}(M \times D_{(\iota)})$ has $2^{2 \cdot 4} = 256$ elements.

The typical use of the order is to say how far a sentence climbs above the individuals, for example in the statement that a theory is third-order.
The trap is the two types in steps 3 and 4: both domains have $16$ elements, but the order of $(\iota, \iota)$ is $2$ and the order of $((\iota))$ is $3$.

### L3 human

Higher-order logic is the logic of [[type theory|Q48KGV33AH]], read classically and extensionally.
Its standard semantics fixes each type as a full power set, so it inherits all the dependence of [[second-order logic|G6X7SZSNC5]] on set theory, and by Hintikka's reduction its validity problem reduces to the validity problem of second-order logic.
Its [[Henkin semantics|~abb2cff1]] is a many-sorted first-order logic with one sort for each type, so it is complete and compact.
In categorical logic, the internal language of a topos is an intuitionistic higher-order logic, and the topos of sets gives the standard semantics.
Proof assistants such as Isabelle/HOL and HOL4 implement Church's version.
