---
tag: JRNNE88P5F
kind: example
name: Kasner metric
msc: [83C15, 83F05]
instance_of: [JRV1T69FYJ]
uses: [4GTNM0WHDH, 45AE2YXWT3]
sources:
  - url: https://en.wikipedia.org/wiki/Kasner_metric
same_as:
  wikidata: Q3333767
  wikipedia: Kasner metric
---

## Example

On $(0, \infty) \times \R^3$ with coordinates $(t, x, y, z)$, the *Kasner metric* with exponents $p_1, p_2, p_3 \in \R$ is
$$g = -dt^2 + t^{2p_1} dx^2 + t^{2p_2} dy^2 + t^{2p_3} dz^2.$$
Apart from the trivial case $p_1 = p_2 = p_3 = 0$, which is flat Minkowski space, it is a [[vacuum solution|JRV1T69FYJ]] exactly when the *Kasner conditions* hold:
$$p_1 + p_2 + p_3 = 1, \qquad p_1^2 + p_2^2 + p_3^2 = 1.$$

Check: a computation of the [[Ricci curvature|4GTNM0WHDH]] gives
$$R_{tt} = \frac{(p_1 + p_2 + p_3) - (p_1^2 + p_2^2 + p_3^2)}{t^2}, \qquad R_{xx} = p_1 (p_1 + p_2 + p_3 - 1)\, t^{2p_1 - 2},$$
and similar formulas for $R_{yy}$ and $R_{zz}$, while the off-diagonal components vanish.
All of them vanish under the Kasner conditions.
Conversely, if all $R_{ii}$ vanish, then either every $p_i = 0$ or $p_1 + p_2 + p_3 = 1$, and then $R_{tt} = 0$ gives $p_1^2 + p_2^2 + p_3^2 = 1$.

Example: $(p_1, p_2, p_3) = (\frac23, \frac23, -\frac13)$.
The sum is $1$ and the sum of squares is $\frac49 + \frac49 + \frac19 = 1$.
Two directions expand while the third contracts.
The exponents $(1, 0, 0)$ also satisfy the conditions; this case is flat, a piece of Minkowski space in Milne-type coordinates.
If no exponent equals $1$, one exponent is negative and the other two are positive, and the curvature blows up as $t \to 0$, a [[gravitational singularity|45AE2YXWT3]].

## Explanations

### L1 human

The Kasner metric describes an empty universe that is the same at every point but expands at different rates in different directions.
The volume grows like $t$, but typically two directions stretch while the third shrinks.
Going back in time towards $t = 0$, the universe is crushed to a singularity, like a cigar or a pancake.
It is the building block of the oscillating picture of singularities studied by Belinski, Khalatnikov and Lifshitz.
