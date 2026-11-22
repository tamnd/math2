---
tag: 32AP5ZDMJJ
kind: example
name: A strong induction with too few base cases, for 2n = 0
msc: ["97E50", "00A35"]
topics: [EEH2F76CYQ]
audience: school
instance_of: [V52HDTMPV5]
uses: [V52HDTMPV5, 0KMVFSHFGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Complete (strong) induction
---

## Example

False claim: $2n = 0$ for every natural number $n$.
Here is a "proof" by [[strong induction|0KMVFSHFGZ]], and it is an instance of the [[error in induction proofs|V52HDTMPV5]] called "too few base cases".

1. Let $P(n)$ be the statement "$2n = 0$".
2. Base case.
   We have $2 \cdot 0 = 0$, so $P(0)$ holds.
3. Step.
   Let $n \ge 1$, and assume $P(k)$ for every natural number $k < n$.
4. Write $n = a + b$ with natural numbers $a < n$ and $b < n$.
5. By the assumption, $2a = 0$ and $2b = 0$, so
   $$2n = 2a + 2b = 0 + 0 = 0,$$
   and $P(n)$ holds.
6. "By strong induction", $P(n)$ holds for every $n$.

Now we check each part.

1. The base case is correct.
2. Step 5 is correct algebra, once numbers $a$ and $b$ with $a, b < n$ exist.
3. For $n \ge 2$ they exist: $a = 1$ and $b = n - 1$ give $a + b = n$, with $1 < n$ and $n - 1 < n$.
4. For $n = 1$ they do not exist.
   The only ways to write $1 = a + b$ with natural numbers are $0 + 1$ and $1 + 0$, and in both one summand is $1$, which is not less than $n = 1$.
5. So the step proves $P(n)$ only for $n \ge 2$, and $P(1)$ needed its own base case.
6. That base case is false, since $2 \cdot 1 = 2 \ne 0$.
   So the claim fails at $n = 1$, and the proof is wrong.

## Remarks

In strong induction the step must work for every $n$ above the base cases.
If it works only from some $n_1$ on, every value below $n_1$ must be checked as a base case.
Here the step correctly derives $P(n)$ from $P(1)$ and $P(n - 1)$ for every $n \ge 2$, so the whole error sits at the single value $n = 1$.

Change the claim and the same proof is correct.
For "$0 \cdot n = 0$", the base cases $n = 0$ and $n = 1$ both hold, since $0 \cdot 1 = 0$, and the step for $n \ge 2$ is the same, so the claim is proved.
The same care is needed for steps of the form "$P(n - 1)$ and $P(n - 2)$ imply $P(n)$": such a step needs $n \ge 2$, so the base cases must include $n = 0$ and $n = 1$, as in [[the proof that $F_n < 2^n$|3ZDPCTKC9M]].

## Explanations

### L1 human

The argument says: every number is the sum of two smaller numbers, and if the smaller numbers have the property, so does the sum.
That is true for $2$, which is $1 + 1$, and for $3$, which is $1 + 2$.
But $1$ is not the sum of two numbers smaller than $1$, because the only choices are $0 + 1$ and $1 + 0$.
So the argument never reaches $1$, and in fact $2 \cdot 1 = 2$, not $0$.
Because the chain breaks at $1$, every later step builds on a false claim.

### L2 human

Compare a correct strong induction of the same shape: every natural number $n \ge 2$ is a product of primes.
The smallest value is $n = 2$, which is prime, so it is a product of one prime.
For the step, let $n \ge 3$ and assume the claim for every $k$ with $2 \le k < n$.
If $n$ is prime, it is a product of one prime.
Otherwise $n = ab$ with $2 \le a, b < n$, by the definition of a composite number, and both factors are in the range of the assumption.
So $a$ and $b$ are products of primes, and then $n = ab$ is one too.

Here the step works for every $n \ge 3$, and the one value below it, $n = 2$, is a base case.
The check is always the same: for each $n$ above the base cases, the smaller values that the step uses must exist and must lie in the range of the assumption.
Watch out for a check of the step at a large $n$ only, where the split always exists.
