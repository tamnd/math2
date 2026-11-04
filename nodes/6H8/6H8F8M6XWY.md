---
tag: 6H8F8M6XWY
kind: proof
name: Proof that the Gaussian integers are a Euclidean domain
msc: [11R11]
proves: 0PN13BB7BT
uses: [0K5W69AC0J, 03AN1V4ZFJ, 09S3PFBEPM, 0GJ2HRG95T]
sources:
  - url: https://proofwiki.org/wiki/Gaussian_Integers_form_Euclidean_Domain
---

## Proof

Let $\Z[i]$ be the ring of [[Gaussian integers|0K5W69AC0J]] and let $N(a + b i) = a^2 + b^2$ be its [[norm|03AN1V4ZFJ]]. For $u \in \C$, $\abs{u}$ is the absolute value.

1. The ring $\Z[i]$ is a subring of the field $\C$, so it is an [[integral domain|09S3PFBEPM]].
2. For $z \in \Z[i]$, $N(z) = \abs{z}^2$ is a natural number. If $z \neq 0$, then $N(z) \ge 1$.
3. Let $z, w \in \Z[i]$ with $w \neq 0$. In $\C$, write $z / w = x + y i$ with $x, y \in \R$.
4. Let $m = \floor{x + \tfrac12}$ and $n = \floor{y + \tfrac12}$. Then $m, n \in \Z$, $\abs{x - m} \le \tfrac12$ and $\abs{y - n} \le \tfrac12$.
5. Put $q = m + n i \in \Z[i]$ and $r = z - q w$. Since $\Z[i]$ is a ring, $r \in \Z[i]$, and $z = q w + r$.
6. In $\C$, $r = w (z/w - q)$. So $\abs{r} = \abs{w} \, \abs{(x - m) + (y - n) i}$.
7. Squaring gives $N(r) = N(w) \big((x - m)^2 + (y - n)^2\big) \le N(w) \big(\tfrac14 + \tfrac14\big) = \tfrac12 N(w)$.
8. Since $N(w) \ge 1$ by step 2, $\tfrac12 N(w) < N(w)$. So $N(r) < N(w)$.
9. In particular, $r = 0$ or $N(r) < N(w)$. With steps 1 and 2, $\Z[i]$ is a [[Euclidean domain|0GJ2HRG95T]] with Euclidean function $N$.

## Idea

Divide in $\C$ and round the real and imaginary parts of $z/w$ to the nearest integers. The rounding error is a complex number of absolute value at most $1/\sqrt{2}$. Multiplying back by $w$ gives a remainder with at most half the norm of $w$.
