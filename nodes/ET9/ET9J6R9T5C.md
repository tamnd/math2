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

An *end of proof mark* is a word or a symbol at the end of a [[proof|0B94TKFQJX]] that tells the reader that the proof is complete.
The classical mark is `Q.E.D.`, an [[abbreviation|4ZNYMYRRY3]] of the Latin phrase *quod erat demonstrandum*, "which was to be demonstrated".
The modern mark is the *tombstone* $\blacksquare$, also called the *Halmos symbol*, or its hollow form $\square$.
The related mark `Q.E.F.`, for *quod erat faciendum*, "which was to be done", ends a construction instead of a proof.
Authors also use end marks for claims inside a proof, and some use them for examples and remarks.
The mark adds no logical content: it records the claim of the author that the argument is finished.

## Motivation

A proof can be long, and the text after it often continues with remarks or a new result.
Without a mark, the reader can be unsure where the proof stops and the commentary starts.
A fixed mark at the end of each proof makes the structure of a page visible at a glance.
A reader can skip a proof and find the next statement by looking for the mark.
Inside a long proof, a separate mark at the end of a claim shows where the proof of the claim stops and the main proof continues.

## Notation

The common end of proof marks are the following.

1. The abbreviation `Q.E.D.` or QED, in capital or small letters.
2. The filled tombstone $\blacksquare$, written `\blacksquare` in TeX. The Unicode character U+220E, "end of proof", is ∎.
3. The hollow square $\square$, written `\square` or `\Box` in TeX. In the AMS theorem environment for LaTeX, it is the default end of proof symbol.
4. Two or four forward slashes, written // or ////.
5. A sentence such as "This completes the proof." or "as required".

The abbreviation `Q.E.F.` ends a construction.
In older English texts, the Latin word *aliter*, "otherwise", introduces a second proof of the same result.
The start of a proof is usually marked by the word *Proof* in bold or italic type.

## Remarks

### Examples

1. [[A proof with a nested claim and two end marks|4P44ZFS5BT]]. The proof that there are infinitely many primes of the form $4k + 3$ contains a claim with its own end mark.
2. [[Euclid's first construction ends with Q.E.F.|8YNCHJY6H0]]. The construction of an equilateral triangle on a given segment ends with "which was to be done", not "which was to be shown".
3. The *Ethics* of Spinoza, published in 1677, uses `Q.E.D.` at the end of its demonstrations, for example after Proposition 3 of Part 1. Its subject is philosophy, not mathematics.
4. A book typeset with the AMS theorem environment shows a hollow square $\square$ at the end of each proof by default.
5. On a chalkboard, a lecturer often draws a filled or hollow square to show the end of a proof.

### Non-examples

1. [[The therefore sign marks a step, not the end of a proof|BVMX2JE2A1]]. The sign $\therefore$ introduces a conclusion inside an argument, and more steps can follow it.
2. In physics, QED usually abbreviates [[quantum electrodynamics|V329C7A1QP]], a theory of light and charged particles. It is not a proof mark.
3. The italic type of a theorem statement marks where the statement ends, but it is not an end of proof mark.

### Basic properties

1. The mark is a claim, not a proof. A proof with a gap is still incomplete when it ends with $\blacksquare$.
2. Marks can nest. A claim inside a proof can end with its own mark, and the main proof then ends with a second mark.
3. The choice between `Q.E.D.` and `Q.E.F.` follows the kind of result. `Q.E.D.` ends a proof that a statement is true, and `Q.E.F.` ends a construction of an object.
4. The mark goes at the end of the last line of the proof, often at the right margin. If the proof ends with a displayed formula, LaTeX users write `\qedhere` to put the mark on that line.

### History

Greek mathematicians, among them Euclid and Archimedes, ended proofs with the phrase ὅπερ ἔδει δεῖξαι (*hoper edei deixai*), which the Latin *quod erat demonstrandum* translates.
The Latin phrase appears in a 1501 translation of Euclid by Giorgio Valla, and Johannes Praetorius used the abbreviation once in 1598.
Paul Halmos claimed that he introduced the filled square as an end of proof mark, and he took it from the end marks of magazine articles.
Its first use as an end of proof symbol appears to be in his book *Measure Theory* of 1950.

### Common errors

1. A student writes $\blacksquare$ to end an argument that is not complete. The mark does not replace the missing steps.
2. A student uses $\therefore$ as an end of proof mark. The therefore sign means "so", and it introduces a conclusion.
3. A student thinks that $\square$ and $\blacksquare$ mean different things. Both mark the end of a proof, and the choice is a matter of style.

## Explanations

### L1 human

When a proof is finished, mathematicians put a small mark at the end.
The old mark is the three letters `Q.E.D.`, from a Latin phrase that means "which was to be shown".
Today most books use a small square, ∎ or $\square$, instead.
The square tells you: the proof stops here.
If the text continues after the square, it is a new part, such as a remark or the next theorem.

### L2 human

Read this short proof and look at the marks.

1. *Claim.* The sum of two even numbers is even.
2. *Proof.* Let $a = 2m$ and $b = 2n$ with integers $m, n$. Then $a + b = 2(m + n)$, and $m + n$ is an integer. $\square$
3. *Remark.* The same proof shows that a sum of any finite number of even numbers is even.

The square after step 2 tells the reader that the proof is complete, so step 3 is a comment, not part of the proof.
The typical use is one mark at the end of each proof, and one more mark for each claim inside a long proof.
A trap: the mark is not a reason; a proof is complete because of its steps, not because of the square.

### L3 human

In a proof assistant, the end of a proof is a command that the system checks.
In Coq, the command `Qed.` closes a proof, and the system accepts it only if no goal remains open.
In Isabelle, the Isar language closes a structured proof with the keyword `qed`.
So in formal proofs the end mark is no longer only a claim of the author: the checker verifies it.
In printed mathematics, the mark keeps its informal role, and the reader must check that every step is present.
The nesting of marks in long proofs corresponds to the nesting of subgoals in a formal proof.
