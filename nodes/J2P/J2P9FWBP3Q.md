---
tag: J2P9FWBP3Q
kind: statement
role: theorem
name: Equivalence of induction and well-ordering
msc: ["03F30", "00A35"]
topics: [EEH2F76CYQ]
audience: ug1
about: [0ASJVEFA9J, 0KMVFSHFGZ, 01BX15HSRR]
uses: [0ASJVEFA9J, 0KMVFSHFGZ, 01BX15HSRR, 0QFT7Z76N5, 0832XVR512]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Relationship to the well-ordering principle
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Equivalence with ordinary induction
  - url: https://en.wikipedia.org/wiki/Well-ordering_principle
    locator: lead section
---

## Statement

Ordinary induction, strong induction and the well-ordering principle are three ways to say the same thing about the natural numbers, once the basic facts about successor and order are fixed.

Let $N$ be a set with an element $0$, a map $S \colon N \to N$ (the [[successor|0832XVR512]] map) and a relation $<$ on $N$, and write $x \le y$ for "$x < y$ or $x = y$".
The base theory consists of four conditions.

1. (B1) The relation $<$ is a strict linear order: no $x$ satisfies $x < x$, $x < y < z$ gives $x < z$, and for all $x, y$ exactly one of $x < y$, $x = y$, $y < x$ holds.
2. (B2) No element $x$ satisfies $x < 0$.
3. (B3) For each $n$, $n < S(n)$, and no $m$ satisfies $n < m < S(n)$.
4. (B4) Each $n \ne 0$ equals $S(k)$ for some $k \in N$.

The three principles, each stated for all subsets $A \subseteq N$, are these.

1. (I) Induction: if $0 \in A$, and $n \in A$ implies $S(n) \in A$ for each $n$, then $A = N$.
2. (SI) Strong induction: if, for each $n$, the inclusion $\{k \in N : k < n\} \subseteq A$ implies $n \in A$, then $A = N$.
3. (WO) Well-ordering: if $A \ne \emptyset$, then $A$ has a least element, an $a \in A$ with $a \le x$ for every $x \in A$.

Theorem: if $N$ satisfies (B1) to (B4), then (I), (SI) and (WO) are equivalent.

## Remarks

### The natural numbers as the main case

The theorem is about the [[natural numbers|0MWKJ44V5A]], with $S(n) = n + 1$ and the usual order, and there (B1) to (B4) all hold.
The abstract form only makes visible which facts each step of the proof uses.
In the [[Peano axioms|0QFT7Z76N5]] the order is defined by $m < n$ when $m + c = n$ for some $c \ne 0$, and then (B1) to (B4) are theorems proved with induction.
They are Lemmas A, B and C of the [[proof of strong induction|C54QYDXFP3]] and Lemma T of the [[proof of the well-ordering principle|QPX5Z5YFH8]].
So the precise claim is this: given the other Peano axioms and (B1) to (B4), the induction axiom can be replaced by (SI) or by (WO).
The principles quantify over all subsets of $N$, as in the second-order Peano axioms.

### How the proof goes

The [[proof by a cycle of implications|4PY5VF3XS4]] shows that (I) implies (SI), that (SI) implies (WO), and that (WO) implies (I).
Each arrow changes the set to which the principle is applied.
To get (SI) from (I), apply induction to the set of $n$ below which everything is in $A$.
To get (WO) from (SI), apply strong induction to the complement of a set with no least element.
To get (I) from (WO), take the least element outside $A$, and note that it is the successor of an element inside $A$.

### Why each hypothesis is needed

Condition (B4), "each nonzero element has a predecessor", is needed for (WO) to imply (I).
Take $N = \{0, 1\} \times \mathbb{N}$ in lexicographic order, with $0 = (0, 0)$ and $S(i, n) = (i, n + 1)$.
This structure satisfies (B1) to (B3), (WO) and (SI), but the first copy $\{0\} \times \mathbb{N}$ contains $0$, is closed under $S$ and is not all of $N$, so (I) fails.
The L2 explanation checks this in detail.

Condition (B1) is used to get (WO) from (SI).
A least element must be compared with every element, and without a linear order an element with nothing below it need not be least.
Conditions (B2) and (B3) are used to get (SI) from (I).
Together they say that the elements below $S(n)$ are the elements below $n$ and $n$ itself.

### What it gives you

Any one of the three principles can serve as the axiom, and then the other two are theorems, which is why books differ on which one they take first.
Proofs by [[minimal counterexample|JGRCNPKNGG]] and by [[infinite descent|0EFYCFHYFG]] are therefore valid exactly when induction is.
In a proof you may choose the most convenient form: induction for a step from $n$ to $n + 1$, strong induction for a step to an unknown smaller case, and well-ordering for a smallest counterexample.

### A direct proof that strong induction gives induction

This direction needs only (B3) and (B4).
Let $A$ satisfy the hypotheses of (I), and suppose $\{k : k < n\} \subseteq A$.
If $n = 0$, then $n \in A$.
Otherwise $n = S(k)$ by (B4), and $k < n$ by (B3), so $k \in A$ and $n = S(k) \in A$.
So $A$ satisfies the hypothesis of (SI), and (SI) gives $A = N$.
The structure $\{0, 1\} \times \mathbb{N}$ above satisfies (SI) but not (I), so (B4) is needed here too.

### Watch out

A claim such as "well-ordering implies induction" with no base theory is false, and the two-copy structure above is a counterexample.
State the base theory whenever you state the equivalence.
The condition (B4) is used only in the arrows that end at (I), so a proof of (I) from (WO) or (SI) must use a predecessor somewhere.

### Generalizations

For any set $X$ with a relation $R$, the analogue of (WO) says that $R$ is well-founded, with "minimal element" in place of "least element", and the analogue of (SI) is well-founded induction.
These two are equivalent for every relation, with no analogue of (B1) to (B4), and the general form belongs to set theory together with transfinite induction.
The first-order versions of the three principles, as schemes for formulas of arithmetic, are compared in mathematical logic.

### Try it

Which of (B1) to (B4) fails for $N = \mathbb{Z}$ with $S(n) = n + 1$ and the usual order?
(B2) fails, because $-1 < 0$, and (B1), (B3) and (B4) hold.

## History

Textbooks state the equivalence in several versions, and the versions differ in the base theory that they assume.

## Explanations

### L1 human

There are three ways to say that the counting numbers have no hidden parts.
Induction says that a property true for $0$ and passed from each number to the next holds for all numbers.
Strong induction says that a property passed to each number from all the numbers below it holds for all numbers.
Well-ordering says that every collection of counting numbers that is not empty has a smallest member.
The theorem says that the three rules say the same thing, once we know basic facts about the order, such as "nothing lies between $3$ and $4$".

### L2 human

We check the two-copy counterexample in detail, to see why (B4) matters.
The set $N$ is $\mathbb{N}$ followed by a second copy of $\mathbb{N}$:
$$(0, 0) < (0, 1) < (0, 2) < \cdots < (1, 0) < (1, 1) < (1, 2) < \cdots.$$
Every nonempty subset $A$ has a least element: if $A$ meets the first copy, take the least $n$ with $(0, n) \in A$, and otherwise the least $n$ with $(1, n) \in A$.
So (WO) holds.
The element $(1, 0)$ is not $S$ of anything, because every $S(i, n) = (i, n + 1)$ has second entry at least $1$, so (B4) fails.
The first copy contains $0$ and is closed under $S$, and it misses $(1, 0)$, so (I) fails.

The lesson is about how the principles are compared: they are equivalent over a base theory, not on their own.
Watch out: in this structure (B1) to (B3) all hold, so the failure comes from (B4) alone.

### L3 human

In the second-order setting, (I) says that no proper subset of $N$ contains $0$ and is closed under $S$, so $N$ is generated by $0$ and $S$.
(WO) together with (B1) says that $<$ is a well-order, and then (B2) to (B4) force the order type $\omega$ of $\mathbb{N}$.
The counterexample has order type $\omega \cdot 2$, the least order type after $\omega$ of a well-order with no largest element.
In first-order arithmetic the induction schema and the least number schema are compared formula class by formula class, which is a topic of mathematical logic.
In type theory, induction for an inductive type is the primitive principle, given by its recursor such as `Nat.rec`, and well-founded induction is derived from it.
