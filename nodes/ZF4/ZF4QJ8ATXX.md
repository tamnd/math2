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

*Statement.* For every integer $n$, the number $3$ divides $n^3 - n$.

*Proof.*

1. Fix an integer $n$.
2. We claim that one of the three integers $n - 1$, $n$, $n + 1$ is divisible by $3$.
3. Proof of the claim: by division with remainder, $n = 3q + r$ for integers $q$ and $r$ with $r \in \{0, 1, 2\}$. There are three cases.
4. Case $r = 0$: then $n = 3q$, so $3 \mid n$.
5. Case $r = 1$: then $n - 1 = 3q$, so $3 \mid n - 1$.
6. Case $r = 2$: then $n + 1 = 3q + 3 = 3(q + 1)$, so $3 \mid n + 1$.
7. The three cases cover all values of $r$, and this proves the claim.
8. Next, $n^3 - n = n(n^2 - 1) = (n - 1)\,n\,(n + 1)$.
9. By the claim, $3$ divides one of the three factors, so $3$ divides their product.
10. Since $n$ was an arbitrary integer, $3 \mid n^3 - n$ for every integer $n$. $\square$

We check the role of each proof word.

1. "Fix" introduces one arbitrary integer $n$, which stays the same in lines 2 to 9. Line 10 uses that $n$ was arbitrary to conclude the "for every" of the statement.
2. "We claim" announces a statement that is not yet proved. The reader knows that lines 3 to 7 prove it, and that the main proof continues after line 7.
3. "There are three cases" is a signpost. It tells the reader how many cases to expect, so the reader can check that none is missing.
4. Each "Case" line starts with its condition and ends with a conclusion of the form $3 \mid (\ldots)$. The three conclusions differ, but each gives the claim.
5. "This proves the claim" closes the claim. Without it, a reader could think that line 8 belongs to case $r = 2$.
6. "Next" in line 8 is a signpost that returns to the main line of the proof.
7. "By the claim" in line 9 names the source of the step. So the reader looks back to line 2 and not to an earlier result.

## Remarks

1. The example shows two levels in one proof: a claim with its own proof, inside the main proof. The words "we claim" and "this proves the claim" mark the borders of the inner level.
2. The step "3 divides one factor, so 3 divides the product" uses that $3 \mid a$ implies $3 \mid ab$ for each integer $b$. This follows from the definition of [[divisibility|0PG2H7WKGG]].
3. The same proof with $2$ in place of $3$ shows that $2 \mid n^2 - n = (n - 1)n$, with two cases for the remainder.
4. The claim is a case of a more general fact: among $m$ consecutive integers, one is divisible by $m$. The same [[proof by cases|0WCP0PVET6]] on the remainder modulo $m$ proves it.

## Explanations

### L1 human

The statement says that $n^3 - n$ is always a multiple of $3$.
For $n = 5$ we get $125 - 5 = 120 = 3 \cdot 40$.
The proof first makes a smaller claim: among three numbers in a row, such as $4$, $5$, $6$, one is a multiple of $3$.
The words "we claim" tell the reader that this smaller claim comes first, and "this proves the claim" tells the reader that it is done.
Then the main proof uses it, because $n^3 - n$ is the product of three numbers in a row.

### L2 human

We follow the proof for $n = 5$ and for $n = -4$.

1. For $n = 5$: $5 = 3 \cdot 1 + 2$, so $q = 1$ and $r = 2$. Case $r = 2$ gives $n + 1 = 6 = 3 \cdot 2$.
2. Then $n^3 - n = 4 \cdot 5 \cdot 6 = 120$, and $3 \mid 6$ gives $3 \mid 120$.
3. For $n = -4$: $-4 = 3 \cdot (-2) + 2$, so $q = -2$ and $r = 2$. Case $r = 2$ gives $n + 1 = -3 = 3 \cdot (-1)$.
4. Then $n^3 - n = -64 + 4 = -60 = (-5)(-4)(-3)$, and $3 \mid -3$ gives $3 \mid -60$.

The typical use of "we claim" is to state a lemma inside a proof.
It suits a lemma that is too small or too special for its own number.
A trap is to forget to close the claim.
If the proof does not say where the proof of the claim ends, the reader cannot tell which lines depend on the case conditions.
