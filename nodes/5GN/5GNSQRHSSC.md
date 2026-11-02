---
tag: 5GNSQRHSSC
kind: example
name: Involution as solution of Babbage's equation
msc: [39B12, 39B22]
instance_of: [GP56NBN9RY]
uses: [Y0EZW47S8M, 27C6J3YNZY, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Involution_(mathematics)
---

## Example

Babbage's functional equation asks for maps $f \colon X \to X$ with $f(f(x)) = x$ for all $x \in X$.
Its solutions are exactly the [[involutions|GP56NBN9RY]] of $X$, and also exactly the [[iterative roots|27C6J3YNZY]] of order $2$ of the identity.

Take $X = \R \setminus \set{-1}$ and $f(x) = \frac{1 - x}{1 + x}$.
First, $f$ maps $X$ into $X$: the equation $\frac{1 - x}{1 + x} = -1$ would give $1 - x = -1 - x$, which is impossible.
Second, for $x \in X$,
$$f(f(x)) = \frac{1 - \frac{1-x}{1+x}}{1 + \frac{1-x}{1+x}} = \frac{(1 + x) - (1 - x)}{(1 + x) + (1 - x)} = \frac{2x}{2} = x.$$
So $f$ is an involution and solves Babbage's equation.
Other solutions on suitable sets are $x \mapsto c - x$, $x \mapsto 1/x$ and the identity.

## Remarks

On an interval $I \subseteq \R$, every [[continuous|0X3WGX95FE]] solution other than the identity is strictly decreasing.
Indeed, a continuous involution is injective, hence strictly monotone.
If it is increasing and $f(x) > x$ for some $x$, then $x = f(f(x)) > f(x) > x$, a contradiction; the case $f(x) < x$ is the same.
So an increasing continuous solution is the identity.
The more general equation $f^n(x) = x$ asks for the iterative roots of order $n$ of the identity; for example the rotation $z \mapsto e^{2\pi i/n} z$ of $\C$ is one.

## Explanations

### L1 human

Babbage's equation asks for a rule that, applied twice, brings every point back to where it started.
Mirror reflections, the change of sign $x \mapsto -x$ and the reciprocal $x \mapsto 1/x$ are such rules.
The map $x \mapsto \frac{1 - x}{1 + x}$ is a less obvious one, and a short computation checks it.
