---
tag: MJNB0GQVVY
kind: example
name: Squaring on the field with four elements is semilinear
msc: ["15A04", "12E20"]
topics: [9080WQTZ3M]
audience: grad
instance_of: [BNPDDM95KF]
uses: [BNPDDM95KF, 0ZXZ82FTX2, 0CGCPX8Z70, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Semilinear_map
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Frobenius_endomorphism
    locator: Definition
---

## Example

In a field where $1 + 1 = 0$, squaring respects sums, and it twists each scalar by squaring it too.
Let $K = \mathbb F_4 = \{0, 1, \omega, \omega^2\}$ be the [[field with four elements|0ZXZ82FTX2]], where $\omega^2 = \omega + 1$ and $1 + 1 = 0$.
View $V = K$ as a vector space of dimension $1$ over $K$.
Let $\sigma \colon K \to K$, $\sigma(a) = a^2$, be the [[Frobenius automorphism|0CGCPX8Z70]], and let $f \colon V \to V$ be $f(x) = x^2$.

1. Since $2 = 0$ in $K$, we get $(x + y)^2 = x^2 + 2xy + y^2 = x^2 + y^2$, so $f$ is additive.
2. For scalars, $f(\lambda x) = \lambda^2 x^2 = \sigma(\lambda)\, f(x)$.
3. The map $\sigma$ is an automorphism of $K$, since it is additive by step 1, multiplicative, and injective on the finite field $K$.
4. By steps 1 to 3, $f$ is $\sigma$-[[semilinear|BNPDDM95KF]].
5. The map $f$ is not [[linear|0RJF668P1T]] over $K$, since $f(\omega \cdot 1) = \omega^2 = \omega + 1$, while $\omega\, f(1) = \omega$.

Check: $f(0) = 0$, $f(1) = 1$, $f(\omega) = \omega^2 = \omega + 1$ and $f(\omega^2) = \omega^4 = \omega$.

## Remarks

Since $\sigma(\omega) = \omega^2 \ne \omega$, we have $\sigma \ne \id$, so $f$ is semilinear for a nontrivial automorphism.
The map $f$ is a bijection with $f \circ f = \id$, since $x^4 = x$ for each $x \in \mathbb F_4$.
If we change the scalars to the prime field $\mathbb F_2$, viewing $\mathbb F_4$ as a space of dimension $2$ over $\mathbb F_2$, then $f$ is linear, since $\sigma$ fixes $0$ and $1$.
For $\mathbb F_q$ with $q = p^k$, applying $x \mapsto x^p$ to the coordinates in a basis of an $\mathbb F_q$-space gives a semilinear map for the Frobenius automorphism.

## Explanations

### L1 human

In the field with four elements, $1 + 1 = 0$, so squaring respects sums.
Squaring also turns a scalar $\lambda$ into $\lambda^2$.
So it is linear up to a twist of the scalars, which is what semilinear means.

### L2 human

This example shows a semilinear map that is not antilinear, since the twist is the Frobenius map and not complex conjugation.
The check $f(\omega) = \omega^2 \ne \omega = \omega f(1)$ shows that $f$ is not linear.
Watch out: additivity of squaring depends on the characteristic being $2$.
