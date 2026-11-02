---
tag: J6NMBX3E55
kind: statement
role: theorem
name: Birkhoff's ergodic theorem
msc: [37A30, 28D05, 37A05]
uses: [556WBDAHNP, 0NFPJVJJHX, X7GTF3D98F, RARTMA0ZEC, 8TD2KCVH5N, 0TTDGTEFMN, AZRPHS478B, V7PA1V3N0K, PQPDQCCD02, 0DFWHQ839T]
about: [8TD2KCVH5N, AZRPHS478B]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodic_theory
    locator: Ergodic theorems
---

## Statement

Let $(X, \mathcal{A}, \mu)$ be a [[probability space|0NFPJVJJHX]], let $T \colon X \to X$ be a [[measure-preserving transformation|556WBDAHNP]], and let $f \colon X \to \R$ be [[integrable|X7GTF3D98F]].
Let $A_n f = \frac{1}{n} \sum_{k=0}^{n-1} f \circ T^k$ be the [[Birkhoff averages|8TD2KCVH5N]] of $f$, and let $\mathcal{I} = \set{A \in \mathcal{A} : T^{-1}(A) = A}$ be the $\sigma$-algebra of invariant sets.
Then:

1. $A_n f(x)$ converges as $n \to \infty$ for [[almost every|RARTMA0ZEC]] $x \in X$, to the [[conditional expectation|0TTDGTEFMN]] $f^* = \mathbb{E}(f \mid \mathcal{I})$;
2. the limit satisfies $f^* \circ T = f^*$ almost everywhere and $\int_X f^* \, d\mu = \int_X f \, d\mu$;
3. $A_n f \to f^*$ also in $L^1(\mu)$;
4. if $T$ is [[ergodic|AZRPHS478B]], then $f^* = \int_X f \, d\mu$ almost everywhere.

## Remarks

The usual proof combines the [[maximal ergodic theorem|V7PA1V3N0K]] with a density argument.
For functions of the form $h + g - g \circ T$, with $h$ invariant and $g$ bounded, the averages converge everywhere, because the sums of $g - g \circ T$ telescope.
The maximal inequality bounds $\sup_n \abs{A_n f}$ in measure by $\norm{f}_1$, and this lets convergence pass to all integrable $f$.
For $f \in L^2(\mu)$, convergence in $L^2$ is the content of the [[mean ergodic theorem|PQPDQCCD02]].

Example: let $T(x) = 2x \bmod 1$ on $[0, 1)$ with Lebesgue measure, which is ergodic, and let $f$ be the indicator of $[1/2, 1)$.
Then $f(T^k(x))$ is the $(k+1)$-st binary digit of $x$, so the theorem says that almost every $x$ has, in the limit, half of its binary digits equal to $1$.

Applied to a sequence of independent identically distributed random variables, viewed as a shift on a product space, the theorem gives the [[strong law of large numbers|0DFWHQ839T]].

The measure must be invariant: for $T(x) = x/2$ on $[0, 1]$ with Lebesgue measure, which is not $T$-invariant, and $f(x) = x$, the averages tend to $0$ everywhere, while $\int_0^1 f \, dx = 1/2$, so conclusion 2 fails.

## Explanations

### L1 human

Follow one orbit for a long time and average a quantity along it: this is a time average.
Average the same quantity over the whole space: this is a space average.
For an ergodic system the two agree for almost every starting point.
So watching one typical trajectory long enough reveals the statistics of the whole system.

### L2 human

The theorem is the basic convergence result of ergodic theory.
Without ergodicity, the limit is still defined almost everywhere, but it can differ on different invariant pieces, and it equals the conditional expectation on the invariant sets.
It is used to prove the strong law of large numbers, the normality of almost every real number, and statistical properties of billiards and geodesic flows.
The same statement holds for measure-preserving flows, with sums replaced by integrals over time.
Kingman's subadditive ergodic theorem extends it from sums $S_n f$ to subadditive sequences, and the ergodic decomposition reduces the non-ergodic case to the ergodic one.
