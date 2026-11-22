---
tag: DQQ6NXK1SQ
kind: example
name: The positive real numbers with product as addition
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [000AYPA9AJ]
uses: [05EGHEQZAW, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Two, Section I
---

## Example

Let $V = \mathbb{R}_{>0}$ be the set of positive [[real numbers|08J2M1JYAG]].
We give it a new addition and a new scalar multiplication, with scalars in $\mathbb{R}$:
$$x \oplus y = xy, \qquad a \odot x = x^a \qquad (x, y \in V,\ a \in \mathbb{R}).$$
So "adding" two vectors multiplies them, and "scaling" by $a$ raises to the power $a$.
We check that $V$ is a real [[vector space|000AYPA9AJ]], with the axioms numbered as in the [[definition|05EGHEQZAW]], for $x, y, z \in V$ and $a, b \in \mathbb{R}$.

1. Closure: for $x, y > 0$ the numbers $xy$ and $x^a$ are positive, so both operations map into $V$.
2. Axiom 1 is associativity of the product: $x \oplus (y \oplus z) = x(yz) = (xy)z = (x \oplus y) \oplus z$.
3. Axiom 2 is commutativity of the product: $x \oplus y = xy = yx = y \oplus x$.
4. Axiom 3: the number $1$ is the zero vector, because $x \oplus 1 = x \cdot 1 = x$.
5. Axiom 4: the negative of $x$ is $1/x$, which is positive, and $x \oplus (1/x) = 1$, the zero vector.
6. Axiom 5 is a law of exponents: $a \odot (b \odot x) = (x^b)^a = x^{ab} = (ab) \odot x$.
7. Axiom 6: $1 \odot x = x^1 = x$.
8. Axiom 7 is the rule for a power of a product: $a \odot (x \oplus y) = (xy)^a = x^a y^a = (a \odot x) \oplus (a \odot y)$.
9. Axiom 8 is the rule for a sum of exponents: $(a + b) \odot x = x^{a + b} = x^a x^b = (a \odot x) \oplus (b \odot x)$.

All eight axioms hold, so $V$ is a real vector space.

## Remarks

The example shows that the zero vector is defined by its role, not by its look.
Here it is the number $1$, the negative of $2$ is $\tfrac{1}{2}$, and the number $0$ is not in $V$ at all.
The [[first consequences of the axioms|5E4VBC0A4H]] still hold in this disguise: $0v = 0$ reads $x^0 = 1$, and $(-1)v = -v$ reads $x^{-1} = 1/x$.

Why do the laws of exponents fit the axioms so well?
The natural logarithm turns $\oplus$ into $+$ and $\odot$ into ordinary multiplication, since $\ln(xy) = \ln x + \ln y$ and $\ln(x^a) = a \ln x$.
So $\ln$ is a [[linear isomorphism|0B8T10CE7N]] from $V$ onto $\mathbb{R}$, and $V$ is a copy of the real line in disguise, of [[dimension|03GSZ8RTZJ]] $1$.
Any $x \ne 1$ is a basis; for $x = e$, each $y > 0$ equals $(\ln y) \odot e$, because $e^{\ln y} = y$.

What changes if we enlarge the set?
If we allow $x = 0$, axiom 4 fails, because $0 \oplus y = 0$ for every $y$, so $0$ has no negative.
If we allow negative numbers, closure fails, because $(-1)^{1/2}$ is not a real number.

## Explanations

### L1 human

Here the "vectors" are positive numbers, "adding" means multiplying, and "scaling by $a$" means raising to the power $a$.
These strange rules still obey every law of a vector space.
For example, "$2$ plus $3$" is $6$, and "$2$ times the vector $3$" is $3^2 = 9$.
The number $1$ plays the role of zero, because multiplying by $1$ changes nothing.

### L2 human

We test axiom 7 with $a = 2$, $x = 3$ and $y = 5$, and then compute a combination.
For the left side, add first and then scale:
$$2 \odot (3 \oplus 5) = 2 \odot 15 = 15^2 = 225.$$
For the right side, scale first and then add:
$$(2 \odot 3) \oplus (2 \odot 5) = 9 \oplus 25 = 225.$$
The two sides agree.
Now compute the combination $(3 \odot 2) \oplus ((-2) \odot 4)$: it is $2^3 \cdot 4^{-2} = 8/16 = \tfrac{1}{2}$.
Check with logarithms: $3 \ln 2 - 2 \ln 4 = 3 \ln 2 - 4 \ln 2 = -\ln 2 = \ln \tfrac{1}{2}$.
The example is the standard test that a student checks axioms from the given operations and not from habit.
