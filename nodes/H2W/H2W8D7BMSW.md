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

A structured proof writes a [[proof|0B94TKFQJX]] as a tree of numbered steps, in which every step states one fact and has its own proof.
That proof is either a short sentence that names what it uses or a list of smaller steps one level down.
Here is a short theorem in this form: for every integer $n$, the remainder of $n^2$ on division by $4$ is $0$ or $1$.

- $\langle 1 \rangle 1$. CASE: $n$ is even.
    - $\langle 2 \rangle 1$. PICK an integer $k$ with $n = 2k$.
      PROOF: by the case assumption and the definition of an even integer.
    - $\langle 2 \rangle 2$. Q.E.D.
      PROOF: $n^2 = 4k^2$ by $\langle 2 \rangle 1$, so the remainder is $0$.
- $\langle 1 \rangle 2$. CASE: $n$ is odd.
    - $\langle 2 \rangle 1$. PICK an integer $k$ with $n = 2k + 1$.
      PROOF: by the case assumption and the definition of an odd integer.
    - $\langle 2 \rangle 2$. Q.E.D.
      PROOF: $n^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1$ by $\langle 2 \rangle 1$, so the remainder is $1$.
- $\langle 1 \rangle 3$. Q.E.D.
  PROOF: by $\langle 1 \rangle 1$ and $\langle 1 \rangle 2$, since every integer is even or odd.

The same proof as a paragraph reads as follows.

> If $n$ is even, write $n = 2k$, so that $n^2 = 4k^2$ leaves remainder $0$.
> If $n$ is odd, write $n = 2k + 1$, so that $n^2 = 4(k^2 + k) + 1$ leaves remainder $1$.
> Every integer is even or odd, so the claim holds.
> $\square$

The two forms hold the same mathematics.
The structured form shows where each case begins and ends, that the two letters $k$ belong to different cases, and which facts each step uses.
A reader who trusts the details reads only the three steps at level 1, and a reader who checks everything opens each step down to its leaves.

## Motivation

A long proof in paragraphs mixes several levels of argument in one text.
The reader must work out which sentence proves which claim, how long an assumption stays in force, and which earlier facts a step uses.
Leslie Lamport argued in 1995 that this hides errors: a step that seems to follow may rest on an assumption whose scope has ended, or on a fact nobody named.
His remedy was to make the levels explicit and to require every step to cite what it uses.

The same tree is how proof assistants hold proofs, so a structured proof is also a halfway house between a paragraph and a machine-checked proof.

## Notation

In $\langle n \rangle m$, the first number is the level and the second counts the steps at that level, so $\langle 2 \rangle 3$ is the third step of the current list at level 2.
In plain text the same names are written `<2>3`.
The keyword PROOF begins the proof of a step, and a leaf proof is a short sentence such as "by $\langle 2 \rangle 1$ and the definition of an injective function".

"ASSUME: $P$ PROVE: $Q$" asserts that $P$ implies $Q$, and inside its proof $P$ may be used.
"CASE: $P$" is short for "ASSUME: $P$ PROVE: the current goal".
"Q.E.D." asserts the current goal, and its proof explains why the earlier steps of the same list give that goal.
The TLA+ proof language follows this format and adds keywords such as PICK, which chooses an object known to exist, SUFFICES, which reduces the goal, and DEFINE.

## Remarks

### Writing one

Start with the theorem as a goal and name every hypothesis.
Write the top level as a short list of steps ending with Q.E.D., where each step is one assertion.
Give each step a proof, and if the proof is a sentence or two citing named facts, stop there.
If it is longer, write it as a list one level down, again ending with Q.E.D.
Cite every fact by the name of its step, its hypothesis or its theorem, never by "hence" alone.
Then read top down and check that each Q.E.D. step follows from the steps of its own list.

The format fits long proofs, proofs with many cases, and proofs that a reader must check line by line, such as correctness proofs for algorithms and systems.
For a proof of a few lines, a plain paragraph is easier to read.

### Two worked trees

[[The composition of injective functions|WMQTJQDMC8]] has two levels.
Its level 1 step is the definition of injectivity written as ASSUME/PROVE, and the two level 2 steps use the injectivity of $g$ and then of $f$, each exactly once.
The same tree appears again in Lean 4, read backward from the goal.

[[The irrationality of the square root of 2|V4KAJ332BE]] has three levels.
The third level proves that $p$ is even, a step that a paragraph proof usually hides in one sentence, and a PICK step names the integer $k$ with $p = 2k$.

### Scope

The scope of an ASSUME or a CASE is the proof of that step.
Outside that proof the assumption is gone, so it cannot leak into a later step.
In the opening example, each letter $k$ lives only inside its own case, and no clash between $n = 2k$ and $n = 2k + 1$ can arise.

[[A two-column proof is not a structured proof|GD8FT1XAQ9]] shows what happens without scope.
The same two cases written as rows of a flat table stand side by side, and read in order they say $2k = 2k + 1$.

### Claims in ordinary writing

An ordinary paper uses a light form of the idea.
A long proof states "Claim 1", proves it, and marks where the inner proof ends, as in [[a proof with a nested claim and two end marks|4P44ZFS5BT]].
The words "we claim" and "this proves the claim" from [[the language of proofs|GKMRQCA8CW]] mark the levels in prose.
A structured proof makes these levels systematic, numbers every step, and cites by number.
Many mathematicians find the full format heavy for short arguments and use it, if at all, only for the hard part of a proof.

### In proof assistants

Proof assistants store proofs with the same tree shape.
In Lean, `have h : P := by ...` states and proves an intermediate step, and an indented block under `·` proves one goal after a case split.
Isabelle's Isar language writes a proof as a block `proof ... qed` with steps `assume`, `have` and `show`.
The TLA+ proof system checks proofs written in Lamport's format, and [[proof assistants and their design|YM6PRDE88V]] describes the systems.

### Watch out

A structured proof and a [[two-column proof|P8PCGFASP8]] are different formats, though both number their steps.
A two-column proof is one flat list with a reason column, and a structured proof is a tree of nested sub-proofs with scope.
Numbering the rows of a table as 1.1, 1.2 and 2.1 does not make it hierarchical unless each level proves the step above it.

A second error is to use a fact from inside a sub-proof after it ends, for example a CASE assumption in the next case.
A third is a Q.E.D. step that cites "the steps above" without names, which lets an unused or missing step go unnoticed.

### History

Lamport proposed the format in "How to Write a Proof", American Mathematical Monthly 102 (1995).
He gave an updated account in "How to Write a 21st Century Proof", Journal of Fixed Point Theory and Applications 11 (2012).
Lamport is a computer scientist, known also for creating LaTeX, and he received the Turing Award for 2013.

### Try it

Write the top level of a structured proof of "$P$ if and only if $Q$".
One answer has three steps: $\langle 1 \rangle 1$ with ASSUME $P$ and PROVE $Q$, then $\langle 1 \rangle 2$ with ASSUME $Q$ and PROVE $P$, and then a Q.E.D. step $\langle 1 \rangle 3$ that cites both.

Using the opening theorem, show that $n^2 + m^2$ never leaves remainder $3$ on division by $4$.
Each square leaves $0$ or $1$, so the sum leaves $0$, $1$ or $2$.

## Explanations

### L1 human

A structured proof is like the outline of a long essay.
The top level lists the main points, each with a number.
Under each point, smaller numbered points explain why it holds.
A reader who only wants the main idea reads the top level.
A reader who wants to check everything opens each point and reads the smaller points under it.

### L2 human

We write a structured proof that the sum of two odd integers is even.

- `<1>1.` ASSUME: $m$ and $n$ are odd integers
  PROVE: $m + n$ is even
    - `<2>1.` PICK integers $k$ and $l$ with $m = 2k + 1$ and $n = 2l + 1$.
      PROOF: by the definition of an odd integer and the assumption of `<1>1`.
    - `<2>2.` $m + n = 2(k + l + 1)$.
      PROOF: $m + n = 2k + 1 + 2l + 1$ by `<2>1`, and the right side equals $2(k + l + 1)$.
    - `<2>3.` Q.E.D.
      PROOF: by `<2>2`, since $k + l + 1$ is an integer.
- `<1>2.` Q.E.D.
  PROOF: by `<1>1`.

The top level has one real step, `<1>1`, which is the theorem in ASSUME/PROVE form.
The level 2 steps prove `<1>1`, they may use its assumption, and each leaf names the facts it uses.
Check: $m = 7$ and $n = 9$ give $k = 3$, $l = 4$ and $m + n = 16 = 2 \cdot 8$.
Watch out: putting every step at level 1 gives a numbered list without hierarchy, which no longer shows which steps prove which.

### L3 human

A structured proof is an informal version of a [[natural deduction|6KT3BJZ7D1]] derivation in the box notation of Fitch or Jaśkowski, where each box is a sub-proof with its own assumptions.
An ASSUME/PROVE step is the introduction rule for implication, a CASE split is the elimination of a disjunction, and PICK is the elimination of an existential quantifier.
In type theory, a structured proof corresponds to a term built from nested `let` bindings, one for each named step.

Declarative proof languages, such as Isar in Isabelle and the language of Mizar, follow this format, and so does the Lean style with `have` steps and indented blocks.
The format moves part of the work of checking from the reader to the writer, because each citation is explicit.
For a human the gain is the choice of depth, a theme of [[level of detail in proofs|VYGBV5D8Y4]], and for a machine each leaf becomes a small separate problem for automation.
How such proofs relate to the acceptance of results in practice is discussed under [[rigor and the acceptance of proofs|1BTHSHST4M]].
