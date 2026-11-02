---
tag: DCJTJXN3SR
kind: definition
name: Favard constant
msc: [41A44, 42A10, 41A17]
defines: 9K1W9Q49NR
uses: []
sources:
  - url: https://en.wikipedia.org/wiki/Favard_constant
---

## Definition

For an integer $r \ge 0$, the *Favard constant* $K_r$ is the number
$$K_r = \frac{4}{\pi} \sum_{k=0}^{\infty} \left(\frac{(-1)^k}{2k + 1}\right)^{r + 1}.$$

## Remarks

The series converges for every $r \ge 0$: for $r = 0$ it is an alternating series, and for $r \ge 1$ it converges absolutely.

Example: $K_0 = \frac{4}{\pi} \left(1 - \frac{1}{3} + \frac{1}{5} - \cdots\right) = \frac{4}{\pi} \cdot \frac{\pi}{4} = 1$.
Likewise $K_1 = \frac{4}{\pi} \sum_{k \ge 0} \frac{1}{(2k+1)^2} = \frac{4}{\pi} \cdot \frac{\pi^2}{8} = \frac{\pi}{2}$.
Further values are $K_2 = \pi^2/8$ and $K_3 = \pi^3/24$.

Non-example: $\frac{4}{\pi} \sum_{k \ge 0} \frac{1}{2k + 1}$ is not a Favard constant; it lacks the signs of the case $r = 0$ and the series diverges.

The even-indexed constants increase and the odd-indexed constants decrease, and both tend to $4/\pi$.
So $1 = K_0 < K_2 < K_4 < \cdots < \frac{4}{\pi} < \cdots < K_3 < K_1 = \frac{\pi}{2}$.
