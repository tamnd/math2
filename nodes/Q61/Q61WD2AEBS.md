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

There are $78498$ primes up to one million, and the smooth estimate $\operatorname{li}(10^6)$ is about $78627.5$, larger by about $130$.
At every $x$ that anyone has computed, the estimate is too large, and yet it is known to be too small for some larger $x$.
We compare the [[prime-counting function|0RQSNVTFVZ]] $\pi(x)$ with the [[logarithmic integral|VP98WSTZWT]] $\operatorname{li}(x)$, and we watch strong [[numerical evidence|JFD3QWCX8Z]] support a false statement.

1. We tabulate both functions, with $\operatorname{li}(x)$ rounded to two decimal places.

| $x$ | $\pi(x)$ | $\operatorname{li}(x)$ | $\operatorname{li}(x) - \pi(x)$ |
|---|---|---|---|
| $10$ | $4$ | $6.17$ | $2.17$ |
| $10^2$ | $25$ | $30.13$ | $5.13$ |
| $10^3$ | $168$ | $177.61$ | $9.61$ |
| $10^4$ | $1229$ | $1246.14$ | $17.14$ |
| $10^5$ | $9592$ | $9629.81$ | $37.81$ |
| $10^6$ | $78498$ | $78627.55$ | $129.55$ |

2. The difference is positive at every entry, and it grows.
   So the statement "$\pi(x) < \operatorname{li}(x)$ for all $x \ge 2$" looks safe.
3. Computation has checked the inequality for all $x$ from $2$ up to $10^{19}$, and the difference stays positive.
4. John Littlewood proved in 1914 that $\pi(x) - \operatorname{li}(x)$ changes sign infinitely often.
   So the statement of step 2 is false, in spite of all the evidence.
5. Littlewood's proof gave no explicit $x$ where the sign changes.
   Stanley Skewes gave the first explicit bound in 1933, assuming the Riemann hypothesis, and it was $e^{e^{e^{79}}}$.
   In 1955 he gave a much larger bound that does not assume the Riemann hypothesis.
6. Later work showed that a sign change occurs below
$$e^{727.9513468} \approx 1.397 \cdot 10^{316}.$$
   The least $x$ with $\pi(x) > \operatorname{li}(x)$ is still unknown.

## Remarks

### Why the table misleads

The growth of the difference in step 1 hides how the difference is made.
Its main smooth part is about $\tfrac12 \operatorname{li}(\sqrt{x})$, which comes from the squares of primes.
On top of that sits an oscillating term that comes from the zeros of the Riemann zeta function.
The oscillating term is usually smaller, and it wins only when many zeros push in the same direction, which first happens far beyond any computation.
[[Skewes's number|71JVW6G7M1]] tells the history of the bounds.

### What the evidence is worth

The inequality holds for every $x$ up to $10^{19}$, which is an enormous number of cases, and it is still false.
A pattern that holds in many cases is not a proof, and this is one of the clearest examples.
The scale explains why: on the scale of $\ln \ln x$, which governs this kind of oscillation, the computed range reaches only about $3.8$, and the first sign change lies near $6.6$.

### Watch out

A difference that grows in a table can still change sign later, if an oscillating term grows faster in the long run.
Before you read a table as evidence for an inequality, ask which term controls the difference and how fast it oscillates.

### Try it

How many digits does the bound $1.397 \cdot 10^{316}$ have?
It has $317$ digits, since the number lies between $10^{316}$ and $10^{317}$.

## Explanations

### L1 human

There is a smooth formula that estimates how many primes lie below a number.
For every number anyone has checked, the formula gives a little too many.
It seems natural to guess that it always gives too many.
But a proof from 1914 shows that very far out the formula sometimes gives too few.
The first place where this happens is so far out that no computer can reach it, so checking more numbers would never have found the error.

### L2 human

We check one row of the table, $x = 100$.
The primes up to $100$ are $2, 3, 5, 7, 11, \dots, 97$, and there are $25$ of them.
The logarithmic integral is computed as a principal value up to $2$ plus an ordinary integral from $2$:
$$\operatorname{li}(100) = \operatorname{li}(2) + \int_2^{100} \frac{dt}{\ln t} = 1.045\ldots + 29.081\ldots = 30.126\ldots$$
So $\operatorname{li}(100) - \pi(100) \approx 5.13$, and the inequality holds at $x = 100$.
The typical use of such a table is to suggest a conjecture and a growth rate for the error.
Watch out: the table shows only where the inequality holds, and Littlewood's theorem shows that this is not everywhere.
