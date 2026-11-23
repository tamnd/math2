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

The statement is that for every integer $n$, the square $n^2$ leaves remainder $0$ or $1$ on division by $4$.
In the notation of [[congruences|0WAY5WX8NY]], $n^2 \equiv 0$ or $n^2 \equiv 1 \pmod 4$.
The proof in the text has four lines.

> (L1) Let $n$ be an integer.
> (L2) If $n$ is even, then $n = 2k$, and $n^2 = 4k^2$.
> (L3) If $n$ is odd, then $n = 2k + 1$, and $n^2 = 4(k^2 + k) + 1$.
> (L4) So $n^2$ leaves remainder $0$ or $1$ on division by $4$.

A self-explanation explains each line through the definitions and the earlier lines, as the method of [[reading proofs|40GCSM2G56]] asks.

Line (L1) fixes an arbitrary integer, so whatever the proof shows about this $n$ holds for all integers.
Before (L2), the reader asks why there are two cases, and answers that every integer is even or odd, so this is a [[proof by cases|0WCP0PVET6]] that covers everything.
In (L2), "even" means $n = 2k$ for an integer $k$, so $n^2 = 4k^2$ with $k^2$ an integer, and the remainder is $0$.
In (L3), "odd" means $n = 2k + 1$, so $n^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1$ with $k^2 + k$ an integer.
The remainder is then $1$, because the remainder on division by $4$ is the unique $r$ with $0 \le r < 4$ and $n^2 = 4q + r$, and $r = 1$ fits.
Line (L4) collects the two cases, which cover all integers, for the arbitrary $n$ of (L1).

Tests: $n = 6$ gives $k = 3$ and $36 = 4 \cdot 9$, remainder $0$.
For $n = 7$, $k = 3$, $k^2 + k = 12$ and $49 = 4 \cdot 12 + 1$, remainder $1$.
A negative number needs no change: $n = -3$ is odd with $k = -2$, so $k^2 + k = 2$ and $9 = 4 \cdot 2 + 1$.

## Remarks

A paraphrase of (L3), such as "for odd $n$ the square is four times something plus one", repeats the line.
The self-explanation says why: the definition of odd, the expansion, and the uniqueness of the remainder.
That last point fills a gap in the text, which shows only the equation, and the uniqueness part of [[division with remainder|0CHQKZFK5S]] turns the equation into a claim about the remainder.

Looking back gives a consequence.
A sum of two squares leaves remainder $0 + 0$, $0 + 1$ or $1 + 1$, that is $0$, $1$ or $2$, on division by $4$.
So no integer that leaves remainder $3$, such as $3$, $7$ or $11$, is a sum of two squares.

The same reading shows more modulo $8$.
An odd square is $4k(k + 1) + 1$, and one of $k$ and $k + 1$ is even, so an odd square leaves remainder $1$ on division by $8$.

## Explanations

### L1 human

The claim is that a square number, divided by $4$, leaves $0$ or $1$ and never $2$ or $3$.
For example, $36$ divided by $4$ is $9$ with nothing left, and $49$ divided by $4$ is $12$ with $1$ left.
The proof looks at even numbers and odd numbers separately.
A good reader asks why there are two cases, why the square of $2k$ is $4k^2$, and why the remainder is $1$ in the odd case.
After that, the reader can rebuild the proof without the book.

### L2 human

Self-explanation follows a fixed pattern: for each line, name the source of each new fact.
A new object, such as $k$, comes from a definition like "even" or "odd".
A new equation, such as $n^2 = 4k^2 + 4k + 1$, comes from algebra on an earlier equation.
A claim about remainders comes from the definition of the remainder and its uniqueness.
A case split comes from a fact that covers all cases, here that every integer is even or odd.

A student studying a proof from a lecture can write one sentence of this kind under each line.
Watch out: explaining only the algebra and skipping the case split leaves unchecked whether the two cases cover all integers.
