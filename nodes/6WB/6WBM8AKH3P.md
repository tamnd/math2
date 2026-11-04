---
tag: 6WBM8AKH3P
kind: proof
name: Proof of the chain rule in several variables
msc: [26B05]
proves: 0EAAS2EHDR
uses: [0135XZZQ8M, 08EVNYZF42, 0MN882VJ4P, 0C13E623WD, 0F3K4C7XYW, 0THBK9V825, 05YBKMRVAR, 0FJZMBX0ZZ]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Theorem 8.3.7
---

## Proof

We write both maps as linear approximations plus errors in little-o form, and we substitute one into the other.

1. Let $U$, $W$, $g$, $f$ and $a$ be as in the statement. Put $b = g(a)$, $A = Dg(a)$ and $B = Df(b)$.
2. By [[linear maps on finite-dimensional spaces are continuous|0C13E623WD]] and [[bounded linear maps are continuous|0F3K4C7XYW]], each linear map between Euclidean spaces is bounded. So there are $C_A, C_B \ge 0$ with $\|A h\| \le C_A \|h\|$ and $\|B w\| \le C_B \|w\|$ for all $h \in \mathbb{R}^n$ and $w \in \mathbb{R}^m$.
3. By step 2, being [[differentiable|0135XZZQ8M]] at a point with derivative $L$ means that $L$ is the [[Fréchet derivative|08EVNYZF42]] there, for the Euclidean norms. So the [[little-o form|0MN882VJ4P]] of the derivative applies.
4. For $h$ with $a + h \in U$, put $r(h) = g(a + h) - g(a) - A h$. For $w$ with $b + w \in W$, put $s(w) = f(b + w) - f(b) - B w$.
5. For $h$ with $a + h \in U$, put $w(h) = g(a + h) - b = A h + r(h)$. Then $b + w(h) = g(a + h) \in W$.
6. By steps 4 and 5, $f(g(a + h)) = f(b + w(h)) = f(b) + B w(h) + s(w(h))$.
7. Since $B$ is linear, $B w(h) = B A h + B r(h)$. So $(f \circ g)(a + h) - (f \circ g)(a) - (B \circ A) h = B r(h) + s(w(h))$.
8. Let $\varepsilon > 0$. By the little-o form for $f$ at $b$, there is $\delta_2 > 0$ with $\|s(w)\| \le \frac{\varepsilon}{2 (C_A + 1)} \|w\|$ for $\|w\| < \delta_2$ and $b + w \in W$.
9. By the little-o form for $g$ at $a$, there is $\delta_1 > 0$ with $\|r(h)\| \le \min\big(1, \frac{\varepsilon}{2 (C_B + 1)}\big) \|h\|$ for $\|h\| < \delta_1$ and $a + h \in U$.
10. Put $\delta = \min\big(\delta_1, \delta_2 / (C_A + 1)\big)$, and let $\|h\| < \delta$ with $a + h \in U$.
11. By steps 2, 5 and 9 and the [[triangle inequality|0FJZMBX0ZZ]], $\|w(h)\| \le C_A \|h\| + \|h\| = (C_A + 1) \|h\| < \delta_2$.
12. So step 8 applies to $w = w(h)$, and $\|s(w(h))\| \le \frac{\varepsilon}{2 (C_A + 1)} (C_A + 1) \|h\| = \frac{\varepsilon}{2} \|h\|$.
13. By steps 2 and 9, $\|B r(h)\| \le C_B \|r(h)\| \le \frac{C_B \varepsilon}{2 (C_B + 1)} \|h\| \le \frac{\varepsilon}{2} \|h\|$.
14. By steps 7, 12 and 13, $\|(f \circ g)(a + h) - (f \circ g)(a) - (B \circ A) h\| \le \varepsilon \|h\|$ for $\|h\| < \delta$ with $a + h \in U$.
15. The [[composition|05YBKMRVAR]] $B \circ A$ is a linear map $\mathbb{R}^n \to \mathbb{R}^k$. By step 14 and the little-o form, the [[composition|0THBK9V825]] $f \circ g$ is differentiable at $a$ with derivative $B \circ A$.
16. That is, $D(f \circ g)(a) = Df(g(a)) \circ Dg(a)$.

## Idea

Near $a$, the map $g$ moves $a + h$ to $b + w$ with $w \approx A h$, and near $b$ the map $f$ acts like $B$. So $f \circ g$ acts like $B A$. The errors stay small: $B$ cannot blow up the error of $g$ by more than a fixed factor, and $w$ is at most a fixed multiple of $\|h\|$.
