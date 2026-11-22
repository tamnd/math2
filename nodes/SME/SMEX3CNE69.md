---
tag: SMEX3CNE69
kind: example
name: Kernel and image of differentiation on cubic polynomials
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [0S23E6YE83, 0WSFKKT6FF, 0ZZXSBTR4J, 0APCFW7639]
uses: [02YFME3RGW, 0JB228DCWB, 0JGB7A6GTS, 00K4FK4NBH, 0JGZCDT5DN, 0SS770NS8B]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Example

Differentiation on cubic polynomials loses exactly the constant term and produces exactly the quadratics, so its kernel and image can be read off by hand.
Let $P_3$ be the [[space of real polynomials of degree at most 3|0JGZCDT5DN]], with basis $1, x, x^2, x^3$.
Let $D \colon P_3 \to P_3$ be differentiation, $D(p) = p'$, which is linear by the [[examples of linear maps|0SS770NS8B]].
For $p = a_0 + a_1 x + a_2 x^2 + a_3 x^3$ we have
$$D(p) = a_1 + 2a_2 x + 3a_3 x^2.$$

1. The equation $D(p) = 0$ means $a_1 = 0$, $2a_2 = 0$ and $3a_3 = 0$, so $a_1 = a_2 = a_3 = 0$ and $p = a_0$ is constant.
2. So the [[kernel|02YFME3RGW]] is the space of constant polynomials, with basis $1$, and the [[nullity|00K4FK4NBH]] is $1$.
3. Each value $D(p)$ has degree at most $2$, so the [[image|0JB228DCWB]] is contained in $P_2$.
4. Each $q = b_0 + b_1 x + b_2 x^2$ in $P_2$ is $D(p)$ for $p = b_0 x + \tfrac{b_1}{2} x^2 + \tfrac{b_2}{3} x^3$.
5. So $\operatorname{im} D = P_2$, with basis $1, x, x^2$, and the [[rank|0JGB7A6GTS]] is $3$.

Check step 4 with $q = 1 + x + x^2$: the recipe gives $p = x + \tfrac{1}{2} x^2 + \tfrac{1}{3} x^3$, and $D(p) = 1 + x + x^2$.
The rank and the nullity add up to $3 + 1 = 4 = \dim P_3$, as the [[rank-nullity theorem|0W4FSW1TVB]] says.

## Remarks

As a map $P_3 \to P_3$, the map $D$ is neither injective nor surjective: $D(1) = D(0)$, and $x^3$ is not in the image.
In finite dimension these two failures always come together for a map from a space to itself.
On the whole ring $\R[x]$ they separate: there $D$ is surjective, because every polynomial has a polynomial antiderivative, but it is still not injective.

The field matters too.
Over a field of characteristic $p > 0$, the kernel of $D$ on $F[x]$ also contains $x^p$, since $D(x^p) = p\,x^{p-1} = 0$.
Over $\R$, step 2 is the polynomial case of the calculus fact that a function with derivative $0$ on an interval is constant.

## Explanations

### L1 human

The polynomials with derivative zero are the constants, so the kernel of differentiation is the set of constants.
The derivative of a cubic is at most a quadratic.
Each quadratic is the derivative of some cubic, so the image is the set of quadratics.

### L2 human

The same answer comes out of the matrix of $D$ in the basis $1, x, x^2, x^3$:
$$\begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
It has one zero column and three independent columns, which gives nullity $1$ and rank $3$.
The kernel also explains the "$+ C$" in an antiderivative: two antiderivatives of the same polynomial differ by an element of the kernel.
Watch out: the image is $P_2$ inside the target $P_3$, not all of $P_3$.
