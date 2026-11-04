---
tag: D5VNWBM9F1
kind: proof
name: Proof of the uniqueness of the derivative
msc: [26B05]
proves: 0762WAE49P
uses: [08EVNYZF42, 0MN882VJ4P, 01ZQQDCERP, 0DC3MPR7C9, 0FJZMBX0ZZ]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.3.2
---

## Proof

We show that $(A - B) v = 0$ for each $v \in V$.

1. Let $V$, $W$, $U$, $f$, $x$, $A$ and $B$ be as in the statement. For $h \in V$ with $x + h \in U$, put $r_A(h) = f(x + h) - f(x) - A h$ and $r_B(h) = f(x + h) - f(x) - B h$.
2. Subtracting the two definitions gives $(A - B) h = r_B(h) - r_A(h)$.
3. Let $\varepsilon > 0$. Both $A$ and $B$ are [[Fréchet derivatives|08EVNYZF42]] of $f$ at $x$. By the [[little-o form of the derivative|0MN882VJ4P]], there is $\delta > 0$ with $\|r_A(h)\| \le \varepsilon \|h\|$ and $\|r_B(h)\| \le \varepsilon \|h\|$. This holds for $\|h\| < \delta$ with $x + h \in U$. We take $\delta$ as the smaller of the two numbers given by $A$ and by $B$.
4. Since $U$ is [[open|01ZQQDCERP]], there is $\rho > 0$ such that the [[open ball|0DC3MPR7C9]] $B(x, \rho)$ lies in $U$.
5. Let $v \in V$. If $v = 0$, then $(A - B) v = 0$. So suppose that $v \ne 0$. Fix $\varepsilon > 0$, and take $\delta$ as in step 3.
6. Choose a real $t > 0$ with $t \|v\| < \min(\delta, \rho)$, and put $h = t v$. Then $\|h\| < \rho$, so $x + h \in U$. Also $\|h\| < \delta$.
7. By steps 2 and 3 and the [[triangle inequality|0FJZMBX0ZZ]], $t \|(A - B) v\| = \|(A - B) h\| \le \|r_B(h)\| + \|r_A(h)\| \le 2 \varepsilon t \|v\|$.
8. Dividing by $t > 0$ gives $\|(A - B) v\| \le 2 \varepsilon \|v\|$.
9. This holds for each $\varepsilon > 0$, so $\|(A - B) v\| = 0$ and $A v = B v$.
10. As $v$ was arbitrary, $A = B$.

## Idea

The difference of two good linear approximations is a linear map whose values are tiny compared with $\|h\|$. Scaling a fixed vector $v$ down to a short step $t v$ and back up shows that this linear map vanishes on $v$. Openness of $U$ is what lets us step from $x$ in every direction.
