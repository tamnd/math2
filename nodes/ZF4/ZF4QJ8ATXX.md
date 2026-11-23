---
tag: ZF4QJ8ATXX
kind: example
name: A proof with "fix" and "we claim" that 3 divides n^3 - n
msc: ["00A35", "11A05"]
topics: [STSM6PR7TX]
audience: ug1
instance_of: [GKMRQCA8CW]
uses: [GKMRQCA8CW, 0PG2H7WKGG, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Methods of proof
---

## Example

The statement is that for every integer $n$, the number $3$ divides $n^3 - n$.
For $n = 5$ this says that $3$ divides $120$, which is true, since $120 = 3 \cdot 40$.
The proof below has a small claim with its own proof inside the main proof, and the [[proof words|GKMRQCA8CW]] mark where the inner part begins and ends.

> (1) Fix an integer $n$.
> (2) We claim that one of the three integers $n - 1$, $n$ and $n + 1$ is divisible by $3$.
> (3) To prove the claim, write $n = 3q + r$ with integers $q$ and $r$ and $r \in \{0, 1, 2\}$, by division with remainder.
> (4) There are three cases.
> (5) If $r = 0$, then $n = 3q$, so $3 \mid n$.
> (6) If $r = 1$, then $n - 1 = 3q$, so $3 \mid n - 1$.
> (7) If $r = 2$, then $n + 1 = 3q + 3 = 3(q + 1)$, so $3 \mid n + 1$.
> (8) The three cases cover every value of $r$, and this proves the claim.
> (9) Next, $n^3 - n = n(n^2 - 1) = (n - 1)\,n\,(n + 1)$.
> (10) By the claim, $3$ divides one of the three factors, so $3$ divides their product.
> (11) Since $n$ was arbitrary, $3 \mid n^3 - n$ for every integer $n$.
> $\square$

"Fix" in line (1) brings in one arbitrary integer that stays the same until line (10), and line (11) uses that it was arbitrary to reach the "for every" of the statement.
"We claim" in line (2) announces a statement that is not yet proved, so the reader knows that an inner proof follows.
"There are three cases" in line (4) is a signpost, and it lets the reader check that no case is missing.
"This proves the claim" in line (8) closes the inner proof.
Without it, a reader could think that line (9) still belongs to the case $r = 2$.
"Next" in line (9) returns to the main line, and "by the claim" in line (10) names the source of the step.

## Remarks

The proof has two levels, and the words "we claim" and "this proves the claim" are the brackets around the inner one.
A [[structured proof|H2W8D7BMSW]] would show the same two levels with numbers and indentation instead of words.

Line (10) uses the fact that $3 \mid a$ implies $3 \mid ab$ for every integer $b$, which follows from the definition of [[divisibility|0PG2H7WKGG]]: if $a = 3s$, then $ab = 3(sb)$.

The claim is a special case of a general fact: among $m$ consecutive integers, one is divisible by $m$.
The same [[proof by cases|0WCP0PVET6]] on the remainder modulo $m$ proves it.
With $m = 2$ the argument shows that $2 \mid n^2 - n = (n - 1)n$.

## Explanations

### L1 human

The statement says that $n^3 - n$ is always a multiple of $3$.
For $n = 5$ we get $125 - 5 = 120 = 3 \cdot 40$.
The proof first proves a smaller fact: among three whole numbers in a row, such as $4$, $5$ and $6$, one is a multiple of $3$.
The words "we claim" tell the reader that this smaller fact comes first, and "this proves the claim" tells the reader that it is done.
Then the main proof uses it, because $n^3 - n$ is the product of three numbers in a row.

### L2 human

We follow the proof for a negative number, $n = -4$, to see that each line still works.
Division with remainder gives $-4 = 3 \cdot (-2) + 2$, so $q = -2$ and $r = 2$.
The case $r = 2$ gives $n + 1 = -3 = 3 \cdot (-1)$, so $3$ divides the factor $n + 1$.
Then $n^3 - n = -64 + 4 = -60$, and the factorization gives $(-5)(-4)(-3) = -60$ as well.
Since $3 \mid -3$, we get $3 \mid -60$, and indeed $-60 = 3 \cdot (-20)$.

"We claim" suits a lemma that is too small or too special to get its own number.
Watch out: a claim that is never closed leaves the reader unsure which lines depend on the case conditions.
Close every claim with a sentence such as "this proves the claim", and only then return to the main proof.
