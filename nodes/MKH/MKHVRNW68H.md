---
tag: MKHVRNW68H
kind: concept
name: Set equality by double inclusion
aliases: [double-inclusion, proving-set-equality-by-double-inclusion, element-chasing]
msc: ["00A35", "03E20"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: school
specializes: [0B94TKFQJX]
uses: [0BSJ7RQ9BW, 0BJR9QR08E, 0TB16T2C97, 0NTF6DMVAP, EGTZPA6QH3]
sources:
  - url: https://en.wikipedia.org/wiki/Subset
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Axiom_of_extensionality
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Summary

To prove that two [[sets|0BSJ7RQ9BW]] are equal, show that each is contained in the other.
This splits one large claim about all elements into two smaller claims, and each of them has the familiar shape "take an element, follow it, see where it lands".

Here is the pattern on a real goal, the distributive law
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C).$$
For the inclusion $\subseteq$, take $x$ in the left side.
Then $x \in A$, and $x \in B$ or $x \in C$; in the first case $x \in A \cap B$, and in the second $x \in A \cap C$, so $x$ is in the right side.
For the inclusion $\supseteq$, take $x$ in the right side; in either case $x \in A$, and $x$ lies in $B$ or in $C$, so $x$ is in the left side.
The [[worked example|PR03MQRDPD]] writes out every step.

In general, the method rests on the rule
$$A \subseteq B \ \text{ and } \ B \subseteq A \implies A = B,$$
where $A \subseteq B$ means that every element of $A$ is an element of $B$.
The rule holds by the [[axiom of extensionality|0TB16T2C97]]: two sets with the same elements are equal.

## Motivation

A set has no formula that you can expand or simplify, the way you expand $(x + 1)^2$.
It is fixed only by its elements, so the claim $A = B$ speaks about every element at once.
Double inclusion cuts that claim into two [[subset|0BJR9QR08E]] claims.
Each one is a universal conditional, "for every $x$, if $x \in A$ then $x \in B$", and you prove it by a [[direct proof|0NTF6DMVAP]] that starts with an arbitrary element.

The goal $A = B$ turns up everywhere in a first course.
The solution set of an equation equals a list of numbers, the kernel of a map equals a subspace, an image equals an interval, two subgroups are the same.
A Venn diagram can suggest such an identity, but it shows only one position of the sets.
Double inclusion turns the picture into an argument that covers every position, including empty and equal sets.
The same idea for numbers is [[equality by two inequalities|S3QADD13E9]], and the next method in the list, [[proving injectivity and surjectivity|DD2P85Y8E9]], uses element chasing in the same way.

## Notation

We write $A \subseteq B$ for "$A$ is a subset of $B$" and $B \supseteq A$ for the same relation read from the other side.
Some books write $A \subset B$ for the same thing, and others keep $A \subset B$ for a proper subset, with $A \ne B$; this is a [[conflicting convention|CSFEP56A7D]], so check the convention of each book.
The two halves of a written proof are often headed "($\subseteq$)" and "($\supseteq$)".
In Lean's Mathlib, `Set.Subset.antisymm` turns two inclusions into an equality, `Set.ext` says that sets with the same elements are equal, and the tactic `ext x` starts an element-chasing proof.

## Remarks

### Why two halves, and why each is a direct proof

The inclusion $A \subseteq B$ is the statement
$$\forall x \, (x \in A \implies x \in B),$$
so its proof starts "Let $x \in A$" and ends "so $x \in B$", with the [[quantifier|EGTZPA6QH3]] handled by taking $x$ arbitrary.
Equality needs the same for the other direction, which is a different statement with a different start.
Together the two halves prove the biconditional "$x \in A \iff x \in B$ for every $x$", and that is exactly what extensionality asks for.

When every step of a chain $x \in A \iff \dots \iff x \in B$ is a true equivalence, one chain does both halves at once.
Then you must check each step in both directions, which is the same amount of work in a shorter form.

### Two more worked goals

The multiples of $6$ are exactly the integers that are multiples of both $2$ and $3$:
$$6\mathbb{Z} = 2\mathbb{Z} \cap 3\mathbb{Z}.$$
The half $\subseteq$ is regrouping, since $6k = 2(3k) = 3(2k)$.
The half $\supseteq$ needs an idea: if $n = 2a = 3b$, then
$$n = 3n - 2n = 3(2a) - 2(3b) = 6(a - b).$$
Check: $n = 18$ has $a = 9$ and $b = 6$, and $6(9 - 6) = 18$.
The [[example on multiples of 6|2ZCM9HEME2]] gives the details and shows why the trick needs $\gcd(2, 3) = 1$.

For an equation, double inclusion says that a list of numbers is the full solution set.
The solution set of $x^2 - 5x + 6 = 0$ in $\mathbb{R}$ is $\{2, 3\}$.
The half $\supseteq$ is substitution, $4 - 10 + 6 = 0$ and $9 - 15 + 6 = 0$.
The half $\subseteq$ uses the factorization $x^2 - 5x + 6 = (x - 2)(x - 3)$: a product of real numbers is $0$ only when a factor is $0$.

### A goal where only one half holds

For a function $f$ and subsets $A$ and $B$ of its domain, the inclusion
$$f(A \cap B) \subseteq f(A) \cap f(B)$$
always holds, but the reverse can fail.
With $f(x) = x^2$, $A = \{-1\}$ and $B = \{1\}$, the left side is $f(\varnothing) = \varnothing$, and the right side is $\{1\}$.
So the attempt at double inclusion breaks at the half $\supseteq$, and the [[failed proof|7T5N9T8W2X]] shows the exact step.
When a half resists, test it on a small case: often the true theorem is the one inclusion.

To prove $A \ne B$, one element is enough: an element of one set that is not in the other.
Here $1$ is that element.

### Watch out

The most common slip is to prove one inclusion twice.
The second half starts again with "Let $x \in A$", renames the variable, and proves $A \subseteq B$ a second time.
One inclusion never gives equality, since $\{1\} \subseteq \{1, 2\}$ and the two sets differ.
Start the second half with an element of $B$.

A second slip is to start with a particular element, such as "Let $x = 3$".
The element must be arbitrary, or the argument says nothing about the other elements.
A third slip is a step that holds in only one direction inside a chain of "if and only if" signs; such a chain proves only one inclusion.

### History

The method rests on the axiom of extensionality.
Ernst Zermelo listed it as the first axiom of his 1908 axiom system for set theory.

### Try it

Prove $A \cup (A \cap B) = A$.
For $\subseteq$, an element of $A \cup (A \cap B)$ is in $A$ or in $A \cap B$, and in both cases it is in $A$.
For $\supseteq$, an element of $A$ is in the union by the definition of union.

Is $A \setminus (B \setminus C) = (A \setminus B) \setminus C$ for all sets?
No: with $A = \{1\}$, $B = \{1\}$ and $C = \{1\}$, the left side is $\{1\} \setminus \varnothing = \{1\}$, and the right side is $\varnothing \setminus \{1\} = \varnothing$.

## Explanations

### L1 human

Two boxes of marbles hold the same marbles when nothing in the first box is missing from the second, and nothing in the second box is missing from the first.
You need both checks.
If you only check the first box, the second box could hold extra marbles.
For example, the even numbers that are multiples of $3$ are exactly the multiples of $6$.
Testing $6$, $12$ and $18$ is not enough, because the two checks must work for every number.

### L2 human

We prove $A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$ for all sets $A$, $B$ and $C$.

1. ($\subseteq$) Let $x \in A \setminus (B \cap C)$.
   Then $x \in A$ and $x \notin B \cap C$, by the definition of set difference.
2. Since $x$ is not in both $B$ and $C$, we have $x \notin B$ or $x \notin C$.
3. If $x \notin B$, then $x \in A \setminus B$, and if $x \notin C$, then $x \in A \setminus C$.
   In both cases $x$ lies in the union on the right.
4. ($\supseteq$) Let $x \in (A \setminus B) \cup (A \setminus C)$.
   Then $x \in A$, and $x \notin B$ or $x \notin C$.
5. In both cases $x$ is not in $B \cap C$, because every element of $B \cap C$ lies in $B$ and in $C$.
   So $x \in A \setminus (B \cap C)$.
6. Both inclusions hold, so the two sets are equal.

The typical goal is an identity built from unions, intersections, differences, images and preimages.
After you unfold the definitions, each half becomes a short proof by cases.
Watch out for step 2: "not in $B \cap C$" does not mean "not in $B$ and not in $C$".
An element of $B$ outside $C$ shows the difference, and the correct [[negation|K930V33BSC]] uses "or".

### L3 human

Double inclusion is the antisymmetry of the partial order $\subseteq$ on a power set.
Every partial order allows the same move, $a \le b$ and $b \le a$ give $a = b$, so the method is a special case of [[equality by two inequalities|S3QADD13E9]].
In algebra it is the standard way to identify two substructures, such as a kernel and an image in an exact sequence, or two ideals of a ring.
In type theory and in topos theory the analogue is extensionality for predicates: two predicates that imply each other define the same subobject.
Proof assistants make the two halves explicit, and the theorem that survives when one half fails, such as $f(A \cap B) \subseteq f(A) \cap f(B)$, is often the correct general statement.
