---
tag: Z6H5WJYJ4H
kind: example
name: An ordinal sum of the Łukasiewicz and product t-norms
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
instance_of: [VR6D8JXX1W]
uses: [BHGCVPAJW0]
sources:
  - url: https://en.wikipedia.org/wiki/Construction_of_t-norms
    locator: Ordinal sums; Ordinal sums of continuous t-norms
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Properties of continuous t-norms
---

## Example

An ordinal sum glues rescaled copies of [[t-norms|BHGCVPAJW0]] along the diagonal of the unit square.
Given t-norms $T_i$ and disjoint open intervals $(a_i, b_i)$, the ordinal sum $T$ uses $T_i$, rescaled, on the square $[a_i, b_i]^2$, and the minimum elsewhere.

$$T(x, y) = a_i + (b_i - a_i) \, T_i\!\left(\frac{x - a_i}{b_i - a_i}, \frac{y - a_i}{b_i - a_i}\right) \quad \text{on } [a_i, b_i]^2.$$

We take the Łukasiewicz t-norm on $[0, \tfrac12]$ and the product t-norm on $[\tfrac12, 1]$, and compute four values.

1. For $T(0.2, 0.4)$, both arguments lie in $[0, \tfrac12]$.
   They rescale to $0.4$ and $0.8$, the Łukasiewicz t-norm gives $\max(0, 0.4 + 0.8 - 1) = 0.2$, and scaling back gives $T = \tfrac12 \cdot 0.2 = 0.1$.
2. For $T(0.6, 0.8)$, both arguments lie in $[\tfrac12, 1]$.
   They rescale to $0.2$ and $0.6$, the product gives $0.12$, and scaling back gives $T = \tfrac12 + \tfrac12 \cdot 0.12 = 0.56$.
3. For $T(0.3, 0.7)$, the arguments lie in different intervals, so $T = \min(0.3, 0.7) = 0.3$.
4. At the shared corner, $T(\tfrac12, \tfrac12)$ is $\tfrac12 \max(0, 1 + 1 - 1) = \tfrac12$ by the first summand and $\tfrac12 + \tfrac12 \cdot 0 = \tfrac12$ by the second.
   So the two formulas agree where the squares meet.
5. The idempotents, the $e$ with $T(e, e) = e$, are exactly $0$, $\tfrac12$ and $1$.
   For $0 < e < \tfrac12$ we get $T(e, e) = \tfrac12 \max(0, 4e - 1)$, which is below $e$ because $2e - \tfrac12 < e$.
   For $\tfrac12 < e < 1$ we get $T(e, e) = \tfrac12 + 2(e - \tfrac12)^2$, which is below $e$ because $2(e - \tfrac12) < 1$.
6. Both summands are continuous, and the pieces agree on the edges of the squares, so $T$ is a continuous t-norm.

## Remarks

The example shows the shape of every continuous t-norm.
By the Mostert-Shields theorem of 1957, a t-norm is continuous exactly when it is an ordinal sum of copies of the Łukasiewicz and product t-norms, with the minimum outside the copies.
The idempotents mark the ends of the copies, as $0$, $\tfrac12$ and $1$ do here.

The Łukasiewicz copy starts at $0$, so $T$ has zero divisors: $T(0.2, 0.2) = \tfrac12 \max(0, 0.4 + 0.4 - 1) = 0$.
If we swap the two summands, putting the product on $[0, \tfrac12]$, the zero divisors disappear, since a product copy at the bottom is positive on positive inputs.
The logic of all continuous t-norms is [[BL|3AQ5GHTXA4]], and this $T$ is one of its standard models.

## Explanations

### L1 human

An ordinal sum builds a new "and" from small copies of old ones.
Split the scale into a lower half and an upper half.
In the lower half use the Łukasiewicz rule, shrunk to fit, and in the upper half use multiplication, shrunk to fit.
If the two inputs lie in different halves, take the smaller one.

### L2 human

To evaluate an ordinal sum, find the interval of each argument.
If both lie in the same interval, rescale them to $[0, 1]$, apply the summand, and scale back.
Otherwise, take the minimum.
Watch out: do not forget to scale back.
In step 2 the product of the rescaled values is $0.12$, but $T(0.6, 0.8) = 0.56$, not $0.12$.
