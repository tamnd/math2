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

Not every [[mathematical definition|8ZCZ3HW91Z]] is a simple abbreviation, and the way a definition gives its meaning decides what you must prove before you may use it.
Compare "$n$ is even if $n = 2k$ for some integer $k$" with "$0! = 1$ and $(n + 1)! = (n + 1) \cdot n!$".
The first needs no proof at all, while the second is legal only because exactly one function obeys the two equations.

An *explicit* definition states a condition or a formula in known terms.
A *recursive* definition gives a start value and a rule that computes each value from earlier ones, and an *inductive* definition describes a set as the smallest set that contains some objects and is closed under some rules.
A definition *by abstraction* takes the [[equivalence classes|0W95W33CMP]] of an [[equivalence relation|0G8VEZ3WTK]] as new objects.
An *axiomatic* definition gives a name to every structure that satisfies a list of axioms.
An *implicit* definition names the one object that satisfies a condition, and a definition by a [[universal property|EN4DD2FAJH]] does this with a condition on maps.
A definition *by construction* builds the object out of objects that already exist.

## Motivation

The factorial of $n$ is most naturally described through the factorial of $n - 1$, so we define it step by step and prove that the steps fix one function.
The fraction $\tfrac{1}{2}$ should be the same number as $\tfrac{2}{4}$, so we define a rational number as a class of fractions.
The word "group" names infinitely many structures at once, so we define it by axioms.
Each of these needs a different justification, and once you know the kind of a definition, you know which proof makes it legal.
The later pages on [[well-defined|HNGZEBKVY2]] operations, on [[definitions that use "the"|5P955TVSS2]] and on [[up to|CBC72TX3NQ]] treat these obligations one at a time.

## Notation

Explicit definitions use "we say that ... if ..." or the symbol $:=$.
Recursive definitions list a base case and a recursive case, often joined by a brace.
The class of $a$ under an equivalence relation $\sim$ is written $[a]$, $[a]_\sim$ or $\bar a$, and the set of classes of $X$ is $X/{\sim}$.
Axiomatic definitions start "A *group* is a pair $(G, \cdot)$ such that the following axioms hold".
Definitions by a universal property have the shape "an object $P$ with maps ... such that for every ... there is a unique ...".

## Remarks

### Four definitions you have met

Here are four definitions from school and first-year courses, one of each common kind.
"An integer $n$ is even if $n = 2k$ for some integer $k$" is explicit: the [[definition of an even integer|BV6E0ZG3YN]] is an abbreviation, and nothing needs a proof.
The [[recursive definition of the factorial|MY3Z0QVFDX]] computes each value from the one before:
$$1! = 1 \cdot 0! = 1, \quad 2! = 2 \cdot 1! = 2, \quad 3! = 3 \cdot 2! = 6, \quad 4! = 4 \cdot 3! = 24.$$
The [[rational numbers defined by abstraction|KF8H084HDE]] are classes of pairs $(a, b)$ with $b \neq 0$, where $(a, b) \sim (c, d)$ means $ad = bc$, so $(1, 2)$ and $(2, 4)$ give one number.
A [[group|G5S1M9]] is defined by axioms, and $\mathbb{Z}$ under addition and the nonzero reals under multiplication both satisfy them.
Each kind brings its own question: does the recursion give one answer, does the class not depend on the pair, are the axioms met by anything?

### Recursion and induction

A recursive definition of a function $f$ on the [[natural numbers|0MWKJ44V5A]] gives $f(0)$ and a rule for $f(n + 1)$ in terms of $f(0), \ldots, f(n)$.
The [[principle of recursive definition|BQ1D7T0EGD]] says that exactly one function obeys such a rule.
[[Mathematical induction|0ASJVEFA9J]] gives the uniqueness, and a union of partial solutions gives the existence.
A rule that looks at larger arguments is not covered, and [[an upward recursion|CCNEXYJDC0]] shows that it can define nothing.

An inductive definition of a set says three things: the set contains some given objects, it is closed under some rules, and it is the smallest such set.
For example, let $E$ be the smallest subset of $\mathbb{N}$ that contains $0$ and contains $n + 2$ whenever it contains $n$.
The smallest set exists, because the intersection of all sets with both properties has both properties again.
The well-formed formulas of logic are defined in the same way.

### Definitions by abstraction

Let $\sim$ be an equivalence relation on a set $X$.
A definition by abstraction takes the classes $[x] = \{ y \in X : y \sim x \}$ as the new objects, and the [[quotient set|0011MTQMR6]] $X/{\sim}$ as the new set.
Related objects become equal, since $[x] = [y]$ exactly when $x \sim y$.
For the rationals this turns $1 \cdot 4 = 2 \cdot 2$ into $\tfrac{1}{2} = \tfrac{2}{4}$.

The definition carries two obligations.
First, $\sim$ must be an equivalence relation, which for fractions needs $b \neq 0$.
Second, every operation stated through representatives must be shown [[well defined|HNGZEBKVY2]].
The [[integers modulo $n$|03VFZ2WETT]] and the [[construction of the integers|0NS58JP68E]] from pairs of natural numbers are built in the same way.

### Axiomatic definitions and constructions

An axiomatic definition does not define one object.
It defines a class of structures: every set with operations that satisfies the axioms is a [[group|G5S1M9]], a [[vector space|000AYPA9AJ]] or a [[metric space|0VKD1TP7F3]].
A theorem about all groups is proved from the axioms alone.
Such a definition cannot be wrong, but it can be empty, so we give examples to show that the axioms have a model.
The [[Peano axioms|0QFT7Z76N5]] are axiomatic as well, and in their second-order form they have only one model up to isomorphism.

A definition by construction builds the new object from old ones.
The real numbers are built as [[Dedekind cuts|0G3RRM41X9]] of rationals, or as classes of Cauchy sequences of rationals.
After the construction we prove the expected properties, and most later proofs use only those properties, not the construction.
One object can have definitions of several kinds: the natural numbers have the Peano axioms and also a construction in set theory, and the two agree up to isomorphism.

### Implicit definitions and universal properties

An [[implicit definition|20CV0X83V2]] names an object by a condition, and it needs a proof that exactly one object meets the condition.
The number $\sqrt{2}$ is the unique real $x > 0$ with $x^2 = 2$.
The exponential function is the unique differentiable $f \colon \mathbb{R} \to \mathbb{R}$ with $f' = f$ and $f(0) = 1$.

A universal property is an implicit definition stated with maps.
A product of sets $A$ and $B$ is a set $P$ with maps $p_1 \colon P \to A$ and $p_2 \colon P \to B$, such that every pair $f \colon Z \to A$, $g \colon Z \to B$ factors through exactly one $h \colon Z \to P$:
$$f = p_1 \circ h, \qquad g = p_2 \circ h.$$
The [[Cartesian product|09CEDJYBKP]] with its two projections works, with $h(z) = (f(z), g(z))$.
Any two products are related by exactly one bijection that respects the maps, so the property fixes the object [[up to|CBC72TX3NQ]] that kind of isomorphism, not up to equality.

### Watch out

An [[upward recursion|CCNEXYJDC0]] such as $f(n) = f(n + 1) + 1$ looks like a recursion, but no function from $\mathbb{N}$ to $\mathbb{N}$ satisfies it.
A recursion with no base case does not fix its function: the rule $(n + 1)! = (n + 1) \cdot n!$ alone is satisfied by $c \cdot n!$ for every constant $c$.
An inductive definition without the word "smallest" fails too, because $\mathbb{N}$ itself contains $0$ and is closed under $n \mapsto n + 2$.
"$x$ is the real number with $x^2 = 2$" is not a legal implicit definition, since $\sqrt{2}$ and $-\sqrt{2}$ both qualify.
An [[ostensive definition|AZKX5AVABY]], which shows some triangles and says "these are triangles", gives no definiens that a proof could use.

### History

Frege, in *Die Grundlagen der Arithmetik* (1884), discussed definitions by abstraction, with the direction of a line obtained from the relation of parallelism.
Dedekind, in *Was sind und was sollen die Zahlen?* (1888), proved that definitions by recursion on the natural numbers are legitimate.
Hilbert's *Grundlagen der Geometrie* (1899) treated geometry axiomatically, with point, line and plane left undefined.

### Try it

First, name the kind of "the set $T$ of strings is the smallest set that contains the empty string and contains $s0$ and $s1$ whenever it contains $s$".
It is an inductive definition, and $T$ is the set of all finite strings of $0$s and $1$s.

Second, why does "$f(0) = 1$ and $f(n + 1) = 2 f(n)$" define a function, and what is it?
It is a recursion with a base case that uses only the previous value, so the principle of recursive definition applies, and $f(n) = 2^n$.

## Explanations

### L1 human

There are several ways to explain a new word in mathematics.
We can say it directly: a number is even when it is two times a whole number.
We can build it step by step: the factorial of $4$ is $4$ times the factorial of $3$, and we start with the factorial of $0$, which is $1$.
We can group things that should count as the same: $\tfrac12$, $\tfrac24$ and $\tfrac36$ name one amount.
Or we can list rules, and anything that obeys the rules gets the name.
Each way needs its own check, for example that the step-by-step rule really gives one answer for each number.

### L2 human

We check that the inductive definition of $E$ above gives the even natural numbers.
Recall that $E$ is the smallest subset of $\mathbb{N}$ with $0 \in E$ and with $n + 2 \in E$ for each $n \in E$, and let $D = \{ 2k : k \in \mathbb{N} \}$.

1. The set $D$ contains $0 = 2 \cdot 0$.
2. If $n = 2k \in D$, then $n + 2 = 2(k + 1) \in D$, so $D$ is closed under the rule.
3. The set $E$ is the smallest set with both properties, so $E \subseteq D$.
4. For the reverse inclusion we show $2k \in E$ by induction on $k$.
   For $k = 0$, $0 \in E$ by the first property.
5. If $2k \in E$, then $2k + 2 = 2(k + 1) \in E$ by the second property.
6. So $D \subseteq E$, and with step 3 we get $E = D$.

The proof shows the usual way to use an inductive definition: to prove that every member of $E$ has a property, show that the given objects have it and that the rules keep it.
Step 3 is where "smallest" does its work, and without it the definition would allow $E = \mathbb{N}$.

### L3 human

The kinds of definitions share a structural meaning.
A recursive definition on $\mathbb{N}$ is the unique map out of an [[initial algebra|R76EC56V9R]]: $\mathbb{N}$ with $0$ and the successor is initial for the functor $X \mapsto 1 + X$.
An inductive definition of a set is a least fixed point of a monotone operator on a power set, which exists by the [[Knaster-Tarski theorem|RHXP3HA64M]].
A definition by abstraction is a quotient, and in a category it is a [[coequalizer|DVSTWGVCSZ]].
A universal property describes a [[representable functor|KCCHH87H6E]], and the [[Yoneda lemma|D6DF1ARPVD]] gives uniqueness up to unique isomorphism.
Axiomatic definitions give the categories of structures in which the other kinds live, and [[equivalent definitions|NZ42PS2P1A]] asks when two definitions of different kinds pick out the same objects.
