---
tag: KH7BAGDK4P
kind: example
name: Catenary
msc: [70C20, 53A04, 49K05]
illustrates: [KHT3FBB7NZ]
uses: [KHT3FBB7NZ, 036696EMG2, 0TH78S7GBZ, 8REBFQD6E0]
sources:
  - url: https://en.wikipedia.org/wiki/Catenary
same_as:
  wikidata: Q214561
  wikipedia: Catenary
---

## Example

A *catenary* is a curve
$$y = a \cosh\left(\frac{x}{a}\right) + c,$$
with constants $a > 0$ and $c \in \R$, where $\cosh$ is the [[hyperbolic cosine|036696EMG2]].
It is the shape of a uniform, flexible, inextensible chain hanging under constant gravity in [[equilibrium|KHT3FBB7NZ]].

Check: let the chain have mass $\lambda$ per unit length, let $g$ be the gravitational acceleration, and put the lowest point at $x = 0$.
The tension acts along the chain, and no horizontal external force acts.
So the horizontal component $H > 0$ of the tension is the same at every point.
Let $s(x)$ be the [[arc length|0TH78S7GBZ]] of the chain from the lowest point to the point $x$.
At $x$, the vertical component of the tension balances the weight $\lambda g s$ of this piece of chain.
Since the tension is tangent to the chain, $H y'(x) = \lambda g s(x)$, so with $a = H / (\lambda g)$ one gets $y' = s / a$.
Differentiating and using $s'(x) = \sqrt{1 + y'^2}$ gives $y'' = \frac{1}{a}\sqrt{1 + y'^2}$.
The function $y = a \cosh(x/a)$ satisfies this: $y' = \sinh(x/a)$ and $y'' = \frac{1}{a}\cosh(x/a) = \frac{1}{a}\sqrt{1 + \sinh^2(x/a)}$.

## Remarks

The same curve solves the [[catenary problem|8REBFQD6E0]] of the calculus of variations: it minimises the potential energy among curves of given length joining two points.
The parameter $a$ is the radius of curvature at the lowest point.
Turned upside down, the catenary is the ideal shape of an arch carrying only its own weight, in pure compression.
A chain hanging under a load that is uniform per horizontal length, as in a suspension bridge deck, takes a parabolic shape instead.

## Explanations

### L1 human

Hold a necklace by its two ends and let it hang: the curve it makes is a catenary.
It looks like a parabola but is a different curve, given by the hyperbolic cosine.
At each point the upward part of the pull along the chain balances the weight of the chain between that point and the lowest point.
This balance forces the shape.
