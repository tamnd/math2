---
tag: XBM7J5R1VQ
kind: statement
role: theorem
name: Lindelöf's theorem
msc: [30C80]
uses: [0DG0Z72CQD, 048F2P90WR, FYR6V2NH6C]
about: [0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Lindel%C3%B6f%27s_theorem
    locator: Statement of the theorem
same_as:
  wikidata: Q4454973
  wikipedia: Lindelöf's theorem
---

## Statement

Let $x_1 < x_2$ and $y_0$ be real numbers, and let $\Omega = \set{z \in \C : x_1 \le \operatorname{Re} z \le x_2, \ \operatorname{Im} z \ge y_0}$ be a closed half-strip.
Let $f \colon \Omega \to \C$ be continuous on $\Omega$ and [[holomorphic|0DG0Z72CQD]] on its interior.
Assume that $\abs{f(z)} \le M$ for each $z$ on the boundary of $\Omega$.
Assume also that there are constants $A, B > 0$ with $\abs{f(x + iy)} \le B (1 + \abs{y})^{A}$ for all $x + iy \in \Omega$.
Then $\abs{f(z)} \le M$ for all $z \in \Omega$.

## Remarks

Proof idea: for $\varepsilon > 0$ let $g_\varepsilon(z) = f(z) e^{i \varepsilon (z - i y_0)}$, so that $\abs{g_\varepsilon(x + iy)} = \abs{f(x + iy)} e^{-\varepsilon (y - y_0)}$.
Then $\abs{g_\varepsilon} \le \abs{f}$ on $\Omega$, and $g_\varepsilon \to 0$ as $\operatorname{Im} z \to \infty$ because $f$ grows at most polynomially.
The [[maximum modulus principle|048F2P90WR]] on the rectangles $\Omega \cap \set{\operatorname{Im} z \le T}$ with $T$ large gives $\abs{g_\varepsilon} \le M$, and $\varepsilon \to 0$ gives $\abs{f} \le M$.
A growth hypothesis is needed.
On the half-strip $\abs{\operatorname{Re} z} \le \frac{\pi}{2}$, $\operatorname{Im} z \ge 0$, the function $\exp(e^{-iz})$ has modulus $\exp(e^{y} \cos x)$.
It is bounded on the boundary, where $\cos x = 0$ or $y = 0$, but unbounded on the line $x = 0$.
The theorem is a case of the [[Phragmén–Lindelöf principle|FYR6V2NH6C]].

## Explanations

### L1 human

On a half-strip, which goes off to infinity in one direction, the maximum principle can fail for fast-growing functions.
Lindelöf's theorem says that polynomial growth is slow enough.
Then a bound on the edges of the half-strip is a bound everywhere inside.

### L2 human

The theorem is used in analytic number theory for functions such as the Riemann zeta function on vertical half-strips.
Together with the [[Hadamard three-lines theorem|WHS58R43N0]] it gives the convexity bounds for the growth of $\zeta(\sigma + it)$ as $t \to \infty$.
In the proof, the factor $e^{i\varepsilon z}$ is the standard device to force decay at infinity before applying the maximum modulus principle.
