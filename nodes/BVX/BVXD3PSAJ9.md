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
We prove it by naming a witness and checking it, and then we find all witnesses.

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $n^2$ | 1 | 4 | 9 | 16 | 25 |
| $2^n$ | 2 | 4 | 8 | 16 | 32 |

1. By the restricted form, the statement is $\exists n \, (n \in \mathbb{Z} \land n > 0 \land n^2 = 2^n)$.
2. For $n = 2$, the conjuncts $2 \in \mathbb{Z}$, $2 > 0$ and $2^2 = 4 = 2^2$ are all true.
3. So $n = 2$ is a witness, and the statement is true by [[existential generalization|33ZNXRFVJJ]].
4. The proof names its witness, so it is a [[constructive proof|01XM7JEKHY]].
5. The table shows that $n = 4$ is a second witness, since $4^2 = 16 = 2^4$, and that $n = 1$ and $n = 3$ are not witnesses.
6. For $n \ge 5$, the induction in [[the universal statement that $n^2 \le 2^n$ for every natural number $n$ is false|ZHVZGEWE9J]] adapts to give $n^2 < 2^n$, so there are no further witnesses.

## Remarks

One checked witness proves an existential statement, and the other elements of the domain need not be examined.
Steps 5 and 6 are not part of the proof; they find all witnesses.
Since $2$ and $4$ are both witnesses, the statement with the [[uniqueness quantifier|0QAJHFGZZJ]], $\exists! n \in \mathbb{Z} \; (n > 0 \land n^2 = 2^n)$, is false, while the existential statement is true.

The domain matters.
Over the positive odd integers there is no witness, because $n^2$ is odd and $2^n$ is even for each odd $n \ge 1$.

## Explanations

### L1 human

The claim is that some positive whole number has its square equal to $2$ raised to that number.
For $2$, the square is $4$ and $2^2$ is $4$, so the claim is true.
One such number is enough to make the claim true.
The number $4$ also works, since $4^2 = 16 = 2^4$.

### L2 human

Prove $\exists n \in \mathbb{N} \; (n^2 + n + 41 \text{ is not prime})$.
For $n = 0, 1, 2, \dots, 39$, the value $n^2 + n + 41$ is prime, so none of these is a witness.
For $n = 40$, the value is $1600 + 40 + 41 = 1681 = 41^2$, which is not prime.
So $n = 40$ is a witness, and the statement is true.
The witness also refutes the universal statement "for every $n$, $n^2 + n + 41$ is prime", which is the typical use of such a search.
Watch out: a search that stops at $n = 10$ finds only primes, and concluding from it that no witness exists is wrong.
