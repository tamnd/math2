---
tag: XDWQGKH180
kind: proof
name: Proof of the product rule in several variables
msc: [26B05]
proves: 0SF85PY0QN
uses: [0135XZZQ8M, 0C13E623WD, 0F3K4C7XYW, 0FJZMBX0ZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Product_rule
    locator: Linear approximations
---

## Proof

We write $f$ and $g$ as linear approximations plus errors, multiply out, and bound each error term.

1. Let $U$, $f$, $g$ and $a$ be as in the statement. Put $A = Df(a)$ and $B = Dg(a)$, two linear maps $\mathbb{R}^n \to \mathbb{R}$.
2. By [[linear maps on finite-dimensional spaces are continuous|0C13E623WD]] and [[bounded linear maps are continuous|0F3K4C7XYW]], there are $C_A, C_B \ge 0$ with $|A h| \le C_A \|h\|$ and $|B h| \le C_B \|h\|$ for each $h$.
3. For $h$ with $a + h \in U$, put $r(h) = f(a + h) - f(a) - A h$ and $s(h) = g(a + h) - g(a) - B h$. Put $\Delta(h) = f(a + h) - f(a) = A h + r(h)$.
4. Let $L \colon \mathbb{R}^n \to \mathbb{R}$ be the map $L h = f(a) \, B h + g(a) \, A h$. It is linear, since $A$ and $B$ are linear.
5. Multiply out, using $f(a + h) = f(a) + \Delta(h)$ and $g(a + h) = g(a) + B h + s(h)$:
$$f(a + h) g(a + h) = f(a) g(a) + f(a) B h + f(a) s(h) + \Delta(h) \big(g(a) + B h + s(h)\big).$$
6. Since $\Delta(h) g(a) = g(a) A h + g(a) r(h)$, step 5 gives $f(a + h) g(a + h) - f(a) g(a) - L h = R(h)$, where
$$R(h) = f(a) \, s(h) + g(a) \, r(h) + \Delta(h) \big(B h + s(h)\big).$$
7. Since $f$ and $g$ are [[differentiable|0135XZZQ8M]] at $a$, there is $\delta_0 > 0$ with $|r(h)| \le \|h\|$ and $|s(h)| \le \|h\|$. This holds for $\|h\| < \delta_0$ with $a + h \in U$.
8. For these $h$, steps 2 and 7 give $|\Delta(h)| \le (C_A + 1) \|h\|$ and $|B h + s(h)| \le (C_B + 1) \|h\|$.
9. For $0 < \|h\| < \delta_0$ with $a + h \in U$, the [[triangle inequality|0FJZMBX0ZZ]] and step 8 give
$$\frac{|R(h)|}{\|h\|} \le |f(a)| \frac{|s(h)|}{\|h\|} + |g(a)| \frac{|r(h)|}{\|h\|} + (C_A + 1)(C_B + 1) \|h\|.$$
10. As $h \to 0$, the first two terms tend to $0$ by the differentiability of $g$ and $f$ at $a$. The last term tends to $0$ as well.
11. So $|R(h)| / \|h\| \to 0$. By step 6, $f g$ is differentiable at $a$ with $D(f g)(a) = L$.
12. That is, $D(f g)(a)(h) = f(a) \, Dg(a)(h) + g(a) \, Df(a)(h)$ for each $h \in \mathbb{R}^n$.

## Idea

Multiplying the two linear approximations gives the constant $f(a) g(a)$, the two cross terms $f(a) B h$ and $g(a) A h$, and some leftovers. Each leftover contains an error term, or a product of two quantities of size about $\|h\|$. So the leftovers are small compared with $\|h\|$.
