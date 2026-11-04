---
tag: CWADDJ6942
kind: proof
name: Proof of the linearity of the derivative
msc: [26B05]
proves: 0CXZ217QDP
uses: [08EVNYZF42, 0MN882VJ4P, 0F3K4C7XYW, 0FJZMBX0ZZ]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.3.6
---

## Proof

We add the two error terms, and we scale one of them.

1. Let $V$, $W$, $U$, $f$, $g$, $x$ and $c$ be as in the statement. Put $A = Df(x)$ and $B = Dg(x)$.
2. Since $A$ and $B$ are bounded, there are $C_A, C_B \ge 0$ with $\|A h\| \le C_A \|h\|$ and $\|B h\| \le C_B \|h\|$ for each $h \in V$. This is the meaning of [[bounded|0F3K4C7XYW]].
3. The map $A + B$ is linear, and $\|(A + B) h\| \le \|A h\| + \|B h\| \le (C_A + C_B) \|h\|$ by the [[triangle inequality|0FJZMBX0ZZ]]. So $A + B$ is bounded.
4. The map $c A$ is linear, and $\|c A h\| = |c| \, \|A h\| \le |c| C_A \|h\|$. So $c A$ is bounded.
5. For $h \in V$ with $x + h \in U$, put $r(h) = f(x + h) - f(x) - A h$ and $s(h) = g(x + h) - g(x) - B h$.
6. Then $(f + g)(x + h) - (f + g)(x) - (A + B) h = r(h) + s(h)$, and $(c f)(x + h) - (c f)(x) - (c A) h = c \, r(h)$.
7. Let $\varepsilon > 0$. By the [[little-o form of the derivative|0MN882VJ4P]] for $f$ and for $g$, there is $\delta > 0$ with $\|r(h)\| \le \varepsilon \|h\|$ and $\|s(h)\| \le \varepsilon \|h\|$. This holds for $\|h\| < \delta$ with $x + h \in U$. We take $\delta$ as the smaller of the two numbers given by $f$ and by $g$.
8. For these $h$, the triangle inequality gives $\|r(h) + s(h)\| \le 2 \varepsilon \|h\|$. Given $\varepsilon' > 0$, we can apply this with $\varepsilon = \varepsilon' / 2$. So $r(h) + s(h) = o(\|h\|)$.
9. For these $h$, also $\|c \, r(h)\| = |c| \, \|r(h)\| \le |c| \varepsilon \|h\|$. Given $\varepsilon' > 0$, we can apply this with $\varepsilon = \varepsilon' / (|c| + 1)$. So $c \, r(h) = o(\|h\|)$.
10. By steps 3, 6 and 8 and the little-o form, $f + g$ is [[Fréchet differentiable|08EVNYZF42]] at $x$ with $D(f + g)(x) = A + B$.
11. By steps 4, 6 and 9 and the little-o form, $c f$ is Fréchet differentiable at $x$ with $D(c f)(x) = c A$.

## Idea

The error of a sum is the sum of the errors, and the error of $c f$ is $c$ times the error of $f$. Both operations keep an error that is small compared with $\|h\|$. The candidate derivatives are again bounded linear maps, so the definition applies.
