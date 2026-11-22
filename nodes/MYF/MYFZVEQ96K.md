---
tag: MYFZVEQ96K
kind: example
name: A numerical check is not a verification
msc: ["00A35", "97E50"]
topics: [N4P3E53HM0]
audience: school
not_instance_of:
  - target: ENY0GKRJS8
    note: a check of the cases n = 1 to 100 is not a proof, so it neither verifies the statement for all n nor explains it; it only gives confidence
uses: [ENY0GKRJS8, 01QZNHQWYD, D6G69GNKPC, 4Y4HWKA2MP]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
---

## Example

Take the statement that $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ for each integer $n \geq 1$.
A computer adds the numbers $1$ to $n$ for each $n$ from $1$ to $100$ and compares each sum with $\frac{n(n + 1)}{2}$.
We check what this computation shows and what it does not.

1. The computation compares $100$ pairs of numbers, and all $100$ pairs agree.
   For example, for $n = 100$ both numbers are $5050$.
2. So the statement is true for $n = 1, 2, \ldots, 100$.
   This part is certain, provided the program is correct.
3. The statement is about every positive integer, and there are infinitely many.
   The computation says nothing about $n = 101$ or about $n = 10^{9}$.
4. So the computation does not verify the statement.
   Verification, the first [[function of proof|ENY0GKRJS8]], needs an argument that covers every $n$.
5. The computation does not explain the formula either.
   It confirms the numbers, but it does not show where the factor $\frac{n + 1}{2}$ comes from.

The [[two proofs of the formula|D6G69GNKPC]] cover every $n$ at once, and the pairing proof also explains it.

## Remarks

The example separates confidence from verification.
After the check a reader can be very confident, and here the statement is in fact true, as the [[sum formula|01QZNHQWYD]] shows.
For other statements the same kind of evidence has failed.
The [[Mertens conjecture|4Y4HWKA2MP]] held for every value that was computed, and it is false.

A computation can be part of a proof when it covers all the cases.
A statement about $n$ modulo $6$ has only six cases, and a computer check of all six is a complete proof.
So the difference is not whether a computer is used.
It is whether the checked cases are all the cases.

## Explanations

### L1 human

Checking a rule for the first hundred numbers is like testing a bridge with a hundred cars.
It shows that the bridge held those cars.
It does not show that the bridge holds every car, and it does not show why the bridge is strong.
A proof is like a calculation of the strength of the bridge, which covers all cars at once.

### L2 human

Here is how far such checks can mislead, with the polynomial $n^2 - n + 41$.
The first values are prime:
$$n = 1: \ 41, \qquad n = 2: \ 43, \qquad n = 3: \ 47.$$
A computer check shows that the value is prime for every $n$ from $1$ to $40$.
At $n = 41$ every term is a multiple of $41$:
$$41^2 - 41 + 41 = 41^2 = 1681.$$
So forty confirming cases did not verify the statement "$n^2 - n + 41$ is prime for each $n \geq 1$".
A numerical check is the right tool for testing a conjecture before you try to prove it, and for finding a counterexample.
Watch out: a larger search does not turn a check into a proof.
Only a search over all cases, or an argument that reduces the problem to finitely many cases, is a proof.
