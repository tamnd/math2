---
tag: A71PPKKTAR
kind: example
name: Lie algebra of vector fields
msc: [17B66, 58A05]
instance_of: [5JJYBJ6A8K]
uses: [F45VQ47GPV, 0V33BNKZ9S, 68FGQEBD6J, 1ZAT1Z967A]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_field
---

## Example

Let $M$ be a [[smooth manifold|F45VQ47GPV]], and let $\mathfrak{X}(M)$ be the real vector space of smooth vector fields on $M$.
A vector field $X$ acts on [[smooth functions|0V33BNKZ9S]] $f$ by differentiation in the direction of $X$, written $Xf$.
The [[Lie bracket of vector fields|68FGQEBD6J]] is the vector field $[X, Y]$ with $[X, Y]f = X(Yf) - Y(Xf)$.
With this bracket, $\mathfrak{X}(M)$ is a real [[Lie algebra|5JJYBJ6A8K]].

Check: the bracket is bilinear over $\R$, and $[X, X] f = X(Xf) - X(Xf) = 0$.
For the Jacobi identity, write each bracket as a commutator of operators on functions.
Expanding $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]]$ gives twelve terms of the form $\pm UVW$ with $\set{U, V, W} = \set{X, Y, Z}$, and they cancel in pairs.

A concrete piece: on $M = \R$ write $\partial = d/dx$.
For smooth functions $f, g$ one gets $[f \partial, g \partial] = (f g' - g f') \partial$.
So $[\partial, x \partial] = \partial$, $[\partial, x^2 \partial] = 2x \partial$ and $[x \partial, x^2 \partial] = x^2 \partial$.
Thus the span of $\partial$, $x\partial$ and $x^2 \partial$ is a three-dimensional Lie subalgebra, and it is isomorphic to the [[special linear Lie algebra|1ZAT1Z967A]] $\mathfrak{sl}_2(\R)$.

## Remarks

If $\dim M \ge 1$, the Lie algebra $\mathfrak{X}(M)$ is infinite-dimensional.
The bracket is not bilinear over the ring of smooth functions: $[X, fY] = f[X, Y] + (Xf) Y$.

## Explanations

### L1 human

A vector field tells each point of a space in which direction to move.
Two vector fields can be combined into a third one, their bracket, which measures how much the two motions fail to commute.
This bracket obeys the same rules as the commutator $AB - BA$ of matrices.
So the vector fields on a space form a Lie algebra, and it is one of the main examples that motivated Lie theory.
On the line, the fields $1$, $x$ and $x^2$ times $d/dx$ form a small closed piece of it that behaves like $2 \times 2$ matrices of trace zero.
