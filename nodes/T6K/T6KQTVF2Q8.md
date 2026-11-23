---
tag: T6KQTVF2Q8
kind: example
name: "Proof by cases: n^2 leaves remainder 0 or 1 on division by 4"
msc: ["03B05", "11A07"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0F72FK8EKB]
uses: [0F72FK8EKB, 0WCP0PVET6, FTH70E7K1D]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunction_elimination
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_by_exhaustion
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.5
---

## Example

Square a few integers and divide by $4$: $3^2 = 9 = 2 \cdot 4 + 1$ leaves $1$, and $6^2 = 36 = 9 \cdot 4$ leaves $0$.
We prove that for every integer $n$, the remainder of $n^2$ on division by $4$ is $0$ or $1$.
The proof uses a [[disjunction|0F72FK8EKB]] twice: a known disjunction gives the cases, and the conclusion is a disjunction.

1. Every integer $n$ is even or odd, so $n = 2k$ or $n = 2k + 1$ for an integer $k$.
   This is the disjunction that we use.
2. In the case $n = 2k$, we get $n^2 = 4k^2$, so the remainder is $0$.
   Disjunction introduction (left) gives "the remainder is $0$ or $1$".
3. In the case $n = 2k + 1$, we get
   $$n^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1,$$
   so the remainder is $1$.
   Disjunction introduction (right) gives "the remainder is $0$ or $1$".
4. The conclusion holds in both cases of step 1, so [[disjunction elimination|FTH70E7K1D]] gives it for every integer $n$.

## Remarks

Both rules of disjunction appear: elimination in step 4, which is [[proof by cases|0WCP0PVET6]], and introduction in steps 2 and 3.
In Lean's Mathlib the same structure is `Or.elim h case1 case2`, where `h` proves "$n$ even or $n$ odd", and the two cases end with `Or.inl` and `Or.inr`.
The disjunction in the conclusion never has both parts true, because a number has one remainder, so the inclusive and exclusive readings agree here.

The result has a quick consequence.
A sum of two squares $a^2 + b^2$ leaves $0 + 0$, $0 + 1$ or $1 + 1$, that is $0$, $1$ or $2$, on division by $4$.
So no integer with remainder $3$, such as $7$, $11$ or $15$, is a sum of two squares.
With $3$ in place of $4$, the three cases $n = 3k$, $3k + 1$, $3k + 2$ show that $n^2$ leaves $0$ or $1$ on division by $3$.

## Explanations

### L1 human

Square some whole numbers and divide by $4$.
Even numbers always leave $0$, and odd numbers always leave $1$.
Since every whole number is even or odd, the remainder is always $0$ or $1$, never $2$ or $3$.

### L2 human

Use the result to show that $n^2 + 2$ is never divisible by $4$.
By the example, $n^2$ leaves $0$ or $1$ on division by $4$, and we use this disjunction by cases.
If $n^2$ leaves $0$, then $n^2 + 2$ leaves $2$.
If $n^2$ leaves $1$, then $n^2 + 2$ leaves $3$.
In both cases the remainder is not $0$, so $4 \nmid n^2 + 2$.
A disjunction once proved becomes the start of new proofs by cases, as here.
Watch out: the cases must come from a true disjunction.
A split into "$n$ divisible by $4$ or $n$ odd" misses $n = 2$, so it proves nothing about $n = 2$.
