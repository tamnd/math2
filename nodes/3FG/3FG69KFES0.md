---
tag: 3FG69KFES0
kind: example
name: An estimate of 2 to the 100 by rounding
msc: ["00A35", "11A99"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [6KCEWEP4WA]
uses: [6KCEWEP4WA]
sources:
  - url: https://en.wikipedia.org/wiki/Power_of_two
    locator: lead section
---

## Example

Which number is larger, $2^{100}$ or $10^{30}$, and by about what factor?
We first use a [[heuristic|6KCEWEP4WA]] estimate to get the size, and then an exact argument to get the answer.

1. We round: $2^{10} = 1024$, which is close to $1000 = 10^3$.
2. We raise both sides to the power $10$:
   $$2^{100} = (2^{10})^{10} \approx (10^3)^{10} = 10^{30}.$$
3. The estimate says that the two numbers are close, but it cannot say which one is larger, because the rounding in step 1 threw that information away.
4. We go back to the exact fact behind the rounding: $2^{10} = 1024 > 1000 = 10^3$, and both sides are positive.
5. For positive numbers, $a > b$ implies $a^{10} > b^{10}$, so $2^{100} > 10^{30}$.
6. The ratio is
   $$\frac{2^{100}}{10^{30}} = \left( \frac{1024}{1000} \right)^{10} = 1.024^{10}.$$
7. The binomial theorem gives the lower bound $1.024^{10} \ge 1 + 10 \cdot 0.024 = 1.24$.
   A direct computation gives $1.024^{10} \approx 1.268$.

So $2^{100}$ is larger than $10^{30}$, by a factor of about $1.27$.

## Remarks

The rounding of step 2 gave the order of size, $10^{30}$, at once.
It could not decide the comparison, since the two numbers differ by less than the error that the rounding made.
The exact argument of steps 4 and 5 uses the same idea, $2^{10}$ against $10^3$, but it keeps the direction of the inequality.
This is the usual relation between a heuristic and a proof: the heuristic finds the idea, and the proof keeps track of what the heuristic ignored.

The error of the rounding grows with the exponent.
For $2^{1000}$ against $10^{300}$ the ratio is $1.024^{100}$, which is about $10.7$, so the rounded estimate is now wrong by a factor of more than $10$.

## Explanations

### L1 human

The number $2^{10}$ is $1024$, a little more than $1000$.
So ten factors of $2^{10}$ give a little more than ten factors of $1000$.
That means $2^{100}$ is a little more than a $1$ followed by $30$ zeros.
The rough idea "$1024$ is about $1000$" told us the size, and the exact fact "$1024$ is more than $1000$" told us which number is bigger.

### L2 human

Compare $3^{20}$ with $10^9$ in the same way.
Round first: $3^2 = 9$ is close to $10$, so
$$3^{20} = 9^{10} \approx 10^{10}.$$
This suggests that $3^{20}$ is larger than $10^9$ by a factor of about $10$.
The exact value is $3^{20} = 3486784401$, about $3.49 \cdot 10^9$.
So $3^{20} > 10^9$ is right, but the factor is about $3.5$, not $10$.
Rounding $9$ up to $10$ ten times overestimates by $(10/9)^{10} \approx 2.87$.
A rounded estimate gives the order of size quickly, and it can be wrong by a large factor when the same rounding is repeated many times.
