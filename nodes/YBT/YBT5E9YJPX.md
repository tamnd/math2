---
tag: YBT5E9YJPX
kind: proof
name: Proof of cancellation in congruences
msc: [11A07]
proves: 09RDZZGJZ9
uses: [0TPW25CBN6, 096PW7Q014, 02WF878BH1, 0GFKP8F8AG, 0DQVHMYAGA, 03BAREW1Z5]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Basic properties
---

## Proof

1. Let $n$ be a positive integer, and let $a, b, c$ be integers with $c a \equiv c b \pmod n$. Let $d = \gcd(c, n)$ be their [[greatest common divisor|02WF878BH1]].
2. Since $n \ne 0$, $c$ and $n$ are not both $0$. So $d$ is a positive integer that divides $c$ and $n$.
3. Write $c = d c'$ and $n = d n'$ with integers $c'$ and $n'$. Since $n > 0$ and $d > 0$, $n' = n / d$ is a positive integer.
4. By the definition of [[congruence|0TPW25CBN6]], $n$ [[divides|096PW7Q014]] $c a - c b = c (a - b)$. So there is an integer $k$ with $c (a - b) = n k$.
5. By step 3, this reads $d c' (a - b) = d n' k$. Since $d \ne 0$, we can divide by $d$ and get $c' (a - b) = n' k$. So $n'$ divides $c' (a - b)$.
6. By [[Bézout's identity|0DQVHMYAGA]], there are integers $x$ and $y$ with $c x + n y = d$.
7. By step 3, this reads $d (c' x + n' y) = d$. Dividing by $d$ gives $c' x + n' y = 1$.
8. Let $e$ be a common divisor of $c'$ and $n'$. By step 7, $e$ divides $1$, so $e = \pm 1$. Hence $\gcd(c', n') = 1$, and $n'$ and $c'$ are [[coprime|0GFKP8F8AG]].
9. By steps 5 and 8 and the [[generalized Euclid's lemma|03BAREW1Z5]], $n'$ divides $a - b$.
10. Hence $a \equiv b \pmod{n / d}$.

## Idea

Divide the relation $n \mid c (a - b)$ by the common factor $d$ of $c$ and $n$. What is left of $c$ shares no factor with what is left of $n$, so Euclid's lemma removes it.
