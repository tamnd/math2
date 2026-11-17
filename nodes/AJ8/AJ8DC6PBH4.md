---
tag: AJ8DC6PBH4
kind: example
name: Squaring on the nonzero real numbers
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0JYTG5K9Y4, 0S21GNW9ZB]
illustrates: [0CXXJNG5B6]
uses: [08J2M1JYAG, 082GHNPJ53, 0S21GNW9ZB, 0W88CEGQP1]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Image and kernel
---

## Example

Let $\mathbb{R}^\times$ be the nonzero [[real numbers|08J2M1JYAG]] under multiplication.
Define $s \colon \mathbb{R}^\times \to \mathbb{R}^\times$ by $s(x) = x^2$.

1. The map is a [[homomorphism|0JYTG5K9Y4]]. Multiplication of real numbers is commutative, so $(xy)^2 = x^2 y^2$.
2. For $x \ne 0$ we have $x^2 > 0$. So the image lies in $\mathbb{R}_{>0}$, the positive real numbers.
3. Each $y > 0$ is the square of $\sqrt{y}$. So the [[image|0S21GNW9ZB]] is exactly $\mathbb{R}_{>0}$.
4. $x^2 = 1$ holds exactly when $x = 1$ or $x = -1$. So the [[kernel|0W88CEGQP1]] is $\{1, -1\}$.
5. The fibre over $4$ is $\{2, -2\} = 2 \cdot \{1, -1\}$, a coset of the kernel.
6. By the [[first isomorphism theorem|0CXXJNG5B6]], $\mathbb{R}^\times / \{1, -1\} \cong \mathbb{R}_{>0}$.

## Remarks

The example shows a homomorphism whose image is a proper subgroup of the codomain.
Squaring is a homomorphism on each [[abelian group|082GHNPJ53]], but not on $S_3$, as the non-examples of [[group homomorphism|0JYTG5K9Y4]] show.
On $\mathbb{C}^\times$, squaring is surjective, because each nonzero complex number has a square root, and the kernel is still $\{1, -1\}$.
On $\mathbb{Q}^\times$, the image is the set of squares of nonzero rationals, and it does not contain $2$.
On the additive group $(\mathbb{R}, +)$, the map $x \mapsto x^2$ is not a homomorphism, because $(1 + 1)^2 \ne 1^2 + 1^2$.

## Explanations

### L1 human

The square of a nonzero number is always positive.
Each positive number is a square, for example $9 = 3^2$.
So squaring sends the nonzero numbers onto the positive numbers.
It forgets the sign: $3$ and $-3$ have the same square, and $\{1, -1\}$ is the kernel.

### L2 human

We check the homomorphism rule and a fibre with numbers.

1. Take $x = -2$ and $y = 3$. Then $s(xy) = s(-6) = 36$, and $s(x)s(y) = 4 \cdot 9 = 36$.
2. The fibre over $9$ is $\{3, -3\}$. Both elements give $9$, and they differ by the factor $-1$ from the kernel.

The typical use is to see that $\mathbb{R}_{>0}$ is a subgroup of $\mathbb{R}^\times$: it is an image.
The trap is the additive group: on $(\mathbb{R}, +)$ the same formula is not a homomorphism.
