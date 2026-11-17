---
tag: 0GHS47PDAQ
kind: concept
name: Universal quantifier
aliases: [for-all, universal-quantification]
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
uses: [0QHEWQD30B, 0ZGC7ZESYN, 0NMG7W7Q11]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
  - book: isbn:9781108439534
    locator: Section 2.2
  - book: isbn:9781108439534
    locator: Section 3.3
same_as:
  wikidata: Q126695
  wikipedia: Universal quantification
---

## Summary

Let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0QHEWQD30B]] on $D$.
The universal quantification of $P$ is the [[proposition|0ZGC7ZESYN]] $\forall x \, P(x)$, read "for all $x$, $P(x)$", which is true when $P(a)$ is true for every $a \in D$, and false when $P(a)$ is false for at least one $a \in D$.
The quantifier $\forall x$ binds the variable $x$; when $P$ has other free variables, $\forall x \, P(x, y)$ is a predicate in the remaining variables.
For a subset $A$ of $D$, the restricted form $\forall x \in A \; P(x)$ is an abbreviation of $\forall x \, (x \in A \to P(x))$, and it is true when every element of $A$ satisfies $P$.
Most definitions and theorems of mathematics are universal statements, so the truth conditions of $\forall$ decide what a proof must show and what a [[counterexample|0ED72CTBNP]] must show.
The precise definition is on the page [[universal quantifier (definition)|0B88PQTJ66]], and the reading of "for all", "every", "each" and "any" in mathematical English is on the page [[quantifiers in mathematical writing|EGTZPA6QH3]].

## Motivation

On a finite domain $D = \{a_1, \dots, a_n\}$, the statement "every element has the property $P$" is the conjunction $P(a_1) \land \dots \land P(a_n)$.
On an infinite domain, such as $\mathbb{N}$, no finite conjunction can say the same thing.
A statement such as "for every natural number $n$, $n^2 + n$ is even" needs a symbol that speaks about all elements at once.
The universal quantifier is this symbol, and it lets one formula express a law with infinitely many instances.

## Notation

The universal quantification of $P$ is written $\forall x \, P(x)$, $\forall x \colon P(x)$, $\forall x, \, P(x)$ or $(\forall x) \, P(x)$; older books write $(x) \, P(x)$, and some books write $\bigwedge_x P(x)$.
The restricted forms are written $\forall x \in A \; P(x)$, $(\forall x \in A) \, P(x)$ or, for an order, $\forall x > 0 \; P(x)$, which means $\forall x \, (x > 0 \to P(x))$.
Two quantifiers of the same kind are often merged: $\forall x, y \in \mathbb{R}$ means $\forall x \in \mathbb{R} \; \forall y \in \mathbb{R}$.
In Lean, $\forall$ is a basic part of the language, and a proof of `∀ x, P x` is a function that sends each `x` to a proof of `P x`.
In the notation of this sub-area, $D$ is the domain, $x, y$ are variables and $P, Q$ are predicates.

## Remarks

### Examples

1. [[For every integer $n$, $n^2 + n$ is even|CXY4EJ2K4X]]: true; checked on a finite domain as a conjunction and proved on $\mathbb{Z}$ with an arbitrary element.
2. [[The statement $\forall n \in \mathbb{N} \; (n^2 \le 2^n)$ is false|ZHVZGEWE9J]]: refuted by the counterexample $n = 3$, and true after the restriction to $n \ge 4$.
3. $\forall x \in \mathbb{R} \; (x^2 \ge 0)$ is true, because the square of a real number is never negative.
4. $\forall x \in \varnothing \; P(x)$ is true for each predicate $P$; this is a [[vacuous truth|0V4QXPGJQK]].
5. The definition of a [[subset|0BJR9QR08E]] is universal: $A \subseteq B$ means $\forall x \, (x \in A \to x \in B)$.

### Non-examples

1. [[The formula $\forall x \, (x \in \mathbb{N} \land x \ge 0)$ is not the restricted statement $\forall x \in \mathbb{N} \; (x \ge 0)$|YQH9WAA6X8]]: with $\land$ in place of $\to$, the formula claims that every element of the domain is a natural number.
2. "Some prime number is even" is not universal: it is true because of the one witness $2$, while "every prime number is even" is false because of $3$. It uses the [[existential quantifier|0MSRQHCNN9]].
3. The open sentence $x^2 \ge 0$ alone is not a universal statement: $x$ is free, so it is a predicate. The page [[a conditional with a hidden quantifier|FWXPGJBK97]] shows how mathematical writing leaves $\forall$ unwritten.

### Basic properties

1. On a finite domain $\{a_1, \dots, a_n\}$, $\forall x \, P(x)$ is equivalent to $P(a_1) \land \dots \land P(a_n)$.
2. Universal instantiation: from $\forall x \, P(x)$ and $a \in D$, conclude $P(a)$. [[Universal generalization|BKQ3YD6SVZ]]: if $P(x)$ is proved for an arbitrary $x$, conclude $\forall x \, P(x)$.
3. Negation: $\neg \forall x \, P(x)$ is equivalent to $\exists x \, \neg P(x)$. This is the [[negation of a universal statement|0P3A06QNDP]], `Classical.not_forall` in Mathlib; only the direction from $\exists x \, \neg P(x)$ to $\neg \forall x \, P(x)$ holds in [[intuitionistic logic|Q11N8X99FK]].
4. For the restricted form, $\neg \forall x \in A \; P(x)$ is equivalent to $\exists x \in A \; \neg P(x)$. Unfolded: $\neg \forall x \, (x \in A \to P(x))$ is equivalent to $\exists x \, (x \in A \land \neg P(x))$.
5. $\forall$ distributes over $\land$: $\forall x \, (P(x) \land Q(x))$ is equivalent to $\forall x \, P(x) \land \forall x \, Q(x)$.
6. $\forall$ does not distribute over $\lor$. On $\mathbb{Z}$, with $P(x)$ "$x$ is even" and $Q(x)$ "$x$ is odd", $\forall x \, (P(x) \lor Q(x))$ is true, while $\forall x \, P(x)$ and $\forall x \, Q(x)$ are both false. The other direction holds.
7. Two universal quantifiers commute: $\forall x \, \forall y \, P(x, y)$ is equivalent to $\forall y \, \forall x \, P(x, y)$. A universal and an existential quantifier do not commute in general; see [[order of quantifiers|0FYQMKFE77]].
8. If $D$ is nonempty, $\forall x \, P(x)$ implies $\exists x \, P(x)$. For the restricted form this needs $A \neq \varnothing$.
9. When $x$ is not free in $q$, $\forall x \, (P(x) \to q)$ is equivalent to $(\exists x \, P(x)) \to q$. This rule is used to move quantifiers in [[prenex normal form|CS82V969DE]].

### Proving and refuting

To prove $\forall x \in A \; P(x)$, we take an arbitrary element $x$ of $A$ and prove $P(x)$; the method is on the page [[proving universal statements|CX38X989TB]].
On a small finite set, a check of every element is also a proof.
To refute $\forall x \in A \; P(x)$, one element $a \in A$ with $P(a)$ false is enough; this is a [[counterexample|0ED72CTBNP]].
Any number of examples with $P(a)$ true does not prove the statement; this error is [[proof by example|ZX6ERT3SW7]].

### History

Gottlob Frege introduced a notation for generality, the first universal quantifier of modern logic, in his Begriffsschrift of 1879.
Charles Sanders Peirce introduced quantifiers independently in the 1880s.
Aristotle's syllogistic already studied sentences of the form "every $A$ is $B$", which modern logic writes as $\forall x \, (A(x) \to B(x))$.

### Common errors

1. A student writes $\forall x \, (x \in A \land P(x))$ for "every element of $A$ has the property $P$". The correct form uses $\to$.
2. A student "proves" a universal statement by checking a few cases. A finite check proves it only when the domain is that finite set.
3. A student moves $\forall$ through $\lor$, and concludes from "every integer is even or odd" that "every integer is even or every integer is odd".

## Explanations

### L1 human

"Every student in the class has a pen" is a "for all" statement.
It is true when each student, one by one, has a pen.
It is false as soon as one student has no pen; that student is a counterexample.
With numbers: "every number from $1$ to $5$ is less than $10$" is true, because $1, 2, 3, 4, 5$ are all less than $10$.
"Every number from $1$ to $5$ is odd" is false, because $2$ is even.

### L2 human

We decide whether $\forall x \in \mathbb{R} \; (x^2 - 4x + 5 > 0)$ is true.

1. Let $x$ be an arbitrary real number. We use no other property of $x$.
2. Complete the square: $x^2 - 4x + 5 = (x - 2)^2 + 1$.
3. A square of a real number is at least $0$, so $(x - 2)^2 + 1 \ge 1 > 0$.
4. Since $x$ was arbitrary, the statement holds for every real $x$, by universal generalization.

Now change the constant: $\forall x \in \mathbb{R} \; (x^2 - 4x + 3 > 0)$.

5. At $x = 2$, $4 - 8 + 3 = -1$, which is not greater than $0$.
6. So $x = 2$ is a counterexample, and the statement is false.

The typical use of the universal quantifier is in the statement of a theorem, which fixes what the proof must cover: every element of the domain.
A trap is to choose a special value in step 1, such as $x = 0$; then the proof covers only that value.

### L3 human

In a structure $\mathcal{M}$ with domain $M$, Tarski's definition of [[satisfaction|2RBQPV02AS]] says that $\mathcal{M} \models \forall x \, \varphi[s]$ when $\mathcal{M} \models \varphi[s(x \mapsto a)]$ for every $a \in M$, where $s$ assigns values to the other free variables.
So $\forall$ is an infinite conjunction over the domain, and in a complete [[Boolean algebra|0XADJKM699]] or [[Heyting algebra|NG943XNQWH]] of truth values it is interpreted as a meet.
In categorical logic, $\forall$ along a projection is the right adjoint of the weakening map, and $\exists$ is its left adjoint; this explains why $\forall$ commutes with $\land$ and $\exists$ commutes with $\lor$.

Standard [[first-order logic|086QKPF0A6]] assumes a nonempty domain, which makes $\forall x \, P(x) \to \exists x \, P(x)$ valid; the restricted form over a set keeps vacuous truth for the empty set.
In type theory, a proof of $\forall x \in A \; P(x)$ is a function that takes $x$ and returns a proof of $P(x)$, so the quantifier is a dependent function type.
Second-order logic allows $\forall$ over predicates and sets, as in the induction axiom $\forall P \, (P(0) \land \forall n \, (P(n) \to P(n + 1)) \to \forall n \, P(n))$.
