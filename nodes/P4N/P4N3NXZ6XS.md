---
tag: P4N3NXZ6XS
kind: proof
name: Proof that the complex numbers form a field
msc: [12D99]
proves: 0FRSR10DWF
uses: [09FTAET5Z4, 0FGENPMPJX, 05V7J4WD1C, 0QA8CHH8MG, 0GYGHKX834, 0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_number
    locator: Abstract and algebraic definitions
---

## Proof

We check the axioms of a [[field|0QA8CHH8MG]] one by one, using the rules for the [[complex numbers|09FTAET5Z4]].

1. Let $z = a + b i$, $w = c + d i$ and $u = e + f i$ be complex numbers, with $a, b, c, d, e, f$ real.
The operations are $z + w = (a + c) + (b + d) i$ and $z w = (a c - b d) + (a d + b c) i$.
2. All computations with $a, \dots, f$ below take place in $\R$. They use only the field axioms of $\R$, by [[the reals form a field|0FGENPMPJX]].
Two complex numbers are compared through their real and imaginary parts, by [[equality of complex numbers|05V7J4WD1C]].
3. Addition is commutative and associative. Indeed, both properties hold for the real parts and for the imaginary parts separately, since they hold in $\R$.
4. Let $0 = 0 + 0 i$. Then $z + 0 = (a + 0) + (b + 0) i = z$.
5. Let $-z = (-a) + (-b) i$. Then $z + (-z) = 0 + 0 i = 0$.
So $(\C, +)$ is an abelian group with identity $0$.
6. Multiplication is commutative. Indeed, $w z = (c a - d b) + (c b + d a) i$, and this equals $z w$ because real multiplication is commutative.
7. Multiplication is associative. We have $z w = (a c - b d) + (a d + b c) i$. Multiplying by $u$ gives
$$(z w) u = (a c e - b d e - a d f - b c f) + (a c f - b d f + a d e + b c e) i.$$
8. Also $w u = (c e - d f) + (c f + d e) i$. Multiplying $z$ by it gives
$$z (w u) = (a c e - a d f - b c f - b d e) + (a c f + a d e + b c e - b d f) i.$$
The real parts in steps 7 and 8 agree, and so do the imaginary parts. So $(z w) u = z (w u)$.
9. Let $1 = 1 + 0 i$. Then $1 \cdot z = (1 a - 0 b) + (1 b + 0 a) i = z$. By step 6, also $z \cdot 1 = z$.
10. Multiplication distributes over addition. We have $w + u = (c + e) + (d + f) i$, so
$$z (w + u) = (a c + a e - b d - b f) + (a d + a f + b c + b e) i.$$
11. Also $z w + z u = \bigl((a c - b d) + (a e - b f)\bigr) + \bigl((a d + b c) + (a f + b e)\bigr) i$. This has the same parts as step 10.
So $z (w + u) = z w + z u$. By step 6, also $(w + u) z = w z + u z$.
12. Steps 3 to 11 show that $\C$ is a [[ring|0894J980RK]], and step 6 shows that it is a [[commutative ring|0GYGHKX834]].
13. We have $0 \neq 1$, because $\operatorname{Re} 0 = 0$ and $\operatorname{Re} 1 = 1$ differ.
14. Now let $z = a + b i \neq 0$. Then $a \neq 0$ or $b \neq 0$, by equality of complex numbers.
Squares of real numbers are nonnegative, and the square of a nonzero real number is positive. So $s = a^2 + b^2 > 0$.
15. Let $v = \dfrac{a}{s} + \dfrac{-b}{s} i$, which makes sense because $s \neq 0$. Then
$$z v = \left( a \cdot \frac{a}{s} - b \cdot \frac{-b}{s} \right) + \left( a \cdot \frac{-b}{s} + b \cdot \frac{a}{s} \right) i = \frac{a^2 + b^2}{s} + 0 i = 1.$$
16. So every nonzero $z$ has a multiplicative inverse $z^{-1} = v$.
Together with steps 12 and 13, this proves that $\C$ is a field.

## Idea

Every field axiom reduces to identities among real numbers, by comparing real and imaginary parts.
The only axiom that needs an idea is the inverse.
The number $a^2 + b^2$ is a positive real, so we can divide by it, and $(a + b i)(a - b i) = a^2 + b^2$.
