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

The existential quantifier turns a property into a claim of existence: "there exists $x$ such that $P(x)$" says that at least one object in the domain has the property.
"Some number from $1$ to $5$ is greater than $4$" is true because $5$ passes the test, and "some number from $1$ to $5$ is greater than $10$" is false because none of $1, 2, 3, 4, 5$ passes it.
In general, let $D$ be a domain of discourse and $P(x)$ a [[predicate|0QHEWQD30B]] on $D$.
The [[proposition|0ZGC7ZESYN]] $\exists x \, P(x)$ is true when $P(a)$ is true for at least one $a \in D$, and false when $P(a)$ is false for every $a \in D$.
An element $a$ with $P(a)$ true is a witness.
For a subset $A$ of $D$, the restricted form is an abbreviation with a [[conjunction|025YZN3VJW]]:
$$\exists x \in A \; P(x) \quad \text{means} \quad \exists x \, (x \in A \land P(x)).$$
The [[formal definition|0JW2FHW7G3]] states this with every condition, and [[quantifiers in mathematical writing|EGTZPA6QH3]] explains how "there is", "some" and "for some" are read.

## Motivation

On a finite domain $\{a_1, \dots, a_n\}$, "some element has property $P$" is the [[disjunction|0F72FK8EKB]] $P(a_1) \lor \dots \lor P(a_n)$.
On an infinite domain such as $\mathbb{N}$ or $\mathbb{R}$, no finite disjunction can say the same thing.
"The equation $x^2 = 2$ has a real solution" needs a symbol that asserts that an element exists without naming it.

Existence theorems, and definitions such as "even", "divides" and "bounded", are existential statements.
The negation of a universal statement is existential, so every [[counterexample|0ED72CTBNP]] is a witness for an existential statement.
In classical logic, $\exists$ is the dual of the [[universal quantifier|0GHS47PDAQ]]: $\exists x \, P(x)$ says the same as $\neg \forall x \, \neg P(x)$.

## Notation

Books write $\exists x \, P(x)$, $\exists x \colon P(x)$, $\exists x, \, P(x)$ or $(\exists x) \, P(x)$, and some write $\bigvee_x P(x)$.
The restricted form is written $\exists x \in A \; P(x)$ or $(\exists x \in A) \, P(x)$, and other conditions work the same way: $\exists x > 0 \; P(x)$ means $\exists x \, (x > 0 \land P(x))$.
Quantifiers of the same kind are often merged, so $\exists x, y \in \mathbb{Z}$ means $\exists x \in \mathbb{Z} \; \exists y \in \mathbb{Z}$.
In Lean and Mathlib, `∃ x, p x` is notation for `Exists`, a proposition whose one constructor takes a witness and a proof that the witness satisfies `p`.
The symbol $\exists!$ is a different quantifier, the [[uniqueness quantifier|0QAJHFGZZJ]].

## Remarks

### A first check on a small domain

Let $D = \{1, 2, 3, 4, 5\}$ and let $P(x)$ be "$x^2 = 2x + 8$".
The values of $x^2 - 2x$ are
$$-1, \quad 0, \quad 3, \quad 8, \quad 15,$$
so $P(4)$ is true and the other four instances are false.
The disjunction of the five instances is true, and so is $\exists x \in D \; P(x)$, with the witness $4$.
For $Q(x)$ "$x^2 = 2x + 1$", none of the five values equals $1$, so all five instances are false and $\exists x \in D \; Q(x)$ is false.
To prove the first statement you need one witness, and to refute the second you need to check all five elements.

### One witness is enough

[[There is a positive integer $n$ with $n^2 = 2^n$|BVXD3PSAJ9]]: the witness $n = 2$ proves it, and $n = 4$ is a second witness.
In the same way, [[one example proves an existential statement|2XMSKQ7YHG]]: the triple $(3, 4, 5)$ shows that some positive integers satisfy $a^2 + b^2 = c^2$.
Refuting needs more: [[the statement $\exists x \in \mathbb{R} \; (x^2 + 1 = 0)$ is false|B5NGFKX1D3]], and the refutation is a proof that $x^2 + 1 \ge 1$ for every real $x$.
Over $\mathbb{C}$ the same formula is true, with the witness $i$.
[[An existential statement over the empty set is false|CHKD0587G6]], because there is nothing to serve as a witness.

### What is not existential

[[The formula $\exists x \, (x \in \mathbb{N} \to x < 0)$ is not the restricted statement $\exists x \in \mathbb{N} \; (x < 0)$|RKBRXZ5FPE]].
With $\to$ in place of $\land$, any element outside $\mathbb{N}$ makes the formula true, while no natural number is negative.
"Every prime number is odd" is not existential: it is a universal statement, and $2$ refutes it.
"There is exactly one real $x$ with $x^2 = 1$" is not $\exists x \in \mathbb{R} \; (x^2 = 1)$.
The existential statement is true, with the witnesses $1$ and $-1$, while the statement with $\exists!$ is false for the same reason.

### The rules you can use

[[Existential generalization|33ZNXRFVJJ]] concludes $\exists x \, P(x)$ from $P(a)$ and $a \in D$.
[[Existential instantiation|WKPW4BAVQT]] introduces, from $\exists x \, P(x)$, a new name $c$ with $P(c)$, and the name must not occur earlier in the proof.
The negation $\neg \exists x \, P(x)$ is equivalent to $\forall x \, \neg P(x)$, the [[negation of an existential statement|05SZQKH75K]], which is `not_exists` in Mathlib.
Both directions of that equivalence hold in [[intuitionistic logic|Q11N8X99FK]].
The dual law, $\neg \forall x \, P(x)$ equivalent to $\exists x \, \neg P(x)$, is `Classical.not_forall`, and its direction from $\neg \forall$ to $\exists \neg$ is classical only; see the [[negation of a universal statement|0P3A06QNDP]].
The quantifier $\exists$ distributes over $\lor$: $\exists x \, (P(x) \lor Q(x))$ is equivalent to $\exists x \, P(x) \lor \exists x \, Q(x)$.
Two existential quantifiers commute, and $\exists x \, \forall y \, P(x, y)$ implies $\forall y \, \exists x \, P(x, y)$, but not conversely; see the [[order of quantifiers|0FYQMKFE77]].
When $x$ is not free in $q$, $\exists x \, (P(x) \land q)$ is equivalent to $(\exists x \, P(x)) \land q$.

### Proving and refuting

To prove $\exists x \in A \; P(x)$, the usual method is to name a witness $a$, check $a \in A$, and check $P(a)$; this is a [[constructive proof|01XM7JEKHY]].
A [[non-constructive existence proof|JZQVJ9XT63]] shows that a witness exists without naming one, for example by deriving a contradiction from $\forall x \in A \; \neg P(x)$.
In the [[interpretation of Brouwer, Heyting and Kolmogorov|1VFH9WT1RZ]], a proof of $\exists x \, P(x)$ is a pair of an element $a$ and a proof of $P(a)$.
So the step from $\neg \forall x \, \neg P(x)$ to $\exists x \, P(x)$ is not valid intuitionistically, because a contradiction does not produce an element.
Non-constructive proofs use this step or the [[law of excluded middle|0RYYK8PG4S]].
To refute $\exists x \in A \; P(x)$, prove $\forall x \in A \; \neg P(x)$ for an arbitrary element.

### Watch out

The quantifier $\exists$ does not distribute over $\land$.
On $\mathbb{Z}$, "some integer is even, and some integer is odd" is true, but "some integer is even and odd" is false.
The direction from $\exists x \, (P(x) \land Q(x))$ to $\exists x \, P(x) \land \exists x \, Q(x)$ is fine.
A second error is to use one letter for two witnesses, as in "$m$ and $n$ are even, so $m = 2k$ and $n = 2k$", which silently forces $m = n$; see [[one letter for two existential witnesses|FDT6332G8D]].
A third is to read "there exists" as "there exists exactly one", and so to reject a statement with two witnesses.

### History

Gottlob Frege, in his Begriffsschrift of 1879, had no separate existential sign; he wrote "some $x$ is $P$" as "not every $x$ is not $P$".
Charles Sanders Peirce and his student Oscar Howard Mitchell introduced existential quantifiers as a separate notion in the 1880s, and Peirce wrote them as sums $\Sigma$.
Aristotle's syllogistic already studied sentences of the form "some $A$ is $B$", which modern logic writes as $\exists x \, (A(x) \land B(x))$.

### Try it

Is $\exists n \in \mathbb{N} \; (n^2 + n + 41 \text{ is not prime})$ true?
Yes: $n = 40$ gives $1681 = 41^2$.

Is $\exists x \in \mathbb{R} \; (x^2 - 4x + 5 = 0)$ true?
No: $x^2 - 4x + 5 = (x - 2)^2 + 1 \ge 1$ for every real $x$, so there is no witness.

## Explanations

### L1 human

"Some student in the class has a red pen" is a "there exists" statement.
It is true as soon as we find one student with a red pen, and we do not need to look at the others.
It is false only when no student has a red pen, so to show that it is false we must check every student.
With numbers, "some number from $1$ to $5$ is greater than $4$" is true because of $5$, and "some number from $1$ to $5$ is greater than $10$" is false.

### L2 human

Decide whether $\exists x \in \mathbb{R} \; (x^2 - 5x + 6 = 0)$ is true.
Try $x = 2$: $4 - 10 + 6 = 0$, so $x = 2$ is a witness, and existential generalization gives the statement.
The witness is not unique, since $x = 3$ gives $9 - 15 + 6 = 0$, and the statement does not claim uniqueness.
Now decide whether $\exists x \in \mathbb{R} \; (x^2 - 4x + 5 = 0)$ is true.
To refute it, prove the negation $\forall x \in \mathbb{R} \; (x^2 - 4x + 5 \neq 0)$.
For an arbitrary real $x$, $x^2 - 4x + 5 = (x - 2)^2 + 1 \ge 1$, so no real number is a witness.
Definitions such as "$a$ divides $b$", which is $\exists k \in \mathbb{Z} \; (b = ak)$, are the most common use of $\exists$.
Watch out: trying a few values, finding no witness, and concluding that none exists is not a refutation.

### L3 human

In a structure $\mathcal{M}$ with domain $M$, Tarski's definition of [[satisfaction|2RBQPV02AS]] says that $\mathcal{M} \models \exists x \, \varphi[s]$ when $\mathcal{M} \models \varphi[s(x \mapsto a)]$ for some $a \in M$.
So $\exists$ is an infinite disjunction over the domain, and in a complete [[Boolean algebra|0XADJKM699]] or [[Heyting algebra|NG943XNQWH]] of truth values it is a join.
In categorical logic, $\exists$ along a projection is the left adjoint of the weakening map, which explains why it commutes with $\lor$ and not in general with $\land$.

In type theory, a proof of $\exists x \in A \; P(x)$ is a dependent pair, and Lean's `Exists` is the version of this type that lives in `Prop`, so a proof does not expose its witness to computation.
Skolemization replaces $\forall x \, \exists y \, \varphi(x, y)$ by $\forall x \, \varphi(x, f(x))$ with a new function symbol $f$, which preserves satisfiability.
Heyting arithmetic has the existence property: if it proves a closed sentence $\exists n \, \varphi(n)$, then it proves $\varphi(\bar{k})$ for some numeral $\bar{k}$.
Peano arithmetic lacks it: for each sentence $G$ it proves $\exists n \, ((n = 0 \land G) \lor (n = 1 \land \neg G))$, and for an undecidable $G$ it proves no instance.
