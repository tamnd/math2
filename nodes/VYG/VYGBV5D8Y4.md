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

Every written [[proof|0B94TKFQJX]] leaves some steps to the reader, and the level of detail is the choice of which ones.
Here is one claim proved twice: for every odd integer $n$, the number $n^2 - 1$ is divisible by $8$.
For a reader who knows some number theory, one sentence is enough.

> The number $n^2 - 1 = (n - 1)(n + 1)$ is a product of two consecutive even numbers, one of which is divisible by $4$.
> $\square$

For a first-year student, the same idea needs its steps written out.

> Let $n$ be odd, so $n = 2k + 1$ for an integer $k$.
> Then $n^2 - 1 = 4k^2 + 4k = 4k(k + 1)$.
> One of the consecutive integers $k$ and $k + 1$ is even, so $k(k + 1) = 2m$ for an integer $m$.
> Hence $n^2 - 1 = 8m$.
> $\square$

Both proofs are complete for their own reader.
An omitted step is acceptable when it is true, when the intended reader can supply it from known results, and when it needs no new idea.
An omitted step that fails any of these tests is a gap.
Too little detail can hide an error, and too much can hide the main idea.

## Motivation

No written proof goes down to the axioms.
In the Principia Mathematica of Whitehead and Russell, the proposition from which $1 + 1 = 2$ follows appears in Volume I after several hundred pages of logic, and the proof is completed in Volume II.
Nobody reads text at that level to understand an argument.
So every proof for a human reader leaves steps out, and the real question is which steps, for which reader, and how a reader can tell an acceptable omission from a gap.

## Notation

Mathematical writing has stock phrases for omitted steps.
"A routine calculation shows" or "expanding gives" mark an omitted calculation.
"By a standard compactness argument" or "by induction on $n$" mark an argument of a known kind.
"Similarly", "by symmetry" and "without loss of generality" mark an omitted case, and "the details are left to the reader" passes a step on openly.
The words "trivial", "obvious" and `clearly` make the same claim with less information, as [[trivial, obvious and clearly|Y0HXCJRB9B]] explains.

## Remarks

### Who the reader is

A textbook for a first course writes most steps, names each definition it uses, and shows each calculation.
Lecture notes for a later course omit the calculations and arguments that the course has already practiced.
A research paper omits the standard arguments of its field and cites known results by number, because it is written for specialists.
A proof for a proof assistant omits only what the machine can find, and the machine decides what that is.
Many guides advise choosing the reader before writing, and saying at the start of a text what background it expects.

### Acceptable omissions

A routine calculation, such as the expansion of $(2k + 1)^2$, may be omitted when the reader can do it in a few lines.
A case that becomes a written case after renaming may be omitted, as in [[the symmetric case of max plus min|E88KBNH3K1]], where the case $b \ge a$ follows from the case $a \ge b$ by exchanging the names.
A known result used in its standard form may stand as a name, as "by the [[triangle inequality|03HF5PMY5T]]" stands for $\lvert a - c \rvert \le \lvert a - b \rvert + \lvert b - c \rvert$.
A repeated argument may be shortened to "the same with $q$ in place of $p$" once its first instance is written out.

[[The square of a prime above 3, written for two readers|X6Z6XZAH8B]] proves that $p^2 \equiv 1 \pmod{24}$ at two levels, a two-line proof for a number theorist and a seven-step proof for a first-year student.

### Gaps

The worst gap is an omitted step that is false, because the omission hides the error.
In [[a routine check that fails|PDNHFSACCV]], the claim that the singular $2 \times 2$ matrices form a subspace has a "routine" closure step that is false.

Other gaps are true but out of the reader's reach.
A step may need an idea, such as an auxiliary construction, that the reader does not have.
Or the omitted step may be the main difficulty, as in "the existence of $c$ is routine" inside a proof of the [[intermediate value theorem|00KAFBR32E]], where the existence of $c$ is the whole theorem and needs the completeness of the real numbers.
A proof whose hard part is "routine to check" is a plan, not a proof.

A case called "similar" may not be.
"Similarly, $f$ is decreasing on $(-\infty, 0)$", after a proof that $f(x) = x^3$ is increasing on $(0, \infty)$, is false, since $x^3$ is increasing on all of $\mathbb{R}$.

### Facts about detail

The level of detail is relative to a reader, so one step can be an acceptable omission for one reader and a gap for another.
Adding a correct step never makes a correct proof wrong, though it can make the idea harder to see.
An omitted step must be one the writer has checked, and a writer who cannot write a step in full should not omit it.
A formal proof has the most detail possible, with one rule of inference per step.
A [[structured proof|H2W8D7BMSW]] lets each reader choose the depth, by reading the top level only or by opening each step down to its leaves.

### Watch out

The most common error is to write `it is easy to see` over a step the writer cannot prove, copied from the tone of a textbook.
The phrase then hides the gap from the writer as well as from the reader.

A related error is to write every algebraic step of a routine calculation and skip the one step that uses the hypothesis.
Detail belongs where the main work is done.

Finally, "the other case is similar" written without checking the other case often fails, because a change of sign or of the direction of an inequality breaks the similarity.

### History

Whitehead and Russell published the three volumes of Principia Mathematica from 1910 to 1913, and their derivation of $1 + 1 = 2$ shows how long a fully detailed proof becomes.
The choice of a definite reader is a theme of Halmos's essay "How to Write Mathematics" (1970).
Lamport's hierarchical proofs of 1995 let each reader choose the depth of reading.

### Try it

For a first-year reader, which step of the short proof above, "one of two consecutive even numbers is divisible by $4$", needs writing out?
One way: the numbers are $2j$ and $2j + 2 = 2(j + 1)$, and one of $j$ and $j + 1$ is even.

A proof says "similarly, the product rule holds" after proving that $a \equiv b$ and $c \equiv d \pmod n$ give $a + c \equiv b + d \pmod n$.
Is this an acceptable omission for a first-year reader?
No, because products need a new identity, $ac - bd = a(c - d) + d(a - b)$, that the sum case never used.

## Explanations

### L1 human

When we give directions to a friend, we do not describe every step.
We say "turn left at the bakery", because the friend knows how to walk to the next corner.
A proof works the same way: it skips the steps that the reader can fill in alone.
For example, a proof for an adult can write "$12 \times 12 = 144$" without the long multiplication.
But a proof must not skip the step where something new happens, and it must not skip a step that is false, because then nobody sees the mistake.

### L2 human

We decide what to write, for a first-year reader, in a proof that $a \equiv b \pmod n$ and $c \equiv d \pmod n$ imply $a + c \equiv b + d \pmod n$.

> By definition, $x \equiv y \pmod n$ means that $n \mid x - y$.
> So there are integers $s$ and $t$ with $a - b = ns$ and $c - d = nt$.
> Then $(a + c) - (b + d) = (a - b) + (c - d) = n(s + t)$.
> Since $s + t$ is an integer, $n \mid (a + c) - (b + d)$.
> $\square$

The definition is written because the proof rests on it, and the integers $s$ and $t$ are written because they are the objects of the proof.
The middle expression $(a - b) + (c - d)$ is the main step, the regrouping, so it stays.
The clause "since $s + t$ is an integer" may go for a later-year reader, but not for a first-year one.
Check: $a = 17$, $b = 2$, $c = 9$, $d = 4$ and $n = 5$ give $s = 3$, $t = 1$ and $26 - 6 = 20 = 5 \cdot 4$.

Watch out: judge the detail by the reader's knowledge, not the writer's.
A step that is routine for the writer, who already knows the proof, can be the hardest step for a reader who does not.

### L3 human

A proof for a human reader describes a formal derivation, compressed by what the writer and the reader share.
The level of detail measures this compression, and the custom of a field fixes how much compression its readers accept.
Proof assistants make the compression explicit: in Lean, tactics such as `simp`, `ring` or `linarith` fill routine steps, and the steps that need human input are the ones a careful text would also write.
When a community accepts a proof with omitted steps is discussed under [[rigor and the acceptance of proofs|1BTHSHST4M]].
The errors that hide in omitted steps are collected in [[fallacies and errors in proofs|T6QQ749DM5]], and the reader's side of the question is [[checking a proof|4M98ZZNK0E]].
