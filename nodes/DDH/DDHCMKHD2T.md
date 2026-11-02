---
tag: DDHCMKHD2T
kind: statement
role: theorem
name: Newton's forward difference formula
msc: [39A70, 41A05]
uses: [E38801KVJ1, 91QMF4R1CY, 092GEF38YD]
about: [3039GWNHWS]
sources:
  - url: https://en.wikipedia.org/wiki/Newton_polynomial
---

## Statement

Let $M$ be an additive commutative monoid, let $G$ be an additive abelian group, let $h \in M$, and let $f \colon M \to G$ be a function.
Let $\Delta_h^k f$ be the [[$k$-th forward difference|E38801KVJ1]] of $f$ with step $h$.
Then for every $n \in \N$ and every $x \in M$,
$$f(x + nh) = \sum_{k=0}^{n} \binom{n}{k} \Delta_h^k f(x),$$
where $\binom{n}{k}$ is the [[binomial coefficient|092GEF38YD]].

## Remarks

The [[shift operator|91QMF4R1CY]] satisfies $E_h = I + \Delta_h$, and $I$ commutes with $\Delta_h$.
So the [[binomial theorem|0EHWPWGHB2]] gives $E_h^n = \sum_k \binom{n}{k} \Delta_h^k$, which is the formula applied at $x$.
Example: for $f(x) = x^2$, $h = 1$ and $x = 0$, the differences at $0$ are $f(0) = 0$, $\Delta f(0) = 1$, $\Delta^2 f(0) = 2$, so $f(n) = n + 2\binom{n}{2} = n + n(n-1) = n^2$.
Let $f \colon \R \to \R$ and $h \ne 0$, and replace the top entry $n$ of $\binom{n}{k}$ by a real number $s$.
This gives the Newton forward interpolation polynomial
$$p(x_0 + sh) = \sum_{k=0}^{n} \binom{s}{k} \Delta_h^k f(x_0), \qquad \binom{s}{k} = \frac{s(s-1)\cdots(s-k+1)}{k!}.$$
It is the unique polynomial of degree at most $n$ that agrees with $f$ at $x_0, x_0 + h, \dots, x_0 + nh$.

## Explanations

### L1 human

If you know the value of a function at one point and all its differences there, you can rebuild its values further along.
This is like Taylor's formula, with differences in place of derivatives and binomial coefficients in place of $s^k / k!$.
For a polynomial only finitely many differences are nonzero, so the formula recovers it from a finite table.

### L2 human

The formula and the [[expansion of iterated differences in shifts|24D1EGHP4G]] are inverse to each other: they express the binomial transform and its inverse.
In numerical analysis it gives the interpolation polynomial at equally spaced nodes, a special case of [[polynomial interpolation|SS1YMS2NPC]].
Letting $n \to \infty$ with real $s$ leads to the [[Newton series|Y2HXSEA2EE]] of $f$.
Over the $p$-adic integers, the same expansion with infinitely many terms is [[Mahler's theorem|D115PG3T7K]].
