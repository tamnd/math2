---
tag: 3ENC7Y5VBE
kind: proof
name: Proof of Morera's theorem by a local primitive
msc: ["30E20"]
proves: 0VDD7W0EKZ
uses: [00FWNP9TXY, 0DG0Z72CQD, 0D1C9Y1EXA, 0D37QFPEZE, 0DJMGPN8K9, 0QEBN8DGVE]
sources:
  - url: https://en.wikipedia.org/wiki/Morera%27s_theorem
    locator: Proof
---

## Proof

1. Let $U \subseteq \C$ be open and let $f : U \to \C$ be continuous. Assume $\oint_{\partial T} f(z) \, dz = 0$ for each closed triangle $T \subseteq U$.
2. For $a, b \in \C$, let $[a, b]$ be the segment path $t \mapsto a + t(b - a)$, $t \in [0, 1]$. All integrals below are [[contour integrals|00FWNP9TXY]].
3. Reversing a segment changes the sign: $\int_{[b, a]} f = -\int_{[a, b]} f$. This follows from the [[substitution|0D37QFPEZE]] $t \mapsto 1 - t$.
4. Fix $c \in U$ and $R > 0$ with $B = \set{z : \abs{z - c} < R} \subseteq U$. It suffices to show that $f$ is [[holomorphic|0DG0Z72CQD]] on each such disc $B$.
5. For $z \in B$, define $F(z) = \int_{[c, z]} f(w) \, dw$. The segment $[c, z]$ lies in $B$ because $B$ is convex.
6. Let $z \in B$ and let $h \ne 0$ with $z + h \in B$. The triangle $T$ with vertices $c$, $z$, $z + h$ lies in $B$, by convexity.
7. Claim: $\int_{[c, z]} f + \int_{[z, z + h]} f + \int_{[z + h, c]} f = 0$. If the vertices are not collinear, the left side is $\pm \oint_{\partial T} f$, so it is $0$ by step 1.
8. If the vertices are collinear, they lie on a line $s \mapsto c + s u$ with $\abs{u} = 1$. By substitution, each segment integral becomes $\int f(c + s u) \, u \, ds$ over an interval of $s$. The three intervals add to zero by additivity of the integral, which proves the claim.
9. By steps 3 and 7, $F(z + h) - F(z) = \int_{[z, z + h]} f(w) \, dw$.
10. Also $\int_{[z, z + h]} f(z) \, dw = \int_0^1 f(z) \, h \, dt = f(z) \, h$. So $$\frac{F(z + h) - F(z)}{h} - f(z) = \frac{1}{h} \int_{[z, z + h]} \bigl( f(w) - f(z) \bigr) \, dw.$$
11. Let $\varepsilon > 0$. Since $f$ is continuous at $z$, there is $\delta > 0$ with $\abs{f(w) - f(z)} < \varepsilon$ for $\abs{w - z} < \delta$.
12. For $0 < \abs{h} < \delta$, each $w$ on $[z, z + h]$ satisfies $\abs{w - z} < \delta$. The segment has length $\abs{h}$.
13. By the [[estimation lemma|0DJMGPN8K9]] and step 12, the right side of step 10 has modulus at most $\frac{1}{\abs{h}} \cdot \varepsilon \abs{h} = \varepsilon$.
14. So $F$ is [[complex differentiable|0D1C9Y1EXA]] at $z$ with $F'(z) = f(z)$. Thus $F$ is holomorphic on $B$ and $F' = f$ there.
15. By [[holomorphic functions are infinitely differentiable|0QEBN8DGVE]], $F'$ is holomorphic on $B$. So $f$ is holomorphic on $B$.
16. Each point of $U$ lies in such a disc $B$. So $f$ is complex differentiable at each point of $U$, and $f$ is holomorphic on $U$.

## Idea

On a disc, integrating $f$ along segments from the center gives a function $F$. The triangle condition makes the difference $F(z + h) - F(z)$ an integral over the short segment from $z$ to $z + h$, so continuity of $f$ gives $F' = f$. The derivative of a holomorphic function is holomorphic, so $f$ is holomorphic.
