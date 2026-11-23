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

The universal quantifier turns a property into a law: "for all $x$, $P(x)$" says that every object in the domain has the property.
"Every number from $1$ to $5$ is less than $10$" is true because each of $1, 2, 3, 4, 5$ passes the test, and "every number from $1$ to $5$ is odd" is false because $2$ fails.
In general, let $D$ be a domain of discourse and $P(x)$ a [[predicate|0QHEWQD30B]] on $D$.
The [[proposition|0ZGC7ZESYN]] $\forall x \, P(x)$ is true when $P(a)$ is true for every $a \in D$, and false when $P(a)$ is false for at least one $a \in D$.
For a subset $A$ of $D$, the restricted form is an abbreviation:
$$\forall x \in A \; P(x) \quad \text{means} \quad \forall x \, (x \in A \to P(x)).$$
The [[formal definition|0B88PQTJ66]] states this with every condition, and [[quantifiers in mathematical writing|EGTZPA6QH3]] explains how "for all", "every", "each" and "any" are read.

## Motivation

On a finite domain $\{a_1, \dots, a_n\}$, "every element has property $P$" is the conjunction $P(a_1) \land \dots \land P(a_n)$.
On an infinite domain such as $\mathbb{N}$, no finite conjunction can say the same thing.
"For every natural number $n$, $n^2 + n$ is even" has infinitely many instances, and it needs a symbol that speaks about all of them at once.

Most definitions and theorems in mathematics are universal statements, so the truth conditions of $\forall$ decide what a proof has to cover and what a [[counterexample|0ED72CTBNP]] has to show.
The definition of a [[subset|0BJR9QR08E]] is universal: $A \subseteq B$ means $\forall x \, (x \in A \to x \in B)$.
Continuity, convergence and divisibility statements all begin with $\forall$, and the [[order of quantifiers|0FYQMKFE77]] decides what they mean.

## Notation

Books write $\forall x \, P(x)$, $\forall x \colon P(x)$, $\forall x, \, P(x)$ or $(\forall x) \, P(x)$; older books write $(x) \, P(x)$, and some write $\bigwedge_x P(x)$.
The restricted form is written $\forall x \in A \; P(x)$ or $(\forall x \in A) \, P(x)$, and other conditions work the same way: $\forall x > 0 \; P(x)$ means $\forall x \, (x > 0 \to P(x))$.
Quantifiers of the same kind are often merged, so $\forall x, y \in \mathbb{R}$ means $\forall x \in \mathbb{R} \; \forall y \in \mathbb{R}$.
In Lean, $\forall$ is built into the language, and a proof of `∀ x, P x` is a function that sends each `x` to a proof of `P x`.

## Remarks

### A first check on a small domain

Let $P(n)$ be "$n^2 + n$ is even" on $D = \{1, 2, 3, 4, 5\}$, as in [[for every integer $n$, $n^2 + n$ is even|CXY4EJ2K4X]].
The values are
$$2, \quad 6, \quad 12, \quad 20, \quad 30,$$
all even, so the conjunction of the five instances is true, and so is $\forall n \in D \; P(n)$.
On $\mathbb{Z}$ the same check never ends, so you prove it for an arbitrary $n$: $n^2 + n = n(n + 1)$, and one of two consecutive integers is even.
That switch, from checking every element to arguing about an arbitrary one, is the method of [[proving universal statements|CX38X989TB]].

### One counterexample is enough

[[The statement $\forall n \in \mathbb{N} \; (n^2 \le 2^n)$ is false|ZHVZGEWE9J]], even though it holds for $n = 0, 1, 2$ and for every $n \ge 4$.
At $n = 3$ we get $9 > 8$, and that single failure refutes the statement.
On the other side, no number of true instances proves a universal statement on an infinite domain; trusting them is the error of [[proof by example|ZX6ERT3SW7]].
The statement $\forall x \in \varnothing \; P(x)$ is true for every $P$, because no counterexample can exist; this is [[vacuous truth|0V4QXPGJQK]].

### What is not universal

[[The formula $\forall x \, (x \in \mathbb{N} \land x \ge 0)$ is not the restricted statement $\forall x \in \mathbb{N} \; (x \ge 0)$|YQH9WAA6X8]].
With $\land$ in place of $\to$, it claims that every element of the domain is a natural number, and $x = -1$ refutes it.
"Some prime is even" is not universal: it uses the [[existential quantifier|0MSRQHCNN9]], and the one witness $2$ makes it true.
The open sentence $x^2 \ge 0$ is not a statement at all, because $x$ is free, although mathematical writing often leaves the $\forall$ unwritten, as in [[a conditional with a hidden quantifier|FWXPGJBK97]].

### The rules you can use

Universal instantiation concludes $P(a)$ from $\forall x \, P(x)$ and $a \in D$, and [[universal generalization|BKQ3YD6SVZ]] concludes $\forall x \, P(x)$ from a proof of $P(x)$ for an arbitrary $x$.
The negation $\neg \forall x \, P(x)$ is equivalent to $\exists x \, \neg P(x)$, the [[negation of a universal statement|0P3A06QNDP]], which is `Classical.not_forall` in Mathlib.
In [[intuitionistic logic|Q11N8X99FK]] only the direction from $\exists x \, \neg P(x)$ to $\neg \forall x \, P(x)$ holds.
The quantifier $\forall$ distributes over $\land$: $\forall x \, (P(x) \land Q(x))$ is equivalent to $\forall x \, P(x) \land \forall x \, Q(x)$.
Two universal quantifiers commute, but $\forall$ and $\exists$ do not, as the [[order of quantifiers|0FYQMKFE77]] shows.
When $x$ is not free in $q$, $\forall x \, (P(x) \to q)$ is equivalent to $(\exists x \, P(x)) \to q$, a rule used to reach [[prenex normal form|CS82V969DE]].
If $D$ is nonempty, $\forall x \, P(x)$ implies $\exists x \, P(x)$.

### Watch out

The quantifier $\forall$ does not distribute over $\lor$.
On $\mathbb{Z}$, "every integer is even or odd" is true, but "every integer is even, or every integer is odd" is false, because both parts fail.
The other direction is fine: if every integer were even, then every integer would be even or odd.
Also watch the connective inside a restricted statement: "every element of $A$ has property $P$" is $\forall x \, (x \in A \to P(x))$, never $\forall x \, (x \in A \land P(x))$.

### History

Gottlob Frege introduced a notation for generality, the first universal quantifier of modern logic, in his Begriffsschrift of 1879.
Charles Sanders Peirce introduced quantifiers independently in the 1880s.
Aristotle's syllogistic already studied sentences of the form "every $A$ is $B$", which modern logic writes as $\forall x \, (A(x) \to B(x))$.

### Try it

Is $\forall x \in \mathbb{R} \; (x^2 - 4x + 5 > 0)$ true?
Yes: $x^2 - 4x + 5 = (x - 2)^2 + 1 \ge 1$ for every real $x$.

Is $\forall x \in \mathbb{R} \; (x^2 - 4x + 3 > 0)$ true?
No: at $x = 2$ the value is $4 - 8 + 3 = -1$, so $x = 2$ is a counterexample.

## Explanations

### L1 human

"Every student in the class has a pen" is a "for all" statement.
It is true when each student, one by one, has a pen.
It is false as soon as one student has no pen, and that student is a counterexample.
With numbers, "every number from $1$ to $5$ is less than $10$" is true, and "every number from $1$ to $5$ is odd" is false because of $2$.

### L2 human

Decide whether $\forall x \in \mathbb{R} \; (x^2 - 4x + 5 > 0)$ is true.
Let $x$ be an arbitrary real number, and use no other property of it.
Complete the square:
$$x^2 - 4x + 5 = (x - 2)^2 + 1.$$
A square of a real number is at least $0$, so $(x - 2)^2 + 1 \ge 1 > 0$.
Since $x$ was arbitrary, universal generalization gives the statement for every real $x$.
Change the constant to $3$ and the statement fails, since $x = 2$ gives $-1$.
A theorem that starts with $\forall$ fixes what its proof must cover, namely every element of the domain.
Watch out: if you choose a special value at the start, such as $x = 0$, the proof covers only that value.

### L3 human

In a structure $\mathcal{M}$ with domain $M$, Tarski's definition of [[satisfaction|2RBQPV02AS]] says that $\mathcal{M} \models \forall x \, \varphi[s]$ when $\mathcal{M} \models \varphi[s(x \mapsto a)]$ for every $a \in M$, where $s$ assigns values to the other free variables.
So $\forall$ is an infinite conjunction over the domain, and in a complete [[Boolean algebra|0XADJKM699]] or [[Heyting algebra|NG943XNQWH]] of truth values it is a meet.
In categorical logic, $\forall$ along a projection is the right adjoint of the weakening map and $\exists$ is its left adjoint, which explains why $\forall$ commutes with $\land$ and $\exists$ commutes with $\lor$.

Standard [[first-order logic|086QKPF0A6]] assumes a nonempty domain, which makes $\forall x \, P(x) \to \exists x \, P(x)$ valid, while the restricted form over a set keeps vacuous truth for the empty set.
In type theory, a proof of $\forall x \in A \; P(x)$ is a function from $A$ to proofs, so the quantifier is a dependent function type.
Second-order logic allows $\forall$ over predicates, as in the induction axiom $\forall P \, (P(0) \land \forall n \, (P(n) \to P(n + 1)) \to \forall n \, P(n))$.
