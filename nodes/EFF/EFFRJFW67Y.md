---
tag: EFFRJFW67Y
kind: concept
name: Foundations of mathematics
msc: ["03A05", "03B30"]
topics: [H8QZY0RZXZ]
audience: ug2
uses: [086QKPF0A6, 0HE5WDQ9FJ, 0B94TKFQJX, GD2JBXJV5Z, X9WYNYE29C]
sources:
  - url: https://en.wikipedia.org/wiki/Foundations_of_mathematics
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Type_theory
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Elementary_theory_of_the_category_of_sets
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordered_pair
    locator: Kuratowski's definition
  - book: isbn:9780122384523
same_as:
  wikidata: Q833585
  wikipedia: Foundations of mathematics
---

## Summary

A foundation of mathematics is a single formal framework in which all of mathematics can be stated and proved.
In set theory the number $0$ is the empty set, $1$ is $\{ 0 \}$, and $2$ is $\{ 0, 1 \}$.
The pair $(a, b)$ is the set $\{ \{ a \}, \{ a, b \} \}$, a function is a set of pairs, and so on up to real numbers and spaces.
Once every notion is coded in this way, every proof becomes a derivation from a few axioms about sets, and a machine can check it.

A foundation has three parts: a formal language, a [[logic|DYJ0KGTPMR]] with rules of proof, and a list of axioms.
It also gives a translation of each mathematical notion, such as number, function and space, into an object of the framework.
The field of foundations studies such frameworks: how to build them, how strong they are, whether they are consistent, and what they cannot prove.
The standard framework today is [[first-order logic|086QKPF0A6]] with the axioms of [[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]] and the axiom of choice (ZFC).
The idea turns the question "is this proof correct?" into a precise question with a checkable answer.

## Motivation

In the nineteenth century mathematics grew in ways that made its basic notions unclear.
Calculus used infinitely small quantities that nobody could define.
Analysts such as Cauchy, Weierstrass and Dedekind replaced them with definitions in terms of real numbers.
The real numbers were then built from the rational numbers, and the rational numbers from the natural numbers.
This chain suggested that all of mathematics could rest on a small base.

Georg Cantor's theory of sets gave a candidate for that base, but around 1900 contradictions appeared in it.
[[Russell's paradox|0HESMMSYEG]] shows that the "set of all sets that are not members of themselves" cannot exist.
The period of doubt that followed is often called the crisis of foundations.
Three programs answered it.
[[Logicism|5PGSQYB5Y1]] tried to reduce mathematics to logic, [[formalism|46JCQ6KDA4]] tried to prove the consistency of formal systems, and [[intuitionism|XQHF63BBYF]] restricted mathematics to constructive methods.
The modern subject keeps the precise tools of these programs and studies them as mathematics.

## Notation

ZF denotes Zermelo-Fraenkel set theory, and ZFC denotes ZF with the axiom of choice.
For a theory $T$, the formula $T \vdash \varphi$ means that $\varphi$ is provable from $T$, and $\operatorname{Con}(T)$ is the statement that $T$ is consistent.
ETCS is Lawvere's elementary theory of the category of sets, MLTT is Martin-Löf type theory, and HoTT is homotopy type theory.
Books use "foundations" both for one chosen framework and for the whole study of such frameworks; we say which sense we mean when it matters.

## Remarks

### What a foundation must supply

A foundation must supply at least five things.

1. A language in which each mathematical statement can be written, for example the language of set theory with the single symbol $\in$.
2. A logic: the rules that say which steps are allowed in a proof, for example the rules of [[first-order logic|086QKPF0A6]].
3. Axioms that state which objects exist, for example the axioms of [[ZFC|0HE5WDQ9FJ]].
4. Encodings of the usual objects, with a check that the encodings have the expected properties.
   The objects include [[natural numbers|0MWKJ44V5A]], [[ordered pairs|0JQWWFCS9R]], functions, [[real numbers|08J2M1JYAG]] and spaces.
5. A precise notion of [[proof|0B94TKFQJX]], so that a finite procedure can check each proof.

A foundation should also be consistent, and mathematicians should believe that its axioms are true of some intended objects.
The second requirement is not a mathematical property, and it is a question for the [[philosophy of mathematics|NTJ5XW0PVD]].

### Set-theoretic foundations

In set-theoretic foundations every object is a set, and the only primitive relation is membership.
The axioms of [[ZFC|0HE5WDQ9FJ]] say which sets exist: the empty set, pairs, unions, power sets, an infinite set, and the images of sets under definable maps.
The natural numbers are the von Neumann numerals $0 = \varnothing$, $1 = \{ 0 \}$, $2 = \{ 0, 1 \}$, and in general $n + 1 = n \cup \{ n \}$.
An ordered pair is the Kuratowski pair $(a, b) = \{ \{ a \}, \{ a, b \} \}$.
A function is a set of ordered pairs, the [[integers|0NS58JP68E]] are equivalence classes of pairs of natural numbers, and a real number is a [[Dedekind cut|0G3RRM41X9]] of rational numbers.
Variants include von Neumann-Bernays-Gödel set theory ([[NBG|7FW29X1ADK]]), which adds classes, and ZFC with [[large cardinal|X1FG7PSCTY]] axioms.

### Type-theoretic foundations

In type-theoretic foundations every object has a type, and a statement about an object makes sense only when the types match.
Russell's ramified theory of types in *Principia Mathematica* was the first such system, and Alonzo Church gave the simple theory of types in 1940.
[[Martin-Löf type theory|X0TBV1B34C]] adds dependent types, whose members can depend on other objects, and it treats proofs as objects.
[[Homotopy type theory|7Y8PYJA1M1]] adds the univalence axiom, which identifies equivalent structures.
Many [[proof assistants|YM6PRDE88V]], such as Lean, Coq and Agda, use a dependent type theory as their foundation, and Isabelle/HOL uses a simple type theory.
The details belong to [[type theory and constructive mathematics|K6P3NSQEZ3]].

### Categorical foundations

In categorical foundations the basic notions are objects and arrows, and a set is described by its maps to and from other sets.
William Lawvere's [[elementary theory of the category of sets|W448SK1RTY]] (ETCS) of 1964 axiomatizes the category of sets in this way.
ETCS has no membership relation: an element of a set $X$ is an arrow from a one-point set to $X$.
ETCS is weaker than ZFC, but it is strong enough for most ordinary mathematics.
[[Toposes|6837RS7N82]] generalize the category of sets, and their internal logic is intuitionistic in general.
These systems belong to [[category theory|Y97P9CSMEN]].

### The role of the incompleteness theorems

[[Gödel's incompleteness theorems|X9WYNYE29C]] apply to each foundation that is consistent, has a decidable set of axioms and is strong enough for basic arithmetic.
The first theorem gives a sentence that the foundation can neither prove nor refute.
The second theorem says that the foundation cannot prove its own consistency.
So no foundation of this kind settles every mathematical question, and none certifies itself.
The theorems do not say that ZFC is inconsistent or unreliable.
They say that confidence in a foundation must come partly from outside it, for example from a model in a stronger theory or from the intended meaning of the axioms.
This ended the original form of [[Hilbert's program|P1RW6JWX73]].

### Foundations and non-foundations

ZFC is a foundation: the language has one binary relation symbol $\in$, the logic is first-order logic, and the encodings above give all objects of ordinary mathematics.
The dependent type theory of Lean, with the library Mathlib, is a foundation in practice, because its kernel checks each proof against fixed typing rules.
ETCS is a foundation of a different shape: it describes sets only through functions, yet the usual number systems can be built in it.

The axioms of a [[group|G5S1M9]] are not a foundation.
They describe a class of structures, and they do not say which sets or numbers exist.
Naive set theory with unrestricted comprehension is not a usable foundation, because Russell's paradox makes it inconsistent, so it proves every statement.
[[Euclid's Elements|83WHDAV68J]] is not a foundation of all mathematics.
It treats geometry and some arithmetic by axioms, with no general notion of set or function.

### First facts about ZFC

If ZF is consistent, then ZFC is consistent; Gödel proved this with the [[constructible universe|6TF2JBTPPJ]], see [[Gödel's consistency of CH and AC|Q9176JRJ5M]].
If ZFC is consistent, then ZFC does not prove $\operatorname{Con}(\mathrm{ZFC})$, by [[Gödel's second incompleteness theorem|4PZM5GJTR5]].
The [[continuum hypothesis|0MN2MER9WN]] is independent of ZFC, if ZFC is consistent, by Gödel (1938) and Cohen (1963).
So the standard foundation leaves natural questions open.
Different foundations can often be compared by [[relative consistency proofs|X3G0RG2GPZ]] and interpretations.
For example, a theorem of ordinary analysis usually has a proof in ZFC and a proof in a dependent type theory.

### Watch out

An encoding is not an identity.
In ZF the numeral $2$ is the set $\{ 0, 1 \}$, so the statement $1 \in 2$ is true, but it is a fact about the encoding and not about numbers.
A mathematician who works on top of the foundation never uses such facts.

The incompleteness theorems do not show that mathematics is inconsistent.
They show that a consistent foundation of this kind is incomplete and cannot prove its own consistency.

A foundation is not a claim that mathematicians think in sets.
It is a claim that their proofs can be translated into checked formal derivations.

### History

Frege's *Begriffsschrift* of 1879 gave the first formal language with quantifiers and exact rules of proof.
Zermelo published his axioms for set theory in 1908, and Fraenkel and Skolem added the axiom of replacement in 1922.
Whitehead and Russell published *Principia Mathematica* in three volumes from 1910 to 1913.
Gödel's incompleteness theorems of 1931 showed the limits of every such foundation.
Later work added categorical and type-theoretic foundations to the set-theoretic one.

### Try it

Write the von Neumann numeral $3$ as a set built from $\varnothing$ alone.
Answer: $3 = \{ 0, 1, 2 \} = \{ \varnothing, \{ \varnothing \}, \{ \varnothing, \{ \varnothing \} \} \}$.

In ZF, is $0 \in 3$ true, and is it a fact about numbers?
It is true, since $0$ is an element of $\{ 0, 1, 2 \}$, but it is a fact about the encoding; it corresponds to $0 < 3$ only because the von Neumann numerals are ordered by membership.

## Explanations

### L1 human

Every theorem in mathematics is proved from earlier theorems, and these are proved from still earlier ones.
The foundations of mathematics ask what is at the bottom of this chain.
The usual answer is that everything can be built from sets, which are collections of objects.
For example, the number $0$ can be the empty set, $1$ can be the set that contains only $0$, and $2$ can be the set that contains $0$ and $1$.
In this way the numbers $0$ to $10$ become 11 particular sets, and facts about numbers become facts about sets.
Around 1900 mathematicians found contradictions in a careless theory of sets, so they wrote down exact rules, called axioms, for which sets exist.
Later Kurt Gödel showed that no such list of rules can answer every question.

### L2 human

We check that the Kuratowski pair $(a, b) = \{ \{ a \}, \{ a, b \} \}$ does the job of an [[ordered pair|0JQWWFCS9R]].
The required property is: $(a, b) = (c, d)$ if and only if $a = c$ and $b = d$.

1. If $a = c$ and $b = d$, then $\{ \{ a \}, \{ a, b \} \} = \{ \{ c \}, \{ c, d \} \}$, because both sides are built from the same sets.
2. For the converse, assume $\{ \{ a \}, \{ a, b \} \} = \{ \{ c \}, \{ c, d \} \}$.
3. Case $a = b$.
   Then the left side is $\{ \{ a \} \}$, a set with one element.
4. In this case $\{ c \}$ and $\{ c, d \}$ are both elements of $\{ \{ a \} \}$, so both are equal to $\{ a \}$.
5. From $\{ c \} = \{ a \}$ we get $c = a$, and from $\{ c, d \} = \{ a \}$ we get $d = a = b$.
   So $a = c$ and $b = d$.
6. Case $a \neq b$.
   Then $\{ a \}$ has one element and $\{ a, b \}$ has two, so the left side has exactly two elements.
7. The right side must then also have two elements, so $\{ c \} \neq \{ c, d \}$, and therefore $c \neq d$.
8. Each side has exactly one element with one member, so $\{ a \} = \{ c \}$, and $a = c$.
9. Each side has exactly one element with two members, so $\{ a, b \} = \{ c, d \} = \{ a, d \}$.
10. So $b \in \{ a, d \}$, and $b \neq a$ by the case assumption, so $b = d$.

The typical use of such a check is to show that an encoding has all the properties that mathematics uses, and no more is needed.
After this check, a mathematician uses $(a, b)$ through its property alone and forgets the definition.
Watch out: the encoding is neither unique nor forced.
The pair $\{ a, \{ a, b \} \}$ also works in ZF, by a proof that uses the axiom of foundation, and different books use different encodings.

### L3 human

A foundation is best seen as a pair: a formal theory and an interpretation of ordinary mathematics in it.
Two foundations are equally good for a body of mathematics when each can interpret the other's treatment of it.
This view makes questions of foundations into questions about interpretations, conservativity and consistency strength.
These are the subjects of [[conservative extensions|N238J43XNE]], [[relative consistency proofs|X3G0RG2GPZ]] and [[reverse mathematics|7SQS69T17R]].
Reverse mathematics shows, for example, that much of classical analysis needs far less than ZFC: it can be done in subsystems of [[second-order arithmetic|DC60FYCSPM]].

The three main styles differ in what they take as primitive.
Set theory takes membership, and it identifies a structure with a set plus relations on it.
Type theory takes typing and computation, so that proofs are objects and many proofs can be run as programs; this is the base of most modern [[proof assistants|YM6PRDE88V]].
Category theory takes composition of maps, so that only properties invariant under isomorphism can be stated, and univalent foundations make this principle an axiom.
The [[incompleteness theorems|X9WYNYE29C]] apply to all three, so the choice between them is a choice of convenience and meaning, not of power to decide every question.
