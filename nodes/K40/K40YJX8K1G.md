---
tag: K40YJX8K1G
kind: definition
name: Higher-order logic
msc: ["03B16", "03B15"]
topics: [MDHDYV8QZW]
audience: grad
defines: P1ABGYRQXH
uses: [086QKPF0A6, 983GZBQYT4, 00E0YZCERH, 09CEDJYBKP, G6X7SZSNC5, KWEJFK5943]
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

Higher-order logic gives each variable a type, and a variable of a higher type ranges over relations between objects of lower types.

The relational types are defined inductively.

1. $\iota$ is a type, the type of individuals.
2. If $\tau_1, \dots, \tau_n$ are types with $n \ge 1$, then $(\tau_1, \dots, \tau_n)$ is a type, the type of $n$-ary relations between objects of types $\tau_1, \dots, \tau_n$.

Higher-order logic over a signature $L$ has, for each type $\tau$, variables of type $\tau$ and quantifiers $\forall$ and $\exists$ over them.
The symbols of $L$ and the terms are as in [[first-order logic|086QKPF0A6]], and every term has type $\iota$.
The formulas are built as in first-order logic, with one more kind of atomic formula, $X(t_1, \dots, t_n)$.
It is allowed when $X$ has type $(\tau_1, \dots, \tau_n)$ and each $t_i$ has type $\tau_i$.
Here $t_i$ is a variable of type $\tau_i$, or a term when $\tau_i = \iota$.

Let $M$ be the domain of an $L$-[[structure|983GZBQYT4]].
In the standard semantics, the domains $D_\tau$ are $D_\iota = M$ and $D_{(\tau_1, \dots, \tau_n)} = \mathcal{P}(D_{\tau_1} \times \dots \times D_{\tau_n})$.
Here $\mathcal{P}$ is the [[power set|00E0YZCERH]] and $\times$ is the [[Cartesian product|09CEDJYBKP]].
A variable of type $\tau$ ranges over $D_\tau$.
The formula $X(t_1, \dots, t_n)$ is true when the tuple of the values of $t_1, \ldots, t_n$ belongs to the value of $X$.

In the Henkin semantics, a model gives a domain $D_\tau \subseteq \mathcal{P}(D_{\tau_1} \times \dots \times D_{\tau_n})$ for each relational type $\tau = (\tau_1, \ldots, \tau_n)$.
These domains must satisfy every instance of the comprehension schema, as in the [[Henkin semantics|KWEJFK5943]] of second-order logic.

The order of $\iota$ is $1$.
The order of $(\tau_1, \dots, \tau_n)$ is one more than the largest order of $\tau_1, \dots, \tau_n$.
The logic of order $k$ allows variables only of types whose order is at most $k$.

## Notation

We write variables of type $\iota$ as $x, y, z$, and variables of type $(\iota, \ldots, \iota)$ as $X, Y, Z$.
Variables of higher types are often script letters such as $\mathcal{X}$.
Some books write $0$ for the type $\iota$, and $\langle \tau_1, \ldots, \tau_n \rangle$ for $(\tau_1, \ldots, \tau_n)$.
Church's simple theory of types uses function types $\sigma \to \tau$ and a type $o$ of truth values instead.
There, a relation of type $(\tau)$ is a function of type $\tau \to o$.
The abbreviation HOL is common, and it also names proof assistants that implement Church's system.

## Remarks

### Counting orders

[[First-order logic|086QKPF0A6]] is the logic of order $1$, and [[second-order logic|G6X7SZSNC5]] is the logic of order $2$.
To find the order of a type, we work from the inside out.
For the type $(\iota, (\iota))$ of relations between individuals and sets of individuals, we get:
$$\operatorname{ord}((\iota, (\iota))) = 1 + \max(\operatorname{ord}(\iota), \operatorname{ord}((\iota))) = 1 + \max(1, 2) = 3.$$
Check: $(\iota)$ has order $1 + 1 = 2$, so the maximum is $2$ and the result is $3$.
The type $((\iota))$ also has order $3$, so its variables range over sets of subsets of the domain.
Both types belong to third-order logic.

### Sentences of order three

The following sentence, with $\mathcal{X}$ of type $((\iota))$, says that [[every family of sets has a union|R6ZVGYF5FF]]:
$$\forall \mathcal{X} \, \exists Y \, \forall x \, \big(Y(x) \leftrightarrow \exists Z \, (\mathcal{X}(Z) \land Z(x))\big).$$
It is valid in the standard semantics.

In third-order logic, [[equality of sets is definable|FHN4MS03B7]] by $\forall \mathcal{Z} \, (\mathcal{Z}(X) \to \mathcal{Z}(Y))$.
This is one order above the second-order definition $\forall X \, (X(x) \to X(y))$ of equality of individuals.

Every second-order sentence is also a higher-order sentence, and it has the same meaning in each semantics.

### What it is not

[[The expression $X(X)$ is not a formula|8FVA1VMBSW]], because no type $\tau$ equals the type $(\tau)$.
So Russell's set of all sets that do not belong to themselves cannot even be written down.

A variable that ranges over all objects of all types at once is not a variable of higher-order logic.
Each variable has exactly one type.

### Why no proof system can be complete

Second-order logic is a part of higher-order logic, and a second-order sentence has the same meaning in both.
In the standard semantics, the valid second-order sentences do not form a computably enumerable set, as [[second-order logic|G6X7SZSNC5]] shows.
So the valid higher-order sentences do not form a computably enumerable set either.
Thus no effective proof system is sound and complete for them.
With the Henkin semantics, a sound and complete proof system exists.

### Everything reduces to second order

Each higher-order sentence $\varphi$ has a second-order sentence $\varphi^*$ that is satisfiable exactly when $\varphi$ is, in the standard semantics.
Then $\varphi$ is valid exactly when $\neg (\neg \varphi)^*$ is valid.

The idea is that second-order logic can describe a power set up to isomorphism.
Take a part $A$ of the domain, a part $B$, and a binary relation $E$.
A second-order sentence can say two things.
First, two elements of $B$ with the same $E$-predecessors in $A$ are equal.
Second, for each subset $X$ of $A$ there is an element $b$ of $B$ with $\set{a \in A : E(a, b)} = X$.
Then $B$ is a copy of $\mathcal{P}(A)$, and a quantifier over $\mathcal{P}(A)$ becomes a quantifier over elements of $B$.
We repeat this step for each type.
So, for the standard semantics, second-order logic already has the full strength of higher-order logic.

### Watch out

The order of a type is not the size of its domain.
Over a domain with $2$ elements, $D_{(\iota, \iota)}$ and $D_{((\iota))}$ both have $16$ elements, but their orders are $2$ and $3$.

A claim about validity must name the semantics.
The standard semantics has no complete proof system, and the Henkin semantics has one.

### History

Chwistek and Ramsey proposed the simple theory of types in the 1920s, as a simplification of the ramified type theory of Whitehead and Russell.
Church gave the simple theory of types with function types in 1940, based on the [[simply typed lambda calculus|2DP940895E]].
Henkin proved in 1950 that the theory of types is complete for his general models.
Hintikka proved the reduction to second order in 1955.
The functional form belongs to [[type theory|Q48KGV33AH]], and this node treats higher-order logic as an extension of first-order logic.

### Try it

What is the order of the type $((\iota, \iota), \iota)$?
The type $(\iota, \iota)$ has order $2$, so the answer is $1 + \max(2, 1) = 3$.

Over $M = \set{1, 2, 3}$, how many elements has $D_{((\iota))}$?
$D_{(\iota)}$ has $2^3 = 8$ elements, so $D_{((\iota))}$ has $2^8 = 256$ elements.

Is $\mathcal{X}(x)$ a formula when $\mathcal{X}$ has type $((\iota))$?
No: $\mathcal{X}$ needs an argument of type $(\iota)$, and $x$ has type $\iota$.

## Explanations

### L1 human

Higher-order logic sorts all objects into levels.
The bottom level holds the individuals, for example the numbers $1, 2, 3$.
The next level holds sets of individuals, for example $\set{1, 2}$.
The level above holds collections of such sets, for example $\set{\set{1}, \set{1, 2}}$.
A variable lives on one level, and a statement may only say that an object belongs to an object one level up.
This rule blocks paradoxes such as a set that belongs to itself.

### L2 human

We compute the orders of some types and the domains of the standard semantics over $M = \set{1, 2}$.

1. The type $\iota$ has order $1$, and $D_\iota = \set{1, 2}$ has $2$ elements.
2. The type $(\iota)$ has order $2$, and $D_{(\iota)} = \mathcal{P}(\set{1, 2})$ has $2^2 = 4$ elements.
3. The type $(\iota, \iota)$ has order $2$, and $D_{(\iota, \iota)} = \mathcal{P}(M \times M)$ has $2^4 = 16$ elements.
4. The type $((\iota))$ has order $3$, and $D_{((\iota))} = \mathcal{P}(D_{(\iota)})$ has $2^4 = 16$ elements.
5. The type $(\iota, (\iota))$ has order $3$, and $D_{(\iota, (\iota))} = \mathcal{P}(M \times D_{(\iota)})$ has $2^{2 \cdot 4} = 256$ elements.

We use the order to say how far a sentence climbs above the individuals, for example when we say that a theory is third-order.
The trap is in steps 3 and 4.
Both domains have $16$ elements, but the order of $(\iota, \iota)$ is $2$ and the order of $((\iota))$ is $3$.

### L3 human

Higher-order logic is the logic of [[type theory|Q48KGV33AH]], read classically and extensionally.
Its standard semantics fixes each type as a full power set.
So it inherits all the dependence of [[second-order logic|G6X7SZSNC5]] on set theory.
By Hintikka's reduction, its validity problem reduces to the validity problem of second-order logic.
Its [[Henkin semantics|KWEJFK5943]] is a many-sorted first-order logic with one sort for each type, so it is complete and compact.
In categorical logic, the internal language of a topos is an intuitionistic higher-order logic, and the topos of sets gives the standard semantics.
Proof assistants such as Isabelle/HOL and HOL4 implement Church's version.
