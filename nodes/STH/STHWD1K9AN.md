---
tag: STHWD1K9AN
kind: concept
name: Elegant and deep
aliases: [elegance-and-depth-in-mathematics, elegant-proof, deep-theorem, brute-force, abstract-nonsense, general-abstract-nonsense]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: research
uses: [4M1FGQ0HNZ, 0B94TKFQJX, 84SZZBACP3, Q1RZT7DV0F]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Philosophy of mathematics
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof techniques
  - url: https://en.wikipedia.org/wiki/Abstract_nonsense
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Elementary_proof
    locator: Prime number theorem
---

## Summary

Mathematicians use a small set of informal words to judge [[proofs|0B94TKFQJX]] and results.
A proof is called `elegant` if it gives insight: it is simple, or it unifies separate ideas, or it shows why the result is true.
A result is *deep* if its proof needs concepts and methods that are more advanced than the concepts needed to state the result.
A proof is by *brute force* if it checks as many cases as needed instead of finding a general principle; when it checks every case, it is a proof by exhaustion.
*Abstract nonsense*, or *general abstract nonsense*, is a joking name for an argument of [[category theory|Q1RZT7DV0F]] that proves a result without any reference to the details of the problem.
These words are part of [[mathematical jargon|4M1FGQ0HNZ]]: they are judgments, not definitions, and no theorem depends on them.
The study of mathematical beauty as an aesthetic value belongs to [[mathematics and culture|FWE06TZ36P]].

## Motivation

Research papers, referee reports and talks use these words to tell the reader what kind of argument to expect.
"This is a deep theorem" warns the reader that the proof needs a large theory.
"By abstract nonsense" tells the reader that the step follows from general facts about categories, such as a universal property, and that the reader can supply it.
"A brute force computation shows" tells the reader that the step is a finite check with no idea behind it.
A reader who knows this code can decide quickly which parts of a paper to read closely.

## Notation

There is no special symbol.
Common phrases are "a deep result", "an `elegant` argument", "a slick proof", "by brute force", "a direct computation", "by general abstract nonsense" and "by generalized abstract nonsense".
The word `beautiful` is used with a meaning close to `elegant`.
Gian-Carlo Rota separated the elegance of a presentation from the beauty of a concept.

## Remarks

### Examples

1. [[A brute force check of the values of n^2 + n + 41|6EHQD2M1PS]]. A finite computation shows that the values are prime for $n = 0, \dots, 39$, and the same computation finds the failure at $n = 40$.
2. [[The uniqueness of a product is abstract nonsense|9NQD3BC9N0]]. A product in any category is unique up to unique isomorphism, and the proof uses only the universal property.
3. The [[irrationality|0DZXAXEJQ9]] of $\pi$ is usually called deep. The statement uses only integers and the number $\pi$, but the usual proofs need real analysis.
4. [[Fermat's last theorem|0Y5X3SDBCZ]] is a deep theorem. The statement is about integers, and the proof by Wiles uses [[elliptic curves|427N6S6QQW]] and [[modular forms|GWKN5VG78A]].
5. The [[four colour theorem|0M406JC8J1]] has a brute force proof. Appel and Haken proved it in 1976 with a computer check of a large finite number of cases.
6. The pairing proof of $1 + 2 + \dots + n = n(n + 1)/2$ is a standard `elegant` proof. Write the sum forwards and backwards; each of the $n$ columns sums to $n + 1$, so twice the sum is $n(n + 1)$.

### Non-examples

1. [[The equation 2^10 = 1024 is not deep|FWDC5ZHAG9]]. The statement and its proof use only multiplication of integers.
2. The [[irrationality of the square root of 2|0DZGSDHD92]] is not deep. Its proof uses only divisibility of integers, which the statement already needs.
3. The [[prime number theorem|0EHBY5Y84N]] is no longer deep in Hardy's sense. It was once thought deep, until [[elementary proofs|84SZZBACP3]] were found.

### Basic properties

1. The words are judgments. Two mathematicians can disagree about whether a proof is `elegant`, and no proof becomes more or less correct by the judgment.
2. Depth is relative to the known proofs. A new proof with simpler methods can change the judgment, as the elementary proofs of the prime number theorem did.
3. Depth is not length. A deep result can have a short proof after the theory exists, and a long brute force proof with basic tools is not deep.
4. Brute force is often the opposite of `elegant`, but it is a valid method. A finite check of every case is a complete proof, even if it gives no insight.
5. Abstract nonsense is rigorous. The phrase marks an argument that uses only general structure, so the same argument applies in every category with that structure.

### History

Eilenberg and Mac Lane introduced categories in a paper of 1942.
Mac Lane later wrote that the subject was then called "general abstract nonsense".
In a 1921 lecture, Hardy said that some theorems "lie deep" and others lie nearer to the surface, and he doubted that the prime number theorem has an elementary proof.
Selberg and Erdős found elementary proofs from 1948, and the theorem was no longer seen as deep in this sense.

### Common errors

1. A reader takes "abstract nonsense" as a criticism, or as a sign that the proof is weak. The phrase is a joke about style; the argument is a complete proof.
2. A reader thinks that a deep result has a hard statement. Depth compares the proof with the statement; a deep result often has a short, simple statement.
3. A writer uses `elegant`, `obvious` or "by brute force" in place of an argument. A proof must still give the argument or the computation.

## Explanations

### L1 human

Mathematicians use some everyday words with special meanings.
A result is "deep" when its statement is simple, but its proof needs a lot of advanced mathematics.
A proof is `elegant` when it is short and shows in a simple way why the result is true.
A proof is "brute force" when it checks many cases one by one.
"Abstract nonsense" is a joke name for proofs that use only very general ideas.
None of these words is a definition; they are opinions that most mathematicians share.

### L2 human

The words give a quick summary of a proof.

1. Fermat's last theorem has a statement that a school student can read. Its proof uses elliptic curves and modular forms, so the theorem is deep.
2. The sum $1 + 2 + \dots + 100$ can be found by brute force, with $99$ additions. The pairing argument finds $100 \cdot 101/2 = 5050$ with one idea, and most readers call it `elegant`.
3. The uniqueness of a product follows only from its universal property, so the proof is abstract nonsense.

The typical use of these words is in the introduction of a paper, to tell the reader what kind of proof follows.
A trap: these words do not replace an argument; a proof that says "by brute force" must still say which cases it checks.

### L3 human

The word "deep" is often made more precise with the gap between the language of a statement and the language of its known proofs.
For arithmetical statements, logic gives one measure of this gap: the weakest formal system in which a proof exists, as in Friedman's conjecture about [[elementary function arithmetic|2JD80TE553]].
"Abstract nonsense" has a precise core: the [[Yoneda lemma|D6DF1ARPVD]] and the uniqueness of universal objects hold in every category, and the [[snake lemma|Q8AYGD93CW]] holds in every abelian category.
Such arguments are often short, so they are `elegant` in the sense of length, but readers new to the language find them hard to follow.
Brute force has become a standard tool with computer-assisted proofs, such as the proofs of the four colour theorem and of the [[Kepler conjecture|AFMBQT06ZV]].
These proofs raise the question of what a proof must explain, beyond being correct.
