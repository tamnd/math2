---
tag: BV08DGBD7C
kind: example
name: Reduction modulo n is a homomorphism
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0JYTG5K9Y4]
illustrates: [0CXXJNG5B6]
uses: [0C4JS9RF5M, 03VFZ2WETT, 0W88CEGQP1]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Congruence classes
---

## Example

Let $n \ge 1$ be an integer.
Define $\varphi \colon (\mathbb{Z}, +) \to \mathbb{Z}/n\mathbb{Z}$ by $\varphi(u) = u \bmod n$, the class of $u$ in the [[integers modulo n|03VFZ2WETT]].

1. The map is a [[homomorphism|0JYTG5K9Y4]]. Write $u = qn + r$ and $v = q'n + r'$. Then $u + v = (q + q')n + (r + r')$, so $u + v$ and $r + r'$ have the same class modulo $n$.
2. The map is surjective. For $0 \le r < n$, we have $\varphi(r) = r \bmod n$.
3. The [[kernel|0W88CEGQP1]] is $n\mathbb{Z}$. Indeed $u \bmod n = 0$ holds exactly when $n$ divides $u$.
4. The fibre over the class of $r$ is the coset $r + n\mathbb{Z}$. For $n = 5$ and $r = 2$ it is $\{\dots, -8, -3, 2, 7, 12, \dots\}$.
5. By the [[first isomorphism theorem|0CXXJNG5B6]], the quotient group $\mathbb{Z}/n\mathbb{Z}$ is isomorphic to the image, the group of classes modulo $n$.

## Remarks

The example shows the standard way to make a finite group from $\mathbb{Z}$: take a homomorphism onto it and look at its kernel.
For $n = 1$ the codomain is the trivial group, and the kernel is all of $\mathbb{Z}$.
When $n$ grows, the kernel $n\mathbb{Z}$ gets sparser and the image $\mathbb{Z}/n\mathbb{Z}$ gets larger.
For no $n \ge 1$ is the map injective, because $\varphi(n) = \varphi(0)$.
If $m$ divides $n$, then $a \bmod n \mapsto a \bmod m$ is a well defined homomorphism $\mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z}$.

## Explanations

### L1 human

A clock with $12$ hours does reduction modulo $12$.
Thirty hours after midnight the hour hand shows $6$, because $30 = 2 \cdot 12 + 6$.
Adding hours and then reading the clock gives the same result as reading the clock and then adding on the clock face.
This is what it means for reduction to be a homomorphism.

### L2 human

We take $n = 5$ and check the rule on $u = 17$ and $v = 9$.

1. $17 = 3 \cdot 5 + 2$, so $\varphi(17) = 2$.
2. $9 = 1 \cdot 5 + 4$, so $\varphi(9) = 4$.
3. In $\mathbb{Z}/5\mathbb{Z}$, $2 + 4 = 6 \equiv 1$.
4. $17 + 9 = 26 = 5 \cdot 5 + 1$, so $\varphi(26) = 1$. Both ways give $1$.

The typical use is a quick test: if $a + b = c$ in $\mathbb{Z}$, then the remainders must also add up modulo $n$.
The trap is a negative integer.
The class of $-7$ modulo $5$ is $3$, not $-2$ written as a remainder, because $-7 = -2 \cdot 5 + 3$ and remainders lie between $0$ and $4$.
