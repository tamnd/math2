---
tag: HM1J3JN5YG
kind: example
name: Cauchy's forward-backward proof of the AM-GM inequality
msc: ["00A35", "26E60"]
topics: [EEH2F76CYQ]
audience: ug2
instance_of: [QC9FKGZH1V]
uses: [0DRF0F3XC9, QC9FKGZH1V, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/AM%E2%80%93GM_inequality
    locator: Proof by Cauchy using forward–backward induction
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Forward-backward induction
---

## Example

We prove the [[inequality of arithmetic and geometric means|0DRF0F3XC9]] by [[forward-backward induction|QC9FKGZH1V]].
Let $n \ge 1$ and let $x_1, \ldots, x_n$ be nonnegative real numbers with mean $A = (x_1 + \cdots + x_n)/n$.
The claim is $\sqrt[n]{x_1 \cdots x_n} \le A$, with equality if and only if $x_1 = \cdots = x_n$.
For each $n \ge 1$, let $P(n)$ be the statement: for all nonnegative reals $x_1, \ldots, x_n$ with mean $A$, we have $x_1 \cdots x_n \le A^n$.
We use one fact twice: for $0 \le a \le b$ and $k \ge 1$, $a^k \le b^k$, with $a^k < b^k$ when $a < b$, because $b^k - a^k = (b - a)(b^{k-1} + b^{k-2} a + \cdots + a^{k-1})$.

Part 1: the inequality.

1. $P(1)$ says $x_1 \le x_1$, which holds.
2. $P(2)$ says $x_1 x_2 \le \left(\frac{x_1 + x_2}{2}\right)^2$. Multiply out: this is $4 x_1 x_2 \le x_1^2 + 2 x_1 x_2 + x_2^2$, that is, $0 \le (x_1 - x_2)^2$, which holds.
3. Forward step: assume $P(n)$, and let $x_1, \ldots, x_{2n} \ge 0$. Let $B$ be the mean of $x_1, \ldots, x_n$ and $C$ the mean of $x_{n+1}, \ldots, x_{2n}$.
4. By $P(n)$ for each half, $x_1 \cdots x_n \le B^n$ and $x_{n+1} \cdots x_{2n} \le C^n$. All four numbers are nonnegative, so the product of the two left sides is at most $B^n C^n = (BC)^n$.
5. By $P(2)$ for $B$ and $C$, $BC \le \left(\frac{B + C}{2}\right)^2$. The fact gives $(BC)^n \le \left(\frac{B + C}{2}\right)^{2n}$.
6. The mean of all $2n$ numbers is $\frac{nB + nC}{2n} = \frac{B + C}{2}$. So steps 4 and 5 give $P(2n)$.
7. By induction on $k$, steps 1 and 3 to 6 give $P(2^k)$ for every $k \ge 0$.
8. Backward step: let $n \ge 2$ and assume $P(n)$. Let $x_1, \ldots, x_{n-1} \ge 0$ have mean $m$, and put $x_n = m$.
9. The mean of $x_1, \ldots, x_n$ is $\frac{(n - 1)m + m}{n} = m$. So $P(n)$ gives $x_1 \cdots x_{n-1} \cdot m \le m^n$.
10. If $m > 0$, divide by $m$: $x_1 \cdots x_{n-1} \le m^{n-1}$. If $m = 0$, all $x_i$ are $0$, because they are nonnegative with sum $0$, and both sides are $0$. This proves $P(n - 1)$.
11. By the validity of forward-backward induction, steps 7 and 10 give $P(n)$ for every $n \ge 1$. For example, $P(5)$ follows from $P(8)$ by three backward steps.
12. Let $G = \sqrt[n]{x_1 \cdots x_n} \ge 0$. If $G > A$, the fact gives $G^n > A^n$, that is, $x_1 \cdots x_n > A^n$, against $P(n)$. So $G \le A$.

Part 2: the case of equality.
Let $E(n)$ be the statement: for all positive reals $x_1, \ldots, x_n$ that are not all equal, $x_1 \cdots x_n < A^n$.

13. If $x_1 = \cdots = x_n = c \ge 0$, then $A = c$ and $x_1 \cdots x_n = c^n = A^n$, so equality holds.
14. $E(2)$: if $x_1 \neq x_2$, then $(x_1 - x_2)^2 > 0$, so the inequality of step 2 is strict.
15. Forward step: assume $E(n)$, and let $x_1, \ldots, x_{2n} > 0$ be not all equal. Then $B, C > 0$. If one half is not constant, $E(n)$ makes one inequality of step 4 strict, and the product is less than $(BC)^n$.
16. If both halves are constant, they have different values $B \neq C$, and $E(2)$ makes the inequality of step 5 strict. In both cases $x_1 \cdots x_{2n} < \left(\frac{B + C}{2}\right)^{2n}$, which is $E(2n)$.
17. Backward step: assume $E(n)$ with $n \ge 3$, and let $x_1, \ldots, x_{n-1} > 0$ be not all equal, with mean $m > 0$. The list $x_1, \ldots, x_{n-1}, m$ is not constant, so $E(n)$ gives $x_1 \cdots x_{n-1} \cdot m < m^n$, and division by $m$ gives $E(n - 1)$.
18. Forward-backward induction from $E(2)$, with $S$ the powers of $2$ from $2$ on, gives $E(n)$ for every $n \ge 2$.
19. If the $x_i$ are not all equal and some $x_i$ is $0$, then some $x_j > 0$, so $A > 0$ and $x_1 \cdots x_n = 0 < A^n$.
20. By steps 18 and 19, the product is less than $A^n$ whenever the $x_i$ are not all equal. Then $G < A$ by the fact, and with step 13, equality holds exactly when all $x_i$ are equal.

For the numbers $1, 2, 6$, the geometric mean is $\sqrt[3]{12} \approx 2.29$ and the arithmetic mean is $3$.

## Remarks

1. The forward step uses the case $2$ twice: once inside each half, through $P(n)$, and once for the two means $B$ and $C$.
2. The backward step works because adding the mean of a list to the list does not change the mean.
3. The other [[proof by induction|8EJJF9T071]] goes from $n$ to $n + 1$ directly, by replacing two numbers on both sides of the mean. It is shorter to state but harder to find.
4. Part 2 is a second forward-backward induction, for the strict inequality. It starts at $n = 2$, because the case $n = 1$ has no list of unequal numbers.

## Explanations

### L1 human

The arithmetic mean of some numbers is their sum divided by how many there are.
The geometric mean is the root of their product: for $2$ and $8$, it is $\sqrt{16} = 4$, while the arithmetic mean is $5$.
The inequality says that the geometric mean is never larger than the arithmetic mean.
Cauchy first proved this for $2$ numbers, then for $4$, $8$, $16$, and so on, by putting two groups together.
Then he showed that if it holds for some number of terms, it also holds for one term fewer.
This fills the gaps: for example, $5$ terms come from $8$ terms after three steps down.

### L2 human

We follow the forward step for the four numbers $1, 4, 2, 8$.

1. The first half $1, 4$ has mean $B = 2.5$, and $1 \cdot 4 = 4 \le 2.5^2 = 6.25$.
2. The second half $2, 8$ has mean $C = 5$, and $2 \cdot 8 = 16 \le 5^2 = 25$.
3. So $1 \cdot 4 \cdot 2 \cdot 8 = 64 \le (BC)^2 = 12.5^2 = 156.25$.
4. The case $2$ for $B$ and $C$ gives $BC = 12.5 \le 3.75^2 = 14.0625$.
5. So $64 \le 156.25 \le 14.0625^2 = 3.75^4 \approx 197.75$, and $3.75$ is the mean of all four numbers.

The typical use of this proof is as a model: an inequality that is easy for two terms and that combines well under doubling.
A trap is to forget the case $m = 0$ in the backward step, where the division is not allowed.
