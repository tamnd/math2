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
We show that any answer fits, and so a guess of the next term is not a conjecture in the sense of [[forming conjectures|R2T42N5XGK]].

1. One rule. $a_n = 2^{n-1}$ gives $1, 2, 4, 8, 16$ and then $32$.
2. A second rule. $b_n = \binom{n-1}{0} + \binom{n-1}{1} + \binom{n-1}{2} + \binom{n-1}{3} + \binom{n-1}{4}$ gives $1, 2, 4, 8, 16$ and then $31$.
3. Every rule. For any number $c$, the sequence $b_n + c\binom{n-1}{5}$ gives $1, 2, 4, 8, 16$, because $\binom{n-1}{5} = 0$ for $n \leq 5$. At $n = 6$ it gives $31 + c$.
4. The conclusion. For each value $v$, the choice $c = v - 31$ gives a polynomial rule whose sixth term is $v$. So the list alone allows every continuation.
5. The status. The question names no mathematical object whose sixth term is asked. The answer "$32$" is a preference for a simple rule, and no proof or counterexample can decide it.

So guessing the next term of a bare list is not forming a conjecture.
A conjecture needs a defined object, such as "the number of regions cut by the chords of $n$ points on a circle", and then the guess "$2^{n-1}$" is a conjecture, and a false one.

## Remarks

Step 3 is a case of [[polynomial interpolation|SS1YMS2NPC]]: for any $k$ values and any further value, a polynomial of degree at most $k$ fits all of them.
The regions of a circle in step 5 are [[Moser's circle problem|M225KZAV4F]], whose answer is $b_n$.
The difference between a puzzle and a conjecture is the definition: once the object is defined, the next term is a fact, and a guess about it can be tested.

## Explanations

### L1 human

The list $1, 2, 4, 8, 16$ looks like doubling, so most people say $32$.
But other simple rules give the same five numbers and then $31$, and more complicated rules give any number at all.
Without knowing where the list comes from, there is no right answer.
Once we know what the numbers count, the question has one answer, and a guess about it becomes a real conjecture.

### L2 human

We find a rule that gives $1, 2, 4, 8, 16, 100$.

1. We need $31 + c = 100$, so $c = 69$.
2. The rule is $e_n = b_n + 69\binom{n-1}{5}$.
3. For $n = 1, \ldots, 5$, the term $69\binom{n-1}{5}$ is $0$, so $e_n = b_n$, which is $1, 2, 4, 8, 16$.
4. For $n = 6$: $e_6 = 31 + 69 \cdot 1 = 100$.

The typical use: this construction shows that a pattern in data needs a reason before it deserves belief.
A trap: the simplest rule is often the intended one in a puzzle, but simplicity is not proof.
