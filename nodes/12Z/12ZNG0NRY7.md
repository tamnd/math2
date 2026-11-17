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

The teaching of sets and relations is the study of how learners meet [[sets|0BSJ7RQ9BW]], the operations on sets, [[binary relations|05AVARPXA2]] and [[functions|0EPAT51DXQ]] as sets of pairs, and of the place of these ideas in curricula.
Its main historical episode is the New Math of the 1950s to the 1970s, which made sets the first language of school mathematics.
Its main school tool is the [[Venn diagram|0KCT6DPXJK]].
The MSC code 97E99 collects other topics of the foundations in education, and this page also takes them.
The field matters because set language is the language of university mathematics, and the history of the New Math shows what can go wrong when it is taught too early or too formally.

## Motivation

Each definition at university level uses sets: a function is a set of ordered pairs, an equivalence relation is a subset of a product, and a group is a set with an operation.
Students who do not read set notation fluently cannot read these definitions.
So a curriculum must decide when and how students learn sets.
Two answers are possible: early, as a foundation of number, or late, as a language for advanced topics.
The New Math tried the first answer on a large scale, and its reception gives evidence about both answers.

## Remarks

### Examples

1. Some New Math textbooks introduced the number $3$ as the common property of all sets with three elements. Children matched sets of objects one to one before they counted.
2. A Venn diagram with two overlapping circles shows the [[intersection|0ZNMMA9TF5]] and the [[union|0X1GSWNBN1]] of two sets. School curricula use it for sorting tasks and for problems of counting with two properties.
3. A first-year course proves the equality of two sets by [[double inclusion|MKHVRNW68H]]. This is often the first proof about sets that students write.
4. A course defines a function as a set of ordered pairs in which each first element appears once. Vinner (1983) found that many students judged functions by a mental picture, not by such a definition.

### Non-examples

1. Axiomatic set theory, with the axioms of Zermelo and Fraenkel and the study of cardinals, is a field of mathematics. It belongs to [[set theory|G9W9J6KPAR]], not to the teaching of sets.
2. A Venn diagram used in a statistics lesson to show events is a tool of probability teaching. It belongs to the teaching of probability.

### Research findings

1. Shlomo Vinner (1983) found that students who had learned the set definition of a function often judged examples by a formula or a graph, not by the definition. The page on [[concept image and concept definition|C5S2X0WDJ8]] treats this research.
2. The reception of the New Math is not the result of a controlled study. The evidence is the reports of teachers, parents and mathematicians, and the decisions of governments to end the reforms.

### Basic properties

1. A Venn diagram for $n$ sets needs $2^n$ regions, one for each choice of "inside" or "outside" for each set. For $n = 3$ this gives $8$ regions, and three circles can produce all of them.
2. Four circles cannot give a Venn diagram for four sets. Each new circle meets each earlier circle in at most $2$ points, so $n$ circles give at most $n^2 - n + 2$ regions. For $n = 4$ this is $14 < 16$.
3. A relation from $A$ to $B$ is a subset of $A \times B$, and a function is a relation in which each element of $A$ appears as a first entry exactly once. School curricula usually meet functions long before this definition.

### History

The New Math started in France and spread to many countries between the 1950s and the 1970s.
In France it aimed to bring school mathematics closer to research mathematics, under the influence of the Bourbaki group.
In the United States, the launch of the satellite Sputnik in 1957 led to the National Defense Education Act of 1958 and to large reforms of school mathematics.
Jean Dieudonné declared "Down with Euclid!" at a meeting on the reform of school mathematics.
In 1965 the physicist Richard Feynman criticized New Math textbooks for teaching words without purpose.
Morris Kline published "Why Johnny Can't Add: the Failure of the New Math" in 1973.
By the end of the 1970s, most countries had abandoned the New Math, and traditional topics returned to the curricula.

### Common errors

1. A teacher treats the Venn diagram as a proof of a set identity. A diagram of one situation shows the identity for one placement of the sets, and a proof must use the definitions.
2. A student confuses $a \in A$ and $\{a\} \subseteq A$. The first says that $a$ is an element of $A$, and the second says that the set with the one element $a$ is a [[subset|0BJR9QR08E]] of $A$.
3. A student believes that the [[empty set|0ECVK59Y03]] is "nothing" and so not a set. The empty set is a set, and it is a subset of each set.

## Explanations

### L1 human

A set is a collection of things, called its elements.
For example, the set of even numbers from $1$ to $10$ is $\{2, 4, 6, 8, 10\}$.
A Venn diagram draws sets as circles: the things in two sets at once go in the overlap of the circles.
In the 1960s many countries taught sets to young children as the first step of mathematics.
This reform, called the New Math, confused many parents and teachers, and it was ended in the 1970s.
Today sets appear in school mostly as a tool, and students study them in depth at university.

### L2 human

We prove one set identity and compare the proof with a Venn diagram.
The identity: for all sets $A$, $B$ and $C$, we have $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.

1. Diagram: we draw three overlapping circles and shade $A \cap (B \cup C)$, then $(A \cap B) \cup (A \cap C)$. The shaded regions agree.
2. The diagram is not yet a proof, because it shows one picture. The proof must work for all sets.
3. First inclusion: let $x \in A \cap (B \cup C)$. Then $x \in A$, and $x \in B$ or $x \in C$.
4. If $x \in B$, then $x \in A \cap B$. If $x \in C$, then $x \in A \cap C$. In both cases $x \in (A \cap B) \cup (A \cap C)$.
5. Second inclusion: let $x \in (A \cap B) \cup (A \cap C)$. Then $x \in A \cap B$ or $x \in A \cap C$.
6. In both cases $x \in A$, and $x \in B$ or $x \in C$. So $x \in A \cap (B \cup C)$.
7. By [[double inclusion|MKHVRNW68H]], the two sets are equal.

The typical use is a first lesson on set proofs, in which the diagram suggests the identity and the element argument proves it.
A trap is to stop at step 1.
For three sets, a careful diagram with all eight regions can serve as a proof, because each element lies in exactly one region.
But this needs an argument, and a student who skips it cannot treat a claim about four sets.

### L3 human

The New Math followed the structural view of mathematics, in which sets and relations are the foundation of all structures.
Its failure in schools is often read as a failure of a top-down transfer from research to teaching.
French didactics names this transfer the didactic transposition, after Yves Chevallard.
The teaching of relations has a later place in most curricula: equivalence relations and partial orders appear at university, often in a [[transition-to-proof course|HQDCSJG379]].
The proof that a relation is an equivalence relation is a standard exercise there, as the page on [[proving a relation is an equivalence relation|RGNF33GVHX]] shows.
