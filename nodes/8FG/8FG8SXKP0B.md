---
tag: 8FG8SXKP0B
kind: example
name: Self-explanation of a proof that a square is 0 or 1 modulo 4
msc: ["00A35", "97E50", "11A07"]
topics: [STSM6PR7TX]
audience: ug1
instance_of: [40GCSM2G56]
uses: [40GCSM2G56, 0WCP0PVET6, 0WAY5WX8NY]
sources:
  - doi: 10.5951/jresematheduc.45.1.0062
    locator: pages 62-101
  - url: https://en.wikipedia.org/wiki/Square_number
    locator: lead section
---

## Example

The statement is: for every integer $n$, the square $n^2$ leaves the remainder $0$ or $1$ on division by $4$.
In the notation of [[congruences|0WAY5WX8NY]], $n^2 \equiv 0$ or $n^2 \equiv 1 \pmod 4$.
The proof in the text has four lines.

> (L1) Let $n$ be an integer.
> (L2) If $n$ is even, then $n = 2k$, and $n^2 = 4k^2$.
> (L3) If $n$ is odd, then $n = 2k + 1$, and $n^2 = 4(k^2 + k) + 1$.
> (L4) So $n^2$ leaves the remainder $0$ or $1$ on division by $4$.

A self-explanation explains each line in terms of the definitions and of the earlier lines, as the method of [[reading proofs|40GCSM2G56]] asks.

1. (L1) The statement is about every integer, so the proof fixes an arbitrary integer $n$. Whatever the proof shows about this $n$ holds for all integers.
2. Before (L2) the reader asks why the proof splits into two cases. Every integer is even or odd, so the two cases cover all integers, and the proof is a [[proof by cases|0WCP0PVET6]].
3. (L2) "Even" means $n = 2k$ for an integer $k$. Squaring gives $n^2 = (2k)^2 = 4k^2$, and $k^2$ is an integer, so the remainder on division by $4$ is $0$.
4. (L3) "Odd" means $n = 2k + 1$ for an integer $k$. Squaring gives $n^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1$, and $k^2 + k$ is an integer.
5. (L3), continued. The remainder is $1$, because $0 \le 1 < 4$, and the remainder on division by $4$ is the unique such number $r$ with $n^2 = 4q + r$.
6. (L4) The two cases give the remainders $0$ and $1$, and the cases cover all integers by item 2. So the conclusion holds for the arbitrary $n$ of (L1).
7. A test of the even case: $n = 6$ gives $k = 3$ and $36 = 4 \cdot 9$, with remainder $0$.
8. A test of the odd case: $n = 7$ gives $k = 3$, $k^2 + k = 12$, and $49 = 4 \cdot 12 + 1$, with remainder $1$.
9. A test of a negative number: $n = -3$ is odd with $k = -2$, so $k^2 + k = 2$ and $9 = 4 \cdot 2 + 1$. The proof needs no change for negative $n$.

## Remarks

1. Compare a paraphrase of (L3) with its self-explanation. The paraphrase "for odd $n$ the square is four times something plus one" repeats the line. The self-explanation of items 4 and 5 says why: the definition of odd, the expansion, and the uniqueness of the remainder.
2. Item 5 fills a gap of the text: the line (L3) shows $n^2 = 4(k^2 + k) + 1$. The uniqueness of the remainder in the [[division algorithm|0CHQKZFK5S]] turns this into the claim about the remainder.
3. The result has a consequence that the reader can find by looking back. A sum of two squares has the remainder $0 + 0$, $0 + 1$ or $1 + 1$, that is $0$, $1$ or $2$, on division by $4$. So no integer with the remainder $3$, such as $3$, $7$ or $11$, is a sum of two squares.
4. Change the modulus from $4$ to $8$. The same method shows that an odd square leaves the remainder $1$, because $4k(k + 1)$ is divisible by $8$. The reader who explained (L3) can see this, since one of $k$ and $k + 1$ is even.

## Explanations

### L1 human

The claim is that a square number, divided by $4$, leaves $0$ or $1$ and never $2$ or $3$.
For example, $36$ divided by $4$ is $9$ with nothing left, and $49$ divided by $4$ is $12$ with $1$ left.
The proof looks at even numbers and odd numbers separately.
Good readers explain each line to themselves.
Why two cases, why is the square of $2k$ equal to $4k^2$, why is the remainder $1$ in the odd case?
After this, the reader can rebuild the proof without the book.

### L2 human

The self-explanation has a fixed pattern: for each line, name the source of each new fact.

1. A new object, such as $k$, comes from a definition: "even" or "odd".
2. A new equation, such as $n^2 = 4k^2 + 4k + 1$, comes from algebra on an earlier equation.
3. A new claim about remainders comes from the definition of the remainder and its uniqueness.
4. A case split comes from a fact that covers all cases: every integer is even or odd.

The typical use is the study of a proof from a lecture: the student writes one sentence of explanation under each line of the proof.
A trap is to explain only the algebra and to skip item 2 of the example.
Without it, the reader has not checked that the two cases cover all integers.
