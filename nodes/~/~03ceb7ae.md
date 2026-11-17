---
tag: ~03ceb7ae
kind: concept
name: Proof assistants in teaching
aliases: [proof-assistants-in-teaching, interactive-theorem-provers-in-education, lean-in-teaching]
msc: ["97U70", "97E50", "97N80", "68V15"]
topics: [VHGA6J4NZK]
audience: research
uses: [0B94TKFQJX, YM6PRDE88V, QF0Q7B5Q73]
sources:
  - url: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
    locator: Mathematics
  - url: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
    locator: External links
  - url: https://en.wikipedia.org/wiki/Rocq
    locator: lead section
  - url: https://doi.org/10.1007/s40753-021-00140-1
    locator: pages 64-93
  - url: https://doi.org/10.1007/978-3-030-28483-1
    locator: whole volume
---

## Summary

A proof assistant is a computer program that checks each step of a formal proof, and in teaching it serves as a tutor that gives instant feedback on students' proofs.
The main systems used in mathematics teaching are Lean, Rocq (formerly Coq) and Isabelle.
Courses use them in transition-to-proof courses, in logic courses, and in interactive games such as the Natural Number Game.
The aims are to make the logical structure of proofs explicit, to give feedback without a human marker, and to let students explore without fear of hidden errors.
Research on the effects is young, and most studies are small and exploratory.
The systems themselves are treated in the topic [[proof assistants and their design|YM6PRDE88V]].

## Motivation

A student who writes a [[proof|0B94TKFQJX]] on paper waits days for feedback, and the feedback depends on the marker.
A proof assistant answers at once: it accepts a step, or it shows the goal that remains and the error.
It does not accept a missing reason or a skipped case.
So it forces the student to make each step explicit, which is one of the hardest skills of the transition to proof.
On the other hand, a formal proof differs from a written proof, and a course must decide how the two relate.

## Remarks

### Examples

1. The Natural Number Game, by Kevin Buzzard and Mohammad Pedramfar, teaches the first steps of Lean through levels on the natural numbers. The player proves facts such as the commutativity of addition from the Peano axioms, by induction.
2. Heather Macbeth uses Lean to teach the fundamentals of proof with instant feedback, in her course notes "The Mechanics of Proof".
3. Terence Tao released a Lean companion to his textbook "Analysis I", with formal versions of selected sections.
4. In computer science, the textbooks "Software Foundations" (with Rocq) and "Concrete Semantics" (with Isabelle) teach logic and the semantics of programs with a proof assistant.
5. [[A proof checked by the Lean proof assistant|QF0Q7B5Q73]] shows two short Lean proofs about the natural numbers.

### Non-examples

1. A computer algebra system, which simplifies $(x + 1)^2$ to $x^2 + 2x + 1$, is not a proof assistant. It computes, but it does not check a proof of a general statement step by step.
2. Dynamic geometry software, which lets students drag a figure and see that a property persists, gives empirical evidence, not a checked proof.
3. An online quiz that checks only the final answer of a calculation does not check a proof.

### Research findings

1. Athina Thoma and Paola Iannone (2022) studied first-year students in the United Kingdom who took voluntary Lean workshops alongside a transition-to-proof module. In this exploratory study, the proofs of the students who engaged with Lean showed more accurate use of mathematical language and symbols, and a clearer structure.
2. The book "Proof Technology in Mathematics Research and Teaching" (2019), edited by Gila Hanna, David Reid and Michael de Villiers, collected chapters on the use of computer tools for proof in research and in teaching.
3. Research does not yet show clear effects of proof assistants on students' ability to write proofs on paper. The studies are small, the students are often volunteers, and the measures differ.

### History

Before Lean, proof assistants were used in teaching mainly in computer science, in courses on logic and on programming languages.
The growth of Lean and of its library Mathlib in the late 2010s and the 2020s brought proof assistants into mathematics departments.
Kevin Buzzard's Xena project at Imperial College London set the aim of formalizing the theorems and proofs of the undergraduate mathematics curriculum in Lean.
Coq was renamed Rocq with the release of Rocq 9.0 in March 2025.

### Common errors

1. A teacher assumes that a student who completes a formal proof understands it. A student can find the right tactics by trial and error, with little understanding of why they work.
2. A course spends most of its time on the syntax of the system. Then the students learn the program, not proof.
3. A teacher treats the formal proof as the model for written proofs. A written proof for a human reader leaves out routine steps that the assistant needs, as the page on [[level of detail in proofs|VYGBV5D8Y4]] explains.

## Explanations

### L1 human

A proof assistant is a computer program that checks proofs.
The student types each step, and the program says at once whether the step is correct.
If a step is missing, the program shows what is still to be proved.
Some teachers use such programs to help students learn proofs.
For example, the Natural Number Game asks players to prove facts like $a + b = b + a$, one step at a time.

### L2 human

We follow a student's proof in Lean 4 with the Mathlib library, of the claim that the sum of two odd integers is even.
The statement is `example (a b : ℤ) (ha : Odd a) (hb : Odd b) : Even (a + b) := by`, and the proof has three lines: `obtain ⟨k, rfl⟩ := ha`, then `obtain ⟨m, rfl⟩ := hb`, then `exact ⟨k + m + 1, by ring⟩`.

1. In Mathlib, `Odd a` means that $a = 2k + 1$ for some integer $k$, and `Even n` means that $n = r + r$ for some integer $r$.
2. The first `obtain` unpacks the hypothesis: Lean replaces $a$ by $2k + 1$. The second does the same for $b$ with $m$.
3. The goal is now: there is $r$ with $(2k + 1) + (2m + 1) = r + r$.
4. The student gives $r = k + m + 1$. The `ring` tactic checks the equation $(2k + 1) + (2m + 1) = (k + m + 1) + (k + m + 1)$ by algebra.
5. Lean accepts the proof. If the student gives $r = k + m$, the `ring` tactic fails, because $(k + m) + (k + m)$ differs from the left side by $2$.

The typical use is a weekly exercise sheet in a transition course, with Lean files that students complete.
A trap is step 1: the student must know Mathlib's definition of `Even`, which differs in form from the textbook definition $n = 2r$.
The page [[proof strategies by logical form|872K5XB580]] gives the same steps for a written proof.

### L3 human

Proof assistants touch several questions of this topic.
They make the warrants of each step explicit, which links them with the [[Toulmin model|~889806ec]] and with [[proof comprehension and validation|~b200f4e2]].
They change the didactic contract of a [[transition-to-proof course|~a913431e]], because the machine, not the teacher, judges validity.
They raise a question for the [[philosophy of mathematics in education|~5b9b7014]]: whether a formally checked proof explains, or only verifies.
The topic [[technology in mathematics education|XANZW7SV7N]] places them among other digital tools.
