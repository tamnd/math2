---
tag: BGTREPJS1V
kind: proof
name: Proof that the Gaussian integers form a Euclidean domain
msc: [11R11]
proves: 0SPYEFH7H4
uses: [0B268GVX95, 00HPT88ZX0, 0GJ2HRG95T, 09S3PFBEPM]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_integer
    locator: Euclidean division
---

## Proof

For a complex number $z = u + vi$, write $\abs{z}^2 = u^2 + v^2$. Recall $\abs{zw}^2 = \abs{z}^2 \abs{w}^2$, and $\abs{\gamma}^2 = N(\gamma)$ for a [[Gaussian integer|0B268GVX95]] $\gamma$, where $N$ is the [[norm|00HPT88ZX0]].

1. Since $\beta \ne 0$, $N(\beta) = \beta\bar\beta$ is a positive integer. So $\dfrac{\alpha}{\beta} = \dfrac{\alpha \bar\beta}{N(\beta)} = s + ti$ with rational numbers $s$ and $t$.
2. Choose integers $m$ and $n$ with $\abs{s - m} \le \frac{1}{2}$ and $\abs{t - n} \le \frac{1}{2}$, for example the nearest integers to $s$ and $t$.
3. Put $q = m + ni$ and $r = \alpha - q\beta$. Both are Gaussian integers, since $\mathbb{Z}[i]$ is closed under sums and products. And $\alpha = q\beta + r$.
4. We have $r = \beta \left(\dfrac{\alpha}{\beta} - q\right) = \beta \big((s - m) + (t - n)i\big)$.
5. So $N(r) = N(\beta) \big((s - m)^2 + (t - n)^2\big) \le N(\beta) \left(\frac{1}{4} + \frac{1}{4}\right) = \frac{1}{2} N(\beta)$.
6. Since $N(\beta) > 0$, this gives $N(r) < N(\beta)$. This proves the division statement.
7. The ring $\mathbb{Z}[i]$ is a subring of the field $\C$. A product of nonzero complex numbers is nonzero, so $\mathbb{Z}[i]$ is an [[integral domain|09S3PFBEPM]].
8. The norm takes nonzero Gaussian integers to positive integers, so it is a function $\mathbb{Z}[i] \setminus \set{0} \to \N$.
9. By steps 3 and 6, for all $\alpha$ and $\beta \ne 0$ there are $q$, $r$ with $\alpha = q\beta + r$ and $r = 0$ or $N(r) < N(\beta)$. So $\mathbb{Z}[i]$ with the norm is a [[Euclidean domain|0GJ2HRG95T]].

## Idea

Divide $\alpha$ by $\beta$ as complex numbers and round the quotient to the nearest lattice point $q$.
The rounding error is a complex number of absolute value at most $\sqrt{2}/2$.
So the remainder $r = \beta(\alpha/\beta - q)$ has norm at most half the norm of $\beta$.
