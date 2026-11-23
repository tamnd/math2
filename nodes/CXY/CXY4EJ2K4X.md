---
tag: CXY4EJ2K4X
kind: example
name: For every integer n, n^2 + n is even
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0GHS47PDAQ]
uses: [0GHS47PDAQ, 0B88PQTJ66, CX38X989TB, 0WCP0PVET6, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.3
---

## Example

Let $P(n)$ be the predicate "$n^2 + n$ is even".
We check the [[universal statement|0B88PQTJ66]] $\forall n \, P(n)$ first on the finite domain $D = \{1, 2, 3, 4, 5\}$, and then on the set $\mathbb{Z}$ of all [[integers|0C4JS9RF5M]].

On the finite domain the statement is the conjunction $P(1) \land P(2) \land P(3) \land P(4) \land P(5)$, and we check each conjunct.

1. $1^2 + 1 = 2 = 2 \cdot 1$, so $P(1)$ is true.
2. $2^2 + 2 = 6 = 2 \cdot 3$, so $P(2)$ is true.
3. $3^2 + 3 = 12 = 2 \cdot 6$, so $P(3)$ is true.
4. $4^2 + 4 = 20 = 2 \cdot 10$, so $P(4)$ is true.
5. $5^2 + 5 = 30 = 2 \cdot 15$, so $P(5)$ is true.
6. All five conjuncts are true, so $\forall n \in D \; P(n)$ is true.

On $\mathbb{Z}$ a check of cases never ends, so we [[prove the universal statement|CX38X989TB]] for an arbitrary element.

7. Let $n$ be an arbitrary integer, and factor $n^2 + n = n(n + 1)$.
8. We use [[proof by cases|0WCP0PVET6]] on the parity of $n$.
   If $n = 2k$ for an integer $k$, then $n(n + 1) = 2 \cdot k(n + 1)$, which is even.
9. If $n = 2k + 1$, then $n + 1 = 2(k + 1)$, and $n(n + 1) = 2 \cdot n(k + 1)$, which is even.
10. Every integer is even or odd, so steps 8 and 9 cover every case, and $P(n)$ is true.
11. Since $n$ was arbitrary, $\forall n \in \mathbb{Z} \; P(n)$ is true.

## Remarks

A universal statement can be established in two ways: by checking every element, which works only on a finite domain, or by a proof for an arbitrary element, which works on any domain.
Steps 1 to 6 are not a proof of the statement on $\mathbb{Z}$; they only test it.

Change the predicate and the result changes.
For "$n^2 + 1$ is even", the instance $n = 2$ gives $5$, which is odd, so $\forall n \in \mathbb{Z} \, (n^2 + 1 \text{ is even})$ is false, with the counterexample $2$.

## Explanations

### L1 human

Take a whole number, square it, and add the number itself.
For $1$ to $5$ you get $2$, $6$, $12$, $20$ and $30$, all even.
To be sure for every whole number, note that $n^2 + n = n \times (n + 1)$ is a product of two neighbors.
Of two neighboring whole numbers, one is always even, so the product is even.

### L2 human

Prove $\forall n \in \mathbb{Z} \; (3 \mid n^3 - n)$ in the same way.
Let $n$ be an arbitrary integer and factor:
$$n^3 - n = (n - 1) \, n \, (n + 1),$$
a product of three consecutive integers.
The remainder of $n$ on division by $3$ is $0$, $1$ or $2$, and in these three cases $3$ divides $n$, $n - 1$ or $n + 1$, respectively.
So $3$ divides the product in every case, and since $n$ was arbitrary, the statement holds for all integers.
A factorization followed by a short case analysis that covers every element is the usual shape of such proofs.
Watch out: testing $n = 1, 2, 3$ and stopping is a check, not a proof.
