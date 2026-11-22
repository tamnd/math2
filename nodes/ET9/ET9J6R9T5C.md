---
tag: ET9J6R9T5C
kind: concept
name: Q.E.D. and end of proof marks
aliases: [qed, quod-erat-demonstrandum, tombstone, halmos-symbol, end-of-proof-symbol, qef, quod-erat-faciendum]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
uses: [0B94TKFQJX, 4ZNYMYRRY3]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section Q
    note: adopted
    mention: wikipedia://en/76765067#161N
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Q.E.D.
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Q.E.D.
    locator: Difference from Q.E.F.
  - url: https://en.wikipedia.org/wiki/Q.E.D.
    locator: Typographical forms used symbolically
  - url: https://en.wikipedia.org/wiki/Tombstone_(typography)
    locator: lead section
inventory: [12PB8WVBA2]
---

## Summary

An end of proof mark is a small sign that says "the proof stops here", so that the reader knows where the argument ends and the commentary begins.
You meet it at the right margin after the last line of a proof, as in "so $a + b = 2(m + n)$ is even. ∎"

An *end of proof mark* is a word or a symbol placed at the end of a [[proof|0B94TKFQJX]] to show that the proof is complete.
The classical mark is `Q.E.D.`, an [[abbreviation|4ZNYMYRRY3]] of the Latin *quod erat demonstrandum*, "which was to be demonstrated".
The modern mark is the *tombstone* $\blacksquare$, also called the *Halmos symbol*, or its hollow form $\square$.
The related mark `Q.E.F.`, for *quod erat faciendum*, "which was to be done", ends a construction instead of a proof.
The mark adds no logical content: it records the author's claim that the argument is finished.

## Motivation

A proof can run over several pages, and the text after it often continues with a remark or the next result.
Without a mark the reader can be unsure where the proof stops.
A fixed mark makes the structure visible at a glance, so a reader can skip a proof and find the next statement by looking for the mark.

Long proofs need more than one mark.
A proof often contains a claim with its own short proof, and a separate mark at the end of that claim shows where the inner proof stops and the main proof resumes.
Some authors also close examples and remarks with a mark, for the same reason.

## Notation

The marks in use are the abbreviation `Q.E.D.` (or QED), the filled square $\blacksquare$, the hollow square $\square$, two or four forward slashes, and closing phrases such as "This completes the proof" or "as required".
In TeX the squares are `\blacksquare` and `\square`, and the Unicode character U+220E, named "end of proof", is ∎.
In the AMS theorem package for LaTeX the default mark is a hollow square, and `\qedhere` moves it onto a displayed formula that ends a proof.
The start of a proof is marked by the word *Proof* in bold or italic type, and in older English texts the Latin word *aliter*, "otherwise", introduces a second proof of the same result.

The same square can mean two things, depending on where it stands.
After a proof, $\square$ means "the proof is complete".
Directly after a statement with no proof, many books use it to mean that the proof is omitted or follows at once from what came before:
$$\text{Lemma 3. Every group of prime order is cyclic.} \quad \square$$
To tell which reading applies, look at what precedes the mark: a proof, or only a statement.
Filled and hollow squares carry the same meaning, and the choice between them is house style.

## Remarks

### One proof, two marks

[[A proof with a nested claim and two end marks|4P44ZFS5BT]] proves that there are infinitely many primes $p \equiv 3 \pmod 4$.
Inside it, a claim says that a product of numbers $\equiv 1 \pmod 4$ is again $\equiv 1 \pmod 4$, and its proof ends with $\square$.
The main proof then continues with $N = 4 p_1 \cdots p_k - 1$, and it ends with $\blacksquare$.
Check on the list $3, 7, 11$:
$$N = 4 \cdot 231 - 1 = 923 = 13 \cdot 71, \qquad 71 \equiv 3 \pmod 4,$$
so $71$ is a new prime of the right form.
The two marks tell you which proof each line belongs to, and marks nest the way brackets do.

### Shown or done

Euclid ended a proof that a statement is true with a Greek phrase that the Latin `Q.E.D.` translates, and he ended a construction with a different phrase, rendered `Q.E.F.`.
[[Euclid's first construction ends with Q.E.F.|8YNCHJY6H0]]: Proposition 1 of Book I constructs an equilateral triangle on a given segment, so it ends with "which was to be done".
Proposition 4 of Book I proves that two triangles with two equal sides and the same included angle are congruent, so it ends with "which was to be shown".
The rule is to read the task in the statement: "prove that" leads to `Q.E.D.`, and "construct" or "find" leads to `Q.E.F.`.
Modern texts rarely keep the distinction, and most end every proof with the same square.

### What is not an end mark

[[The therefore sign marks a step, not the end of a proof|BVMX2JE2A1]].
The sign $\therefore$ means "so", and an argument can use it several times before the end, so it does not close anything.
In physics, QED usually abbreviates [[quantum electrodynamics|V329C7A1QP]], the theory of light and charged particles, and it is not a proof mark.
The italic type of a theorem statement shows where the statement ends, but it says nothing about a proof.

### Watch out

The first error is to treat the mark as part of the argument.
A proof with a gap is still incomplete when it ends with $\blacksquare$, and the square does not replace the missing steps.

The second error is to end a proof with $\therefore$.
A student who writes "$\therefore$ $n^2$ is odd" as the last line leaves the reader unsure whether the proof is finished, since $\therefore$ only introduces a conclusion.

The third error is to stop reading at the first square in a nested proof.
In the example above the first $\square$ ends only the claim, and the main argument comes after it.

### History

Greek mathematicians, among them Euclid and Archimedes, ended proofs with the phrase *hoper edei deixai*, "which was to be shown", and the Latin *quod erat demonstrandum* translates it.
The filled square as an end of proof mark is credited to Paul Halmos, who said that he took it from the end marks of magazine articles.
Spinoza's *Ethics*, published in 1677, ends its demonstrations with Q.E.D., although its subject is philosophy.

### Try it

First, a text states that the sum of two odd integers is even, puts a square right after the statement, and moves on to the next theorem.
What does the square mean?
It means that the proof of Theorem 2 is omitted or left to the reader, since no proof stands before the mark.

Second, which mark fits the end of "Find the point on the line $y = 2x$ that is closest to $(5, 0)$"?
The task is to find an object, so in Euclid's style the mark is `Q.E.F.`; the answer is $(1, 2)$, and a modern text would simply end with a square.

## Explanations

### L1 human

When a proof is finished, mathematicians put a small mark at the end.
The old mark is the three letters `Q.E.D.`, from a Latin phrase that means "which was to be shown".
Today most books use a small square, ∎ or $\square$, instead.
The square tells you: the proof stops here.
If the text continues after the square, it is a new part, such as a remark or the next theorem.

### L2 human

Read this short proof and look at the mark.
*Claim.* The sum of two even numbers is even.
*Proof.* Let $a = 2m$ and $b = 2n$ with integers $m$ and $n$, and add:
$$a + b = 2m + 2n = 2(m + n),$$
and $m + n$ is an integer, so $a + b$ is even.
$\square$
*Remark.* The same proof shows that a sum of any finite number of even numbers is even.

The square tells you that the proof is complete, so the remark is a comment and not a step.
In practice a text has one mark at the end of each proof and one more for each claim inside a long proof.
The proof is complete because of its steps, and the square only reports that the author believes so.

### L3 human

In a proof assistant the end of a proof is a command that the system checks.
In Coq the command `Qed.` closes a proof, and the system accepts it only when no goal remains open.
In Isabelle the Isar language closes a structured proof with the keyword `qed`.
So in formal proofs the end mark is no longer only a claim of the author, because the checker verifies it.
The nesting of marks in long printed proofs corresponds to the nesting of subgoals in a formal proof, where each inner goal must be closed before the outer one.
