---
tag: 0MSRQHCNN9
kind: concept
name: Existential quantifier
aliases: [there-exists, existential-quantification]
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
uses: [0QHEWQD30B, 0ZGC7ZESYN, 025YZN3VJW, 0F72FK8EKB, 0GHS47PDAQ]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
  - book: isbn:9781108439534
    locator: Section 2.2
  - book: isbn:9781108439534
    locator: Section 3.3
same_as:
  wikidata: Q773483
  wikipedia: Existential quantification
---

## Summary

Let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0QHEWQD30B]] on $D$.
The existential quantification of $P$ is the [[proposition|0ZGC7ZESYN]] $\exists x \, P(x)$, read "there exists $x$ such that $P(x)$", which is true when $P(a)$ is true for at least one $a \in D$, and false when $P(a)$ is false for every $a \in D$.
An element $a$ with $P(a)$ true is a witness for the statement.
For a subset $A$ of $D$, the restricted form $\exists x \in A \; P(x)$ is an abbreviation of $\exists x \, (x \in A \land P(x))$, with a [[conjunction|025YZN3VJW]], and it is true when some element of $A$ satisfies $P$.
Existence theorems, the definitions of "even", "divides" and "bounded", and the negations of universal statements are existential statements.
The precise definition is on the page [[existential quantifier (definition)|0JW2FHW7G3]], and the reading of "there is", "some" and "for some" in mathematical English is on the page [[quantifiers in mathematical writing|EGTZPA6QH3]].

## Motivation

On a finite domain $D = \{a_1, \dots, a_n\}$, the statement "some element has the property $P$" is the [[disjunction|0F72FK8EKB]] $P(a_1) \lor \dots \lor P(a_n)$.
On an infinite domain, such as $\mathbb{N}$ or $\mathbb{R}$, no finite disjunction can say the same thing.
A statement such as "the equation $x^2 = 2$ has a real solution" needs a symbol that asserts the existence of one element without naming it.
The existential quantifier is this symbol, and it is the dual of the [[universal quantifier|0GHS47PDAQ]]: $\exists x \, P(x)$ says the same as $\neg \forall x \, \neg P(x)$ in classical logic.

## Notation

The existential quantification of $P$ is written $\exists x \, P(x)$, $\exists x \colon P(x)$, $\exists x, \, P(x)$ or $(\exists x) \, P(x)$; some books write $\bigvee_x P(x)$.
The restricted forms are written $\exists x \in A \; P(x)$, $(\exists x \in A) \, P(x)$ or, for an order, $\exists x > 0 \; P(x)$, which means $\exists x \, (x > 0 \land P(x))$.
Two quantifiers of the same kind are often merged: $\exists x, y \in \mathbb{Z}$ means $\exists x \in \mathbb{Z} \; \exists y \in \mathbb{Z}$.
In Lean and Mathlib, `∃ x, p x` is notation for `Exists`, an inductive proposition with one constructor that takes a witness and a proof that the witness satisfies `p`.
The symbol $\exists!$ is a different quantifier, the [[uniqueness quantifier|0QAJHFGZZJ]].

## Remarks

### Examples

1. [[There is a positive integer $n$ with $n^2 = 2^n$|~06f18a25]]: true, with the witness $n = 2$; the witness $n = 4$ also works.
2. [[The statement $\exists x \in \mathbb{R} \; (x^2 + 1 = 0)$ is false|~836e0f17]]: refuted by a proof of $\forall x \in \mathbb{R} \; \neg(x^2 + 1 = 0)$; the same formula over $\mathbb{C}$ is true.
3. "There is a prime number greater than $100$" is true, with the witness $101$: no prime $p \le 10$ divides $101$, and $11^2 = 121 > 101$.
4. The definition "$n$ is even" is existential: $\exists k \in \mathbb{Z} \; (n = 2k)$. For $n = 14$ the witness is $k = 7$.
5. [[One example proves an existential statement|2XMSKQ7YHG]]: the triple $(3, 4, 5)$ proves that some positive integers satisfy $a^2 + b^2 = c^2$.
6. [[An existential statement over the empty set is false|~1ea5e30b]]: with no element to serve as a witness, $\exists x \in \varnothing \; P(x)$ is false for each $P$.
7. [[Two existential quantifiers can be exchanged|~25ac0d7f]]: $\exists x \, \exists y \, P(x, y)$ and $\exists y \, \exists x \, P(x, y)$ have the same truth value.

### Non-examples

1. [[The formula $\exists x \, (x \in \mathbb{N} \to x < 0)$ is not the restricted statement $\exists x \in \mathbb{N} \; (x < 0)$|~481b912c]]: with $\to$ in place of $\land$, any element outside $\mathbb{N}$ makes the formula true.
2. "Every prime number is odd" is not existential: it is a universal statement, and it is false because of $2$. The existential statement "some prime number is odd" is true, with the witness $3$.
3. "There is exactly one real $x$ with $x^2 = 1$" is not the statement $\exists x \in \mathbb{R} \; (x^2 = 1)$. The existential statement is true, with the witnesses $1$ and $-1$, while the statement with $\exists!$ is false.

### Basic properties

1. On a finite domain $\{a_1, \dots, a_n\}$, $\exists x \, P(x)$ is equivalent to $P(a_1) \lor \dots \lor P(a_n)$. On the empty domain, it is false.
2. Negation: $\neg \exists x \, P(x)$ is equivalent to $\forall x \, \neg P(x)$. This is the [[negation of an existential statement|05SZQKH75K]], `not_exists` in Mathlib, and both directions hold in [[intuitionistic logic|Q11N8X99FK]].
3. For the restricted form, $\neg \exists x \in A \; P(x)$ is equivalent to $\forall x \in A \; \neg P(x)$. Unfolded: $\neg \exists x \, (x \in A \land P(x))$ is equivalent to $\forall x \, (x \in A \to \neg P(x))$.
4. Duality: $\neg \forall x \, P(x)$ is equivalent to $\exists x \, \neg P(x)$ in classical logic; this is `Classical.not_forall` and the page [[negation of a universal statement|0P3A06QNDP]].
5. $\exists$ distributes over $\lor$: $\exists x \, (P(x) \lor Q(x))$ is equivalent to $\exists x \, P(x) \lor \exists x \, Q(x)$.
6. $\exists$ does not distribute over $\land$. On $\mathbb{Z}$, with $P(x)$ "$x$ is even" and $Q(x)$ "$x$ is odd", $\exists x \, P(x) \land \exists x \, Q(x)$ is true, while $\exists x \, (P(x) \land Q(x))$ is false. The direction from $\exists x \, (P(x) \land Q(x))$ to $\exists x \, P(x) \land \exists x \, Q(x)$ holds.
7. Two existential quantifiers commute. The formula $\exists x \, \forall y \, P(x, y)$ implies $\forall y \, \exists x \, P(x, y)$, and the converse fails in general; see [[order of quantifiers|0FYQMKFE77]].
8. [[Existential generalization|33ZNXRFVJJ]]: from $P(a)$ for an element $a \in D$, conclude $\exists x \, P(x)$.
9. [[Existential instantiation|WKPW4BAVQT]]: from $\exists x \, P(x)$, introduce a new name $c$ with $P(c)$. The name must not occur earlier in the proof; the page [[one letter for two existential witnesses|FDT6332G8D]] shows what goes wrong otherwise.
10. When $x$ is not free in $q$, $\exists x \, (P(x) \land q)$ is equivalent to $(\exists x \, P(x)) \land q$.

### Proving and refuting

To prove $\exists x \in A \; P(x)$, the usual method is to name a witness $a$, check that $a \in A$, and check that $P(a)$ is true; this is a [[constructive proof|01XM7JEKHY]].
A [[non-constructive existence proof|JZQVJ9XT63]] shows that a witness exists without naming it, for example by deriving a contradiction from $\forall x \in A \; \neg P(x)$, or by a case split in which each case gives a different candidate.
To refute $\exists x \in A \; P(x)$, one proves $\forall x \in A \; \neg P(x)$, usually with an arbitrary element; checking some elements is not enough.
On a small finite set, a check of every element both proves and refutes.

### Intuitionistic reading

In the [[Brouwer–Heyting–Kolmogorov interpretation|1VFH9WT1RZ]], a proof of $\exists x \, P(x)$ is a pair: an element $a$ together with a proof of $P(a)$.
So an intuitionistic proof of an existential statement always contains a witness, at least in principle.
The classical rule from $\neg \forall x \, \neg P(x)$ to $\exists x \, P(x)$ is not valid intuitionistically, because a contradiction from "no element works" does not produce an element.
Non-constructive proofs use this rule or the [[law of excluded middle|0RYYK8PG4S]].

### History

Gottlob Frege, in his Begriffsschrift of 1879, did not use a separate existential symbol; he expressed "some $x$ is $P$" as "not every $x$ is not $P$".
Charles Sanders Peirce and his student Oscar Howard Mitchell introduced existential quantifiers as a separate notion in the 1880s, with Peirce writing them as sums $\Sigma$.
Aristotle's syllogistic already studied sentences of the form "some $A$ is $B$", which modern logic writes as $\exists x \, (A(x) \land B(x))$.

### Common errors

1. A student writes $\exists x \, (x \in A \to P(x))$ for "some element of $A$ has the property $P$". The correct form uses $\land$.
2. A student uses one letter for the witnesses of two different existential statements, as in "$m$ is even and $n$ is even, so $m = 2k$ and $n = 2k$".
3. A student reads "there exists" as "there exists exactly one", and so rejects a statement that has two witnesses.
4. A student names a witness and does not check it. A witness proves the statement only after the check that it lies in $A$ and satisfies $P$.

## Explanations

### L1 human

"Some student in the class has a red pen" is a "there exists" statement.
It is true as soon as we find one student with a red pen; we do not need to look at the others.
It is false only when no student at all has a red pen, so to show it is false, we must check every student.
With numbers: "some number from $1$ to $5$ is greater than $4$" is true, because of $5$.
"Some number from $1$ to $5$ is greater than $10$" is false, because none of $1, 2, 3, 4, 5$ is.

### L2 human

We decide whether $\exists x \in \mathbb{R} \; (x^2 - 5x + 6 = 0)$ is true.

1. Try the witness $x = 2$: $4 - 10 + 6 = 0$.
2. So $x = 2$ satisfies the predicate, and the statement is true by existential generalization.
3. The witness is not unique: $x = 3$ gives $9 - 15 + 6 = 0$. The statement does not claim uniqueness.

Now decide whether $\exists x \in \mathbb{R} \; (x^2 - 4x + 5 = 0)$ is true.

4. To refute it, we prove the negation $\forall x \in \mathbb{R} \; (x^2 - 4x + 5 \ne 0)$.
5. Let $x$ be an arbitrary real number. Then $x^2 - 4x + 5 = (x - 2)^2 + 1 \ge 1$, so $x^2 - 4x + 5 \neq 0$.
6. Since $x$ was arbitrary, no real number is a witness, and the existential statement is false.

The typical use of the existential quantifier is in definitions, such as "$a$ divides $b$" for $\exists k \in \mathbb{Z} \; (b = ak)$, and in the conclusion of existence theorems.
A trap is to try a few values in step 4, find no witness among them, and conclude that the statement is false.

### L3 human

In a structure $\mathcal{M}$ with domain $M$, Tarski's definition of [[satisfaction|2RBQPV02AS]] says that $\mathcal{M} \models \exists x \, \varphi[s]$ when $\mathcal{M} \models \varphi[s(x \mapsto a)]$ for some $a \in M$.
So $\exists$ is an infinite disjunction over the domain, and in a complete [[Boolean algebra|0XADJKM699]] or [[Heyting algebra|NG943XNQWH]] of truth values it is interpreted as a join.
In categorical logic, $\exists$ along a projection is the left adjoint of the weakening map, which explains why it commutes with $\lor$ and not in general with $\land$.

In type theory, a proof of $\exists x \in A \; P(x)$ is a pair of an element and a proof, so the quantifier is a dependent pair type.
In Lean, `Exists` is the version of this type that lives in `Prop`, so a proof does not expose its witness to computations.
Skolemization replaces $\forall x \, \exists y \, \varphi(x, y)$ by $\forall x \, \varphi(x, f(x))$ with a new function symbol $f$, which preserves satisfiability and underlies resolution proving.
Heyting arithmetic has the existence property: if it proves a closed sentence $\exists n \, \varphi(n)$, then it proves $\varphi(\bar{k})$ for some numeral $\bar{k}$.
Peano arithmetic lacks this property: for each sentence $G$ it proves $\exists n \, ((n = 0 \land G) \lor (n = 1 \land \neg G))$, and for an undecidable $G$ it proves no instance.
