---
tag: RB6G2NWW4J
kind: example
name: Euclid's proof of the infinitude of primes as a Book proof
msc: ["00A35", "11A41"]
topics: [1BTHSHST4M]
audience: school
instance_of: [A4RJYP79A7]
uses: [A4RJYP79A7, 0292EPPPT0, 0SPBEDVNW1, 0SN0MAEKYX, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_theorem
    locator: Euclid's proof
  - url: https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK
    locator: Outline
---

## Example

[[Euclid's theorem|0292EPPPT0]] says that there are infinitely many [[prime numbers|0SN0MAEKYX]].
We give Euclid's proof, and then we check it against the criteria of a [[proof from the Book|A4RJYP79A7]].

1. Let $p_1, \dots, p_k$ be any finite list of primes, with $k \ge 1$.
2. Put $N = p_1 p_2 \cdots p_k + 1$.
   Each $p_i$ is at least $2$, so $N \ge 3$.
3. Since $N \ge 2$, $N$ has a [[prime divisor|0SPBEDVNW1]] $q$.
4. Suppose $q = p_i$ for some $i$.
   Then $q$ [[divides|096PW7Q014]] both the product $p_1 \cdots p_k$ and $N$, so it divides their difference $N - p_1 \cdots p_k = 1$, which is impossible because $q \ge 2$.
5. So $q$ is a prime that is not in the list.
6. Step 5 holds for every finite list, so no finite list holds all the primes, and there are infinitely many.
7. Check with the list $2, 3, 5, 7, 11, 13$: $N = 30031 = 59 \cdot 509$, and the primes $59$ and $509$ are not in the list.

Now the criteria.
The proof is correct, since each step follows from the steps before it and from the existence of a prime divisor.
It is brief, with six short steps.
It turns on one idea, the number $N$ of step 2, and the rest checks that $N$ works.
It needs little background, only divisibility and prime divisors, so a school student can follow it.
And it explains why the primes never run out: a product of primes plus one shares no prime factor with them.
So the proof meets each criterion, and it is a standard example of a Book proof.

## Remarks

Step 7 shows a common error: $N$ need not be prime, and $30031$ is not.
The proof claims only that the prime factors of $N$ are new.

The proof is often written as a [[proof by contradiction|0J0XBKG64S]], starting from a supposed list of all primes.
The version above is direct: it builds a new prime from each finite list.
Both versions are correct, and the direct one avoids an extra layer of supposition.

The existence of a prime divisor in step 3 is the one fact that the proof takes from outside, and its proof is also short: the least divisor of $N$ that is greater than $1$ must be prime.
The variant [[with n! + 1|TMXSM5BNVK]] uses the same idea with a different number.
The theorem is Proposition 20 of Book IX of Euclid's *Elements*.
Aigner and Ziegler open their book with six proofs of the theorem, among them Euclid's and Furstenberg's, which shows that the Book can hold more than one proof of a theorem.

## Explanations

### L1 human

Suppose someone hands you a list of primes and says that it has all of them.
Multiply all the primes of the list together, and add $1$.
Each prime of the list leaves remainder $1$ when it divides this new number, so none of them divides it.
But every whole number larger than $1$ has some prime factor, so the new number has a prime factor that is missing from the list.
The list was not complete, and no list can be.

### L2 human

We run the proof for the list $2, 3, 5$.
The product is $2 \cdot 3 \cdot 5 = 30$, so $N = 31$, and dividing $31$ by $2$, $3$ and $5$ leaves remainder $1$ each time.
So no prime of the list divides $31$, and its prime divisor is $31$ itself, a new prime.
Now run it again with the longer list $2, 3, 5, 31$:
$$N = 2 \cdot 3 \cdot 5 \cdot 31 + 1 = 931 = 7^2 \cdot 19.$$
This time $N$ is not prime, and the new primes are $7$ and $19$.
The typical use of the example is to show the shape of a Book proof: one construction, then a short check.
Watch out: do not say that $N$ is a new prime, since the second run shows that $N$ can be composite.
