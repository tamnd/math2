---
tag: QZKW59K1HH
kind: definition
name: Wynn's epsilon algorithm
msc: [65B05, 65B10, 40A25]
defines: 6X0C4HNMAZ
uses: [0QE8STGJH2, S6E3H24FGB]
sources:
  - url: https://en.wikipedia.org/wiki/Shanks_transformation
---

## Definition

Let $(A_n)_{n \ge 0}$ be a [[sequence|0QE8STGJH2]] of real or complex numbers.
*Wynn's epsilon algorithm* defines numbers $\varepsilon_k^{(n)}$ for $k \ge -1$ and $n \ge 0$ by
$$\varepsilon_{-1}^{(n)} = 0, \qquad \varepsilon_0^{(n)} = A_n, \qquad \varepsilon_{k+1}^{(n)} = \varepsilon_{k-1}^{(n+1)} + \frac{1}{\varepsilon_k^{(n+1)} - \varepsilon_k^{(n)}},$$
as long as no denominator is $0$.
The even entries are the values of the [[Shanks transformation|S6E3H24FGB]]: $\varepsilon_{2k}^{(n)} = e_k(A_{n+k})$.
The odd entries are auxiliary quantities.

## Remarks

Check for $k = 1$: $\varepsilon_1^{(n)} = \frac{1}{\Delta A_n}$, where $\Delta A_n = A_{n+1} - A_n$, and
$$\varepsilon_2^{(n)} = A_{n+1} + \frac{1}{\frac{1}{\Delta A_{n+1}} - \frac{1}{\Delta A_n}} = A_{n+1} - \frac{\Delta A_n \Delta A_{n+1}}{\Delta A_{n+1} - \Delta A_n},$$
which equals $S(A_{n+1}) = \frac{A_{n+2}A_n - A_{n+1}^2}{A_{n+2} - 2A_{n+1} + A_n}$.
Example: for $A_0 = 1$, $A_1 = \frac23$, $A_2 = \frac{13}{15}$ one gets $\varepsilon_1^{(0)} = -3$, $\varepsilon_1^{(1)} = 5$ and $\varepsilon_2^{(0)} = \frac23 + \frac18 = \frac{19}{24}$.
Non-example: for a constant sequence $A_n = c$ already $\varepsilon_1^{(n)} = \frac{1}{0}$ is undefined; in practice the algorithm stops when two neighbouring entries agree.

## Explanations

### L1 human

Each new entry comes from the entry two columns back and the difference of two entries one column back.
