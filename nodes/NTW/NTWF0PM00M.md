---
tag: NTWF0PM00M
kind: proof
name: Proof that the units of the Gaussian integers are 1, -1, i and -i
msc: [11R11]
proves: 06RH4XAGRY
uses: [0K5W69AC0J, 03AN1V4ZFJ, 019NFGFPR5]
sources:
  - url: https://proofwiki.org/wiki/Units_of_Gaussian_Integers
---

## Proof

Let $\Z[i]$ be the ring of [[Gaussian integers|0K5W69AC0J]] and let $N(a + b i) = a^2 + b^2$ be its [[norm|03AN1V4ZFJ]].

1. For $z = a + b i$, let $\bar z = a - b i$ be its complex conjugate. Then $N(z) = z \bar z$.
2. Complex conjugation is multiplicative: $\overline{z w} = \bar z \, \bar w$. So $N(z w) = z w \bar z \bar w = N(z) N(w)$ for all $z, w \in \Z[i]$.
3. The elements $1, -1, i, -i$ lie in $\Z[i]$. They are [[units|019NFGFPR5]], because $1 \cdot 1 = 1$, $(-1)(-1) = 1$ and $i \cdot (-i) = -i^2 = 1$.
4. Conversely, let $u = a + b i$ be a unit of $\Z[i]$, with $a, b \in \Z$. Then there is $v \in \Z[i]$ with $u v = 1$.
5. By step 2, $N(u) N(v) = N(1) = 1$. Both $N(u)$ and $N(v)$ are nonnegative integers, so $N(u) = 1$.
6. So $a^2 + b^2 = 1$ with $a, b \in \Z$. If $\abs{a} \ge 2$ or $\abs{b} \ge 2$, the sum is at least $4$. So $a, b \in \set{-1, 0, 1}$.
7. The sum $a^2 + b^2$ is $1$ exactly when one of $a, b$ is $0$ and the other is $\pm 1$. So $u \in \set{1, -1, i, -i}$.
8. By steps 3 and 7, the units of $\Z[i]$ are exactly $1$, $-1$, $i$ and $-i$.

## Idea

The norm is multiplicative and takes nonnegative integer values. If $u v = 1$, the norms multiply to $1$, so $N(u) = 1$. The only lattice points at distance $1$ from the origin are $\pm 1$ and $\pm i$.
