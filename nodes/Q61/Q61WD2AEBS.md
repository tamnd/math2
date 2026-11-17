---
tag: Q61WD2AEBS
kind: example
name: pi(x) < li(x) for all computed x
msc: ["11N05", "11Y35"]
topics: [DME0TPC348]
audience: research
instance_of: [JFD3QWCX8Z]
uses: [JFD3QWCX8Z, 0RQSNVTFVZ, VP98WSTZWT, 71JVW6G7M1]
sources:
  - url: https://en.wikipedia.org/wiki/Skewes%27s_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Prime-counting_function
    locator: lead section
---

## Example

We compare the [[prime-counting function|0RQSNVTFVZ]] $\pi(x)$ with the [[logarithmic integral|VP98WSTZWT]] $\operatorname{li}(x)$.
The data are strong [[numerical evidence|JFD3QWCX8Z]] for the inequality $\pi(x) < \operatorname{li}(x)$, and the inequality is false.

1. The data.

| $x$ | $\pi(x)$ | $\operatorname{li}(x)$ | $\operatorname{li}(x) - \pi(x)$ |
|---|---|---|---|
| $10$ | $4$ | $6.17$ | $2.17$ |
| $10^2$ | $25$ | $30.13$ | $5.13$ |
| $10^3$ | $168$ | $177.61$ | $9.61$ |
| $10^4$ | $1229$ | $1246.14$ | $17.14$ |
| $10^5$ | $9592$ | $9629.81$ | $37.81$ |
| $10^6$ | $78498$ | $78627.55$ | $129.55$ |

2. The conjecture. The difference is positive at every point, and it grows. The conjecture "$\pi(x) < \operatorname{li}(x)$ for all $x \geq 2$" looks safe.
3. More data. The inequality has been checked for all $x$ from $2$ up to $10^{19}$, and the difference stays positive.
4. The theorem. John Littlewood proved in 1914 that $\pi(x) - \operatorname{li}(x)$ changes sign infinitely often. So the conjecture of step 2 is false.
5. The scale. Littlewood's proof gave no explicit $x$. Stanley Skewes gave the first explicit bound in 1933, under the Riemann hypothesis; it was near $e^{e^{e^{79}}}$.
6. Today. Later work showed that a sign change occurs below $e^{727.9513468} \approx 1.397 \cdot 10^{316}$. The least $x$ with $\pi(x) > \operatorname{li}(x)$ is still unknown.

## Remarks

The growth of the difference in step 1 is misleading.
The difference is about $\tfrac12 \operatorname{li}(\sqrt{x})$, which comes from the squares of primes, plus an oscillating term from the zeros of the zeta function.
The oscillating term is usually smaller, and it wins only when many zeros push in the same direction.
See [[Skewes's number|71JVW6G7M1]] for the history of the bounds, and [[numerical evidence for conjectures|JFD3QWCX8Z]] for the scale $\ln \ln x$ that explains why no computer range is enough.

## Explanations

### L1 human

There is a smooth formula that estimates how many primes lie below a number.
For every number anyone has checked, the formula gives too many.
It seems natural to guess that it always gives too many.
But a proof from 1914 shows that, very far out, the formula sometimes gives too few.
The first place where this happens is so far out that no computer can reach it.

### L2 human

We check one row of step 1.

1. The primes up to $100$ are $2, 3, 5, 7, 11, \ldots, 97$, and there are $25$ of them.
2. $\operatorname{li}(100) = 30.126\ldots$, computed as $\operatorname{li}(2) + \int_2^{100} dt/\ln t$ with $\operatorname{li}(2) = 1.045\ldots$.
3. So $\operatorname{li}(100) - \pi(100) \approx 5.13$, and the inequality holds at $x = 100$.

The typical use: a table of this kind suggests a conjecture and a growth rate for the error.
A trap: a difference that grows in the table can still change sign, when an oscillating term grows faster in the long run.
