---
tag: XHHKMPD8A9
kind: example
name: A heuristic count of twin primes
msc: ["11N05", "11N36"]
topics: [DME0TPC348]
audience: research
instance_of: [VCQQNJ3SEZ]
uses: [VCQQNJ3SEZ, KTQDWMASNY, 0FER36N8SB, P6YN35K009]
sources:
  - url: https://en.wikipedia.org/wiki/Twin_prime
    locator: First Hardy–Littlewood conjecture
  - url: https://en.wikipedia.org/wiki/Probabilistic_number_theory
    locator: lead section
---

## Example

Up to one million there are exactly $8169$ [[twin prime|KTQDWMASNY]] pairs $(p, p + 2)$, and a short [[heuristic argument|VCQQNJ3SEZ]] predicts about $8248$.
We build that prediction step by step and test it.
Let $\pi_2(x)$ be the number of pairs $(p, p + 2)$ of primes with $p + 2 \le x$.

1. The naive model treats a number near $t$ as prime with probability $1/\ln t$, independently of its neighbors.
   Then $p$ and $p + 2$ are both prime with probability $1/(\ln t)^2$, and the model predicts
$$\pi_2(x) \approx \int_2^x \frac{dt}{(\ln t)^2}.$$
2. The prime $2$ needs a correction.
   For a random integer $n$, the numbers $n$ and $n + 2$ are both odd with probability $\tfrac12$, while two independent numbers are both odd with probability $\tfrac14$.
   So the prime $2$ multiplies the prediction by $2$.
3. Each odd prime $q$ needs a correction as well.
   Neither $n$ nor $n + 2$ is divisible by $q$ for $q - 2$ of the $q$ residues of $n$, while independence would give $\left(\tfrac{q-1}{q}\right)^2$.
   So $q$ multiplies the prediction by
$$\frac{(q-2)/q}{\left((q-1)/q\right)^2} = \frac{q(q-2)}{(q-1)^2}.$$
4. The product of all the corrections is $2C_2$, where $C_2$ is the twin prime constant:
$$C_2 = \prod_{q \ge 3} \frac{q(q-2)}{(q-1)^2} = 0.6601618\ldots, \qquad \pi_2(x) \approx 2C_2 \int_2^x \frac{dt}{(\ln t)^2}.$$
5. We test the prediction against the true counts, rounded to one decimal place.

| $x$ | $\pi_2(x)$ | naive model | corrected prediction | ratio |
|---|---|---|---|---|
| $10^3$ | $35$ | $34.7$ | $45.8$ | $0.76$ |
| $10^4$ | $205$ | $162.2$ | $214.2$ | $0.96$ |
| $10^5$ | $1224$ | $945.8$ | $1248.7$ | $0.98$ |
| $10^6$ | $8169$ | $6247.0$ | $8248.0$ | $0.99$ |

The ratio in the last column is $\pi_2(x)$ divided by the corrected prediction, and it moves toward $1$ as $x$ grows.
Since the integral tends to infinity, the heuristic predicts infinitely many twin primes, at a definite rate.
That is the [[twin prime conjecture|0FER36N8SB]] with a rate, and it is unproved.

## Remarks

### What the agreement shows

The corrected prediction is the case of pairs in the first Hardy-Littlewood conjecture on [[prime k-tuples|P6YN35K009]].
Its agreement with the table is strong evidence, because a formula with no free parameter matches four counts that range over two orders of magnitude.
It is still not a proof.
The model assumes that primes behave like random numbers once the divisibility by small primes is accounted for, and nobody has proved that assumption.
Yitang Zhang proved in 2013 that some fixed gap between primes occurs infinitely often, but the gap $2$ itself is open.

### What changes with the model

The naive model looks good at $x = 10^3$ only by chance.
For larger $x$ it is too low by a steady factor near $2C_2 \approx 1.32$, and the local corrections remove exactly that factor.
The same reasoning applied to the pairs $(p, p + 1)$ gives a correction factor $0$ at the prime $2$, since one of $n$ and $n + 1$ is always even.
That correctly predicts that $(2, 3)$ is the only such pair.

### Watch out

A model that fits the count of primes can still miss how primes relate to each other.
The naive model predicts $\pi(10^6)$ well, but it misses the twin count by about $24$ percent, because it ignores the parity of $p$ and $p + 2$.
Before trusting a random model for pairs, check the corrections at each small prime.

### Try it

Compute the correction factor for the prime $q = 3$.
It is $\tfrac{3 \cdot 1}{2^2} = 0.75$, because only one residue of $n$ modulo $3$ keeps both $n$ and $n + 2$ free of the factor $3$.

What does the model predict for pairs $(p, p + 4)$?
The local factors are the same as for $(p, p + 2)$, since $4$ has no odd prime factor, so the model predicts the same count asymptotically.

## Explanations

### L1 human

Near a million, about one number in $14$ is prime.
If primes were scattered at random, two numbers $2$ apart would both be prime about once in $14 \times 14$ tries.
But all primes except $2$ are odd, so if $p$ is prime then $p + 2$ is odd too, and that doubles the chance.
Other small primes change the chance a little more.
With these corrections the guess for the number of twin pairs below a million is $8248$, and the true number is $8169$.
The guess also says that the pairs never run out, but a good guess is not a proof.

### L2 human

We compute the first factors of the product for $C_2$.
For $q = 3$, $5$ and $7$ the factors are
$$\frac{3 \cdot 1}{2^2} = 0.75, \qquad \frac{5 \cdot 3}{4^2} = 0.9375, \qquad \frac{7 \cdot 5}{6^2} = 0.97222\ldots$$
Their product is
$$0.75 \cdot 0.9375 \cdot 0.97222\ldots = 0.68359\ldots,$$
and the full product over all odd primes is $0.66016\ldots$.
Each factor equals $1 - 1/(q-1)^2$, so the factors approach $1$ fast enough for the product to converge.
The typical use is to compute one local factor for each prime and multiply them, which gives the constant of any Hardy-Littlewood conjecture.
Watch out: the product converges slowly, so the constant is computed in practice by faster series, not by a direct product.
