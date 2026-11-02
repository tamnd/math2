---
tag: KQ57DC3AKM
kind: statement
role: theorem
name: Wiener–Ikehara theorem
msc: ["11M45", "40E05", "44A10"]
uses: [D6XWK1NRY1, 0WFF6AZPBP, 05XT5AVJBK, 087EMZTHWN]
about: [D6XWK1NRY1]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener–Ikehara_theorem
same_as:
  wikidata: Q7999144
  wikipedia: Wiener–Ikehara theorem
---

## Statement

Let $A \colon [0, \infty) \to [0, \infty)$ be a nondecreasing [[monotone function|0WFF6AZPBP]].
Assume that the [[Laplace transform|05XT5AVJBK]]
$$f(s) = \int_0^\infty A(x) e^{-xs} \, dx$$
converges for every complex $s$ with $\operatorname{Re} s > 1$.
Assume also that there is a real number $c \ge 0$ such that $f(s) - \frac{c}{s - 1}$ extends to a continuous function on the closed half-plane $\operatorname{Re} s \ge 1$.
Then
$$\lim_{x \to \infty} e^{-x} A(x) = c.$$

## Remarks

The proof is Fourier-analytic.
One integrates $f(s) - \frac{c}{s-1}$ on vertical lines against a Fejér-type kernel with compactly supported Fourier transform, lets $\operatorname{Re} s \to 1^+$, and uses the Riemann–Lebesgue lemma; monotonicity of $A$ then removes the smoothing.

Example: the [[prime number theorem|0EHBY5Y84N]].
Let $\psi(y) = \sum_{n \le y} \Lambda(n)$ with the [[von Mangoldt function|087EMZTHWN]] $\Lambda$, and put $A(x) = \psi(e^x)$.
Then $\int_0^\infty \psi(e^x) e^{-xs} \, dx = -\frac{\zeta'(s)}{s \, \zeta(s)}$ for $\operatorname{Re} s > 1$.
This differs from $\frac{1}{s - 1}$ by a function continuous on $\operatorname{Re} s \ge 1$, because $\zeta$ has a simple pole at $1$ and [[does not vanish on the line|CXES7915R7]] $\operatorname{Re} s = 1$.
So $\psi(y)/y \to 1$, which is equivalent to the prime number theorem.

The hypothesis is only continuity up to the boundary line, not analytic continuation beyond it.

## Explanations

### L1 human

The theorem reads the growth of a nondecreasing function off its Laplace transform.
If the transform behaves like $\frac{c}{s-1}$ near the line $\operatorname{Re} s = 1$ and has no other trouble on that line, then the function grows like $c e^x$.
Applied to the primes, it turns the fact that the zeta function has no zeros on the line $\operatorname{Re} s = 1$ into the prime number theorem.

### L2 human

In Dirichlet series form: if $a_n \ge 0$ and $F(s) = \sum a_n n^{-s}$ converges for $\operatorname{Re} s > 1$ with $F(s) - \frac{c}{s-1}$ continuous on $\operatorname{Re} s \ge 1$, then $\sum_{n \le y} a_n \sim c\,y$.
This follows by applying the theorem to $A(x) = \sum_{n \le e^x} a_n$.
The theorem is a special case of Wiener's general Tauberian theory; Newman's later contour-integral proof of the prime number theorem uses a closely related Tauberian argument.
