---
tag: B60DBNF77S
kind: concept
name: Kinds of definitions
aliases: [kinds-of-mathematical-definitions]
msc: ["00A35"]
topics: [BP0WAF23HB]
audience: ug2
uses: [8ZCZ3HW91Z, 0G8VEZ3WTK, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Definition
    locator: Recursive definitions
  - url: https://en.wikipedia.org/wiki/Recursive_definition
    locator: Form of recursive definitions
  - url: https://en.wikipedia.org/wiki/Equivalence_class
    locator: Definition and notation
  - url: https://en.wikipedia.org/wiki/Universal_property
    locator: Existence and uniqueness
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Summary

A [[mathematical definition|8ZCZ3HW91Z]] can give its new term a meaning in several ways, and each way carries its own proof obligation.
An explicit definition states a condition or a formula in known terms.
A recursive definition gives a start value and a rule that computes each value from earlier values.
An inductive definition describes a set as the smallest set that contains some objects and is closed under some rules.
A definition by abstraction takes the [[equivalence classes|0W95W33CMP]] of an [[equivalence relation|0G8VEZ3WTK]] as the new objects.
An axiomatic definition calls every structure that satisfies a list of axioms by the new name.
An implicit definition names the solution of a condition, such as an equation.
A definition by a [[universal property|EN4DD2FAJH]] names an object by the way that maps go into it or out of it.
A definition by construction builds the object from objects that already exist.
The kinds matter because a reader who knows the kind knows which proof makes the definition legal.

## Motivation

The simplest definitions are abbreviations: "even" abbreviates "equal to $2k$ for some integer $k$".
Many objects of mathematics cannot be defined in this way.
The factorial $n!$ needs all the earlier values, so we define it step by step.
The rational number $\tfrac{1}{2}$ is "the same" as $\tfrac{2}{4}$, so we define it as a class of fractions.
The word "group" names infinitely many different structures at once, so we define it by axioms.
The product of two sets is best described by what it does, so category theory defines it by a universal property.
Each of these needs a different justification, and the names of the kinds help to find the right one.

## Notation

1. Explicit definitions use "we say that ... if ..." or the symbol $:=$.
2. Recursive definitions list a base case and a recursive case, often with a brace: $0! := 1$ and $(n + 1)! := (n + 1) \cdot n!$.
3. Classes of an equivalence relation $\sim$ are written $[a]$, $[a]_\sim$ or $\bar a$, and the set of classes of a set $X$ is written $X/{\sim}$.
4. Axiomatic definitions use "A *group* is a pair $(G, \cdot)$ such that the following axioms hold."
5. Definitions by a universal property use "the product of $A$ and $B$ is an object $P$ with maps $p_1, p_2$ such that, for each ..., there is a unique ...".

## Remarks

### The kinds and their proof obligations

| Kind | Example | What must be proved |
|---|---|---|
| explicit | $n$ is even if $n = 2k$ for some integer $k$ | nothing, if the definiens uses only known terms |
| recursive | $0! = 1$, $(n+1)! = (n+1) \cdot n!$ | exactly one function satisfies the recursion (recursion theorem) |
| inductive | the even natural numbers: $0$, and $n + 2$ for each member $n$ | a smallest closed set exists (the intersection of all closed sets) |
| by abstraction | $\mathbb{Q}$ as classes of pairs $(a, b)$ with $b \neq 0$ | the relation is an equivalence relation, and each operation is well defined |
| axiomatic | group, vector space, metric space | nothing for the definition; examples show that the axioms are not empty |
| implicit | $\sqrt{2}$ is the positive real $x$ with $x^2 = 2$ | a solution exists and it is unique |
| universal property | product, quotient, free group | an object with the property exists; uniqueness up to unique isomorphism follows |
| by construction | real numbers as Dedekind cuts | the constructed object has the expected properties |

### Explicit definitions

The definiens is a condition $C(x)$ or a term $t$ in known symbols.
The new term is an abbreviation, so it can always be removed again.
Examples are the [[definition of an even integer|BV6E0ZG3YN]] and the [[definition of divisibility|73TT8GGNBM]].

### Recursive and inductive definitions

A recursive definition of a function $f$ on the [[natural numbers|0MWKJ44V5A]] gives $f(0)$ and a rule for $f(n + 1)$ from $f(0), \ldots, f(n)$.
The [[principle of recursive definition|BQ1D7T0EGD]] says that exactly one function satisfies such a rule.
Its proof uses [[mathematical induction|0ASJVEFA9J]] for uniqueness and a union of partial solutions for existence.
The [[recursive definition of the factorial|MY3Z0QVFDX]] is the standard example.
A rule that refers to larger arguments is not covered by the theorem, and it can fail, as the [[upward recursion|CCNEXYJDC0]] shows.
An inductive definition of a set says: the set contains given objects, it is closed under given rules, and it is the smallest such set.
The smallest set exists, because the intersection of all sets with the two properties again has them.
The well-formed formulas of logic and the set of even natural numbers have inductive definitions.

### Definitions by abstraction

Let $\sim$ be an equivalence relation on a set $X$.
A definition by abstraction takes the classes $[x] = \{y \in X : y \sim x\}$ as new objects, and the [[quotient set|0011MTQMR6]] $X/{\sim}$ as the new set.
Two objects become equal exactly when they are related: $[x] = [y]$ if and only if $x \sim y$.
The [[rational numbers defined by abstraction|KF8H084HDE]], the [[integers modulo $n$|03VFZ2WETT]] and the [[construction of the integers|0NS58JP68E]] from pairs of natural numbers are of this kind.
Each operation on classes must be shown [[well defined|HNGZEBKVY2]].

### Axiomatic definitions

An axiomatic definition does not define one object.
It defines a class of structures: each set with operations that satisfies the axioms is a [[group|G5S1M9]], a [[vector space|000AYPA9AJ]] or a [[metric space|0VKD1TP7F3]].
A theorem about all groups is proved from the axioms only.
The [[Peano axioms|0QFT7Z76N5]] are axiomatic too, but their second-order form has only one model up to isomorphism.

### Implicit definitions and universal properties

An [[implicit definition|20CV0X83V2]] names an object by a condition that it satisfies, such as an equation.
It needs a proof that exactly one object satisfies the condition.
For example, the real exponential function is the unique differentiable $f \colon \mathbb{R} \to \mathbb{R}$ with $f' = f$ and $f(0) = 1$.
A universal property is an implicit definition in terms of maps.
The product of sets $A$ and $B$ is a set $P$ with maps $p_1 \colon P \to A$ and $p_2 \colon P \to B$ such that each pair of maps $f \colon Z \to A$, $g \colon Z \to B$ factors as $f = p_1 h$, $g = p_2 h$ through exactly one $h \colon Z \to P$.
The [[Cartesian product|09CEDJYBKP]] $A \times B$ with the two projections has this property.
Any two objects with the property are isomorphic by exactly one isomorphism that respects the maps, so the definition fixes the object [[up to|CBC72TX3NQ]] unique isomorphism.

### Definitions by construction

A definition by construction builds the new object from old ones.
The real numbers are built as [[Dedekind cuts|0G3RRM41X9]] of rational numbers, or as classes of Cauchy sequences of rational numbers.
After the construction, one proves the properties that the object should have, and then most proofs use only these properties.

### Examples

1. The [[recursive definition of the factorial|MY3Z0QVFDX]]: $0! = 1$ and $(n + 1)! = (n + 1) \cdot n!$, so $4! = 24$.
2. The [[rational numbers defined by abstraction|KF8H084HDE]]: a rational number is a class of pairs $(a, b)$ with $b \neq 0$, under $(a, b) \sim (c, d) \iff ad = bc$.
3. The definition of a group is axiomatic: it lists four conditions, and each structure that meets them is a group.
4. The set $E$ of even natural numbers has an inductive definition: $0 \in E$, $n \in E$ implies $n + 2 \in E$, and $E$ is the smallest such set.
5. The number $\sqrt{2}$ has an implicit definition: it is the unique real $x > 0$ with $x^2 = 2$.

### Non-examples

1. An [[upward recursion|CCNEXYJDC0]] such as $f(n) = f(n + 1) + 1$ looks like a recursive definition, but it defines no function from $\mathbb{N}$ to $\mathbb{N}$.
2. An [[ostensive definition|AZKX5AVABY]], which shows some triangles and says "these are triangles", is not a mathematical definition: no proof can use pictures as a definiens.
3. "$x$ is the real number with $x^2 = 2$" is not a legal implicit definition, because both $\sqrt 2$ and $-\sqrt 2$ satisfy the condition.

### Basic properties

1. One object can have definitions of several kinds. The natural numbers have an axiomatic definition (Peano) and a definition by construction in set theory, and these agree up to isomorphism.
2. A recursive definition can be turned into an explicit one: $f(n)$ is the value $g(n)$ of each function $g$ on $\{0, \ldots, n\}$ that satisfies the recursion there.
3. A definition by abstraction turns an equivalence relation into equality: $[x] = [y] \iff x \sim y$, because two classes are equal or disjoint.
4. An axiomatic definition cannot be wrong, but it can be empty. A list of axioms with no model defines nothing useful.

### History

Frege, in *Die Grundlagen der Arithmetik* (1884), discussed definitions by abstraction, with the direction of a line defined from the relation of parallelism.
Dedekind, in *Was sind und was sollen die Zahlen?* (1888), proved that definitions by recursion on the natural numbers are legitimate.
Hilbert's *Grundlagen der Geometrie* (1899) made axiomatic definitions the model for modern mathematics.

### Common errors

1. A student gives a recursive definition without a base case. Then the rule $(n + 1)! = (n + 1) \cdot n!$ alone is satisfied by $c \cdot n!$ for each constant $c$.
2. A student defines an operation on classes by a formula in representatives and does not check that it is well defined.
3. A student thinks that an axiomatic definition describes one object. The axioms of a group describe all groups, and they fix no particular group.

## Explanations

### L1 human

There are several ways to explain a new word in mathematics.
We can describe it directly: a number is even when it is two times a whole number.
We can build it step by step: the factorial of $4$ is $4$ times the factorial of $3$, and we start at the factorial of $0$, which is $1$.
We can group things that we want to count as the same: the fractions $\tfrac12$, $\tfrac24$ and $\tfrac36$ name the same amount.
Or we can list rules: anything that obeys the rules gets the name.
Each way needs its own check, for example that the step-by-step rule really gives one answer for each number.

### L2 human

We check that the following inductive definition gives the even natural numbers.
Let $E$ be the smallest subset of $\mathbb{N}$ with $0 \in E$ and with $n + 2 \in E$ for each $n \in E$.
Let $D = \{2k : k \in \mathbb{N}\}$.

1. The set $D$ contains $0 = 2 \cdot 0$.
2. If $n = 2k \in D$, then $n + 2 = 2(k + 1) \in D$. So $D$ has both closure properties.
3. The set $E$ is the smallest set with the two properties, so $E \subseteq D$.
4. Conversely, we show $2k \in E$ by induction on $k$. For $k = 0$, $0 \in E$ by the first property.
5. If $2k \in E$, then $2k + 2 = 2(k + 1) \in E$ by the second property.
6. So $D \subseteq E$, and with step 3, $E = D$.

The typical use of an inductive definition is a proof by induction on the rules: to show that each member of $E$ has a property, show that the given objects have it and that the rules keep it.
A trap is to forget the word "smallest": $\mathbb{N}$ itself contains $0$ and is closed under $n \mapsto n + 2$, so without "smallest" the definition does not fix $E$.

### L3 human

The kinds of definitions have a common structural meaning.
A recursive definition on $\mathbb{N}$ is the unique map out of an initial algebra: $\mathbb{N}$ with $0$ and the successor is the [[initial algebra|R76EC56V9R]] of the functor $X \mapsto 1 + X$.
An inductive definition of a set is a least fixed point of a monotone operator on a power set, which exists by the [[Knaster-Tarski theorem|RHXP3HA64M]].
A definition by abstraction is a quotient, and in a category it is a [[coequalizer|DVSTWGVCSZ]].
A universal property describes a [[representable functor|KCCHH87H6E]], and the [[Yoneda lemma|D6DF1ARPVD]] gives the uniqueness up to unique isomorphism.
Axiomatic definitions give the categories of structures in which the other kinds of definitions live.
The [[well-defined|HNGZEBKVY2]], [[up to|CBC72TX3NQ]] and [[equivalent definitions|NZ42PS2P1A]] pages treat the obligations that these kinds create.
