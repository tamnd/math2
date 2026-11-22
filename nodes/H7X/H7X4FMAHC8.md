---
tag: H7X4FMAHC8
kind: example
name: Irrational a and b with a to the power b rational, by construction
msc: ["00A35", "11J72"]
topics: [958EF46EYJ]
audience: ug1
instance_of: [01XM7JEKHY]
not_instance_of:
  - target: JZQVJ9XT63
    note: the proof names the pair a = sqrt(2), b = log_2 9 and checks it, so it is constructive
uses: [01XM7JEKHY, 0DZGSDHD92, 8V5FDX9562, 0V948DE5KA]
sources:
  - url: https://en.wikipedia.org/wiki/Constructive_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Irrational_number
    locator: lead section
---

## Example

Statement: there are irrational numbers $a$ and $b$ such that $a^b$ is rational.
We give a [[constructive proof|01XM7JEKHY]] with an explicit pair.

1. Let $a = \sqrt{2}$ and $b = \log_2 9$.
2. The number $a$ is irrational, by the [[irrationality of the square root of 2|0DZGSDHD92]].
3. By the rule for the [[logarithm of a power|0V948DE5KA]],
   $$b = \log_2 3^2 = 2 \log_2 3.$$
4. The number $\log_2 3$ is irrational, as [[the logarithm of 3 to base 2 is irrational|8V5FDX9562]] shows.
   If $b = \frac{p}{q}$ were rational, then $\log_2 3 = \frac{p}{2q}$ would be rational too.
   So $b$ is irrational.
5. Compute the power with the rule $(x^r)^s = x^{rs}$, which holds for $x > 0$:
   $$a^b = \left(2^{1/2}\right)^{2 \log_2 3} = 2^{\log_2 3} = 3.$$
6. So $a$ and $b$ are irrational, and $a^b = 3$ is rational.

Check: $\log_2 9 \approx 3.1699$ and $\sqrt{2}^{3.1699} = 2^{1.58496} \approx 3.000$.

## Remarks

The proof names the pair and checks each property, so it is not a [[non-constructive existence proof|JZQVJ9XT63]].
Compare it with [[the proof by cases that some irrational power is rational|7X8GT7Y5WY]], which uses $\sqrt{2}^{\sqrt{2}}$ and does not decide which of two pairs works.
The constructive proof costs more, because it needs the irrationality of $\log_2 3$, which rests on the fact that $2^p = 3^q$ has no solution in positive integers.
The proof by cases needs only the irrationality of $\sqrt{2}$.

The same idea gives many pairs.
For any integer $m \ge 2$ that is not a power of $2$, the number $\log_2 m$ is irrational, and the pair $a = \sqrt{2}$, $b = 2 \log_2 m$ has $a^b = m$.
For $m = 4$ the idea breaks down: $b = 2 \log_2 4 = 4$ is rational, so the pair does not meet the conditions.

## Explanations

### L1 human

A root such as $\sqrt{2}$ is not a fraction.
A logarithm such as $\log_2 9$, the power of $2$ that gives $9$, is not a fraction either.
Put them together: $\sqrt{2}$ raised to the power $\log_2 9$ is exactly $3$.
So two numbers that are not fractions can combine to give a whole number.
The proof names both numbers, so anyone can check the claim.

### L2 human

We check step 5 slowly, with the rules of exponents for a positive base.
First write the root as a power, $\sqrt{2} = 2^{1/2}$.
Then multiply the exponents, which the rule $(x^r)^s = x^{rs}$ allows because the base $2$ is positive:
$$\left(2^{1/2}\right)^{b} = 2^{b/2}.$$
By step 3, $\frac{b}{2} = \log_2 3$, and $2^{\log_2 3} = 3$ because $\log_2$ is the inverse of $t \mapsto 2^t$.

The typical use: a logarithm undoes a power, so a power with a logarithm in the exponent can often be computed exactly.
Watch out: the rule $(x^r)^s = x^{rs}$ fails for negative bases.
For example $\left((-1)^2\right)^{1/2} = 1$, but $(-1)^{2 \cdot 1/2} = -1$.
