---
tag: BVXD3PSAJ9
kind: example
name: There is a positive integer n with n^2 = 2^n
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0MSRQHCNN9]
uses: [0MSRQHCNN9, 0JW2FHW7G3, 01XM7JEKHY, 0QAJHFGZZJ, 33ZNXRFVJJ]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.3
---

## Example

Consider the [[existential statement|0JW2FHW7G3]] $\exists n \in \mathbb{Z} \; (n > 0 \land n^2 = 2^n)$, "there is a positive integer $n$ with $n^2 = 2^n$".
We prove it by naming a witness and checking it.

1. By the definition of the restricted form, the statement is $\exists n \, (n \in \mathbb{Z} \land n > 0 \land n^2 = 2^n)$.
2. Try $n = 1$: $1^2 = 1$ and $2^1 = 2$, so $n = 1$ is not a witness.
3. Try $n = 2$: $2 \in \mathbb{Z}$ and $2 > 0$, and $2^2 = 4 = 2^2$. All three conjuncts are true.
4. So $n = 2$ is a witness, and the statement is true by [[existential generalization|33ZNXRFVJJ]].
5. This proof names the witness, so it is a [[constructive proof|01XM7JEKHY]].

The witness is not unique.

6. For $n = 3$: $3^2 = 9$ and $2^3 = 8$, so $n = 3$ is not a witness.
7. For $n = 4$: $4^2 = 16 = 2^4$, so $n = 4$ is a second witness.
8. For $n \ge 5$, the induction on the page [[the universal statement that $n^2 \le 2^n$ for every natural number $n$ is false|ZHVZGEWE9J]] gives the strict inequality $n^2 < 2^n$, so there are no further witnesses.

## Remarks

The example shows that one checked witness proves an existential statement, and that the other elements of the domain do not need to be examined.
Steps 6 to 8 are not part of the proof; they find all witnesses.
Since $2$ and $4$ are both witnesses, the statement with the [[uniqueness quantifier|0QAJHFGZZJ]], $\exists! n \in \mathbb{Z} \; (n > 0 \land n^2 = 2^n)$, is false, while the existential statement is true.

The domain matters.
Over the positive odd integers, the statement has no witness: $n^2$ is odd and $2^n$ is even for each odd $n \ge 1$.

## Explanations

### L1 human

The claim is that some positive whole number has its square equal to the power of $2$ with the same exponent.
For $2$, the square is $4$ and $2^2$ is $4$, so the claim is true.
One such number is enough to make the claim true.
The number $4$ also works, since $16 = 16$.

### L2 human

We prove $\exists n \in \mathbb{N} \; (n^2 + n + 41 \text{ is not prime})$.

1. For $n = 0, 1, 2, \dots, 39$, the value $n^2 + n + 41$ is prime, so none of these is a witness.
2. Try $n = 40$: $40^2 + 40 + 41 = 1600 + 81 = 1681 = 41^2$.
3. So $1681$ is not prime, $n = 40$ is a witness, and the statement is true.

The typical use of a witness is in the refutation of a universal statement: here it refutes "for every $n$, $n^2 + n + 41$ is prime".
A trap is to stop after $n = 0$ to $10$, find only primes, and conclude that no witness exists.
