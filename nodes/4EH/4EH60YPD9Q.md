---
tag: 4EH60YPD9Q
kind: statement
role: theorem
name: Dini–Lipschitz criterion
msc: [42A20, 41A17]
uses: [AXCJBSQZWF, RWKQ5EP4YF, 08VZ57PT26, G12KXDHPPS, 0X3WGX95FE]
about: [G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Dini–Lipschitz_criterion
same_as:
  wikidata: Q5278349
  wikipedia: Dini–Lipschitz criterion
---

## Statement

Let $f \colon \R \to \C$ be a [[continuous|0X3WGX95FE]] $2\pi$-periodic function with [[modulus of continuity|AXCJBSQZWF]]
$$\omega(\delta) = \sup \set{\abs{f(x) - f(y)} : x, y \in \R, \ \abs{x - y} \le \delta}.$$
Suppose that
$$\lim_{\delta \to 0^+} \omega(\delta) \log \frac{1}{\delta} = 0.$$
Then the partial sums of the [[Fourier series|G12KXDHPPS]] of $f$ converge to $f$ [[uniformly|08VZ57PT26]] on $\R$.

## Remarks

Let $E_N(f)$ be the uniform distance from $f$ to the trigonometric polynomials of degree at most $N$.
Since $S_N T = T$ for such a polynomial $T$, one gets $\sup \abs{f - S_N f} \le (1 + L_N) E_N(f)$, where $L_N$ is the [[Lebesgue constant|RWKQ5EP4YF]].
Jackson's theorem gives $E_N(f) \le C \omega(1/N)$ with an absolute constant $C$, and $L_N = O(\log N)$, so the error is $O(\omega(1/N) \log N)$, which tends to $0$ by hypothesis.
Example: every Hölder continuous $f$, with $\omega(\delta) \le C \delta^\alpha$ for some $\alpha > 0$, satisfies the hypothesis; so does $f$ with $\omega(\delta) \le C / (\log(1/\delta))^{2}$ for small $\delta$.

## Explanations

### L1 human

A continuous function can have a badly behaved Fourier series.
The criterion says that a little more regularity than continuity is enough to rule this out.
The required regularity just beats the logarithmic growth of the Lebesgue constants.

### L2 human

The proof is a model of a general principle: if a linear approximation process has norms $L_N$, then it converges for all functions whose best approximation error is $o(1/L_N)$.
Here the norms grow like $\log N$, and Jackson's theorem converts best approximation error into modulus of continuity.
The criterion contains the uniform convergence of Fourier series of Hölder and Lipschitz continuous functions.
