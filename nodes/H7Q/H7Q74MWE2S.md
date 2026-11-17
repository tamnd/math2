---
tag: H7Q74MWE2S
kind: example
name: A finite check of Goldbach from 4 to 100
msc: ["11P32", "00A35"]
topics: [DME0TPC348]
audience: ug1
not_instance_of:
  - target: JFD3QWCX8Z
    note: the check covers every case of a finite statement, so it is a proof of that statement and not evidence for unchecked cases
uses: [JFD3QWCX8Z, 063JNBSMJ0, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
    locator: Computational results
  - url: https://en.wikipedia.org/wiki/Proof_by_exhaustion
    locator: lead section
---

## Example

The statement $G_{100}$: "every even $n$ with $4 \leq n \leq 100$ is a sum of two primes".
We prove $G_{100}$ by checking all its cases, and we compare the check with [[numerical evidence|JFD3QWCX8Z]].

1. The cases. There are $49$ even numbers from $4$ to $100$.
2. The check. For each $n$ we list the least prime $p$ with $n - p$ prime.
   - $p = 2$: $n = 4$.
   - $p = 3$: $n = 6, 8, 10, 14, 16, 20, 22, 26, 32, 34, 40, 44, 46, 50, 56, 62, 64, 70, 74, 76, 82, 86, 92, 100$.
   - $p = 5$: $n = 12, 18, 24, 28, 36, 42, 48, 52, 58, 66, 72, 78, 84, 88, 94$.
   - $p = 7$: $n = 30, 38, 54, 60, 68, 80, 90, 96$.
   - $p = 19$: $n = 98$, with $98 = 19 + 79$.
3. The count. The lists of step 2 contain $1 + 24 + 15 + 8 + 1 = 49$ numbers, so every case is covered.
4. The conclusion. $G_{100}$ is proved. The proof is a [[proof|0B94TKFQJX]] by exhaustion, and it is complete.

The check is not numerical evidence in the sense of the concept.
Numerical evidence supports a statement about cases that were not checked, and here no case is left unchecked.

## Remarks

The same $49$ checks are also numerical evidence for the full [[Goldbach's conjecture|063JNBSMJ0]].
So the role of a computation depends on the statement it is attached to: a proof of $G_{100}$, and only evidence for the conjecture.
The case $n = 98$ is the only one up to $100$ that needs a prime as large as $19$: $98 - 3 = 95$, $98 - 5 = 93$, $98 - 7 = 91 = 7 \cdot 13$, $98 - 11 = 87$, $98 - 13 = 85$ and $98 - 17 = 81$ are all composite.
The page [[Goldbach's conjecture for small even numbers|51WEX891JK]] does the same check for the even numbers up to $30$.

## Explanations

### L1 human

The claim is only about the even numbers from $4$ to $100$.
There are $49$ of them, and we can check each one, for example $30 = 7 + 23$ and $98 = 19 + 79$.
After all $49$ checks, the claim is proved.
Nothing is left to guess, so this is a proof and not just evidence.

### L2 human

We check the hardest case, $n = 98$.

1. $98 - 3 = 95 = 5 \cdot 19$.
2. $98 - 5 = 93 = 3 \cdot 31$.
3. $98 - 7 = 91 = 7 \cdot 13$.
4. $98 - 11 = 87 = 3 \cdot 29$, $98 - 13 = 85 = 5 \cdot 17$ and $98 - 17 = 81 = 3^4$.
5. $98 - 19 = 79$, and $79$ is prime.

The typical use: a statement about finitely many cases can be proved by a complete check, by hand or by computer.
A trap: the check must cover every case; a list that misses one even number proves nothing about it.
