---
tag: 6YY8W7HG5M
kind: concept
name: Probabilistic proofs of non-probabilistic theorems
msc: ["00A35", "41A10", "11K16", "60F15"]
topics: [GB14W4SYPK]
audience: grad
uses: [3B55HNS754, 0WQNRCNY3M, 02HZ1BK3MW, 0DFWHQ839T, 0JQE130DHW]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_probabilistic_proofs_of_non-probabilistic_theorems
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bernstein_polynomial
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Normal_number
    locator: lead section
---

## Summary

Some theorems say nothing about chance, yet their best proofs bring in a random object.
The proof reads a deterministic quantity as an [[expected value|0WQNRCNY3M]], a probability or a limit of [[random variables|0PNRKMRC55]], and then a theorem of probability finishes the job.

Here is the standard first case.
The [[Weierstrass approximation theorem|0JQE130DHW]] says that every continuous function $f$ on $[0, 1]$ is a uniform limit of polynomials.
Bernstein's proof flips a coin with success probability $x$ a total of $n$ times, counts the successes $S_n$, and looks at the average value of $f(S_n/n)$.
That average is a polynomial in $x$, and since $S_n/n$ is close to $x$ with high probability, the polynomial is close to $f(x)$.

Such a proof is fully rigorous.
A probability space is a measure space, so probability theory is a part of analysis, and every step can be rewritten as a statement about sums or integrals.
The language of probability organizes long estimates into a few standard steps, and it says in advance what a typical term should do.

## Motivation

Some estimates in analysis and number theory are sums with many terms of different sizes.
A direct estimate of such a sum can be long and opaque.
Sometimes the sum is the expected value of a random variable with a simple structure, such as a sum of independent terms.
Then general theorems control it at once: the variance bounds the spread through [[Chebyshev's inequality|02HZ1BK3MW]], and the [[strong law of large numbers|0DFWHQ839T]] gives the limit.

The finite form of the idea, in combinatorics, is the [[probabilistic method|3B55HNS754]], and its simplest cases are the [[averaging argument|HXP9VMXV8S]] and the [[counting arguments for existence|1KVSS0KRZA]].
The proofs surveyed here use the same idea with continuous probability, in approximation theory, in number theory and in potential theory.

## Notation

We write $\mathbb{P}$ for a probability and $\mathbb{E}$ for an expected value.
For $x \in [0, 1]$ and $n \ge 1$, the random variable $S_n$ has the [[binomial distribution|0WCWA1KT3M]] with parameters $n$ and $x$: it counts the successes in $n$ independent [[Bernoulli trials|0PHC9FE2V5]] with success probability $x$.
For a function $f$ on $[0, 1]$, the $n$-th [[Bernstein polynomial|0JT92VK307]] of $f$ is
$$B_n f(x) = \sum_{k=0}^{n} f\left(\frac{k}{n}\right) \binom{n}{k} x^k (1 - x)^{n-k} = \mathbb{E}\left[f\left(\frac{S_n}{n}\right)\right].$$
The second equality holds because $S_n = k$ with probability $\binom{n}{k} x^k (1 - x)^{n-k}$.

## Remarks

### Bernstein's proof of the Weierstrass theorem

Let $f \colon [0, 1] \to \mathbb{R}$ be continuous, let $M = \max |f|$, and let $\varepsilon > 0$.

1. By [[uniform continuity|0M4JJT780X]], there is $\delta > 0$ with $|f(y) - f(x)| < \varepsilon$ whenever $|y - x| < \delta$.
2. Fix $x \in [0, 1]$.
   By the formula of the Notation, $B_n f(x) - f(x) = \mathbb{E}[f(S_n/n) - f(x)]$.
3. On the event $|S_n/n - x| < \delta$, the difference $|f(S_n/n) - f(x)|$ is less than $\varepsilon$, by step 1.
   On the other event, it is at most $2M$.
4. So $|B_n f(x) - f(x)| \le \varepsilon + 2M \cdot \mathbb{P}(|S_n/n - x| \ge \delta)$.
5. The mean of $S_n/n$ is $x$, and its variance is $x(1 - x)/n \le 1/(4n)$.
6. By Chebyshev's inequality, $\mathbb{P}(|S_n/n - x| \ge \delta) \le 1/(4n\delta^2)$.
7. So, for every $x \in [0, 1]$,
   $$|B_n f(x) - f(x)| \le \varepsilon + \frac{M}{2n\delta^2}.$$
8. For $n \ge M/(2\varepsilon\delta^2)$, the error is at most $2\varepsilon$ at every point, so $B_n f \to f$ [[uniformly|08VZ57PT26]].

Each $B_n f$ is a polynomial of degree at most $n$, so the theorem follows.
Step 6 is the identity $\sum_k (k - nx)^2 \binom{n}{k} x^k (1 - x)^{n-k} = nx(1 - x)$ in disguise, so the proof can be written with no probability at all, but the probabilistic form shows why each step is natural.

### Borel's theorem on normal numbers

A real number $x \in [0, 1)$ is [[normal|C98T2T5FJS]] in base $b$ if each block of $L$ digits appears in its base $b$ expansion with limit frequency $b^{-L}$, for every $L \ge 1$.
Borel's theorem says that almost every real number is normal in every base.

1. Choose $x$ at random in $[0, 1)$, with the [[Lebesgue measure|2Z2QVWZ262]] as the probability.
2. The binary digits $d_1, d_2, \ldots$ of $x$ are then independent, and each is $0$ or $1$ with probability $1/2$.
3. By the strong law of large numbers, $(d_1 + \cdots + d_n)/n \to 1/2$ with probability $1$.
4. So the set of $x$ where the frequency of the digit $1$ is not $1/2$ is a [[null set|VQQM4Y550T]].
5. The same argument works for each base $b$ and each block $w$ of length $L$: split the positions into $L$ classes modulo $L$, so that the blocks that start in one class do not overlap and are independent.
6. There are countably many pairs $(b, w)$, and a countable union of null sets is a null set.
7. So the set of numbers that fail to be normal in some base is a null set.

The proof shows that normal numbers exist, and it names none.

### More examples

In number theory, the [[Hardy-Ramanujan theorem|ZJNW10PZKK]] says that almost every integer $n$ has about $\ln \ln n$ distinct prime factors.
Turán's proof computes the mean and the [[variance|0477R9PYAE]] of the number of prime factors over $n \le N$, both of size about $\ln \ln N$, and Chebyshev's inequality then shows that the proportion of $n \le N$ far from the mean tends to $0$.
The [[Erdős-Kac theorem|BY5WRND0J1]] refines this: the number of distinct prime factors of $n$ is approximately normally distributed, with mean and variance $\ln \ln n$.

In potential theory, [[Kakutani's solution|CCEKM4241P]] of the [[Dirichlet problem|8D56GQ4AG8]] gives the harmonic function at a point as the expected boundary value at the place where a [[Brownian motion|22735FGJV6]] started at that point first leaves the domain.
In combinatorics, a random coloring proves the [[lower bound for Ramsey numbers|SAZNT80CG5]].

### What is not a probabilistic proof

A proof of a theorem about random objects, such as the law of large numbers itself, is a proof in probability theory, and its statement already involves chance.
A heuristic that treats the primes as random gives predictions, for example on the gaps between primes, but it is not a proof, because the primes are a fixed set and the model is not derived from the definition of a prime.
A Monte Carlo estimate of an integral is not a proof of its value either: a random sample gives a value that is probably close, and a proof needs a bound that holds with certainty.

### The rules of the game

Positive probability gives existence: if a random object has a property with probability greater than $0$, then some object has it.
Probability $1$ gives "almost all", not "all": the rational numbers are not normal, and they form a null set.
The probability can always be removed, since every statement on a finite or a measure space is a statement about sums or integrals.
The proofs often give rates: for $f(x) = x^2$ the error of $B_n f$ is exactly $x(1 - x)/n$, at most $1/(4n)$.
And measure-theoretic existence proofs are non-constructive, like counting arguments.

### Watch out

It is a mistake to think that a probabilistic proof is only a heuristic.
A proof on a probability space is as rigorous as any proof in analysis.
It is also a mistake to read "with probability $1$" as "for every element".
Bernstein's proof gives every point, while Borel's proof gives almost every point only.
And a fixed object is not random: the binary digits of $\sqrt{2}$ are fixed, and the independence of digits holds only for a randomly chosen $x$, so Borel's theorem says nothing about whether $\sqrt{2}$ is normal.

### History

Karl Weierstrass proved his approximation theorem in 1885, and Sergei Bernstein gave the probabilistic proof with his polynomials in 1912.
Émile Borel proved in 1909 that almost every real number is normal, and David Champernowne gave an explicit base $10$ normal number in 1933.
Pál Turán gave his variance proof of the Hardy-Ramanujan theorem in 1934, and Shizuo Kakutani connected Brownian motion with the Dirichlet problem in 1944.
Burgess Davis later gave a proof of [[Picard's little theorem|R2PHM118NG]] with Brownian motion.

### Try it

First, compute $B_1 f$ for $f(x) = x^2$.
It is $f(0)(1 - x) + f(1)x = x$, so the error is $x - x^2 = x(1 - x)$, which matches the formula $x(1 - x)/n$ with $n = 1$.

Second, bound $\mathbb{P}(|S_{100}/100 - 1/2| \ge 0.1)$ for $x = 1/2$ by Chebyshev's inequality.
The variance of $S_{100}/100$ is $1/400$, so the bound is $(1/400)/0.01 = 1/4$.

## Explanations

### L1 human

Some facts about numbers and curves contain no chance at all.
Mathematicians can still prove them with coin flips inside the argument.
For example, flip a fair coin many times, and about half of the flips come up heads.
In the same way, a number chosen at random has about half of its binary digits equal to $1$.
So numbers with this property exist, even though the statement says nothing about chance.

### L2 human

We compute the Bernstein polynomials of $f(x) = x^2$ and check the error bound.
By the Notation, $B_n f(x) = \mathbb{E}[(S_n/n)^2]$, and for any random variable $Y$ we have $\mathbb{E}[Y^2] = \operatorname{Var}(Y) + (\mathbb{E}[Y])^2$.
With $Y = S_n/n$, the mean is $x$ and the variance is $x(1 - x)/n$, so
$$B_n f(x) = x^2 + \frac{x(1 - x)}{n}.$$
Check with $n = 2$ by the sum:
$$B_2 f(x) = 0 \cdot (1 - x)^2 + \tfrac{1}{4} \cdot 2x(1 - x) + 1 \cdot x^2 = x^2 + \frac{x(1 - x)}{2}.$$
The error $x(1 - x)/n$ has its maximum $1/(4n)$ at $x = 1/2$.

The variance gives the rate of approximation at once, and this is the typical gain of the probabilistic view.
Watch out: $B_n f$ need not agree with $f$ at the points $k/n$.
For example, $B_2 f(1/2) = 1/4 + 1/8 = 3/8$, but $f(1/2) = 1/4$.

### L3 human

Probabilistic proofs fall into a few patterns.
In the first, a deterministic quantity is an expected value, and concentration inequalities control it: Bernstein's proof, Turán's proof and the probabilistic method in combinatorics.
In the second, a set of measure $1$ is nonempty: Borel's theorem and many results on typical elements in analysis.
In the third, a stochastic process solves a differential equation: Brownian motion gives harmonic functions, and the Feynman-Kac formula extends this to the heat equation with a potential.

The same ideas run through later areas.
Probabilistic number theory studies arithmetic functions as sums of almost independent random variables.
In ergodic theory, Furstenberg's correspondence principle turns statements about sets of integers into statements about measure-preserving systems.
In complexity theory, random choices prove the existence of good objects such as expanders and codes, and the search for explicit constructions is a separate problem.
