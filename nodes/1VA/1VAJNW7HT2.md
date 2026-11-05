---
tag: 1VAJNW7HT2
kind: proof
name: Proof of Prime number theorem
msc: [11N05]
proves: 0EHBY5Y84N
sources:
  - wikipedia: en:23692@r1368746397
    locator: Prime number theorem, section Proof sketch
    note: adopted
    mention: wikipedia://en/23692#3EK8
    sections: [Proof]
---

## Proof

Here is a sketch of the proof referred to in one of Terence Tao's lectures. Like most proofs of the PNT, it starts out by reformulating the problem in terms of a less intuitive, but better-behaved, prime-counting function. The idea is to count the primes (or a related set such as the set of prime powers) with *weights* to arrive at a function with smoother asymptotic behavior. The most common such generalized counting function is the Chebyshev function $\psi(x)$, defined by

$$\psi(x) = \sum_{k \geq 1} \sum_\overset{p^k \le x,}{\!\!\!\!p \text{ is prime}\!\!\!\!} \log p \; .$$

This is sometimes written as

$$\psi(x) = \sum_{n\le x} \Lambda(n) \; ,$$

where $\Lambda(n)$ is the [[von Mangoldt function|087EMZTHWN]], namely

$$\Lambda(n) = \begin{cases} \log p & \text{ if } n = p^k \text{ for some prime } p \text{ and integer } k \ge 1, \\ 0 & \text{otherwise.} \end{cases}$$

It is now relatively easy to check that the PNT is equivalent to the claim that

$$\lim_{x\to\infty} \frac{\psi(x)}{x} = 1 \; .$$

Indeed, this follows from the easy estimates

$$\psi(x) = \sum_\overset{p\le x}{\!\!\!\! p \text{ is prime}\!\!\!\!} \log p \left\lfloor \frac{\log x}{\log p} \right\rfloor \le \sum_\overset{p\le x}{\!\!\!\! p \text{ is prime}\!\!\!\!} \log x = \pi(x)\log x$$

and (using big $O$ notation) for any $\varepsilon > 0$,

$$\psi(x) \ge \sum_{\!\!\!\!\overset{x^{1-\varepsilon}\le p\le x}{p \text{ is prime}}\!\!\!\!} \log p \ge \sum_{\!\!\!\!\overset{x^{1-\varepsilon}\le p\le x}{p \text{ is prime}}\!\!\!\!} (1-\varepsilon)\log x=(1-\varepsilon)\left(\pi(x)+O\left(x^{1-\varepsilon}\right)\right)\log x \; .$$

The next step is to find a useful representation for $\psi(x)$. Let $\zeta(s)$ be the Riemann zeta function. It can be shown that $\zeta(s)$ is related to the [[von Mangoldt function|087EMZTHWN]] $\Lambda(n)$, and hence to $\psi(x)$, via the relation

$$-\frac{\zeta'(s)}{\zeta(s)} = \sum_{n = 1}^\infty \Lambda(n) \, n^{-s} \; .$$

A delicate analysis of this equation and related properties of the zeta function, using the Mellin transform and Perron's formula, shows that for non-integer $x$ the equation

$$\psi(x) = x \; - \; \log(2\pi) \; - \!\!\!\! \sum\limits_{\rho :\, \zeta(\rho) = 0} \frac{x^\rho}{\rho}$$

holds, where the sum is over all zeros (trivial and nontrivial) of the zeta function. This striking formula is one of the so-called explicit formulas of number theory, and is already suggestive of the result we wish to prove, since the term $x$ (claimed to be the correct asymptotic order of $\psi(x)$) appears on the right-hand side, followed by (presumably) lower-order asymptotic terms.

The next step in the proof involves a study of the zeros of the zeta function. The trivial zeros −2, −4, −6, −8, ... can be handled separately:

$$\sum_{n=1}^\infty \frac{1}{2n\,x^{2n}} = -\frac{1}{2}\log\left(1-\frac{1}{x^2}\right),$$

which vanishes for large $x$. The nontrivial zeros, namely those on the critical strip $0 \le \operatorname{Re}(s) \le 1$, can potentially be of an asymptotic order comparable to the main term $x$ if $\operatorname{Re}(\rho) = 1$, so we need to show that all zeros have real part strictly less than 1.

To do this, we take for granted that $\zeta(s)$ is [[meromorphic|0NSD1TPHR0]] in the half-plane $\operatorname{Re}(s) > 0$, and is analytic there except for a simple pole at $s = 1$, and that there is a product formula

$$\zeta(s)=\prod_p\frac{1}{1-p^{-s}}$$

for $\operatorname{Re}(s) > 1$. This product formula follows from the existence of unique prime factorization of integers, and shows that $\zeta(s)$ is never zero in this region, so that its logarithm is defined there and

$$\log\zeta(s)=-\sum_p\log \left(1-p^{-s} \right)=\sum_{p,n}\frac{p^{-ns}}{n} \; .$$

Write $s = x + iy$ ; then

$$\big| \zeta(x+iy) \big| = \exp\left( \sum_{n,p} \frac{\cos ny\log p}{np^{nx}} \right) \; .$$

Now observe the identity

$$3 + 4 \cos \phi+ \cos 2 \phi = 2 ( 1 + \cos \phi )^2\ge 0 \; ,$$

so that

$$\left| \zeta(x)^3 \zeta(x+iy)^4 \zeta(x+2iy) \right| = \exp\left( \sum_{n,p} \frac{3 + 4 \cos(ny\log p) + \cos( 2 n y \log p )}{np^{nx}} \right) \ge 1$$

for all $x > 1$. Suppose now that $\zeta(1 + iy) = 0$. Certainly $y$ is not zero, since $\zeta(s)$ has a simple pole at $s = 1$. Suppose that $x > 1$ and let $x$ tend to 1 from above. Since $\zeta(s)$ has a simple pole at $s = 1$ and $\zeta(x + 2iy)$ stays analytic, the left hand side in the previous inequality tends to 0, a contradiction.

Finally, we can conclude that the PNT is heuristically true. To rigorously complete the proof there are still serious technicalities to overcome, due to the fact that the summation over zeta zeros in the explicit formula for $\psi(x)$ does not converge absolutely but only conditionally and in a "principal value" sense. There are several ways around this problem but many of them require rather delicate complex-analytic estimates. Edwards's book provides the details. Another method is to use Ikehara's Tauberian theorem, though this theorem is itself quite hard to prove. D.J. Newman observed that the full strength of Ikehara's theorem is not needed for the prime number theorem, and one can get away with a special case that is much easier to prove.
