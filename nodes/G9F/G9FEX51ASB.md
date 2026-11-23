---
tag: G9FEX51ASB
kind: example
name: A finite list does not determine its continuation
msc: ["00A35", "41A05"]
topics: [DME0TPC348]
audience: ug1
not_instance_of:
  - target: R2T42N5XGK
    note: a guess of the next term of a bare list concerns no defined object, so it cannot be true or false and is not a conjecture
uses: [R2T42N5XGK, SS1YMS2NPC, M225KZAV4F]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_interpolation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Strong_law_of_small_numbers
    locator: lead section
---

## Example

A puzzle asks for "the next term of $1, 2, 4, 8, 16$".
Most people answer $32$, but the count of regions that the chords of $6$ points cut in a disc is $31$, and it starts with the same five numbers.
We show that every answer fits the list, so a guess of the next term is not a conjecture in the sense of [[forming conjectures|R2T42N5XGK]].

1. One rule is $a_n = 2^{n-1}$, which gives $1, 2, 4, 8, 16$ and then $32$.
2. A second rule adds binomial coefficients:
$$b_n = \binom{n-1}{0} + \binom{n-1}{1} + \binom{n-1}{2} + \binom{n-1}{3} + \binom{n-1}{4}.$$
   For $n \le 5$ this is the sum of all binomial coefficients $\binom{n-1}{j}$, which is $2^{n-1}$, so $b_n$ gives $1, 2, 4, 8, 16$.
   For $n = 6$ the term $\binom55 = 1$ is missing, so $b_6 = 1 + 5 + 10 + 10 + 5 = 31$.
3. For any number $c$, the rule $b_n + c\binom{n-1}{5}$ also gives $1, 2, 4, 8, 16$, because $\binom{n-1}{5} = 0$ for $n \le 5$.
   At $n = 6$ it gives $31 + c$.
4. For any value $v$, the choice $c = v - 31$ gives a polynomial rule whose sixth term is $v$.
   So the five terms allow every continuation.
5. The question names no mathematical object whose sixth term is asked.
   The answer $32$ is a preference for a simple rule, and no proof or counterexample can decide between $32$ and $31$.

So guessing the next term of a bare list is not forming a conjecture.

## Remarks

### What turns a guess into a conjecture

A conjecture needs a defined object.
Take "the number of regions into which the chords between $n$ points on a circle, in general position, cut the disc".
Now the sixth term is a fact, and the guess $2^{n-1}$ is a conjecture that can be tested.
It is false: the true count is $b_n$, the answer to [[Moser's circle problem|M225KZAV4F]], and the sixth term is $31$.
The same five numbers were a puzzle before the definition and a test case after it.

### The general fact behind it

Step 3 is a case of [[polynomial interpolation|SS1YMS2NPC]].
For any $k$ given values and any further value, there is a polynomial of degree at most $k$ that takes all of them.
So no finite list of terms, however long, fixes the next term, and a pattern that holds in many cases is not a proof of the next one.

### Watch out

The simplest rule is often the one a puzzle intends, and in many real problems it is also the true one.
Simplicity is still a reason to try a rule first, not a reason to believe it.
The circle regions show a case where the simplest rule fails at the first term it was not built from.

### Try it

Find a rule that gives $1, 2, 4, 8, 16$ and then $0$.
Take $c = 0 - 31 = -31$, so the rule $b_n - 31\binom{n-1}{5}$ works.

Give a rule other than $2n - 1$ that starts $1, 3, 5, 7$.
The rule $2n - 1 + (n-1)(n-2)(n-3)(n-4)$ starts $1, 3, 5, 7$ and gives $33$ at $n = 5$.

## Explanations

### L1 human

The list $1, 2, 4, 8, 16$ looks like doubling, so most people say the next number is $32$.
But another simple rule gives the same five numbers and then $31$, and more complicated rules give any number at all.
Without knowing where the list comes from, there is no right answer.
Once we know what the numbers count, the question has one answer, and a guess about it becomes a real conjecture that we can test and try to prove.

### L2 human

We find a rule that gives $1, 2, 4, 8, 16, 100$.
We need $31 + c = 100$, so $c = 69$, and the rule is
$$e_n = b_n + 69\binom{n-1}{5}.$$
For $n = 1, \dots, 5$ the added term is $0$, so $e_n = b_n$, which gives $1, 2, 4, 8, 16$.
For $n = 6$ the added term is $69\binom55 = 69$, so
$$e_6 = 31 + 69 = 100.$$
The typical use of this construction is to show that a pattern in data needs a reason before it deserves belief.
Watch out: the construction proves that the data allow every next term, and it says nothing about which rule a particular object follows.
