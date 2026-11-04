---
tag: GAJVSVCX74
kind: proof
name: Proof of Riemann's criterion for integrability
msc: [26A42]
proves: 017DH8WXTE
uses: [021XJAQVDC, 09FQT057T7, 0QRQVH0CRW, 0EEKF7YFBW, 0BTMQ04556, 04KFTA34C5, 0N1JQXZXHC]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.14
---

## Proof

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be bounded. Write $U(P)$ and $L(P)$ for the upper and lower [[Darboux sums|0QRQVH0CRW]] of $f$, and $U^*$ and $L^*$ for the upper and lower [[Darboux integrals|09FQT057T7]].

1. Let $R$ be a [[refinement|0EEKF7YFBW]] of a partition $Q$. Each subinterval of $R$ lies in exactly one subinterval $J$ of $Q$, and the subintervals of $R$ inside $J$ have total length $|J|$.
2. On a smaller set the [[supremum|0BTMQ04556]] is no larger and the [[infimum|04KFTA34C5]] is no smaller. Grouping the terms by step 1 gives $U(R) \le U(Q)$ and $L(R) \ge L(Q)$.
3. For any partitions $P$ and $Q$, let $R$ consist of the points of both. Then $L(P) \le L(R) \le U(R) \le U(Q)$ by step 2, since $m_i \le M_i$ on each subinterval.
4. Taking the supremum over $P$ and then the infimum over $Q$ in step 3 gives $L^* \le U^*$.

First assume that $f$ is [[Riemann integrable|0N1JQXZXHC]], with integral $I$.

5. By the theorem that [[Darboux and Riemann integrals agree|021XJAQVDC]], $L^* = U^* = I$.
6. Let $\varepsilon > 0$. The number $I + \varepsilon/2$ is not a lower bound of the upper sums, so there is $P_1$ with $U(P_1) < I + \varepsilon / 2$. In the same way, there is $P_2$ with $L(P_2) > I - \varepsilon/2$.
7. Let $P$ consist of the points of $P_1$ and $P_2$. By step 2, $U(P) - L(P) \le U(P_1) - L(P_2) < \varepsilon$.

Now assume that for each $\varepsilon > 0$ there is a partition $P$ with $U(P) - L(P) < \varepsilon$.

8. Let $\varepsilon > 0$ and take such a $P$. By the definitions of $L^*$ and $U^*$ and by step 4, $L(P) \le L^* \le U^* \le U(P)$.
9. So $0 \le U^* - L^* \le U(P) - L(P) < \varepsilon$. This holds for every $\varepsilon > 0$, so $U^* = L^*$.
10. By the theorem that [[Darboux and Riemann integrals agree|021XJAQVDC]], $f$ is Riemann integrable on $[a, b]$.

## Idea

The upper and lower Darboux integrals are squeezed between $L(P)$ and $U(P)$ for every partition $P$. So they are equal exactly when the gap $U(P) - L(P)$ can be made as small as we like. Equality of the Darboux integrals is the same as Riemann integrability.
