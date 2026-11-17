---
tag: E1PE9R8DBB
kind: concept
name: Mathematical rigour
aliases: [rigour, rigor, mathematical-rigor, rigorous-proof]
msc: ["00A35"]
topics: [1BTHSHST4M]
audience: ug1
uses: [0B94TKFQJX, GD2JBXJV5Z, Y0HXCJRB9B]
sources:
  - url: https://en.wikipedia.org/wiki/Rigour
    locator: Mathematics
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: History
  - book: isbn:9781108439534
    locator: Introduction
---

## Summary

Mathematical rigour is the property of an argument in which each step is justified, and the justification can be checked by a competent reader.
A step is justified when it is an axiom, a definition, a hypothesis, a result proved before, or a consequence of earlier steps by a valid rule of inference.
An argument is rigorous for a stated audience when each step that it leaves out can be filled in by that audience with routine work, and no step depends on a picture, an intuition or an unproved claim.
Rigour is the standard by which mathematicians accept a [[proof|0B94TKFQJX]], and it is what makes a theorem reliable for all later use.

## Motivation

Many statements look true from a picture or from a few cases.
A continuous curve that starts below the horizontal axis and ends above it seems to cross the axis.
Yet over the rational numbers the function $f(x) = x^2 - 2$ is negative at $x = 1$ and positive at $x = 2$, and it has no rational zero, as [[this example|ARWPBPW0Y3]] shows.
So the crossing depends on a property of the real numbers that the picture does not show.

Rigour is the answer to this problem.
A rigorous proof names each property that it uses, so a reader can see where a hypothesis enters and what fails without it.
It also lets one result serve as a safe step in another proof, because each step was checked.
Without rigour, an error in one argument can spread to every result that uses it.

## Notation

There is no symbol for rigour.
American books spell the word "rigor", and British books spell it "rigour"; this site uses "rigour".
The adjective is "rigorous" in both spellings.

Several words describe the level of detail of a proof.
A "sketch" or an "outline" gives the main steps and leaves gaps on purpose.
A "complete proof" or a "full proof" claims that no gap remains for the intended reader.
A "formal proof" is a derivation in a formal system, in which each step follows a stated rule; the page [[formal and informal proofs|8VZ77R4R8S]] treats it.
The words [[trivial, obvious and clearly|Y0HXCJRB9B]] claim that a step is routine, and they hide a gap when the step is not routine.

## Remarks

### Examples

- The supremum proof of the [[intermediate value theorem|00KAFBR32E]] is rigorous: it uses the [[completeness axiom|0AXWET80YW]] at one named step. [[This example|ARWPBPW0Y3]] compares it with the picture argument.
- The pairing argument for $1 + 2 + \cdots + n = n(n+1)/2$ is rigorous for a school reader, and an induction makes it rigorous for a reader who asks what the dots mean. [[This example|KQZNTQG6KM]] gives both levels.
- The [[epsilon-delta definition of a limit|0GBZDAFPX8]] makes "$f(x)$ gets close to $L$" into a statement with quantifiers, so a proof about limits can check each inequality.
- The proof that $\sqrt{2}$ is [[irrational|0DZGSDHD92]] is rigorous: each step uses the hypothesis $\sqrt{2} = a/b$, the definition of an even number, or arithmetic.
- A proof checked by a proof assistant, such as [[this Lean proof|QF0Q7B5Q73]], is rigorous at the highest level: a program checks each step against fixed rules.

### Non-examples

- [[Euclid's proof of his first proposition|GQCW6RG3GB]] is not rigorous by modern standards. The condition that fails: one step, the meeting of two circles, follows from no stated axiom.
- The [[checks of $n^2 + n + 41$|H75AB4EJT5]] for $n = 0$ to $39$ are not a rigorous proof that the value is always prime. The condition that fails: the steps cover only forty cases, and the claim is about all natural numbers.
- The argument "a curve that goes from below the axis to above it must cross the axis" is not rigorous. The condition that fails: the step uses a picture, and the property behind it, the completeness of $\mathbb{R}$, is not named.

### Basic properties

- Rigour is relative to the audience. A proof for research specialists leaves out steps that a proof for first-year students must write.
- Rigour is relative to the period. The standard of the 18th century accepted arguments with infinitely small quantities that the standard of the late 19th century rejected; the page [[history of proof and rigour|20F7K9RVT6]] tells this story.
- Rigour is not formality. A rigorous informal proof can be expanded into a formal derivation, but the informal proof is already rigorous when each gap is routine for its reader.
- Rigour is a property of the argument, not of the conclusion. A false argument can have a true conclusion, and a correct theorem can have an incorrect published proof.
- Rigour depends on the starting points. A proof is rigorous relative to the [[axioms|GD2JBXJV5Z]] and the earlier results that it uses.

### History

Greek mathematics made deductive proof the standard, and [[Euclid's Elements|83WHDAV68J]] was the model of rigour for more than two thousand years.
In the 19th century Bolzano (1817) and Cauchy (1821) proved the intermediate value theorem, which earlier authors had taken as evident.
In the late 19th century Hilbert and others found that the Elements uses assumptions that its axioms do not state, and [[Hilbert's axioms|KM1FB8XZ2R]] filled these gaps.
In the 20th century rigour came to mean, in principle, that a proof can be written in a formal system such as set theory, and today proof assistants check such proofs.

### Common errors

- To think that a rigorous proof must be long and full of symbols. A rigorous proof gives each step that its reader needs, and no more.
- To think that a picture or a computation of many cases is a rigorous proof of a general claim. A picture can suggest the proof, and the proof must still name each property that it uses.
- To think that rigour is fixed for all time. The standard changed in the 19th century, and it changes again with computer proofs, as the page [[computer-assisted proof|MC18C7BMFT]] explains.

## Explanations

### L1 human

A rigorous argument is one in which each step has a reason that anyone can check.
The reason can be a rule we agreed on, a fact we proved before, or simple arithmetic.
Take the claim "the sum of two odd numbers is even".
The example $3 + 5 = 8$ is not a reason, because it is only one case.
A rigorous argument says: an odd number is one more than an even number, so the sum of two odd numbers is two more than the sum of two even numbers, and that is even.
Each part of this sentence can be checked, and it works for every pair of odd numbers.

### L2 human

We test the rigour of a short proof by giving, for each step, the reason that justifies it.
The claim: if $n$ is an integer and $n^2$ is even, then $n$ is even.

1. Suppose that $n$ is odd. Reason: we prove the [[contrapositive|0BB5TPGQ1N]], that if $n$ is odd, then $n^2$ is odd.
2. Then $n = 2k + 1$ for some integer $k$. Reason: this is the definition of an odd integer.
3. So $n^2 = 4k^2 + 4k + 1$. Reason: we expand the square by the laws of algebra.
4. So $n^2 = 2(2k^2 + 2k) + 1$. Reason: we factor $2$ from the first two terms.
5. So $n^2$ is odd. Reason: the number $2k^2 + 2k$ is an integer, so $n^2$ has the form of the definition.
6. So if $n^2$ is even, then $n$ is even. Reason: a statement and its contrapositive are equivalent.

Each step has a reason, so the proof is rigorous for a first-year reader.
The typical use of this test is to check one's own proof before handing it in.
A trap is to accept a step because it "looks right": the step "if $n^2$ is even then $n$ is even, since squares keep parity" names no reason that a reader can check.

### L3 human

Two notions of rigour live side by side.
The practical notion is social: a proof is rigorous when experts agree that each gap can be filled with routine work.
The ideal notion is formal: a proof is rigorous when it can be expanded into a derivation in a formal system, such as first-order logic with the axioms of set theory, in which a program can check each step.
Most mathematicians accept the practical notion and believe that it implies the ideal one, and the page [[formal and informal proofs|8VZ77R4R8S]] discusses this belief.

Rigour has costs and limits.
Very long proofs, such as the classification of finite simple groups, strain the practical notion, and computer proofs strain the idea that a human checks each step; the pages [[long proofs and surveyability|RM0S65BHWH]] and [[computer-assisted proof|MC18C7BMFT]] treat these cases.
The debate around the essay of Jaffe and Quinn in 1993 asked how much speculation mathematics should allow before rigour arrives; see [[the Jaffe-Quinn and Thurston debate|K3M3TEX7SJ]].
The philosophical question of why rigorous proofs give knowledge belongs to the [[philosophy of mathematics|NTJ5XW0PVD]].
