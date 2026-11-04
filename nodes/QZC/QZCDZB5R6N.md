---
tag: QZCDZB5R6N
kind: proof
name: Proof that the exponential of a sum of commuting matrices is the product of the exponentials
msc: [15A16]
proves: 04BD23PSK5
uses: [0K665H5V1S, 0EHWPWGHB2, 06JZGMYTYD, 0E8HNVBCSP, 07XBM3A9J5]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_exponential
    locator: Elementary properties
---

## Proof

We compare partial sums and bound the difference with a matrix norm. The binomial theorem is where $A B = B A$ enters.

1. For an $n \times n$ matrix $X = (x_{ij})$ over $\mathbb{K}$, let $\norm{X} = n \max_{i,j} \abs{x_{ij}}$. Then $\abs{x_{ij}} \le \norm{X}$, $\norm{X + Y} \le \norm{X} + \norm{Y}$ and $\norm{c X} = \abs{c} \norm{X}$ for $c \in \mathbb{K}$.
2. For matrices $X, Y$, each entry of $X Y$ satisfies $\abs{\sum_l x_{il} y_{lj}} \le n \max \abs{x_{il}} \max \abs{y_{lj}}$. Multiplying by $n$ gives $\norm{X Y} \le \norm{X} \norm{Y}$. By induction, $\norm{X^k} \le \norm{X}^k$ for $k \ge 1$.
3. Let $S_N(X) = \sum_{k=0}^{N} X^k / k!$. By the [[definition of the matrix exponential|0K665H5V1S]], each entry of $S_N(X)$ tends to the matching entry of $e^X$ as $N \to \infty$.
4. The finite sums $\sum c_{jk} A^j B^k$ with $c_{jk} \in \mathbb{K}$ form a subring of the ring of matrices. It is commutative, because $A B = B A$. So the [[binomial theorem|0EHWPWGHB2]] applies: $(A + B)^m = \sum_{k=0}^{m} \binom{m}{k} A^k B^{m-k}$.
5. Dividing by $m!$ and summing over $m \le N$ gives $S_N(A + B) = \sum_{k + l \le N} \frac{A^k B^l}{k! \, l!}$, where $k, l \ge 0$.
6. Expanding the product gives $S_N(A) S_N(B) = \sum_{k \le N, \, l \le N} \frac{A^k B^l}{k! \, l!}$.
7. Let $T_N$ be the set of pairs $(k, l)$ with $k \le N$, $l \le N$ and $k + l > N$. By steps 5 and 6, $\Delta_N = S_N(A) S_N(B) - S_N(A + B) = \sum_{(k,l) \in T_N} \frac{A^k B^l}{k! \, l!}$.
8. Let $a = \norm{A}$ and $b = \norm{B}$. For $(k, l) \in T_N$, $k$ and $l$ are not both $0$. Steps 1 and 2 then give $\norm{A^k B^l} \le a^k b^l$. When $k = 0$ or $l = 0$, the factor $I_n$ is simply left out.
9. By steps 1, 7 and 8, $\norm{\Delta_N} \le \sum_{(k,l) \in T_N} \frac{a^k b^l}{k! \, l!}$.
10. Let $s_N(x) = \sum_{k=0}^{N} x^k / k!$ for real $x$. Steps 5 to 7 hold for the commuting real numbers $a$ and $b$ too. So the right side of step 9 equals $s_N(a) s_N(b) - s_N(a + b)$.
11. By the [[power series of the exponential function|06JZGMYTYD]], $s_N(x) \to e^x$ for each real $x$. So the right side of step 9 tends to $e^a e^b - e^{a+b}$, which is $0$ by the [[exponential of a sum|0E8HNVBCSP]].
12. By steps 1, 9 and 11, each entry of $\Delta_N$ tends to $0$.
13. Entry $(i, j)$ of $S_N(A) S_N(B)$ is $\sum_l S_N(A)_{il} S_N(B)_{lj}$, a finite sum of products. By step 3 and the [[algebra of limits|07XBM3A9J5]], it tends to $\sum_l (e^A)_{il} (e^B)_{lj}$, the entry $(i, j)$ of $e^A e^B$.
14. By step 3, entry $(i, j)$ of $S_N(A + B)$ tends to entry $(i, j)$ of $e^{A+B}$.
15. By steps 7, 13 and 14, entry $(i, j)$ of $\Delta_N$ tends to entry $(i, j)$ of $e^A e^B - e^{A+B}$. By step 12, this entry is $0$.
16. Hence $e^{A+B} = e^A e^B$.

## Idea

Because $A$ and $B$ commute, $(A + B)^m$ expands by the binomial theorem, exactly as for numbers. Then the partial sums of $e^{A+B}$ and of $e^A e^B$ differ only by the terms $A^k B^l / (k! \, l!)$ with $k + l > N$. A submultiplicative norm bounds this tail by the same tail for the real numbers $\norm{A}$ and $\norm{B}$, which tends to $0$.
