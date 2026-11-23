---
tag: WKM6535VHG
kind: concept
name: Moore method and inquiry-based learning
aliases: [moore-method, modified-moore-method, inquiry-based-learning-in-mathematics, ibl]
msc: ["97D40", "97E50"]
topics: [VHGA6J4NZK]
audience: ug2
uses: [0B94TKFQJX, 8ZCZ3HW91Z, 0ED72CTBNP, GD2JBXJV5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Moore_method
    locator: The original method
  - url: https://en.wikipedia.org/wiki/Robert_Lee_Moore
    locator: Unusual teacher
  - url: https://doi.org/10.1080/10511979908965940
    locator: pages 339-354
  - url: https://doi.org/10.5951/jresematheduc.45.4.0406
    locator: pages 406-418
  - url: https://en.wikipedia.org/wiki/Inquiry-based_learning
    locator: History
---

## Summary

On the first day of the course the teacher gives no lecture.
She hands out one sheet with three definitions and the statement "Theorem 1: if $a \mid b$ and $b \mid c$, then $a \mid c$", and says that at the next meeting someone will prove it at the board.
Two days later a student presents a proof, the class questions each line, and the theorem goes into everyone's notes only when the class accepts the proof.

That is the Moore method: a way to teach a proof-based course in which the students prove the theorems themselves.
The teacher writes a list of [[definitions|8ZCZ3HW91Z]] and statements, the students prove them outside class, and in class they present proofs that the other students check.
The teacher does not give proofs.
The method is named after the topologist Robert Lee Moore (1882 to 1974), who taught this way at the University of Texas.
Modern inquiry-based learning (IBL) in mathematics keeps the main idea, that students build the content through their own proofs, and often adds group work and reading.

## Motivation

In a lecture course, students see finished [[proofs|0B94TKFQJX]] and rarely make their own.
They can follow a proof in class and still be unable to prove a similar result alone.
Moore's view is often quoted as "that student is taught the best who is told the least".
If students must find each proof themselves, then they must learn how to start, how to use a definition and how to test a claim.
And because the class checks the proofs, the students also learn to judge proofs, a skill that lectures rarely train.

## Notation

"Moore method" usually means the original form: individual work, no reading, and presentation at the board.
"Modified Moore method" names the many variants that relax these rules.
"Inquiry-based learning" (IBL) is the wider name now in use, and it covers courses with group work, worksheets and reading, as long as students produce the main results.

## Remarks

### How a course runs

The teacher's main work happens before the course: writing a sequence of definitions, theorems and questions in which each theorem is within reach given the earlier ones.
The list includes tasks to find examples and [[counterexamples|0ED72CTBNP]], for instance to show that a hypothesis of a theorem cannot be dropped.
Between meetings the students work on the list.
In class, the teacher asks a student to present a proof, and Moore often called on the weaker students first.

The other students check the proof and ask questions.
If a gap appears and the presenter cannot repair it, the theorem stays open for the next meeting.
Accepted proofs become results that later proofs may use, so over the term the class builds the theory of the course itself.
The teacher guides by the choice and order of the tasks and by questions, not by proofs.

### Where it fits

The method suits courses whose content grows from a short list of definitions and axioms: topology, number theory, abstract algebra, real analysis and [[transition-to-proof courses|HQDCSJG379]].
It needs classes small enough that each student presents often, and Moore's own classes were small graduate classes.
It also costs coverage: a Moore course covers less material than a lecture course of the same length, and its advocates accept this cost for the depth that students gain.

### Three courses

[[Moore's course in point-set topology|W05DW690QG]] is the original form, as his student Floyd Burton Jones described it.
[[An inquiry-based unit on divisibility|EAWQDSME6M]] is a modern week in a transition course, with a short list of theorems that students prove in groups.
Dana Ernst's open textbook "An Introduction to Proof via Inquiry-Based Learning" is a full list of tasks for a transition course in this style.

### What it is not

[[A lecture course with proof homework|KWHDSAXJAF]] is not the Moore method, because the teacher proves the theorems of the course and the students only prove exercises.
A problem-solving seminar on separate contest problems is inquiry-based, but its problems do not build one theory in sequence.
A course in which students find patterns by experiment and never prove them is discovery learning, while in the Moore method a result enters the theory only with a proof.

### History

Moore taught at the University of Pennsylvania from 1911 and moved to the University of Texas in 1920, where he taught until 1969.
He supervised about 50 doctoral students, among them Raymond Wilder, Gordon Whyburn and Mary Ellen Rudin.
His record as a teacher is marred by racism: he refused to teach Black students.
Later teachers adapted the method, and William Mahavier (1999) described how he ran such courses.
The Journal of Inquiry-Based Learning in Mathematics publishes course notes in this style.

### What the research shows

Sandra Laursen, Marja-Liisa Hassi, Marina Kogan and Timothy Weston (2014) compared IBL and non-IBL sections of college mathematics courses, more than 100 sections at four universities.
Students in IBL sections reported higher learning gains, and in IBL sections women reported gains similar to men's, while in non-IBL sections women reported lower gains.
The study used students' own reports and was not a randomized experiment, so it shows an association, not a proven effect of the method.

### Watch out

The most common mistake is to give the proof when the class is stuck.
This turns the course back into a lecture, and a better response is a hint in the form of a new, smaller task.
A second mistake is to accept a proof that the class has not checked, since the check by the class is half of the method.
A third is a list with no example or counterexample tasks, so that students prove statements about objects they have never seen.
And the method can fail outright: with a list that is too hard, in a class too large for students to present, or for students who need more support than the method gives.

### Try it

Write the next task after "Theorem 1: if $a \mid b$ and $b \mid c$, then $a \mid c$" that asks students to test a claim instead of proving it.
One answer: "Prove or disprove: if $a \mid bc$, then $a \mid b$ or $a \mid c$"; it is false, since $6 \mid 2 \cdot 3$ but $6 \nmid 2$ and $6 \nmid 3$.

A student presents a proof with a gap, and nobody in the class can repair it.
What does the teacher do in the Moore method?
The theorem stays open until a later meeting, and the teacher may add a smaller task to the list as a hint.

## Explanations

### L1 human

In most mathematics classes, the teacher shows how to prove a theorem.
In a Moore method class, the teacher only says what the theorem is.
The students go home and try to prove it themselves.
At the next class, a student shows a proof at the board, and the other students check it.
For example, the teacher may ask the class to prove that if $a$ divides $b$ and $b$ divides $c$, then $a$ divides $c$.
Students learn more slowly this way, but they learn to make proofs, not only to follow them.

### L2 human

We plan the first week of an IBL course on sets.
The sheet gives the definitions of subset, equality of sets, union, intersection and complement in a universe $U$.
Task 1 asks for a proof that $A \subseteq A \cup B$ for all sets $A$ and $B$.
Task 2 asks for a proof that if $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$.
Task 3 asks whether $A \cup B = A \cup C$ forces $B = C$, and the counterexample $A = \{1\}$, $B = \{1\}$, $C = \emptyset$ shows that it does not:
$$A \cup B = \{1\} = A \cup C, \qquad B \ne C.$$
Task 4 asks for a proof that $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$, by [[double inclusion|MKHVRNW68H]].

At the meeting, students present tasks 1 to 3, and the class checks each step against the definitions.
If nobody has a complete proof of task 4, it stays open, and the teacher adds the hint "first prove $\subseteq$".
Such a plan suits a class of 10 to 30 students who meet several times a week.
The form "prove or give a counterexample" in task 3 matters, because it trains students to test a claim before they try to prove it.

### L3 human

The Moore method treats mathematics as an activity rather than a body of results, which connects it with the [[philosophy of mathematics in education|174ES70CS8]].
In the language of [[proof schemes|YVNRVXJR68]], it aims at the axiomatic scheme, because students build results from a list of definitions and axioms in the style of the [[axiomatic method|GD2JBXJV5Z]].
[[Reasoning and proof in the classroom|E77B813MT4]] studies classroom argumentation in general, and the Moore method is one way to organize it.
The topic [[problem solving and inquiry in teaching|T9NYH735DA]] treats inquiry-based teaching outside proof courses.
