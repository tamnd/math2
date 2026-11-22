---
tag: R1SP7B1F0V
kind: example
name: All maps of the real line under composition do not form an algebra
msc: ["15A04", "16S50"]
topics: [9080WQTZ3M]
audience: ug1
not_instance_of:
  - target: 5JA4CYT1TB
    note: with f(x) = x² and g = h = id, f ∘ (g + h) sends x to 4x² but f ∘ g + f ∘ h sends x to 2x², so left distributivity fails
uses: [0GZB2SN0PH, 1TZSV19D85, 05YBKMRVAR]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: Description
  - url: https://en.wikipedia.org/wiki/Function_space
    locator: lead section
---

## Example

If the maps are allowed to be nonlinear, composing does not respect sums, so the algebra laws break.
Let $\R^\R$ be the set of all maps $\R \to \R$, with pointwise addition and scalar multiplication, which is a vector space by the [[function space example|0GZB2SN0PH]].
Take [[composition|05YBKMRVAR]] as the multiplication, and let $f(x) = x^2$ and $g = h = \id_\R$.

1. We have $(f \circ (g + h))(x) = f(2x) = 4x^2$.
2. We have $(f \circ g + f \circ h)(x) = x^2 + x^2 = 2x^2$.
3. So $f \circ (g + h) \ne f \circ g + f \circ h$, and left distributivity fails.
4. Hence $\R^\R$ with composition is not a ring, and not an [[associative algebra|1TZSV19D85]].
5. Right distributivity holds for all maps, since $((g + h) \circ f)(x) = g(f(x)) + h(f(x))$.
6. The scalar rule also fails, since $(f \circ (2\id))(1) = 4$ but $(2 f)(1) = 2$.

Check: at $x = 1$, the two sides in steps 1 and 2 are $4$ and $2$.

## Remarks

The failure in step 3 comes from $f$, which is not additive.
If we change the set to the linear maps $\R \to \R$, we get the algebra $\End(\R) \cong \R$.
Composition is still associative on $\R^\R$, and $\id_\R$ is still a unit, so $\R^\R$ is a monoid under composition.
The additive maps $\R \to \R$ do form a ring under composition, because left distributivity is exactly additivity of the left factor.

## Explanations

### L1 human

Squaring the double of a number gives four times its square, not twice its square.
So composing with the squaring map does not respect sums.
This breaks a rule that every algebra must satisfy.

### L2 human

The example shows where linearity enters the algebra $\End(V)$.
Right distributivity holds for every map, by the definition of the sum, but left distributivity needs the left factor to be additive.
Watch out: a space of maps with composition need not be a ring.
