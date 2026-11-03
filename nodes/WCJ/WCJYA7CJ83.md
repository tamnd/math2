---
tag: WCJYA7CJ83
kind: example
name: Lie algebra of an associative algebra
msc: [17B60, 16W99]
instance_of: [5JJYBJ6A8K]
uses: [3CTW1P4HBP, ZKFN197MBR, T2HH02QC2M]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra
---

## Example

Let $A$ be an [[associative algebra|3CTW1P4HBP]] over a field $k$.
Define $[a, b] = ab - ba$, the [[commutator|T2HH02QC2M]] of $a$ and $b$.
Then $A$ with this bracket is a [[Lie algebra|5JJYBJ6A8K]], often written $A_L$ or $A^-$.

Check of the axioms.
The bracket is bilinear because the product of $A$ is bilinear.
For each $a$, $[a, a] = aa - aa = 0$.
The [[Jacobi identity|ZKFN197MBR]] holds because $A$ is associative: in the cyclic sum each of the six products of $a, b, c$ appears once with each sign.

The same construction makes every associative ring a Lie ring.

## Remarks

For $A = M_n(k)$ this gives the general linear Lie algebra $\mathfrak{gl}_n(k)$.
For $A = \End(V)$ it gives $\mathfrak{gl}(V)$.
If $A$ is commutative, all brackets vanish and $A_L$ is abelian.
Every Lie algebra over a field embeds in a Lie algebra of this form, namely in its universal enveloping algebra.

## Explanations

### L1 human

Any setting where one can multiply in a non-commutative way gives a Lie algebra for free.
Keep the addition and replace the product $ab$ by $ab - ba$.
This new bracket measures how far $a$ and $b$ are from commuting.
Matrices with $AB - BA$ are the main case.
