---
tag: 3JF4PFZFYZ
kind: proof
name: Proof of the generalized Euclid's lemma
msc: [11A05]
proves: 03BAREW1Z5
uses: [0GFKP8F8AG, 0DQVHMYAGA, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_lemma
    locator: Proofs
---

## Proof

We use Bézout's identity.

1. Let $n$, $a$ and $b$ be integers with $n \mid ab$, and let $n$ and $a$ be [[coprime|0GFKP8F8AG]], so $\gcd(n, a) = 1$.
2. By [[Bézout's identity|0DQVHMYAGA]], there are integers $x$ and $y$ with $n x + a y = 1$.
3. Multiplying by $b$ gives $b = n b x + a b y$.
4. Since $n$ [[divides|096PW7Q014]] $ab$, there is an integer $k$ with $ab = n k$. Then $a b y = n k y$.
5. So $b = n b x + n k y = n (b x + k y)$, and $b x + k y$ is an integer.
6. Hence $n \mid b$.

## Idea

Coprimality gives $nx + ay = 1$. Multiplying by $b$ writes $b$ as a sum of two multiples of $n$: one is visibly a multiple, and the other is a multiple of $ab$.
