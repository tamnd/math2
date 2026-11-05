---
tag: WG0QYY878Y
kind: statement
role: proposition
name: Riemann's formula
sources:
  - wikipedia: en:250178@r1370942184
    locator: Skewes's number, section Riemann's formula
    note: adopted
    mention: wikipedia://en/250178#EB25
    sections: [Statement]
inventory: [AHT5YK5WYE]
---

## Statement

Riemann gave an explicit formula for $\pi(x)$, whose leading terms are (ignoring some subtle convergence questions)

$$\pi(x) = \operatorname{li}(x) - \tfrac{1}{2}\operatorname{li}(\sqrt{x\,}) - \sum_{\rho} \operatorname{li}(x^\rho) + \text{smaller terms}$$

where the sum is over all $\rho$ in the set of non-trivial zeros of the Riemann zeta function.

The largest error term in the approximation $\pi(x) \approx \operatorname{li}(x)$ (if the Riemann hypothesis is true) is negative $\tfrac{1}{2}\operatorname{li}(\sqrt{x\,})$, showing that $\operatorname{li}(x)$ is usually larger than $\pi(x)$. The other terms above are somewhat smaller, and moreover tend to have different, seemingly random complex [[arguments|070PFSYJJR]], so mostly cancel out. Occasionally however, several of the larger ones might happen to have roughly the same complex argument, in which case they will reinforce each other instead of cancelling and will overwhelm the term $\tfrac{1}{2}\operatorname{li}(\sqrt{x\,})$.

The reason why the Skewes number is so large is that these smaller terms are quite a *lot* smaller than the leading error term, mainly because the first [[complex|09FTAET5Z4]] zero of the zeta function has quite a large [[imaginary part|09FTAET5Z4]], so a large number (several hundred) of them need to have roughly the same argument in order to overwhelm the dominant term. The chance of $N$ random complex numbers having roughly the same argument is about 1 in $2^N$. This explains why $\pi(x)$ is sometimes larger than $\operatorname{li}(x),$ and also why it is rare for this to happen. It also shows why finding places where this happens depends on large scale calculations of millions of high precision zeros of the Riemann zeta function.

The argument above is not a proof, as it assumes the zeros of the Riemann zeta function are random, which is not true. Roughly speaking, Littlewood's proof consists of [[Dirichlet's approximation theorem|04JAY9DGB7]] to show that sometimes many terms have about the same argument. In the event that the Riemann hypothesis is false, the argument is much simpler, essentially because the terms $\operatorname{li}(x^{\rho})$ for zeros violating the Riemann hypothesis (with [[real part|09FTAET5Z4]] greater than $\tfrac{1}{2}$) are eventually larger than $\operatorname{li}(x^{1/2})$.

The reason for the term $\tfrac{1}{2}\mathrm{li}(x^{1/2})$ is that, roughly speaking, $\mathrm{li}(x)$ actually counts powers of [[primes|01826KMG2H]], rather than the primes themselves, with $p^n$ weighted by $\frac{1}{n}$. The term $\tfrac{1}{2}\mathrm{li}(x^{1/2})$ is roughly analogous to a second-order correction accounting for squares of primes.
