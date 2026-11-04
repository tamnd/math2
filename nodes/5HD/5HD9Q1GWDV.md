---
tag: 5HD9Q1GWDV
kind: proof
name: Proof of Fubini's theorem for Riemann integrals on a rectangle
msc: ["26B15"]
proves: 0R0T1VWH5X
uses: [0NKBMFC18R, 0P4WX7Y502, 0QRQVH0CRW, 09FQT057T7, 021XJAQVDC, 05RCDKHZM6, 0MBWQKM8QR, 06SESV7GQY, 07PFYV65MB, 06B8BNJCD6, 0V4DET59NW, 0S9EK5MQPE]
sources:
  - url: https://www.jirka.org/ra/html/sec_iteratedints.html
    locator: Theorem 10.2.2
---

## Proof

We compare lower and upper sums of $f$ on a grid with the Darboux sums of the inner integral.

1. Let $R$ and $f$ be as in the statement. By the definition of the [[double integral|0NKBMFC18R]], $f$ is bounded, say $\abs{f} \le B$. Let $I = \iint_R f \, dA$, and let $F(x) = \int_c^d f(x, y) \, dy$ for $x \in [a, b]$.
2. Take partitions $a = x_0 < \dots < x_k = b$ and $c = y_0 < \dots < y_l = d$, with rectangles $R_{ij} = [x_{i-1}, x_i] \times [y_{j-1}, y_j]$. Let $m_{ij} = \inf_{R_{ij}} f$ and $M_{ij} = \sup_{R_{ij}} f$. Let $L = \sum_{i,j} m_{ij} \Delta A_{ij}$ and $U = \sum_{i,j} M_{ij} \Delta A_{ij}$.
3. Each Riemann sum $S$ of $f$ for this grid satisfies $L \le S \le U$. For each $\eta > 0$, there are Riemann sums $S$ with $S < L + \eta$, and others with $S > U - \eta$. Choose the points $p_{ij}$ with $f(p_{ij})$ close to $m_{ij}$, or close to $M_{ij}$.
4. Fix $i$ and $x \in [x_{i-1}, x_i]$. For $y \in [y_{j-1}, y_j]$ we have $m_{ij} \le f(x, y) \le M_{ij}$.
5. The function $y \mapsto f(x, y)$ is integrable on $[c, d]$. By [[additivity over intervals|05RCDKHZM6]], it is integrable on each $[y_{j-1}, y_j]$, and $F(x)$ is the sum of these integrals.
6. By [[monotonicity of the integral|0MBWQKM8QR]] and step 4, $m_{ij} (y_j - y_{j-1}) \le \int_{y_{j-1}}^{y_j} f(x, y) \, dy \le M_{ij} (y_j - y_{j-1})$. Summing over $j$ gives $\sum_j m_{ij} (y_j - y_{j-1}) \le F(x) \le \sum_j M_{ij} (y_j - y_{j-1})$.
7. In particular $\abs{F(x)} \le B (d - c)$, so $F$ is bounded. Let $P = (x_0, \dots, x_k)$. Taking the infimum and the supremum of step 6 over $x \in [x_{i-1}, x_i]$, and summing over $i$, gives $L \le L(F, P) \le U(F, P) \le U$. Here $L(F, P)$ and $U(F, P)$ are the [[Darboux sums|0QRQVH0CRW]] of $F$.
8. Let $\underline{J}$ and $\overline{J}$ be the lower and upper [[Darboux integrals|09FQT057T7]] of $F$. Then $L(F, P) \le \underline{J}$ and $\overline{J} \le U(F, P)$. Also $\underline{J} \le \overline{J}$, since every lower sum is at most every upper sum (compare both with a common refinement).
9. We now prove the first equality. Let $\varepsilon > 0$. Since $f$ is integrable, there is $\delta > 0$ with $\abs{S - I} < \varepsilon$ for all Riemann sums $S$ whose rectangles have diameter less than $\delta$.
10. Choose the grid of step 2 with all diameters less than $\delta$. By step 3, $L \ge I - \varepsilon$ and $U \le I + \varepsilon$. By steps 7 and 8, $I - \varepsilon \le \underline{J} \le \overline{J} \le I + \varepsilon$.
11. Since $\varepsilon$ was arbitrary, $\underline{J} = \overline{J} = I$. By the theorem that [[Darboux and Riemann integrals agree|021XJAQVDC]], $F$ is integrable and $\int_a^b F(x) \, dx = I$.
12. This says that the [[iterated integral|0P4WX7Y502]] $\int_a^b \int_c^d f(x, y) \, dy \, dx$ exists and equals $\iint_R f \, dA$.
13. Exchange the roles of $x$ and $y$ in steps 2 to 11. This uses the hypothesis that $x \mapsto f(x, y)$ is integrable for each $y$. It gives $\int_c^d \int_a^b f(x, y) \, dx \, dy = \iint_R f \, dA$.
14. Now let $f$ be [[continuous|0S9EK5MQPE]] on $R$. The rectangle $R$ is closed and bounded, so it is compact by the [[Heine–Borel theorem|07PFYV65MB]]. So $f$ is bounded by the [[extreme value theorem|0V4DET59NW]].
15. For each $x$, the function $y \mapsto f(x, y)$ is continuous on $[c, d]$, so it is [[integrable|06SESV7GQY]]. In the same way, each $x \mapsto f(x, y)$ is integrable. So steps 2 to 8 apply.
16. By the [[Heine–Cantor theorem|06B8BNJCD6]], $f$ is uniformly continuous on $R$. Let $\varepsilon > 0$. There is $\delta > 0$ with $\abs{f(p) - f(q)} < \varepsilon$ when $\norm{p - q} < \delta$.
17. For a grid whose rectangles have diameter less than $\delta$, we get $M_{ij} - m_{ij} \le \varepsilon$. So $U - L \le \varepsilon (b - a)(d - c)$.
18. By steps 7 and 8, $\overline{J} - \underline{J} \le \varepsilon (b - a)(d - c)$ for each $\varepsilon > 0$. So $\underline{J} = \overline{J}$, and $F$ is integrable. Let $I_0 = \int_a^b F(x) \, dx$. Then $L \le I_0 \le U$ for each such grid.
19. Each Riemann sum $S$ for such a grid also satisfies $L \le S \le U$, by step 3. So $\abs{S - I_0} \le U - L \le \varepsilon (b - a)(d - c)$.
20. Hence $f$ is Riemann integrable on $R$, with $\iint_R f \, dA = I_0$. So all hypotheses of the theorem hold, and the two equalities follow from steps 12 and 13.

## Idea

On a fine grid, the lower and upper sums of $f$ are close to the double integral. On each vertical strip, the inner integral $F(x)$ is squeezed between the column sums of the infima and suprema of $f$. So the Darboux sums of $F$ are squeezed between the lower and upper sums of $f$, and $F$ integrates to the double integral.
