---
tag: T4RFYT8HDN
kind: statement
role: theorem
name: Gelfand's spectral radius formula
msc: [46H05, 47A10]
uses: [EH0CZ19RKP, QWQC5SV0SD, Q71WX8HFYT, 05M5SWSZZD]
about: [9V7YQA85PC]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_radius
---

## Statement

Let $A$ be a complex [[Banach algebra|9KYWN94QDN]] with unit $1 \ne 0$, and let $a \in A$.
Let $\sigma(a)$ be the [[spectrum|EH0CZ19RKP]] of $a$, and let $r(a) = \max \set{\abs{\lambda} : \lambda \in \sigma(a)}$ be its [[spectral radius|9V7YQA85PC]].
Then the [[limit|05M5SWSZZD]] of $\norm{a^n}^{1/n}$ exists, and
$$r(a) = \lim_{n \to \infty} \norm{a^n}^{1/n} = \inf_{n \ge 1} \norm{a^n}^{1/n}.$$

## Remarks

The maximum exists because $\sigma(a)$ is compact and, by the [[nonemptiness of the spectrum|QWQC5SV0SD]], nonempty.
Lower bound: by the [[spectral mapping theorem for polynomials|Q71WX8HFYT]], $\lambda^n \in \sigma(a^n)$ for $\lambda \in \sigma(a)$, and every $\mu \in \sigma(b)$ satisfies $\abs{\mu} \le \norm{b}$; so $r(a)^n \le \norm{a^n}$ for every $n$.
Upper bound: for $\abs{\lambda} > r(a)$ the resolvent $(\lambda 1 - a)^{-1}$ is holomorphic, and its Laurent series $\sum_{n \ge 0} a^n \lambda^{-n-1}$ converges there; applying functionals and the uniform boundedness principle gives $\limsup_n \norm{a^n}^{1/n} \le r(a)$.

Example: on $C([0,1])$ with the sup norm, $\norm{f^n} = \norm{f}^n$, so the formula gives $r(f) = \norm{f} = \max \abs{f}$, the largest absolute value of a point of the range.
For a nilpotent element, $a^n = 0$ for large $n$, so $r(a) = 0$ and $\sigma(a) = \set{0}$, even if $\norm{a}$ is large.
For matrices this is [[Gelfand's formula|3KX0KQ7V05]].

## Explanations

### L1 human

The spectral radius measures the largest size of a point of the spectrum.
The norm of $a$ may be bigger than this, but the norms of the powers $a^n$ grow at the exponential rate $r(a)^n$.
Taking $n$-th roots and letting $n$ grow recovers $r(a)$ from norms alone.

### L2 human

The formula shows that $r(a)$ depends only on the norms of the powers of $a$.
So it does not change when the spectrum is computed in a closed subalgebra containing $a$ and $1$.
In a C*-algebra, the C* identity gives $\norm{a^{2^k}} = \norm{a}^{2^k}$ for self-adjoint $a$, so $r(a) = \norm{a}$; this is a key step in the commutative Gelfand–Naimark theorem.
It also shows that the Gelfand transform satisfies $\norm{\hat a}_\infty = r(a)$ in a commutative unital Banach algebra.
