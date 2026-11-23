---
tag: HQDCSJG379
kind: concept
name: Transition-to-proof courses
aliases: [transition-to-proof-course, bridge-course, introduction-to-proof-course, transition-course]
msc: ["97E50", "97B40", "97D70"]
topics: [VHGA6J4NZK]
audience: ug1
uses: [0B94TKFQJX, 958EF46EYJ, 0ASJVEFA9J, 0BSJ7RQ9BW, FA6YZGR2SS]
sources:
  - book: isbn:9781108439534
    locator: Introduction
  - book: isbn:9781108439534
    locator: Chapter 3
  - url: https://doi.org/10.1007/BF01273731
    locator: pages 249-266
  - url: https://doi.org/10.1007/978-94-007-2129-6_17
    locator: pages 391-420
  - url: https://doi.org/10.2307/30034698
    locator: pages 4-36
  - url: https://en.wikipedia.org/wiki/Mathematical_maturity
    locator: Progression
---

## Summary

In the third week of a bridge course, a student must prove that if $3n + 2$ is odd, then $n$ is odd, for every integer $n$.
She writes $3n + 2 = 2k + 1$, solves to get $n = \frac{2k - 1}{3}$, and stops, because she cannot see whether that fraction is an odd integer.
Her neighbor tries the contrapositive: if $n = 2k$ is even, then $3n + 2 = 6k + 2 = 2(3k + 1)$ is even, and the proof is done in one line.
Both students know the same algebra, and what separates them is a method of proof chosen from the logical form of the statement.

A transition-to-proof course is a university course whose main aim is to teach students to read and write [[proofs|0B94TKFQJX]], before or alongside their first proof-based courses.
Its usual content is the logic of statements and quantifiers, the language of [[sets|0BSJ7RQ9BW]], functions and relations, the [[basic proof methods|958EF46EYJ]], and [[mathematical induction|0ASJVEFA9J]].
It is the standard answer of mathematics departments, especially in the United States, to the difficulty of the step from calculation to proof.

## Motivation

School mathematics and first-year calculus ask students mostly to compute.
Later courses, such as real analysis and abstract algebra, ask students to prove theorems from definitions.
Many students who did well in the first kind of course struggle in the second.
Robert Moore (1994) followed students through a transition course and found that their difficulties lay with definitions, notation and getting started, not with the content.
A transition course isolates those skills and teaches them on simple content, so that later courses can spend their time on their own content.

## Notation

Other names for the course are "bridge course", "introduction to proof", "foundations of mathematics" and "mathematical reasoning".
Some departments give the role to a first course in discrete mathematics or number theory, which then teaches proof through its content.

## Remarks

### What the course contains

A typical course runs from logic through proof methods and sets to induction, relations and functions, and some texts put sets before logic.
The content is chosen to be simple, so that the difficulty lies in the proof and not in the mathematics.
Typical theorems concern parity, divisibility, set identities and properties of functions.
Some courses end with a short unit on cardinality or on elementary number theory, and they prepare students for both analysis and algebra.

### Four textbooks

Daniel Velleman's *How to Prove It* (first edition 1994, third edition 2019) begins with sentential and quantificational logic.
It then organizes proof strategies by the [[logical form|872K5XB580]] of the goal and the givens, before it treats relations, functions and induction.
Richard Hammack's *Book of Proof* is a freely available textbook that covers sets, logic, direct proof, contrapositive and contradiction, induction, relations, functions and cardinality.
Ted Sundstrom's *Mathematical Reasoning: Writing and Proof* is also freely available, follows a similar plan, and adds preview activities before each section.
Dana Ernst's *An Introduction to Proof via Inquiry-Based Learning* asks students to prove the theorems themselves, which brings the [[Moore method|WKM6535VHG]] to the transition course.

### What it is not

A calculus course with a few proofs in the lectures is not a transition course, since its aim is calculus and students do not practice writing proofs.
A course in [[mathematical logic|DYJ0KGTPMR]] studies logic as a subject, with formal systems and completeness, while a transition course uses logic as a tool.
A course for contest training teaches some proof, but its aim is hard problems, not the habits of reading and writing proofs.

### What the research says

Moore (1994) identified seven sources of difficulty among students in a transition course.
They concerned knowing the definitions, intuitive understanding, concept images, generating examples, using definitions to structure a proof, language and notation, and how to begin.
Annie Selden and John Selden (2003) asked a small group of undergraduates in a transition course to judge whether given arguments proved a theorem.
At first the students often could not tell valid arguments from invalid ones, and their judgments became more accurate as they reflected during the interview.
Annie Selden (2012), in ICMI Study 19, reviewed research on the transition to proof at university and the forms of courses that respond to it.
Research does not yet say which form of transition course works best, since studies compare few courses and use different measures.

### Watch out

A student may treat the logic unit as separate from the proofs that follow.
The opening shows the cost: the contrapositive was in the logic unit, and the first student did not think to use it.
A student may also memorize the proofs of the course, when tests ask for new proofs with the same methods.
A course can fail too, if it spends most of its time on truth tables and leaves little time for writing proofs.

### Try it

First, prove that if $n^2$ is even, then $n$ is even.
Assume $n = 2k + 1$; then $n^2 = 2(2k^2 + 2k) + 1$ is odd, so the contrapositive holds.

Second, why does a bridge course prove facts about parity rather than about continuity?
Parity needs only one short definition, so the student's effort goes into the logic of the proof.

## Explanations

### L1 human

In school, mathematics is mostly about finding answers.
At university, it is also about proving that a statement is true in every case.
Many students find that step hard, so many universities offer a special course for it.
In the course, students learn what words like "for all" and "if ... then" mean, and they practice short proofs.
For example, they prove that the square of every even number is even: if $n = 2k$, then $n^2 = 4k^2 = 2(2k^2)$.
After the course they take analysis and algebra, where proofs are the main work.

### L2 human

Here is one week of a transition course, on proof by contrapositive.
The week opens with logic: "if $P$, then $Q$" has the same truth table as "if not $Q$, then not $P$".
The [[proof by contrapositive|0BB5TPGQ1N]] turns that fact into a method: to prove "if $P$, then $Q$", assume not $Q$ and derive not $P$.

The teacher then proves a model case: if $n^2$ is even, then $n$ is even.
Assume $n$ is odd, say $n = 2k + 1$, and compute
$$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,$$
which is odd.
Students practice on the statement of the opening, and they write each proof in sentences, with a first line that says "we prove the contrapositive".
The teacher marks for logic and for language, as [[writing proofs|8JQHJK94RZ]] describes.
Watch out: passing the course does not mean a student can prove theorems in any field, since each field still has its own definitions and strategies.

### L3 human

The transition course answers a change in what is expected of students between school and university.
David Tall described the change as a move from the embodied and symbolic worlds of school mathematics to the formal world of axioms and proofs.
Terence Tao describes three stages of mathematical education, pre-rigorous, rigorous and post-rigorous, and the transition course marks the start of the rigorous stage.
Research on the course draws on [[proof schemes|YVNRVXJR68]], [[concept image and concept definition|C5S2X0WDJ8]] and [[student difficulties with proof|5K2969GSWE]].
Alternatives to a separate course are proof taught inside each course, the Moore method, and courses with [[proof assistants|KGPHY3F0GC]].
[[University mathematics education|ACJ8SVB1GD]] places the course among the other questions of teaching at university.
