---
tag: TB9PSFGFKZ
kind: example
name: Unpacking too far in a parity proof
msc: ["00A35", "11A05"]
topics: [STSM6PR7TX]
audience: ug1
not_instance_of:
  - target: 41JZ39GE3F
    note: the writer does not stop at the integers, whose rules of algebra are known results, and unpacks them into their set-theoretic construction, so the proof loses its point
uses: [41JZ39GE3F, BV6E0ZG3YN, 0NS58JP68E, 5M5Q062R1X]
sources:
  - url: https://en.wikipedia.org/wiki/Integer
    locator: Construction
  - url: https://en.wikipedia.org/wiki/Parity_(mathematics)
    locator: lead section
---

## Example

The exercise is to prove that the sum of two even integers is even.
A student starts well and then goes on unpacking, which makes this a flawed example.

1. "$m$ is even" is unpacked to "$m = 2k$ for an integer $k$", by the [[definition of an even integer|BV6E0ZG3YN]].
   This step is correct.
2. "$n$ is even" is unpacked to "$n = 2l$ for an integer $l$".
   This step is correct.
3. The student then unpacks "integer".
   In the [[construction of the integers from the natural numbers|0NS58JP68E]], an integer is a class of pairs $(a, b)$ of natural numbers, with $(a, b) \sim (c, d)$ when $a + d = b + c$.
4. The student writes $k = [(a, b)]$ and $l = [(c, d)]$, and computes $2k = [(a, b)] + [(a, b)] = [(2a, 2b)]$.
5. The student now tries to prove $2k + 2l = 2(k + l)$ from the definition of addition of classes, and the answer runs to a page.

We check the text against the method of [[unpacking definitions|41JZ39GE3F]].
After steps 1 and 2 the goal "$m + n$ is even" needs only $2k + 2l = 2(k + l)$, which is the distributive law of the integers, a known result.
Steps 3 to 5 unpack a term whose properties are already known, and so they prove the distributive law again, which is not the exercise.
The flaw is a failure of the stopping rule: stop at a term whose needed properties are known results.

The proof that the exercise asks for is [[the proof that the sum of two even integers is even|5M5Q062R1X]].
It reads $m + n = 2k + 2l = 2(k + l)$, and $k + l$ is an integer.

## Remarks

The text is not false.
The construction of the integers is correct, and the long computation can be completed.
It fails as an answer because it buries a three-line argument under a proof of rules that the course has already established.
The same error in analysis is to unpack "real number" into Dedekind cuts while proving a limit.

Where to stop depends on the course.
In a course that constructs the integers, an exercise may ask exactly for the distributive law of classes, and then steps 3 to 5 are the right level.
The opposite error is to unpack too little: a student who does not unpack "even" has no equation and cannot start at all.

## Explanations

### L1 human

To check that $6 + 8$ is even, we write $6 = 2 \times 3$ and $8 = 2 \times 4$, so $6 + 8 = 2 \times 7$.
We do not stop to ask what the number $3$ "really is".
A student who does that turns a short answer into a long one.
Unpacking a definition is useful only until the known facts can finish the job.

### L2 human

We decide where to stop in the claim "if $A \subseteq B$, then $A \cap C \subseteq B \cap C$" for sets $A$, $B$ and $C$.
The goal unpacks to "for all $x$, if $x \in A \cap C$, then $x \in B \cap C$".
The intersection unpacks to "$x \in A$ and $x \in C$", and the given to "if $x \in A$, then $x \in B$".

Now we stop, because the remaining words are "$\in$", "and" and "if".
The proof follows: from $x \in A$ the given yields $x \in B$, and with $x \in C$ we get $x \in B \cap C$.
We do not unpack "set" or "$\in$" into the axioms of set theory, since the proof does not need them.
Watch out: a deeper unpacking is not more rigorous when the deeper facts are already proved; it is only longer.
