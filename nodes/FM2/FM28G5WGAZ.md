---
tag: FM28G5WGAZ
kind: example
name: "A conditional with a disjunctive hypothesis: (p or q) implies r is equivalent to (p implies r) and (q implies r)"
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0JMR2HM2N2]
uses: [0JMR2HM2N2, 05RSK4Q657, 0NMG7W7Q11, 025YZN3VJW, 0F72FK8EKB]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunction_elimination
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.5
---

## Example

"If it rains or it snows, the match is canceled" makes the same promise as the pair "if it rains, the match is canceled" and "if it snows, the match is canceled".
With $p$ for "it rains", $q$ for "it snows" and $r$ for "the match is canceled", the claim is that
$$(p \lor q) \to r \;\equiv\; (p \to r) \land (q \to r),$$
that is, the two formulas are [[logically equivalent|0JMR2HM2N2]].
We find the rows where each side is false and compare them.

1. An [[implication|0NMG7W7Q11]] $a \to b$ is false only when $a$ is true and $b$ is false.
2. So the left side is false exactly when $p \lor q$ is true and $r$ is false.
   By the definition of [[disjunction|0F72FK8EKB]], $p \lor q$ is true when at least one of $p$, $q$ is true.
3. Write each row as three letters for $p$, $q$ and $r$.
   The left side is false exactly in the rows TTF, TFF and FTF.
4. By the definition of [[conjunction|025YZN3VJW]], the right side is false exactly when $p \to r$ is false or $q \to r$ is false.
5. The part $p \to r$ is false in the rows TTF and TFF, and the part $q \to r$ is false in the rows TTF and FTF.
6. So the right side is false exactly in the rows TTF, TFF and FTF, the same rows as in step 3.

The full [[truth table|05RSK4Q657]] confirms steps 3 and 6.

| $p$ | $q$ | $r$ | $p \lor q$ | $(p \lor q) \to r$ | $p \to r$ | $q \to r$ | $(p \to r) \land (q \to r)$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T |
| T | T | F | T | F | F | F | F |
| T | F | T | T | T | T | T | T |
| T | F | F | T | F | F | T | F |
| F | T | T | T | T | T | T | T |
| F | T | F | T | F | T | F | F |
| F | F | T | F | T | T | T | T |
| F | F | F | F | T | T | T | T |

The fifth and the eighth columns agree in all eight rows, so the two formulas are equivalent.

## Remarks

The equivalence is the logical form of [[proof by cases|0WCP0PVET6]].
To prove that $r$ follows from "$p$ or $q$", you prove that $r$ follows from $p$ and that $r$ follows from $q$.
With $n$ cases it reads $(p_1 \lor \cdots \lor p_n) \to r \equiv (p_1 \to r) \land \cdots \land (p_n \to r)$, by induction on $n$.

Change the "or" in the hypothesis to "and" and the equivalence fails.
[[The formulas $(p \land q) \to r$ and $(p \to r) \land (q \to r)$ are not equivalent|WAPV0FBEAE]], and they differ in the row TFF.
The correct form for a conjunctive hypothesis is $(p \land q) \to r \equiv (p \to r) \lor (q \to r)$: both sides are false only in the row TTF.

## Explanations

### L1 human

"If it rains or it snows, the match is canceled" makes two promises at once.
It says "if it rains, the match is canceled", and it says "if it snows, the match is canceled".
The big promise is broken exactly when it rains or snows and the match goes on.
That is exactly when one of the two small promises is broken, so the one sentence and the pair say the same thing.

### L2 human

We prove that $n^2 + n$ is even for every integer $n$, with the equivalence as the plan.

1. Let $p$ be "$n$ is even", $q$ be "$n$ is odd", and $r$ be "$n^2 + n$ is even".
   Each integer is even or odd, so $p \lor q$ is true.
2. By the equivalence, to prove $(p \lor q) \to r$ it is enough to prove $p \to r$ and $q \to r$.
3. Proof of $p \to r$: if $n = 2k$, then $n^2 + n = 2k(2k + 1)$, which is even.
4. Proof of $q \to r$: if $n = 2k + 1$, then $n^2 + n = (2k + 1)(2k + 2) = 2(2k + 1)(k + 1)$, which is even.
5. By steps 2 to 4, $(p \lor q) \to r$ holds, and with step 1, $r$ holds.

Every proof by cases has this shape: cases that together cover all possibilities, and one implication for each case.
Watch out for a forgotten case: a proof of $p \to r$ alone does not prove $(p \lor q) \to r$.
