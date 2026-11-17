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

We prove: for every integer $n$, the remainder of $n^2$ on division by $4$ is $0$ or $1$.
The proof uses a [[disjunction|0F72FK8EKB]] twice: a known disjunction gives the cases, and the conclusion is a disjunction.

1. Every integer $n$ is even or odd: $n = 2k$ or $n = 2k + 1$ for an integer $k$. This is the disjunction that we use.
2. Case $n = 2k$. Then $n^2 = 4k^2$, so the remainder is $0$.
3. From "the remainder is $0$", disjunction introduction (left) gives "the remainder is $0$ or $1$".
4. Case $n = 2k + 1$. Then $n^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1$, so the remainder is $1$.
5. From "the remainder is $1$", disjunction introduction (right) gives "the remainder is $0$ or $1$".
6. The conclusion holds in both cases of step 1. By [[disjunction elimination|FTH70E7K1D]], it holds for every integer $n$.

## Remarks

The example shows both rules of disjunction: elimination in step 6, which is [[proof by cases|0WCP0PVET6]], and introduction in steps 3 and 5.
In Lean's Mathlib the same structure is `Or.elim h case1 case2`, where `h` proves "$n$ even or $n$ odd", and `case1` and `case2` end with `Or.inl` and `Or.inr`.

The disjunction in the conclusion is never true in both parts, because a number has one remainder.
So here the inclusive and the exclusive readings agree.

A consequence: a sum of two squares $a^2 + b^2$ has remainder $0 + 0$, $0 + 1$ or $1 + 1$, that is $0$, $1$ or $2$, on division by $4$.
So no integer with remainder $3$, such as $7$, $11$ or $15$, is a sum of two squares.

If we divide by $3$ instead of $4$, the same method with the three cases $n = 3k$, $3k + 1$, $3k + 2$ shows that $n^2$ has remainder $0$ or $1$ on division by $3$.

## Explanations

### L1 human

Square some whole numbers and divide by $4$.
$3^2 = 9 = 2 \times 4 + 1$ leaves $1$.
$6^2 = 36 = 9 \times 4$ leaves $0$.
Even numbers always leave $0$ and odd numbers always leave $1$.
Since every whole number is even or odd, the remainder is always $0$ or $1$, never $2$ or $3$.

### L2 human

We use the result to show that $n^2 + 2$ is never divisible by $4$.

1. By the example, $n^2$ has remainder $0$ or $1$ on division by $4$.
2. Case remainder $0$: $n^2 + 2$ has remainder $2$.
3. Case remainder $1$: $n^2 + 2$ has remainder $3$.
4. In both cases the remainder is not $0$, so $4$ does not divide $n^2 + 2$.

The typical use of a proved disjunction is to start a new proof by cases, as in this step 1.

A trap: the cases of step 1 of the example come from a true disjunction, "$n$ even or $n$ odd".
A split into cases that do not cover every integer, such as "$n$ divisible by $4$ or $n$ odd", proves nothing about $n = 2$.
