---
tag: VE6ACCC4F7
kind: example
name: A computer check of Goldbach's conjecture up to a bound is not a proof of the conjecture
msc: ["11P32", "00A35"]
topics: [1BTHSHST4M]
audience: research
not_instance_of:
  - target: MC18C7BMFT
    note: no proved reduction takes the infinitely many even numbers to the checked range, so the computation proves only a bounded statement
uses: [MC18C7BMFT, 063JNBSMJ0, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
    locator: Computational results
  - url: https://en.wikipedia.org/wiki/Computer-assisted_proof
    locator: lead section
---

## Example

[[Goldbach's conjecture|063JNBSMJ0]] says that each even integer $n > 2$ is the sum of two [[primes|01826KMG2H]].
Tomás Oliveira e Silva, Siegfried Herzog and Silvio Pardi checked it by computer for each even $n$ up to $4 \cdot 10^{18}$, and they published the result in 2014.
We check the conditions of a [[computer-assisted proof|MC18C7BMFT]] for this computation, and we find the condition that fails.

1. The computation. For each even $n$ with $4 \le n \le 4 \cdot 10^{18}$, the program finds a prime $p$ such that $n - p$ is also prime. For small $n$ we can repeat it by hand: $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, $10 = 3 + 7$ and $100 = 3 + 97$.
2. Each pair $(p, n - p)$ is a certificate: anyone can test the two numbers for primality and add them. So the computation proves the bounded statement "each even $n$ with $4 \le n \le 4 \cdot 10^{18}$ is a sum of two primes".
3. The conjecture is a statement about infinitely many even numbers. A computer-assisted proof of it would need a written argument that reduces all even numbers to a finite list of cases.
4. No such argument is known. No theorem says that a counterexample, if one exists, must be smaller than $4 \cdot 10^{18}$.
5. So the condition of a proved reduction fails. The computation is a computer-assisted proof of the bounded statement, and it is evidence for the conjecture, but it is not a proof of the conjecture.

## Remarks

The example separates two uses of a computer that look alike.
In the [[proof of the four colour theorem|17BMQS5PTG]], a written argument shows that the checked configurations cover every case, and so the check completes a proof.
In the Goldbach computation, no written argument connects the checked range to the remaining numbers, and so the check gives only evidence.
The weighing of such evidence is the subject of [[plausible reasoning and experimental mathematics|DME0TPC348]].

The situation changes if a theorem gives a bound.
Suppose that someone proved that each even $n > N$ is a sum of two primes, for some explicit $N$ with $N \le 4 \cdot 10^{18}$.
Then the computation would cover the remaining cases, and the two parts together would be a computer-assisted proof of the conjecture.
Harald Helfgott's proof of the weak Goldbach conjecture, on sums of three primes, announced in 2013, has this form: analytic estimates for large numbers and computer checks for small numbers.

## Explanations

### L1 human

Goldbach's conjecture says that every even number from $4$ on is the sum of two primes, for example $10 = 3 + 7$.
Computers have checked every even number up to four billion billions, and each one works.
This is a huge amount of checking, but it is not a proof.
The even numbers never end, and nobody has shown that a failure, if there is one, would have to be small.
So the checks make the conjecture very believable, but they do not make it certain.

### L2 human

We compare the Goldbach computation with a check that does prove a statement.

1. Claim A: each even $n$ with $4 \le n \le 20$ is a sum of two primes. We check the $9$ cases: $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, $10 = 3 + 7$, $12 = 5 + 7$, $14 = 3 + 11$, $16 = 3 + 13$, $18 = 5 + 13$, $20 = 3 + 17$.
2. The $9$ cases are all the cases of Claim A, so the check of step 1 proves Claim A.
3. Claim B: each even $n \ge 4$ is a sum of two primes. The check of step 1 covers $9$ of infinitely many cases.
4. The check proves nothing about $n = 22$ or larger, so it does not prove Claim B.

The typical use of the comparison is to decide whether a computation finishes a proof: we ask whether a proved argument shows that the computed cases are all the cases.
A trap is the size of the computation.
A check up to $4 \cdot 10^{18}$ is as far from a proof of Claim B as a check up to $20$, because in both cases the number of remaining cases is infinite.
