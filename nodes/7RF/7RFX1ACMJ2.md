---
tag: 7RFX1ACMJ2
kind: example
name: 22/7 approximates π but does not equal it
msc: ["00A35", "11Y60"]
topics: [Z2WNQ1DNTX]
audience: school
instance_of: [BCGR3NPPXC]
uses: [BCGR3NPPXC, 0C1VYVNV2N, 0VM8B2SB4P, 0DZXAXEJQ9]
sources:
  - url: https://en.wikipedia.org/wiki/Approximations_of_%CF%80
    locator: lead section
---

## Example

A school exercise says "take $\pi = \frac{22}{7}$".
We compare the fraction $\frac{22}{7}$ with the number [[π|0C1VYVNV2N]] and choose the correct sign from the [[equality, definition and equivalence signs|BCGR3NPPXC]].

1. Long division gives the [[decimal expansion|0VM8B2SB4P]]
   $$\frac{22}{7} = 3.142857\,142857\ldots,$$
   with the block $142857$ repeated.
2. The decimal expansion of $\pi$ begins $3.141592653\ldots$.
3. The two numbers agree in the digits $3.14$ and differ in the next digit, and
   $$\frac{22}{7} - \pi \approx 3.142857 - 3.141593 = 0.001264.$$
4. So $\frac{22}{7} \ne \pi$, and the true statement is $\frac{22}{7} \approx \pi$, with a relative error of $\frac{0.001264}{3.1416} \approx 0.04\%$.
5. There is a stronger reason: $\pi$ is an [[irrational number|0DZXAXEJQ9]], so no fraction of integers equals $\pi$.
6. A precise statement with only exact signs is
   $$3.141 < \pi < 3.142 < \frac{22}{7}.$$

## Remarks

The sign $\approx$ is correct here and the sign $=$ is wrong.
The sign $\approx$ carries no fixed precision, so step 6 gives the same information as inequalities, which are exact and can be used in a proof.

Archimedes proved $3 \tfrac{10}{71} < \pi < 3 \tfrac{1}{7}$, and $3 \tfrac{1}{7} = \frac{22}{7}$ is his upper bound.
A much better fraction is
$$\frac{355}{113} = 3.14159292\ldots,$$
whose error is less than $3 \times 10^{-7}$, so it agrees with $\pi$ to six decimal places.

## Explanations

### L1 human

Many people use $\frac{22}{7}$ for $\pi$ in school problems.
Divide $22$ by $7$ and you get $3.1428\ldots$, while $\pi$ is $3.1415\ldots$.
They are very close, but they are not the same number.
So we write $\frac{22}{7} \approx \pi$, with the wavy sign that means "about equal".

### L2 human

How much error does the rounding $\pi \approx \frac{22}{7}$ cause in the area of a circle of radius $10$?
The exact area is
$$\pi r^2 = 100 \pi \approx 314.159.$$
With $\frac{22}{7}$ in place of $\pi$ the area is
$$\frac{22}{7} \cdot 100 = \frac{2200}{7} \approx 314.286.$$
The difference is about $0.126$, which is $100$ times the error $0.001264$ from step 3.
Check: $100 \times 0.001264 = 0.1264$.
So an error in $\pi$ is multiplied by $r^2$, and the result is less accurate in absolute terms than the input.
The fraction $\frac{22}{7}$ is fine for a quick estimate by hand with three correct digits.
Watch out: a computation that starts with $\pi \approx \frac{22}{7}$ must end with $\approx$ too, and its digits after the third are not reliable.
