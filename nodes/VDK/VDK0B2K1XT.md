---
tag: VDK0B2K1XT
kind: example
name: The Minkowski form gives no angle
msc: ["15A63", "97G70"]
topics: [VKVAJ94SKZ]
audience: ug1
not_instance_of:
  - target: 0ZEHZY85E6
    note: for the form u_1 v_1 - u_2 v_2 the quotient that should be a cosine can exceed 1, because the Cauchy-Schwarz inequality fails for this form
uses: [0ZEHZY85E6, 0RFWW56Y22, TFGECQ5C32]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Schwarz_inequality
    locator: Statement of the inequality
---

## Example

Let $u \star v = u_1 v_1 - u_2 v_2$ on $\mathbb{R}^2$, the [[Minkowski form|TFGECQ5C32]].
We try to define an angle by the formula of the [[angle between vectors|0ZEHZY85E6]], with $\star$ in place of the dot product.

1. Let $u = (2, 1)$ and $v = (1, 0)$.
2. Then $u \star u = 4 - 1 = 3$, $v \star v = 1 - 0 = 1$ and $u \star v = 2 - 0 = 2$.
3. The quotient is $\dfrac{u \star v}{\sqrt{u \star u}\sqrt{v \star v}} = \dfrac{2}{\sqrt{3}} \approx 1.155$.
4. This number is larger than $1$, so no real $\theta$ has it as its cosine.
5. So the formula defines no angle between $u$ and $v$.

## Remarks

Step 3 shows that the Cauchy-Schwarz inequality fails for $\star$: $(u \star v)^2 = 4 > 3 = (u \star u)(v \star v)$.
The [[Cauchy-Schwarz inequality|0RFWW56Y22]] holds for the dot product and for every inner product, so there the quotient always lies in $[-1, 1]$.
This is why the angle formula in $\mathbb{R}^n$ needs the Cauchy-Schwarz inequality first.
In special relativity the reversed inequality $(u \star v)^2 \geq (u \star u)(v \star v)$ holds for time-like vectors, and the quotient is a hyperbolic cosine.

## Explanations

### L1 human

The angle formula divides a product by two lengths and calls the result a cosine.
A cosine is always between $-1$ and $1$.
With a wrong "product", the quotient can be larger than $1$, here about $1.155$.
Then there is no angle at all.

### L2 human

The check of the hypothesis is the point: before we take an arccosine, we must know that its argument is in $[-1, 1]$.
For the dot product, the Cauchy-Schwarz inequality gives this; for other forms, it may fail.
A trap: a formula that works in the plane can fail for a form that only looks like the dot product.
