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

A heuristic argument in mathematics is a non-rigorous argument that predicts a mathematical fact, often in a precise quantitative form.
Common kinds are probabilistic models, which treat a deterministic object as random, dimension counts, which compare the number of free parameters with the number of conditions, and scaling arguments, which compare the sizes of terms.
The prediction is a [[conjecture|WMEMMHZ3BH]], and its precise form makes it testable by numerical evidence.
A heuristic can fail when the object has structure that the model ignores.
Heuristic arguments matter because many central conjectures, such as the twin prime and Hardy-Littlewood conjectures, are believed mainly for heuristic reasons.

## Motivation

Numerical evidence alone is weak when the scale of a problem is beyond computation.
A heuristic argument adds a reason: a model in which the conjecture is the expected behaviour.
It also produces numbers, such as an asymptotic constant, that a computation can compare with the data.

The models are simple.
The [[prime number theorem|0EHBY5Y84N]] says that the primes near $x$ have density about $1/\ln x$.
If the [[primes|0SN0MAEKYX]] behaved like random numbers with this density, many questions about them would become exercises in probability.
The answers of those exercises are conjectures about the real primes, and the corrections needed to make the model fit the data are themselves informative.

## Notation

The Cramér model is a sequence of independent random events $E_n$, $n \geq 3$, where $E_n$ ("$n$ is prime") has probability $1/\ln n$.
In this model the expected number of primes up to $x$ is $\sum_{3 \leq n \leq x} 1/\ln n \approx \operatorname{li}(x)$.

A dimension count predicts the dimension of a solution set as
$$\text{expected dimension} = (\text{number of parameters}) - (\text{number of independent conditions}).$$
A negative expected dimension predicts no solutions for general data, and $0$ predicts finitely many.

A scaling argument compares the number of candidates of size about $X$ with the probability that one candidate is a solution.

## Remarks

### Examples

1. [[A heuristic count of twin primes|XHHKMPD8A9]]: the Cramér model, corrected for divisibility by small primes, predicts about $2C_2 \int_2^x dt/(\ln t)^2$ twin prime pairs up to $x$. At $x = 10^6$ the prediction is $8248$, and the true count is $8169$.
2. [[A dimension count predicts the lines on surfaces in space|MSMXVPKRN1]]: lines in space form a family of dimension $4$, and a line on a surface of degree $d$ must satisfy $d + 1$ conditions. The count predicts finitely many lines on a cubic surface, in agreement with the [[twenty-seven lines|VQK5HQFYEM]].
3. The Hardy and Littlewood prediction for the number of Goldbach partitions; see [[Goldbach partitions grow with n|RKFZV5NFXE]].
4. A scaling argument for $x^n + y^n = z^n$: there are about $X^3$ triples with entries near $X$, and $x^n + y^n - z^n$ has size about $X^n$. If it took each value with similar probability, the expected number of solutions near $X$ would be about $X^{3-n}$. This predicts few solutions for $n \geq 4$, in agreement with [[Fermat's Last Theorem|0Y5X3SDBCZ]].
5. The [[Bateman–Horn conjecture|6NY57KQZZF]] extends the twin prime count to the prime values of several polynomials at once.

### Non-examples

1. [[Erdős's lower bound for Ramsey numbers is a proof|2D3GCG17FA]]: it uses random colourings, but every step is rigorous and the conclusion is certain. A probabilistic proof is not a heuristic argument.
2. The [[heuristics of discovery|X1NSTVGDNQ]], such as "solve a simpler problem first", are strategies for finding a solution. They do not predict a mathematical fact, so they are heuristics in another sense.
3. A table of verified cases is [[numerical evidence|JFD3QWCX8Z]], not a heuristic argument: it gives no model from which the conjecture follows.

### Basic properties

1. A heuristic argument proves nothing. Its conclusion is a conjecture, which may be false.
2. Naive models must be corrected for local structure. The twin prime model needs a factor for each small prime, which gives the constant $2C_2$.
3. A model can fail for a reason invisible to it. For $x^n + y^n = z^n$, the scaling of example 4 predicts about a constant number of solutions near each size $X$ for $n = 3$, so infinitely many in total, but [[Fermat's Last Theorem for n = 3|07NKG38VEG]] says that there are none.
4. The Cramér model fails in short intervals. Helmut Maier proved in 1985 that for each $\lambda > 1$ the number of primes in $(x, x + (\ln x)^\lambda]$ is not asymptotic to $(\ln x)^{\lambda - 1}$, as the model predicts.
5. A dimension count gives the right answer for general data, and it can fail for special data whose conditions are dependent.
6. A heuristic prediction that agrees with numerical data at many sizes is strong evidence in the sense of [[plausible reasoning|8DHD3H1CJ9]], because a precise agreement is improbable by chance.

### History

Godfrey Hardy and John Littlewood used the circle method in 1923 to derive conjectural asymptotic formulas for prime pairs and for Goldbach partitions.
Harald Cramér introduced his random model of the primes in 1936 and derived from it a conjecture on the size of [[prime gaps|2AEK2Z6RQD]].
Paul Bateman and Roger Horn stated their general conjecture in 1962.
Maier's theorem of 1985 showed the first failure of the Cramér model.
Dimension counts are classical in enumerative geometry, where they guided the work of the nineteenth century before rigorous foundations existed.

### Common errors

1. Using the naive model without local corrections. It predicts the wrong constant for twin primes, and it gives nonsense for pairs $(p, p+1)$, which are both prime only for $p = 2$.
2. Treating a heuristic as a proof. The twin prime conjecture is open despite its strong heuristic support.
3. Confusing a heuristic with a probabilistic proof. A heuristic assumes that the object behaves like a random one; a probabilistic proof studies a genuinely random object and draws a certain conclusion.

## Explanations

### L1 human

A heuristic argument is a careful guess with a reason behind it.
For example, about one number in $14$ near a million is prime.
If primes were scattered at random with this density, pairs of primes two apart would still appear again and again.
This suggests that there are infinitely many such pairs, and it even predicts how many.
The prediction matches the real counts, but it is not a proof, because primes are not truly random.

### L2 human

We compare the Cramér model with the true count of primes.

1. In the model, the expected number of primes up to $x$ is about $\operatorname{li}(x)$.
2. For $x = 10^6$: $\operatorname{li}(10^6) \approx 78627.5$, and the true count is $\pi(10^6) = 78498$.
3. The relative difference is about $0.16\%$, so the model fits the count well.
4. For twin primes the naive model predicts $\int_2^{10^6} dt/(\ln t)^2 \approx 6247$ pairs, and the true count is $8169$.
5. The factor $8169/6247 \approx 1.31$ is close to $2C_2 \approx 1.3203$, the correction for divisibility by small primes.

The typical use: a model that fits one statistic is tested on another, and the failure shows which structure the model misses.
A trap: a model that fits the counts of primes can still miss correlations between primes, as step 4 shows.

### L3 human

Heuristic arguments express a view of mathematical objects as a mixture of structure and randomness.
The structure is the set of local constraints, such as congruences modulo small primes or the algebraic identities of a variety.
The randomness is the assumption that, after these constraints, the object behaves like a generic one.
The Hardy-Littlewood constants are products of local densities, one for each prime, and the expected dimension is the generic codimension of the conditions.
A failure of a heuristic, such as Maier's theorem or the absence of solutions for $n = 3$, points to a structure the model did not include: large-scale correlations of the primes, or the arithmetic of the cubic curve $x^3 + y^3 = z^3$.
Rigorous methods, such as sieves and the circle method, sometimes follow the heuristic closely.
For twin primes and for Goldbach's conjecture, the parity problem of sieve theory is one obstacle between the heuristic and a proof.
