---
tag: KGPHY3F0GC
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

A student opens the Natural Number Game in a web browser.
The first level shows a goal in which both sides of an equation are the same expression, and one tactic that says "both sides are equal" closes it, written `rfl` in the current version.
The next level gives a hypothesis $y = x + 7$ and the goal $2y = 2(x + 7)$, and the student learns to rewrite with the hypothesis, after which the goal closes.
A few worlds later, the same student proves that addition of natural numbers is commutative by [[induction|0ASJVEFA9J]], and the program has checked every step on the way.

A proof assistant is a computer program that checks each step of a formal proof, and in teaching it acts as a tutor that answers at once.
The systems used most in mathematics teaching are Lean, Rocq (formerly Coq) and Isabelle.
Teachers use them in transition-to-proof courses, in logic courses and in games such as the Natural Number Game.
Their aims are to make the logical structure of a proof visible, to give feedback without a human marker, and to let students try ideas without fear of hidden errors.
Research on their effects is young, and most studies are small and exploratory.

## Motivation

A student who writes a [[proof|0B94TKFQJX]] on paper waits days for feedback, and the feedback depends on the marker.
A proof assistant answers at once: it accepts a step, or it shows the goal that remains and the error.
It does not accept a missing reason or a skipped case, so it forces the student to make every step explicit, one of the hardest skills of the transition to proof.
On the other hand, a formal proof is not a written proof, and a course must decide how the two relate.
The systems themselves are treated in the topic [[proof assistants and their design|YM6PRDE88V]].

## Notation

A proof in Lean is written with tactics, commands such as `rfl`, `rw`, `intro`, `induction` and `exact` that change the current goal.
The program shows the "goal state": the hypotheses in force and what remains to be proved.
Mathlib is Lean's large library of formalized mathematics, and its definitions can differ in form from textbook ones.

## Remarks

### Courses and materials

The Natural Number Game, by Kevin Buzzard and Mohammad Pedramfar, first released in 2019, teaches the first steps of Lean through levels on the natural numbers built from the [[Peano axioms|0QFT7Z76N5]].
Heather Macbeth's course notes "The Mechanics of Proof" use Lean to teach the basics of proof with instant feedback.
Terence Tao released a Lean companion to his textbook "Analysis I", with formal versions of selected sections.
In computer science, "Software Foundations" (with Rocq) and "Concrete Semantics" (with Isabelle) teach logic and the semantics of programs with a proof assistant.
The example [[a proof checked by the Lean proof assistant|QF0Q7B5Q73]] shows two short Lean proofs about the natural numbers.

### What is not a proof assistant

A computer algebra system that expands $(x + 1)^2$ to $x^2 + 2x + 1$ computes, but it does not check a proof of a general statement step by step.
Dynamic geometry software lets students drag a figure and see that a property persists, which is strong empirical evidence but not a checked proof.
An online quiz that checks only the final answer of a calculation checks no proof at all.

### What the research shows

Athina Thoma and Paola Iannone (2022) studied first-year students in the United Kingdom who took voluntary Lean workshops alongside a transition-to-proof module.
In this exploratory study, the written proofs of the students who engaged with Lean used mathematical language and symbols more accurately and had a clearer structure.
The students chose whether to take part, so the study cannot say whether Lean caused the difference.

The book "Proof Technology in Mathematics Research and Teaching" (2019), edited by Gila Hanna, David Reid and Michael de Villiers, collects chapters on computer tools for proof in research and in teaching.
Taken together, the research does not yet show a clear effect of proof assistants on students' ability to write proofs on paper.
The studies are small, the students are often volunteers, and the measures differ from study to study.

### History

Before Lean, proof assistants were used in teaching mainly in computer science, in courses on logic and on programming languages.
The growth of Lean and its library Mathlib in the late 2010s and the 2020s brought proof assistants into mathematics departments.
Kevin Buzzard's Xena project at Imperial College London set the aim of formalizing the theorems and proofs of the undergraduate mathematics curriculum in Lean.
Coq was renamed Rocq with the release of Rocq 9.0 in March 2025.

### Watch out

A student who completes a formal proof may not understand it, since tactics can be found by trial and error.
A course that spends most of its time on the syntax of the system teaches the program, not proof.
And the formal proof is a poor model for written proofs: a proof for a human reader leaves out routine steps that the assistant needs, as [[level of detail in proofs|VYGBV5D8Y4]] explains.

### Try it

In the second level of the Natural Number Game, the hypothesis is $y = x + 7$ and the goal is $2y = 2(x + 7)$.
What does rewriting with the hypothesis do, and why does the goal then close?
It replaces $y$ by $x + 7$ in the goal, giving $2(x + 7) = 2(x + 7)$, and an equation with identical sides closes by reflexivity.

Is a graphing calculator that plots $\sin^2 x + \cos^2 x$ as a flat line at height $1$ a proof assistant?
No, it shows evidence for the identity on a finite set of points, and it checks no proof of it.

## Explanations

### L1 human

A proof assistant is a computer program that checks proofs.
The student types each step, and the program says at once whether the step is correct.
If a step is missing, the program shows what is still to be proved.
Some teachers use such programs to help students learn proofs.
For example, the Natural Number Game asks players to prove facts like $a + b = b + a$, one step at a time.

### L2 human

We follow a student's proof in Lean 4 with Mathlib that the sum of two odd integers is even.
The statement is `example (a b : ℤ) (ha : Odd a) (hb : Odd b) : Even (a + b) := by`, and the proof has three lines: `obtain ⟨k, rfl⟩ := ha`, then `obtain ⟨m, rfl⟩ := hb`, then `exact ⟨k + m + 1, by ring⟩`.

In Mathlib, `Odd a` means that $a = 2k + 1$ for some integer $k$, and `Even n` means that $n = r + r$ for some integer $r$.
The first `obtain` unpacks the hypothesis and replaces $a$ by $2k + 1$, and the second does the same for $b$ with $m$.
The goal is now to find $r$ with $(2k + 1) + (2m + 1) = r + r$.
The student gives $r = k + m + 1$, and the `ring` tactic checks the equation
$$(2k + 1) + (2m + 1) = (k + m + 1) + (k + m + 1)$$
by algebra.
If the student gives $r = k + m$ instead, `ring` fails, because $(k + m) + (k + m)$ is $2$ less than the left side.

A weekly sheet of Lean files like this one is a typical use in a transition course.
Watch out for the definition of `Even`: it has the form $n = r + r$, not the textbook form $n = 2r$, and the student must know which one Lean expects.
[[Proof strategies by logical form|872K5XB580]] gives the same moves for a written proof.

### L3 human

Proof assistants touch several questions of research on teaching proof.
They make the warrant of each step explicit, which links them with the [[Toulmin model|RVZCSFDB2Y]] and with [[proof comprehension and validation|52Y2MW27J0]].
They change the rules of a [[transition-to-proof course|HQDCSJG379]], because the machine, not the teacher, judges validity.
They also raise a question for the [[philosophy of mathematics in education|174ES70CS8]]: whether a formally checked proof explains, or only verifies.
The topic [[technology in mathematics education|XANZW7SV7N]] places them among other digital tools.
