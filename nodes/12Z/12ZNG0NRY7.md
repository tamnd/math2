---
tag: 12ZNG0NRY7
kind: concept
name: Teaching sets and relations
aliases: [teaching-sets-and-relations, sets-in-school-mathematics]
msc: ["97E60", "97E99", "97A30"]
topics: [VHGA6J4NZK]
audience: research
uses: [0BSJ7RQ9BW, 0KCT6DPXJK, 05AVARPXA2, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/New_Math
    locator: Overview
  - url: https://en.wikipedia.org/wiki/New_Math
    locator: Reception
  - url: https://en.wikipedia.org/wiki/Mathematics_education_in_the_United_States
    locator: New Math
  - url: https://doi.org/10.1080/0020739830140305
    locator: pages 293-305
---

## Summary

A student is asked to show that $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ for all sets $A$, $B$ and $C$.
She draws three overlapping circles twice, shades the left side in one picture and the right side in the other, sees the same region, and writes "proved".
Her teacher then asks for the same check with four sets, and she finds that four circles cannot even show all sixteen ways an element can sit inside or outside four sets.
The picture made the identity believable, and only an argument with elements makes it certain.

The teaching of sets and relations studies how learners meet [[sets|0BSJ7RQ9BW]], the operations on sets, [[binary relations|05AVARPXA2]], and [[functions|0EPAT51DXQ]] as sets of pairs, and where these ideas belong in a curriculum.
Its main school tool is the [[Venn diagram|0KCT6DPXJK]], and its main historical episode is the New Math of the 1950s to the 1970s, which made sets the first language of school mathematics.
The MSC code 97E60 covers the field, and 97E99 collects other items of class 97E.

## Motivation

Almost every definition at university uses sets.
A function is a set of ordered pairs, an equivalence relation is a subset of a product, and a group is a set with an operation.
Students who do not read set notation fluently cannot read these definitions, so a curriculum must decide when and how they learn it.
One answer is early, as a foundation of number, and the other is late, as a language for advanced topics.
The New Math tried the first answer on a large scale, and its reception is the main evidence about both.

## Notation

School books write $\{2, 4, 6\}$ for a set given by a list and $\{x : x > 0\}$ or $\{x \mid x > 0\}$ for a set given by a property.
The symbols $\in$ and $\subseteq$ are a frequent source of confusion, and some school books write $\subset$ where others mean proper inclusion by it.

## Remarks

### The New Math

The New Math made sets the starting point of school mathematics.
Some of its textbooks introduced the number $3$ as what all sets with three elements have in common, and children matched sets of objects one to one before they counted.
Others taught the vocabulary of union, [[intersection|0ZNMMA9TF5]], [[subset|0BJR9QR08E]] and the [[empty set|0ECVK59Y03]] in the first grades.
The aim was a school mathematics with the structure of research mathematics.
The result, in the eyes of many parents, teachers and mathematicians, was a new vocabulary without new understanding.

The verdict on the New Math does not come from a controlled study.
The evidence is the reports of teachers, parents and mathematicians, and the decisions of school authorities to end the reforms.

### What research on functions found

Shlomo Vinner (1983) studied students who had learned the definition of a function as a set of ordered pairs in which each first entry appears once.
Many of them still judged examples by whether there was a formula or a smooth graph, not by the definition.
So learning the set definition did not replace the earlier picture.
[[Concept image and concept definition|C5S2X0WDJ8]] treats this research in detail.

### What a Venn diagram can and cannot do

A Venn diagram for $n$ sets needs $2^n$ regions, one for each choice of "inside" or "outside" for each set.
Three circles in general position give all $8$ regions.
Each new circle meets each earlier circle in at most $2$ points, so $n$ circles give at most
$$n^2 - n + 2$$
regions, and for $n = 4$ that is $14 < 16$.
So four circles cannot form a Venn diagram, and ellipses or other shapes are needed.
For three sets, a diagram with all eight regions can support a proof, because every element lies in exactly one region, but that reasoning must be stated.

### History

The New Math began in the United States in the 1950s, with projects such as the School Mathematics Study Group.
After the launch of Sputnik in 1957, the National Defense Education Act of 1958 gave the reforms new money and urgency.
At the Royaumont seminar of 1959, Jean Dieudonné called for an end to the teaching of Euclidean geometry, with the slogan "Down with Euclid!".
France ran its own "modern mathematics" reform from the late 1960s, under the influence of the Bourbaki group.
In 1965 the physicist Richard Feynman criticized New Math textbooks for teaching words without purpose, and Morris Kline published *Why Johnny Can't Add: The Failure of the New Math* in 1973.
By the late 1970s most countries had moved away from the New Math.

### Watch out

The student in the opening treated a picture as a proof.
A diagram shows one placement of the sets, and a proof must use the definitions of the operations.
A second error is to confuse $a \in A$ with $\{a\} \subseteq A$.
For $A = \{1, 2\}$, both $1 \in A$ and $\{1\} \subseteq A$ hold, but $\{1\} \in A$ is false.
A third is to think the empty set is "nothing" and so not a set, when in fact it is a set and a subset of every set.

### Try it

First, is $\{\varnothing\}$ empty?
No, it has one element, the empty set.

Second, how many regions must a Venn diagram for five sets have?
It needs $2^5 = 32$ regions, and five circles give at most $25 - 5 + 2 = 22$.

## Explanations

### L1 human

A set is a collection of things, called its elements.
The set of even numbers from $1$ to $10$ is $\{2, 4, 6, 8, 10\}$.
A Venn diagram draws sets as circles, and the things that are in two sets at once go in the overlap.
In the 1960s many countries taught sets to young children as the first step of mathematics.
That reform, called the New Math, confused many parents and teachers, and it was dropped in the 1970s.
Today sets appear in school mostly as a tool, and students study them in depth at university.

### L2 human

Here is the element proof that the student in the opening needed.
We show that each side of $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ is contained in the other.

1. Let $x \in A \cap (B \cup C)$.
   Then $x \in A$, and $x \in B$ or $x \in C$.
2. If $x \in B$, then $x \in A \cap B$, and if $x \in C$, then $x \in A \cap C$.
   In both cases $x \in (A \cap B) \cup (A \cap C)$.
3. Now let $x \in (A \cap B) \cup (A \cap C)$.
   In either case $x \in A$, and $x \in B$ or $x \in C$, so $x \in A \cap (B \cup C)$.
4. By [[double inclusion|MKHVRNW68H]], the two sets are equal.

The typical lesson uses the diagram to suggest the identity and the element argument to prove it.
Watch out: a student who stops at the diagram has no method for four sets, while the element argument works for any number.

### L3 human

The New Math followed the structural view of mathematics, in which sets and relations are the foundation of all structures.
Its failure in schools is often read as a failure of a top-down transfer from research to teaching.
French didactics calls such a transfer the didactic transposition, after Yves Chevallard.
Relations come later in most curricula: equivalence relations and partial orders appear at university, often in a [[transition-to-proof course|HQDCSJG379]].
Showing that a relation is an equivalence relation is a standard exercise there, as [[proving a relation is an equivalence relation|RGNF33GVHX]] shows.
