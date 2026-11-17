---
tag: H2W8D7BMSW
kind: concept
name: Structured and hierarchical proofs
aliases: [structured-proofs, hierarchical-proof, structured-proof]
msc: ["00A35", "68V15"]
topics: [STSM6PR7TX]
audience: research
uses: [0B94TKFQJX, 8JQHJK94RZ, GKMRQCA8CW, 6KT3BJZ7D1]
sources:
  - doi: 10.1080/00029890.1995.12004627
    locator: pages 600-608
  - doi: 10.1007/s11784-012-0071-6
    locator: pages 43-63
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: Fitch-style propositional logic
  - url: https://en.wikipedia.org/wiki/Proof_assistant
    locator: lead section
---

## Summary

A structured proof, or hierarchical proof, is a [[proof|0B94TKFQJX]] written as a tree of numbered steps.
Each step states one assertion, and each step has its own proof.
The proof of a step is a short paragraph that names the facts it uses.
Otherwise it is a list of steps at the next lower level.
The last step of each list asserts the goal of that list, and its proof cites the earlier steps of the list.
The format was proposed by Leslie Lamport in 1995, with step names such as $\langle 2 \rangle 3$ for the third step at level 2.
It matters because it shows the logical structure of a long proof at a glance, and it lets a reader stop at any depth.
It is also close to the form in which proof assistants check proofs.

## Motivation

A long proof in paragraphs mixes several levels of argument in one text.
The reader must find out alone which sentence proves which claim, how long an assumption stays in force, and which earlier facts a step uses.
Lamport argued that informal proofs in this form hide errors, because a step that "follows" can depend on an assumption that no longer holds.
A hierarchical format makes the scope of each assumption visible, and it forces the writer to name the facts that each step uses.
It also serves readers with different needs.
A reader who trusts the details reads only the top level, and a reader who checks every step expands each step to its leaves.

## Notation

1. Step names: $\langle n \rangle m$ is step number $m$ at level $n$. Level 1 is the top level. The steps of the proof of $\langle 1 \rangle 2$ are $\langle 2 \rangle 1$, $\langle 2 \rangle 2$, and so on.
2. The keyword PROOF begins the proof of a step. A leaf proof is a short sentence such as "by $\langle 2 \rangle 1$ and the definition of an injective function".
3. A step of the form "ASSUME: $P$ PROVE: $Q$" asserts that $P$ implies $Q$. Inside its proof, $P$ may be used as a fact.
4. A step "CASE: $P$" is short for "ASSUME: $P$ PROVE: the current goal".
5. The step "Q.E.D." asserts the current goal, and its proof explains why the earlier steps of the same list imply that goal.
6. The TLA+ proof language follows Lamport's format. It has more keywords, such as PICK (choose an object known to exist), SUFFICES (reduce the goal) and DEFINE (define a symbol).

## Remarks

### When it applies

The format fits long proofs, proofs with many cases, and proofs that a reader must check line by line.
Examples are proofs of the correctness of algorithms and of systems.
It also fits a proof that will later be checked by a proof assistant, because the steps can become lemmas or tactic blocks.
For a short proof of a few lines, an ordinary paragraph is easier to read.

### The steps

1. Write the theorem as a goal, with every hypothesis named.
2. Write the top-level proof: a short list of steps at level 1, ending with a Q.E.D. step. Each step is one assertion.
3. Give each step a proof. If the proof is one or two sentences that cite named facts, stop.
4. If a proof is longer, write it as a list of steps at the next level, ending with a Q.E.D. step.
5. In every proof, cite each fact by the name of its step, its hypothesis or its theorem. Do not write "hence" without the names.
6. Read the proof top down: check that the Q.E.D. step of each list follows from the steps of that list.

### Claims and sub-proofs in ordinary writing

An ordinary paper uses a light form of the same idea.
A long proof states "Claim 1", gives its proof, and marks the end of that inner proof.
An instance is [[a proof with a nested claim and two end marks|4P44ZFS5BT]].
Words such as "we claim" and "this proves the claim", described on the page [[the language of proofs|GKMRQCA8CW]], mark the levels in prose.
A structured proof makes these levels systematic and numbers them.

### Proofs in the style of proof assistants

Proof assistants store proofs with the same tree structure.
In Lean, `have h : P := by ...` states and proves an intermediate step, and an indented block under `·` proves one goal of a case split.
Isabelle has the Isar language, in which a proof is a block `proof ... qed` with steps `have`, `show` and `assume`.
The TLA+ proof system checks proofs written in Lamport's hierarchical format.
The page [[proof assistants and their design|YM6PRDE88V]] describes the systems.

### Examples

1. [[A structured proof that a composition of injective functions is injective|WMQTJQDMC8]]. It has two levels, with an ASSUME/PROVE step at level 1, and a Lean version of the same tree.
2. [[A structured proof that the square root of 2 is irrational|V4KAJ332BE]]: three levels, with a PICK step and a sub-proof that $p$ is even.
3. A proof by cases has the top level "$\langle 1 \rangle 1$. CASE: $n$ is even", "$\langle 1 \rangle 2$. CASE: $n$ is odd", "$\langle 1 \rangle 3$. Q.E.D." The proof of $\langle 1 \rangle 3$ says that every integer is even or odd.
4. An "if and only if" statement has the top level "$\langle 1 \rangle 1$. ASSUME: $P$ PROVE: $Q$", "$\langle 1 \rangle 2$. ASSUME: $Q$ PROVE: $P$", "$\langle 1 \rangle 3$. Q.E.D."

### Non-examples

1. [[A two-column proof is not a structured proof|GD8FT1XAQ9]]. A flat table of statements and reasons has no levels. So the scope of a case assumption cannot be shown.
2. A paragraph proof with "Claim 1" and "Claim 2" can fail to be a structured proof in Lamport's sense. This happens if its steps are not numbered and not cited by name. It is still a proof.
3. A numbered list of steps at one level is not hierarchical. It is a linear proof, and each step that needs a long argument stays a long paragraph.

### Basic properties

1. A structured proof is a tree. The root is the theorem, the inner nodes are steps with lists of sub-steps, and the leaves are steps with short proofs.
2. The scope of an ASSUME or a CASE is the proof of that step. Outside that proof the assumption is not available, so an assumption cannot leak into a later step.
3. Each structured proof can be flattened into a paragraph proof, by writing the steps in order with the proof words of [[the language of proofs|GKMRQCA8CW]]. The levels then become signposts.
4. The tree of a structured proof is a tree of [[natural deduction|6KT3BJZ7D1]] in informal language. An ASSUME/PROVE step is the introduction of an implication, and a CASE split is the elimination of a disjunction.
5. A structured proof is not a two-column proof. A two-column proof is one flat list with a reason column. A structured proof is a tree of nested sub-proofs, as the page [[two-column proof|P8PCGFASP8]] explains.

### History

Leslie Lamport proposed the hierarchical format in "How to Write a Proof", American Mathematical Monthly 102 (1995).
He gave an updated account in "How to write a 21st century proof", Journal of Fixed Point Theory and Applications 11 (2012).
Lamport is a computer scientist who received the 2013 Turing Award, and he wrote the first manual of LaTeX.
Proof languages with similar block structure exist in proof assistants, such as the Isar language of Isabelle.

### Common errors

1. A writer confuses a structured proof with a two-column proof and writes a flat table. The levels, which are the point of the format, then disappear.
2. A writer uses a fact from inside a sub-proof after the sub-proof ends, for example the assumption of a CASE step in a later case.
3. A Q.E.D. step cites "the steps above" without names. The reader cannot then check which steps the conclusion needs, and an unused or missing step goes unnoticed.

### Related methods

1. [[Writing proofs|8JQHJK94RZ]]: the general advice for proofs in paragraphs.
2. [[Two-column proof|P8PCGFASP8]]: a flat format with one reason for each statement, used in school geometry.
3. [[Level of detail in proofs|VYGBV5D8Y4]]: a structured proof lets the reader choose the depth, which is one answer to the question of detail.

## Explanations

### L1 human

A structured proof is like the outline of a long essay.
The top level lists the main points, each with a number.
Under each point, smaller numbered points explain why it holds.
A reader who only wants the main idea reads the top level.
A reader who wants to check everything opens each point and reads the smaller points under it.
For example, a proof can have three top steps.
They are "1. the number $p$ is even", "2. the number $q$ is even", "3. so the fraction $p/q$ was not in lowest terms".

### L2 human

We write a structured proof that the sum of two odd integers is even.

- `<1>1.` ASSUME: $m$ and $n$ are odd integers. PROVE: $m + n$ is even.
    - `<2>1.` PICK integers $k$ and $l$ with $m = 2k + 1$ and $n = 2l + 1$. PROOF: by the definition of an odd integer and the assumption of `<1>1`.
    - `<2>2.` $m + n = 2(k + l + 1)$. PROOF: $m + n = 2k + 1 + 2l + 1$ by `<2>1`, and the right side equals $2(k + l + 1)$.
    - `<2>3.` Q.E.D. PROOF: by `<2>2`, since $k + l + 1$ is an integer.
- `<1>2.` Q.E.D. PROOF: by `<1>1`.

1. The top level has one real step, `<1>1`, which is the theorem in ASSUME/PROVE form.
2. The level 2 steps prove `<1>1`, and they may use its assumption.
3. Each leaf proof names the facts it uses.

The typical use of the format is to check a proof where the writer is not sure of each step.
Each leaf can then be checked alone.
A trap is to make every step a leaf at level 1.
The result is a numbered list without a hierarchy, and it does not show which steps prove which.

### L3 human

A structured proof is an informal version of a natural deduction derivation, in the box notation of Fitch or Jaśkowski.
There each box is a sub-proof with its own assumptions.
In type theory, a proof is a term.
A structured proof corresponds to a term built with nested `let` bindings, one for each named step.
The declarative proof languages of proof assistants, such as Isar in Isabelle and the proofs of Mizar, follow this format.
So does the Lean style with `have` steps and indented blocks.
The format moves part of the work of checking from the reader to the writer, because each citation is explicit.
For the human reader the gain is the choice of depth, a theme of the page [[level of detail in proofs|VYGBV5D8Y4]].
For a machine the gain is that each leaf is a small, separate problem for automation.
The relation of such proofs to the acceptance of results in practice is a topic of [[rigour and the acceptance of proofs|1BTHSHST4M]].
