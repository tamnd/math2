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

Let $\pi_2(x)$ be the number of [[twin prime|KTQDWMASNY]] pairs $(p, p+2)$ with $p + 2 \leq x$.
We predict $\pi_2(x)$ by a [[heuristic argument|VCQQNJ3SEZ]] and compare the prediction with the data.

1. The naive model. A number near $t$ is prime with probability about $1/\ln t$. If $p$ and $p + 2$ were independent, a pair near $t$ would occur with probability $1/(\ln t)^2$. This predicts $\pi_2(x) \approx \int_2^x dt/(\ln t)^2$.
2. The correction at $2$. For random integers $n$, both $n$ and $n + 2$ are odd with probability $1/2$, not $(1/2)^2 = 1/4$. So the prime $2$ multiplies the prediction by $2$.
3. The correction at an odd prime $q$. Neither $n$ nor $n + 2$ is divisible by $q$ with probability $(q - 2)/q$. Independent events would give $((q-1)/q)^2$. So $q$ multiplies the prediction by $\dfrac{q(q-2)}{(q-1)^2}$.
4. The corrected prediction. The product of the factors is $2C_2$, where $C_2 = \prod_{q \geq 3} \dfrac{q(q-2)}{(q-1)^2} = 0.6601618\ldots$ is the twin prime constant. The prediction is $\pi_2(x) \approx 2C_2 \int_2^x dt/(\ln t)^2$.
5. The test.

| $x$ | $\pi_2(x)$ | naive model | corrected prediction | ratio |
|---|---|---|---|---|
| $10^3$ | $35$ | $34.7$ | $45.8$ | $0.76$ |
| $10^4$ | $205$ | $162.2$ | $214.2$ | $0.96$ |
| $10^5$ | $1224$ | $945.8$ | $1248.7$ | $0.98$ |
| $10^6$ | $8169$ | $6247.0$ | $8248.0$ | $0.99$ |

The last column is $\pi_2(x)$ divided by the corrected prediction, and it approaches $1$.
6. The conclusion. The heuristic predicts infinitely many twin primes, since the integral tends to infinity. This is the [[twin prime conjecture|0FER36N8SB]], with a precise rate.

## Remarks

The prediction of step 4 is the case of prime pairs in the first Hardy-Littlewood conjecture, which treats every admissible [[prime k-tuple|P6YN35K009]].
The naive model of step 1 is close at $x = 10^3$ only by chance; for larger $x$ it is too low by the factor $2C_2 \approx 1.32$.
The same reasoning applied to $(p, p + 1)$ gives a correction factor $0$ at the prime $2$, which correctly predicts that $(2, 3)$ is the only such pair.
The conjecture is open, although Yitang Zhang proved in 2013 that some gap below a fixed bound occurs infinitely often.

## Explanations

### L1 human

Near a million, about one number in $14$ is prime.
If primes were random, two numbers $2$ apart would both be prime about once in $14 \times 14$ tries.
But primes are odd, and that doubles the chance, and other small primes change it a little more.
With these corrections, the guess for the number of twin prime pairs below a million is $8248$.
The true number is $8169$, very close, and the guess says that the pairs never run out.

### L2 human

We compute the first factors of the product in step 4.

1. For $q = 3$: $\dfrac{3 \cdot 1}{2^2} = 0.75$.
2. For $q = 5$: $\dfrac{5 \cdot 3}{4^2} = 0.9375$.
3. For $q = 7$: $\dfrac{7 \cdot 5}{6^2} = 0.9722\ldots$.
4. The product of these three factors is $0.6836\ldots$, and the full product over all odd primes is $0.6601618\ldots$.

The factors tend to $1$ like $1 - 1/(q-1)^2$, so the product converges.
The typical use: compute the local correction at each prime and multiply them, which gives the constant of a Hardy-Littlewood conjecture.
A trap: the product converges slowly, so the constant must be computed by a faster method, not by a direct product.
