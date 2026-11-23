---
tag: VCQQNJ3SEZ
kind: concept
name: Heuristic arguments in mathematics
aliases: [heuristic-argument, probabilistic-heuristic, cramer-model]
msc: ["00A35", "11N05", "11N36"]
topics: [DME0TPC348]
audience: research
uses: [8DHD3H1CJ9, WMEMMHZ3BH, 0SN0MAEKYX, 0EHBY5Y84N]
sources:
  - url: https://en.wikipedia.org/wiki/Heuristic_argument
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Probabilistic_number_theory
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Maier%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Twin_prime
    locator: First Hardy–Littlewood conjecture
---

## Summary

A heuristic argument predicts a mathematical fact from a model that is not fully justified.
It does not prove the fact, but it often predicts a number that the data can then confirm or refute.

Here is the standard case.
The [[prime number theorem|0EHBY5Y84N]] says that a number near $t$ is prime with a chance of about $1/\ln t$.
If the [[primes|0SN0MAEKYX]] behaved like random numbers with this density, a pair $t, t + 2$ would be a pair of primes with a chance of about $1/(\ln t)^2$.
After a correction for divisibility by small primes, the model predicts about
$$2 C_2 \int_2^{x} \frac{dt}{(\ln t)^2}, \qquad 2 C_2 \approx 1.3203,$$
pairs of twin primes up to $x$.
At $x = 10^6$ this is about $8248$, and the true count is $8169$, within $1\%$.
The agreement is strong evidence for the twin prime [[conjecture|WMEMMHZ3BH]], and the conjecture is still open.

Common kinds of heuristic argument are random models, which treat a fixed object as if it were random, dimension counts, which compare free parameters with conditions, and scaling arguments, which compare the sizes of terms.
A heuristic can fail when the object has structure that the model ignores.

## Motivation

[[Numerical evidence|JFD3QWCX8Z]] alone is weak when the scale of a problem is beyond computation.
A heuristic argument adds a reason: a model in which the conjecture is the expected behavior.
It also produces numbers, such as the constant $2C_2$, that a computation can compare with the data.
Many central conjectures, such as the twin prime conjecture and the Hardy-Littlewood conjectures, are believed mainly for heuristic reasons.

The corrections that a model needs are informative too.
The naive model, with no correction, predicts the wrong constant for twin primes, and the size of the error points to the small primes.
So heuristics and data improve each other, in the spirit of [[plausible reasoning|8DHD3H1CJ9]].

## Notation

The Cramér model is a sequence of independent random events $E_n$, $n \ge 3$, where $E_n$ ("$n$ is prime") has probability $1/\ln n$.
In this model the expected number of primes up to $x$ is $\sum_{3 \le n \le x} 1/\ln n$, which is close to $\operatorname{li}(x)$.
A dimension count predicts
$$\text{expected dimension} = (\text{number of parameters}) - (\text{number of independent conditions}).$$
A negative expected dimension predicts no solutions for general data, and $0$ predicts finitely many.
A scaling argument compares the number of candidates of size about $X$ with the chance that one candidate is a solution.

## Remarks

### Three kinds of model

[[A heuristic count of twin primes|XHHKMPD8A9]] works out the random model and its correction factor.
The same model, with local factors, gives the Hardy and Littlewood prediction for the number of ways to write $n$ as a sum of two primes; see [[Goldbach partitions grow with n|RKFZV5NFXE]].
The [[Bateman-Horn conjecture|6NY57KQZZF]] extends the count to the prime values of several polynomials at once.

[[A dimension count predicts the lines on surfaces in space|MSMXVPKRN1]] is the geometric kind.
The lines in space form a family of dimension $4$, and a line lies on a surface of degree $d$ when it satisfies $d + 1$ conditions.
For a cubic surface, $4 - 4 = 0$ predicts finitely many lines, in agreement with the [[twenty-seven lines|VQK5HQFYEM]].

A scaling argument treats $x^n + y^n = z^n$.
There are about $X^3$ triples with entries near $X$, and $x^n + y^n - z^n$ has size about $X^n$.
If it took each value with about the same chance, the expected number of solutions near $X$ would be about
$$\frac{X^3}{X^n} = X^{3-n},$$
which predicts few solutions for $n \ge 4$, in agreement with [[Fermat's Last Theorem|0Y5X3SDBCZ]].

### What it is not

[[Erdős's lower bound for Ramsey numbers is a proof|2D3GCG17FA]], although it uses random colorings.
Every step there is rigorous and the conclusion is certain, so a probabilistic proof is not a heuristic argument.
The [[heuristics of discovery|X1NSTVGDNQ]], such as "solve a simpler problem first", are strategies for finding a solution, and they predict no mathematical fact.
A table of verified cases is numerical evidence, not a heuristic argument, because it gives no model from which the conjecture follows.

### Where models fail

The scaling argument above predicts about a constant number of solutions near each size $X$ for $n = 3$, so infinitely many in total.
But [[Fermat's Last Theorem for n = 3|07NKG38VEG]] says that there are none, so the model missed the arithmetic of the cubic curve.
The Cramér model fails in short intervals: Helmut Maier proved in 1985 that for each $\lambda > 1$ the number of primes in $(x, x + (\ln x)^\lambda]$ is not asymptotic to $(\ln x)^{\lambda - 1}$, as the model predicts.
A dimension count gives the right answer for general data and can fail for special data whose conditions are dependent.

### Watch out

A heuristic argument proves nothing, and its conclusion is a conjecture that may be false.
The twin prime conjecture is open despite the close agreement at $10^6$.

The naive model needs local corrections.
Without them it predicts many pairs $(p, p + 1)$ of primes, but such a pair needs an even prime, so the only one is $(2, 3)$.

Do not confuse a heuristic with a probabilistic proof.
A heuristic assumes that a fixed object behaves like a random one, while a probabilistic proof studies an object that really is random and draws a certain conclusion.

### History

Godfrey Hardy and John Littlewood used the circle method in 1923 to derive conjectured asymptotic formulas for prime pairs and for Goldbach partitions; see the [[Hardy-Littlewood circle method|ZQFBEX62D0]].
Harald Cramér introduced his random model of the primes in 1936 and derived from it a conjecture on the size of [[prime gaps|2AEK2Z6RQD]].
Paul Bateman and Roger Horn stated their general conjecture in 1962.
Maier's theorem of 1985 was the first proof that the Cramér model fails somewhere.

### Try it

Use the density $1/\ln t$ to estimate the number of primes between $10^6$ and $10^6 + 1000$.
Since $\ln 10^6 \approx 13.8$, the estimate is $1000/13.8 \approx 72$, and the true count is $75$.

What does a dimension count predict for lines on a surface of degree $4$ in space?
It gives $4 - 5 = -1$, so a general quartic surface contains no line.

## Explanations

### L1 human

A heuristic argument is a careful guess with a reason behind it.
About one number in $14$ near a million is prime.
If primes were scattered at random with this density, pairs of primes two apart would still turn up again and again.
This suggests that there are infinitely many such pairs, and it even predicts how many.
The prediction matches the real counts, but it is not a proof, because the primes are not truly random.

### L2 human

We compare the Cramér model with the true counts up to $10^6$.
For all primes, the model predicts about $\operatorname{li}(10^6) \approx 78627.5$, and the true count is $\pi(10^6) = 78498$.
The relative error is about $0.16\%$, so the model fits this count well.
For twin primes, the naive model predicts
$$\int_2^{10^6} \frac{dt}{(\ln t)^2} \approx 6247$$
pairs, and the true count is $8169$.
The ratio $8169/6247 \approx 1.31$ is close to $2C_2 \approx 1.3203$, the correction for divisibility by small primes.

The typical use: a model that fits one statistic is tested on another, and a failure shows which structure the model misses.
Watch out: a model that fits the count of primes can still miss the correlations between primes, as the twin prime count shows.

### L3 human

Heuristic arguments express a view of mathematical objects as a mixture of structure and randomness.
The structure is the set of local constraints, such as congruences modulo small primes or the algebraic identities of a variety.
The randomness is the assumption that, after these constraints, the object behaves like a generic one.
The Hardy-Littlewood constants are products of local densities, one for each prime, and the expected dimension is the generic codimension of the conditions.
A failure of a heuristic, such as Maier's theorem or the absence of solutions for $n = 3$, points to structure that the model left out.
Rigorous methods, such as sieves and the circle method, sometimes follow the heuristic closely.
For twin primes and for Goldbach's conjecture, the parity problem of sieve theory is one obstacle between the heuristic and a proof.
