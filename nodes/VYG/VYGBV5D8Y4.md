---
tag: VYGBV5D8Y4
kind: concept
name: Level of detail in proofs
aliases: [level-of-detail-in-proofs, gaps-in-proofs]
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: ug2
uses: [0B94TKFQJX, 8JQHJK94RZ, Y0HXCJRB9B]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
  - url: https://en.wikipedia.org/wiki/Principia_Mathematica
    locator: Contents
  - url: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Mathematics
    locator: Proofs
---

## Summary

The level of detail of a written [[proof|0B94TKFQJX]] is a choice of steps.
Some steps the proof writes out, and the other steps it leaves to the reader.
An omitted step is acceptable for a given reader when three conditions hold.
The step is true, this reader can supply it with known results and methods, and it needs no new idea.
An omitted step that fails one of these conditions is a gap.
A proof is complete for a reader when it has no gap for that reader.
So the same argument can be complete for a specialist and incomplete for a first-year student.
The idea matters because a proof with too little detail can hide an error.
And a proof with too much detail can hide its main idea.

## Motivation

No written proof gives every step down to the axioms.
In the Principia Mathematica of Whitehead and Russell, the proposition from which $1 + 1 = 2$ follows appears in Volume I.
It comes after several hundred pages of logic, and the proof is completed in Volume II.
A proof at that level of detail is a formal derivation, and nobody reads such text to understand an argument.
So every proof for a human reader leaves steps out.
The question is which steps a writer may leave out, for which reader, and how the reader can tell an acceptable omission from a gap.

## Notation

1. Phrases for an omitted calculation: "a routine calculation shows", "expanding gives", "a short computation shows".
2. Phrases for an omitted argument of a known kind: "by a standard argument", "by a standard compactness argument", "by induction on $n$".
3. Phrases for an omitted case: "similarly", "the other case is the same with $a$ and $b$ exchanged", "by symmetry", "without loss of generality".
4. Phrases that pass a step to the reader: "the details are left to the reader", "we leave the verification as an exercise".
5. The words "trivial", "obvious" and `clearly` make the same claim with less information, as the page [[trivial, obvious and clearly|Y0HXCJRB9B]] explains.

## Remarks

### Who the reader is

1. A textbook for a first course writes most steps, names each definition it uses, and shows each calculation.
2. Lecture notes for a later course omit the calculations and the arguments that the course has already practised.
3. A research paper omits the standard arguments of its field and cites the known results by number, so it is written for a specialist.
4. A proof for a proof assistant omits nothing that the machine cannot find, and the machine decides which steps it can find alone.

Style guides advise the writer to choose the reader before writing, and to state the expected background at the start of a text.

### Acceptable omissions

1. A routine calculation, such as the expansion of $(2k + 1)^2$, when the reader can do it in a few lines.
2. A case that is the same as a written case after renaming, such as the case $b \ge a$ after the case $a \ge b$.
3. A step that uses a known result in its standard form, with the result named.
4. A repeated argument, when the first instance is written out and the later instance is "the same with $q$ in place of $p$".

### Gaps

1. An omitted step that is false. This is the most dangerous case, because the omission hides the error.
2. An omitted step that needs an idea that the reader does not have, such as an auxiliary construction.
3. An omitted step that is the main difficulty of the proof. If "it is routine to check" covers the hard part, the proof is a plan, not a proof.
4. A case called "similar" that is not similar, for example because a sign or an inequality changes.

### Examples

1. [[The congruence p^2 = 1 mod 24 for primes p > 3, written for two readers|X6Z6XZAH8B]]. It gives a two-line proof for a number theorist and a seven-step proof for a first-year student.
2. [[An omitted symmetric case in max(a, b) + min(a, b) = a + b|E88KBNH3K1]]. The omitted case follows from the written case by exchanging the names $a$ and $b$.
3. "By induction on $n$" in a paper on combinatorics, for a formula such as $1 + 3 + \cdots + (2n - 1) = n^2$. The base case $1 = 1^2$ and the step $n^2 + (2n + 1) = (n + 1)^2$ are routine for the reader of such a paper.
4. "By the [[triangle inequality|03HF5PMY5T]]" in an analysis course, for $\lvert a - c \rvert \le \lvert a - b \rvert + \lvert b - c \rvert$. The name of the result is the whole step.

### Non-examples

1. [[A routine check that fails: singular matrices do not form a subspace|PDNHFSACCV]]. The step called routine is false. So the omission is a gap, not an acceptable omission.
2. "The existence of the point $c$ is routine" in a proof of the [[intermediate value theorem|00KAFBR32E]]. The existence of $c$ is the whole theorem, and it needs the completeness of the real numbers.
3. "Similarly, $f$ is decreasing on $(-\infty, 0)$" after a proof that $f(x) = x^3$ is increasing on $(0, \infty)$. The second claim is false, because $x^3$ is increasing on all of $\mathbb{R}$, so the case is not similar.

### Basic properties

1. The level of detail is relative to the reader. A step can be an acceptable omission for one reader and a gap for another.
2. Adding a correct step never makes a correct proof wrong. It can make the proof longer and the idea harder to see.
3. An omitted step must be one that the writer has checked. A writer who cannot write the step in full should not omit it.
4. A formal proof has the maximal level of detail: each step is one application of a rule of inference.
5. A [[structured proof|H2W8D7BMSW]] lets the reader choose the level, by reading the top level only or by expanding each step to its leaves.

### History

Whitehead and Russell published the three volumes of Principia Mathematica from 1910 to 1913.
Their derivation of $1 + 1 = 2$ shows the length of a fully detailed proof.
Paul Halmos discussed the choice of detail for the reader in his essay "How to Write Mathematics" of 1970.
Leslie Lamport proposed hierarchical proofs in 1995 so that each reader can choose the depth of reading.

### Common errors

1. A student copies `it is easy to see` from a textbook for a step that the student cannot prove. The phrase then hides a gap from the writer as well as from the reader.
2. A student writes every algebraic step of a routine calculation but omits the one step that uses the hypothesis. The level of detail should be highest at the step that does the main work.
3. A student writes "the other case is similar" without checking the other case. A change of sign or of the direction of an inequality often breaks the similarity.

## Explanations

### L1 human

When we give directions to a friend, we do not describe every step.
We say "turn left at the bakery", because the friend knows how to walk to the next corner.
A proof works the same way: it skips the steps that the reader can fill in alone.
For example, a proof for an adult reader can write "$12 \times 12 = 144$" without showing the long multiplication.
But a proof must not skip the step where something new or surprising happens.
And it must not skip a step that is false, because then nobody sees the mistake.

### L2 human

We decide what to write in a proof, for a first-year reader, that $a \equiv b \pmod n$ and $c \equiv d \pmod n$ imply $a + c \equiv b + d \pmod n$.

1. The definition: $x \equiv y \pmod n$ means that $n \mid x - y$. We write this, because the whole proof rests on it.
2. The hypotheses give integers $s$ and $t$ with $a - b = ns$ and $c - d = nt$. We write this, because it introduces the objects of the proof.
3. Then $(a + c) - (b + d) = (a - b) + (c - d) = n(s + t)$. We write the middle expression, because the regrouping is the main step.
4. Since $s + t$ is an integer, $n \mid (a + c) - (b + d)$. We may omit "since $s + t$ is an integer" for a later-year reader, but not for a first-year reader.
5. The analogous statement for products needs $ac - bd = a(c - d) + d(a - b)$. A proof that says "similarly for products" omits this new identity, so for products the word "similarly" would hide a step.

The typical use of the idea is to decide, line by line, whether the intended reader can supply a step.
A trap is to judge by the writer's own knowledge.
A step that is routine for the writer, who knows the proof, can be the hardest step for a reader who does not.

### L3 human

A proof for a human reader is a description of a formal derivation, compressed by the shared knowledge of the writer and the reader.
The level of detail measures this compression, and the standard of a field fixes how much compression its readers accept.
Proof assistants make the compression explicit.
In Lean, automation such as `simp`, `ring` or `linarith` fills routine steps.
The steps that need human input are the ones that a careful text would also write.
The debate on what a gap is, and when a community accepts a proof with omitted steps, belongs to [[rigour and the acceptance of proofs|1BTHSHST4M]].
The errors that hide in omitted steps are collected in [[fallacies and errors in proofs|T6QQ749DM5]].
The reader's side of the question is the page [[checking a proof|4M98ZZNK0E]].
