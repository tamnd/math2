---
tag: J3PN78KXPF
kind: proof
name: Proof of Rouché's theorem by the argument principle and continuity
msc: [30C15]
proves: 0D430QR02W
uses: [0DG0Z72CQD, 0NSD1TPHR0, 0C9S13WKMF, 07PFYV65MB, 0V4DET59NW, 0QEBN8DGVE, 064N002TX4, 0PN2BXRS8G, 0DJMGPN8K9, 0T7ABX4CWE]
sources:
  - url: https://en.wikipedia.org/wiki/Rouch%C3%A9%27s_theorem
    locator: Proof of the symmetric form of Rouché's theorem
---

## Proof

1. Let $f$ and $g$ be [[holomorphic|0DG0Z72CQD]] on an open set $W$ that contains $\set{z : \abs{z - c} \le r}$. Let $C$ be the circle $\abs{z - c} = r$, and assume $\abs{g} < \abs{f}$ on $C$.
2. For $t \in [0, 1]$, let $F_t = f + t g$. It is holomorphic on $W$, so it is [[meromorphic|0NSD1TPHR0]] on $W$ with no poles.
3. On $C$, the [[reverse triangle inequality|0C9S13WKMF]] gives $\abs{F_t} \ge \abs{f} - t \abs{g} \ge \abs{f} - \abs{g}$.
4. The circle $C$ is compact by the [[Heine–Borel theorem|07PFYV65MB]]. By [[attainment of bounds|0V4DET59NW]], $\abs{f} - \abs{g}$ has a minimum $m$ on $C$, and $m > 0$ by hypothesis. So $\abs{F_t} \ge m$ on $C$.
5. Let $Z(t)$ be the number of zeros of $F_t$ in $\abs{z - c} < r$, counted with [[order|064N002TX4]]. By step 4 and the [[argument principle|0PN2BXRS8G]], $Z(t) = \frac{1}{2\pi i} \oint_C \frac{F_t'}{F_t} \, dz$, a [[circle integral|0T7ABX4CWE]]. In particular $Z(t)$ is an integer.
6. For $s, t \in [0, 1]$, a direct expansion gives $(f' + t g')(f + s g) - (f' + s g')(f + t g) = (t - s)(g' f - f' g)$.
7. Dividing by $F_t F_s$ gives $\frac{F_t'}{F_t} - \frac{F_s'}{F_s} = \frac{(t - s)(g' f - f' g)}{F_t F_s}$ on $C$.
8. By [[holomorphic functions are infinitely differentiable|0QEBN8DGVE]], $f'$ and $g'$ are holomorphic, hence continuous. So $\abs{g' f - f' g}$ has a maximum $K_0$ on $C$.
9. By steps 4 and 7, $\abs{F_t'/F_t - F_s'/F_s} \le \abs{t - s} K_0 / m^2$ on $C$. The length of $C$ is $2\pi r$.
10. By the [[estimation lemma|0DJMGPN8K9]] and step 5, $\abs{Z(t) - Z(s)} \le \frac{1}{2\pi} \cdot 2\pi r \cdot \frac{\abs{t - s} K_0}{m^2} = \frac{r K_0}{m^2} \abs{t - s}$.
11. Choose an integer $q \ge 1$ with $q > r K_0 / m^2$, and let $t_j = j/q$ for $j = 0, \dots, q$. By step 10, $\abs{Z(t_{j+1}) - Z(t_j)} < 1$.
12. Since the values of $Z$ are integers, $Z(t_{j+1}) = Z(t_j)$ for each $j$. Hence $Z(0) = Z(1)$.
13. Here $F_0 = f$ and $F_1 = f + g$. So $f$ and $f + g$ have the same number of zeros in $\abs{z - c} < r$, counted with order.

## Idea

Move continuously from $f$ to $f + g$ through $f + t g$. The condition $\abs{g} < \abs{f}$ on the circle keeps every $f + t g$ away from zero there. So the argument principle counts the zeros of each $f + t g$ by an integral that depends continuously on $t$. An integer that varies continuously cannot change.
