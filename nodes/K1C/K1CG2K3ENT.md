---
tag: K1CG2K3ENT
kind: proof
name: Proof of the existence and uniqueness of a fraction in lowest terms
msc: [11A05]
proves: 0R64A2CVN4
uses: [0NCJ5WXN6Z, 0C4JS9RF5M, 02WF878BH1, 096PW7Q014, 0GFKP8F8AG, 03BAREW1Z5]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_fraction
    locator: Uniqueness
---

## Proof

We divide by the greatest common divisor for existence, and use the generalized Euclid's lemma for uniqueness.
Recall that two fractions $a / b$ and $c / d$ of [[integers|0C4JS9RF5M]] are the same [[rational number|0NCJ5WXN6Z]] when $a d = b c$.
Let $q$ be a rational number, and write $q = c / d$ with integers $c$ and $d \neq 0$.

1. Existence. Let $g = \gcd(c, d)$ be the [[greatest common divisor|02WF878BH1]]. Since $1$ [[divides|096PW7Q014]] $c$ and $d$, and $c$, $d$ are not both $0$, we get $g \ge 1$.
2. Since $g$ divides $c$ and $d$, there are integers $c'$ and $d'$ with $c = g c'$ and $d = g d'$. Since $d \neq 0$, also $d' \neq 0$.
3. We show that $\gcd(c', d') = 1$. Let $e \ge 1$ be a common divisor of $c'$ and $d'$, with $c' = e u$ and $d' = e v$.
4. Then $c = (g e) u$ and $d = (g e) v$, so $g e$ is a common divisor of $c$ and $d$. Hence $g e \le g$.
5. Since $g \ge 1$, step 4 gives $e \le 1$, so $e = 1$. Every common divisor of $c'$ and $d'$ is therefore at most $1$, and $1$ is one of them. So $\gcd(c', d') = 1$.
6. If $d' > 0$, let $a = c'$ and $b = d'$. If $d' < 0$, let $a = -c'$ and $b = -d'$. In both cases $b > 0$.
7. The integers $a, b$ have the same divisors as $c', d'$, because $k \mid x$ exactly when $k \mid -x$. So $\gcd(a, b) = 1$.
8. We have $c b = \pm g c' d' = a d$, with the same sign on both sides. So $a / b = c / d = q$.
9. Uniqueness. Let $a / b = a' / b' = q$, with $b, b' > 0$ and $\gcd(a, b) = \gcd(a', b') = 1$. Then $a b' = a' b$.
10. So $b$ divides $a b'$. Since $b$ and $a$ are [[coprime|0GFKP8F8AG]], the [[generalized Euclid's lemma|03BAREW1Z5]] gives $b \mid b'$.
11. In the same way, $b'$ divides $a' b$ and is coprime to $a'$, so $b' \mid b$.
12. Write $b' = b k$ with $k$ an integer. Since $b, b' > 0$, we get $k > 0$, so $k \ge 1$ and $b' \ge b$. In the same way, $b \ge b'$. So $b = b'$.
13. Then $a b = a' b$ with $b \neq 0$, so $(a - a') b = 0$ and $a = a'$. So the pair $(a, b)$ is unique.

## Idea

Dividing the top and the bottom by their greatest common divisor leaves no common factor, and a sign change makes the bottom positive.
For uniqueness, cross-multiplying shows that each denominator divides the other.
Two positive numbers that divide each other are equal, and then the numerators agree too.
