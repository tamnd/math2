---
tag: AM4GQQMZ3C
kind: concept
name: Inductive and recursive definitions
aliases: [definition-by-base-and-rule, inductively-defined-set]
msc: ["00A35", "03E20"]
topics: [EEH2F76CYQ]
audience: ug1
uses: [0ASJVEFA9J, 0DSHAVH45F]
sources:
  - url: https://en.wikipedia.org/wiki/Recursive_definition
    locator: Form of recursive definitions
  - url: https://en.wikipedia.org/wiki/Recursive_definition
    locator: Examples of recursive definitions
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Summary

An inductive definition describes a collection by a starting point and a way to make new members from old ones.
For example, the sequence with $h_0 = 0$ and $h_{n+1} = 2h_n + 1$ has the values $0, 1, 3, 7, 15$, and induction proves that $h_n = 2^n - 1$ for every $n$.

In general, an inductive definition of a set $S$ has base clauses, rules and an extremal clause.
The base clauses say that some given objects are in $S$.
Each rule says that if some objects are in $S$, then an object built from them is in $S$.
The extremal clause says that $S$ is the smallest set that contains the given objects and is closed under the rules.
A recursive definition of a sequence or a function on the [[natural numbers|0MWKJ44V5A]] gives the first values and a rule that computes each later value from earlier values.
Both kinds come with a proof method: a property holds for every member of $S$ if it holds for the given objects and each rule keeps it.

## Motivation

Some sets are easy to build step by step and hard to describe by one condition.
The balanced strings of parentheses are an example: the empty string is balanced, a balanced string inside one more pair of parentheses is balanced, and two balanced strings side by side are balanced.
In the same way, the rule from one term of a sequence to the next is often simple while no closed formula is known yet.
The minimum number of moves in the [[Tower of Hanoi|0906Z03EMN]] obeys $h_{n+1} = 2h_n + 1$, and that rule comes first; the formula $h_n = 2^n - 1$ comes after.

Most objects of discrete mathematics and computing are defined this way: sequences, strings, lists, trees, arithmetic expressions, formulas and programs.
[[Mathematical induction|0ASJVEFA9J]] proves facts about recursive sequences, and [[structural induction|12MQ2NJ29A]] proves facts about inductively defined sets.
In logic the formulas of a language are defined in the same way, and set theory proves that recursion on $\mathbb{N}$ defines a unique function.

## Notation

A recursive definition of a sequence lists the base and the rule, as in $a_0 = c$ and $a_{n+1} = g(n, a_n)$ for $n \ge 0$.
An inductive definition of a set is often written as clauses: "(i) $x_0 \in S$; (ii) if $x \in S$, then $f(x) \in S$; (iii) nothing else is in $S$."
The last clause is the extremal clause, and books also write it as "$S$ is the smallest such set" or "$S$ is the intersection of all such sets".
In computing, an inductive definition is often a grammar, such as $B ::= \varepsilon \mid (B) \mid B B$ for balanced strings, a [[context-free grammar|CTCY2R8Q77]].

In Lean 4 the command `inductive` declares a type by its constructors, for example `inductive Tree where | leaf : Tree | node : Tree → Tree → Tree`.
Lean then makes the recursor `Tree.rec`, which gives both definitions by recursion and proofs by induction on the type.

## Remarks

### A set built by rules

Take the balanced strings: $\varepsilon$ is balanced, $(w)$ is balanced when $w$ is, and $uv$ is balanced when $u$ and $v$ are.
To show that $(()())$ is a member, build it.
The base gives $\varepsilon$, the first rule gives $()$, the second rule gives $()()$, and the first rule again gives $(()())$.

To show that every member has some property, check the base and each rule.
Every member has as many "(" as ")": the empty string has $0$ of each, and each rule adds equal numbers.
To show that $)($ is not a member, find a property that all members have and $)($ lacks.
Equal counts do not help, since $)($ has one of each.
The property "empty or starts with (" works, and the [[balanced strings of parentheses|VRVKTEHBB0]] check it rule by rule.

### The smallest closed set

Why does the extremal clause define one set?
Let $U$ be a set, let $B \subseteq U$ be the base objects, and let each rule be a function $f \colon U^k \to U$ for some $k \ge 1$.
Call $C \subseteq U$ closed if $B \subseteq C$ and $f(x_1, \ldots, x_k) \in C$ for each rule $f$ and all $x_1, \ldots, x_k \in C$.
The set $U$ itself is closed, so there is at least one closed set.
The intersection $S$ of all closed sets is closed, because each condition holds in every closed set and so holds in their intersection.
So $S$ is the smallest closed set, and it is unique, because two smallest closed sets contain each other.

The same $S$ is the set of objects reached from $B$ by finitely many uses of the rules.
The reachable objects form a closed set, so they contain $S$.
Each reachable object lies in every closed set, by induction on the number of rule uses, so it lies in $S$.

### Proof by induction on the rules

Let $P$ be a property of the elements of $U$.
Suppose that $P(b)$ holds for each $b \in B$, and that for each rule $f$, if $P(x_1), \ldots, P(x_k)$ hold, then $P(f(x_1, \ldots, x_k))$ holds.
Then $P(x)$ holds for each $x \in S$.
The proof is one line: the set $\{x \in U : P(x)\}$ is closed, and $S$ lies inside every closed set.
This principle is [[structural induction|12MQ2NJ29A]], and ordinary induction is the case $U = \mathbb{N}$, $B = \{0\}$, with the one rule $n \mapsto n + 1$.

### Recursion on the natural numbers

A [[definition by recursion|0DSHAVH45F]] gives $f(0)$ and a rule for $f(n + 1)$ in terms of $n$ and $f(n)$.
The recursion theorem of set theory says that exactly one function satisfies such a definition, and the [[principle of recursive definition|BQ1D7T0EGD]] states it.
In practice two facts matter: the values exist and are unique, and each fact about the values is proved by induction on $n$.
The [[factorial|MY3Z0QVFDX]], with $0! = 1$ and $(n + 1)! = (n + 1) \cdot n!$, looks back one step, so one start value is enough.
The [[Fibonacci sequence|0GA9K57A39]] looks back two steps, $F_{n+2} = F_{n+1} + F_n$, so it needs two start values, $F_0 = 0$ and $F_1 = 1$.

The [[sequence $h_{n+1} = 2h_n + 1$|7WJPXGA2ZV]] shows the usual workflow.
Compute a few terms from the rule, guess a closed form, and prove it by induction, with the base case from the base and the step from the rule.

### What fails to be a definition

Rules without the extremal clause do not fix a set.
"$0 \in S$, and $n \in S$ implies $n + 2 \in S$" is true of the even numbers and also of $\mathbb{N}$, as [[closure rules without the word smallest|FVT2EA59S4]] shows.

An [[upward recursion|CCNEXYJDC0]] such as $f(n) = f(n + 1) + 1$ computes a value from a later value.
No function from $\mathbb{N}$ to $\mathbb{N}$ satisfies it, because it would give $f(0) = f(k) + k \ge k$ for every $k$.

The rule $a_{n+2} = a_{n+1} + a_n$ with the single start value $a_0 = 1$ does not define a sequence either.
The value $a_1$ is free, so the rule has many solutions: $a_1 = 1$ gives $1, 1, 2, 3, 5$, and $a_1 = 2$ gives $1, 2, 3, 5, 8$.

### Watch out

A function on an inductively defined set can be defined by recursion on the rules only when each element is built in exactly one way.
[[Binary trees|02A8EMC83C]] have this property, but the balanced strings do not.
The empty string satisfies $\varepsilon = \varepsilon\varepsilon$, so it comes from the base and also from the second rule.
A "definition" such as $g(\varepsilon) = 0$, $g((w)) = g(w)$ and $g(uv) = g(u) + g(v) + 1$ gives $g(\varepsilon) = 0$ and also $g(\varepsilon) = g(\varepsilon) + g(\varepsilon) + 1 = 1$.
Such a $g$ is not [[well defined|HNGZEBKVY2]].
The fix is a grammar with unique readings, or a proof that every way of building an element gives the same value.

### History

Richard Dedekind, in *Was sind und was sollen die Zahlen?* (1888), defined the natural numbers as the intersection of all sets that contain the first number and are closed under the successor map.
In the same work he proved that definitions by recursion on the natural numbers are legitimate.

### Try it

First, describe the smallest set $S$ with $1 \in S$ and $n \in S \Rightarrow 2n \in S$.
It is $\{1, 2, 4, 8, \ldots\}$, the powers of $2$: every power of $2$ is reached, and the powers of $2$ form a closed set.

Second, define $a_0 = 2$ and $a_{n+1} = a_n^2$, and find $a_n$.
The terms are $2, 4, 16, 256$, and induction gives $a_n = 2^{2^n}$, because $(2^{2^n})^2 = 2^{2^{n+1}}$.

## Explanations

### L1 human

Some collections are best described by a starting point and a way to make new members.
Start with the number $0$, and say that whenever a number is in the collection, the number two larger is too.
Then $0$, $2$, $4$, $6$ and so on are in the collection.
We also say that nothing else is in it, and this last sentence makes the collection exactly the even numbers.
A sequence can be described in the same way: start with $0$, and get each term by doubling the last one and adding $1$.
This gives $0$, $1$, $3$, $7$, $15$, and so on.

### L2 human

Let us define a set $S$ of natural numbers inductively and find it.
The base is $1 \in S$, the rule is "if $n \in S$, then $3n \in S$", and $S$ is the smallest set with these two properties.
The rule gives $3$, then $9$, then $27$, so each power $3^k$ is in $S$, by induction on $k$.
Conversely, the set $T = \{3^k : k \in \mathbb{N}\}$ contains $1 = 3^0$, and it is closed under the rule:
$$3 \cdot 3^k = 3^{k+1} \in T.$$
Since $S$ is the smallest closed set, $S \subseteq T$, and so $S = T$.

Now prove by induction on the rules that each element of $S$ is odd.
The base element $1$ is odd, and if $n$ is odd, then $3n$ is odd, as a product of two odd numbers.
That is the typical use of an inductive definition: check the base objects, then check that each rule keeps the property.
Watch out for the inclusion $S \subseteq T$: it needs the word "smallest", and without it $\mathbb{N}$ would satisfy the base and the rule too.

### L3 human

An inductive definition is a least fixed point.
The rules define a monotone operator $\Phi(X) = B \cup \{f(\vec x) : f \text{ a rule}, \ \vec x \in X^k\}$ on the subsets of $U$, and $S$ is the least $X$ with $\Phi(X) \subseteq X$.
By the [[Knaster-Tarski theorem|RHXP3HA64M]], this $S$ is also the least fixed point of $\Phi$.
When all rules are finitary, $S = \bigcup_{n} \Phi^n(\emptyset)$, and the stage $n$ at which an element first appears is a height for proofs by [[induction on size|B2D8PTFNN1]].
With infinitary rules, the stages run through the ordinals, and the theory of inductive definitions in logic studies how long they run.

In type theory, an inductive type is the [[initial algebra|R76EC56V9R]] of a functor, and its recursor is the unique map out of that algebra.
Lean, Coq and Agda take [[inductive types|Q80JWCWNKX]] as primitive, so the natural numbers, lists and trees are all instances of one form of declaration.
The dual notion, the greatest fixed point, gives coinductive definitions of infinite objects such as streams.
