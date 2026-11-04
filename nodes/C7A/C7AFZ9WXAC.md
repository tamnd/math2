---
tag: C7AFZ9WXAC
kind: proof
name: Proof that there are exactly n nth roots of unity
msc: [11R18]
proves: 0E021GF2B8
uses: [057BH3JC9S, 0CF0XGYHNJ, 0J817RTVG6, 0S61N75H45, 03MTBVG3VE, 04R3CY41VJ, 0WB57D9488, 0FRSR10DWF]
sources:
  - url: https://en.wikipedia.org/wiki/Root_of_unity
    locator: Elementary properties
---

## Proof

1. Let $n \ge 1$, and let $\omega_k = e^{2 \pi i k / n}$ for $0 \le k < n$.
By [[the description of the nth roots of unity|057BH3JC9S]], the $n$th [[roots of unity|0S61N75H45]] are exactly the numbers $\omega_0, \dots, \omega_{n-1}$.
2. It remains to show that these $n$ numbers are distinct.
3. Let $\zeta = e^{2 \pi i / n}$. By [[Euler's formula|04R3CY41VJ]] at real arguments, where the series are the real [[sine and cosine|0WB57D9488]], $\zeta = \cos \frac{2 \pi}{n} + i \sin \frac{2 \pi}{n}$.
4. By [[de Moivre's formula|03MTBVG3VE]] and Euler's formula again, $\zeta^k = \cos \frac{2 \pi k}{n} + i \sin \frac{2 \pi k}{n} = \omega_k$ for $0 \le k < n$.
5. By [[exp(2 pi i/n) is a primitive root of unity|0CF0XGYHNJ]], $\zeta$ is a [[primitive|0J817RTVG6]] $n$th root of unity.
So $\zeta^n = 1$ and $\zeta^j \neq 1$ for $1 \le j < n$.
6. Suppose that $\omega_k = \omega_l$ with $0 \le l < k < n$. By step 4, $\zeta^l \zeta^{k - l} = \zeta^l$, that is, $\zeta^l (\zeta^{k - l} - 1) = 0$.
7. Since $\zeta^n = 1$ and $0^n = 0$, we have $\zeta \neq 0$. So $\zeta^l \neq 0$, because [[$\C$ is a field|0FRSR10DWF]] and a field has no zero divisors.
Indeed, multiplying by the inverse of $\zeta^l$ cancels it.
8. So $\zeta^{k - l} = 1$ with $1 \le k - l < n$. This contradicts step 5.
9. Hence $\omega_0, \dots, \omega_{n-1}$ are $n$ distinct numbers, and by step 1 there are exactly $n$ complex $n$th roots of unity.

## Idea

Every $n$th root of unity is a power $\zeta^k$ of $\zeta = e^{2 \pi i / n}$ with $0 \le k < n$.
If two of these powers were equal, a smaller positive power of $\zeta$ would equal $1$, which primitivity forbids.
