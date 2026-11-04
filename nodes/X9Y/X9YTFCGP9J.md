---
tag: X9YTFCGP9J
kind: proof
name: Proof that an algebraic extension of an algebraic extension is algebraic
msc: [12F05]
proves: 0TPWS0K1BC
uses: [09EYMKMSB9, 0NPW1DWECM, 0GK1WB9R98, 0N5QW9K7MH, 0A7KJ68XHT, 0DFYTNZ6AM, 0NRYPM9Y27, 0MA5B744K3]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Corollary 1.31
---

## Proof

1. Let $K \subseteq L \subseteq M$ be fields with $M/L$ and $L/K$ [[algebraic|09EYMKMSB9]]. Let $a \in M$. We show that $a$ is [[algebraic|0NPW1DWECM]] over $K$.
2. Since $a$ is algebraic over $L$, it has a [[minimal polynomial|0GK1WB9R98]] $m = x^n + c_{n-1} x^{n-1} + \dots + c_0$ over $L$, with $c_i \in L$.
3. Let $E_0 = K$, and for $1 \le i \le n$ let $E_i = E_{i-1}(c_{i-1})$, the [[subfield of $M$ generated|0MA5B744K3]] by $E_{i-1}$ and $c_{i-1}$. Then $K = E_0 \subseteq E_1 \subseteq \dots \subseteq E_n \subseteq M$.
4. Each $c_{i-1}$ is algebraic over $K$, since $L/K$ is algebraic. A nonzero polynomial over $K$ with root $c_{i-1}$ is also one over $E_{i-1}$. So $c_{i-1}$ is algebraic over $E_{i-1}$.
5. By the [[degree of a simple extension|0N5QW9K7MH]], $[E_i : E_{i-1}]$ equals the degree of the minimal polynomial of $c_{i-1}$ over $E_{i-1}$. So it is finite.
6. All coefficients of $m$ lie in $E_n$, so $m \in E_n[x]$ is nonzero with $m(a) = 0$. So $a$ is algebraic over $E_n$, and $[E_n(a) : E_n]$ is finite by the same result.
7. By the [[tower law|0A7KJ68XHT]], applied $n$ times, $[E_n(a) : K] = [E_n(a) : E_n] \cdot [E_n : E_{n-1}] \cdots [E_1 : E_0]$. This is a product of finitely many finite numbers, so it is finite.
8. So $E_n(a)/K$ is a [[finite extension|0NRYPM9Y27]]. Since [[finite extensions are algebraic|0DFYTNZ6AM]], the element $a \in E_n(a)$ is algebraic over $K$.
9. Since $a \in M$ was arbitrary, $M/K$ is algebraic.

## Idea

The element $a$ satisfies a polynomial with only finitely many coefficients from $L$. Adjoining these coefficients to $K$ gives a finite extension, and $a$ is algebraic over it. The tower law then makes the whole extension containing $a$ finite over $K$, and finite extensions are algebraic.
