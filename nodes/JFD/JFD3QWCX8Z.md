---
tag: JFD3QWCX8Z
kind: concept
name: Numerical evidence for conjectures
aliases: [computational-evidence, verification-up-to-a-bound]
msc: ["00A35", "11Y35", "11N05"]
topics: [DME0TPC348]
audience: research
uses: [8DHD3H1CJ9, WMEMMHZ3BH, 0ED72CTBNP, 0RQSNVTFVZ]
sources:
  - url: https://en.wikipedia.org/wiki/Skewes%27s_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/P%C3%B3lya_conjecture
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mertens_conjecture
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
    locator: Computational results
---

## Summary

Numerical evidence for a [[conjecture|WMEMMHZ3BH]] is the check, by computation, of many of its cases.
It makes the conjecture more believable, and it says nothing certain about the cases beyond the check.

Here is the case that every number theorist knows.
Give each integer $n \ge 1$ the sign $\lambda(n) = +1$ when $n$ has an even number of prime factors, counted with repetition, and $-1$ when the number is odd.
So $\lambda(1) = 1$, $\lambda(2) = \lambda(3) = -1$, $\lambda(4) = 1$ and $\lambda(12) = -1$, since $12 = 2 \cdot 2 \cdot 3$.
The running total $L(n) = \lambda(1) + \cdots + \lambda(n)$ starts
$$1, 0, -1, 0, -1, 0, -1, -2, -1, 0, -1, -2, -3, \ldots$$
In 1919 George Pólya asked whether $L(n) \le 0$ for every $n \ge 2$.
It is true for every $n$ from $2$ to $906150256$, and then $L(906150257) = 1$.
More than $9 \cdot 10^8$ checked cases did not make the conjecture true.

A typical claim of numerical evidence reads "the statement holds for every $n \le N$" with a large bound $N$.
Such a claim supports the conjecture by [[plausible reasoning|8DHD3H1CJ9]].
Its weight depends on whether the checked range reaches the scale at which a failure could appear.

## Motivation

Many conjectures in number theory and combinatorics are statements about all integers.
A computer can check the first $10^{12}$ or $10^{18}$ cases, and for most such conjectures it finds no [[counterexample|0ED72CTBNP]].
How much belief should such a check produce?

The answer is not a count of cases.
In number theory many quantities grow like $\ln x$ or $\ln \ln x$, and $\ln \ln 10^{18}$ is only about $3.7$.
A failure that needs $\ln \ln x$ to reach about $6.6$ can stay out of reach of every possible computer.
So numerical evidence must be read with an idea of the scale of the problem, and that idea often comes from a [[heuristic argument|VCQQNJ3SEZ]].

## Notation

For a statement $P(n)$ about integers $n \ge n_0$, "$P$ is verified up to $N$" means that $P(n)$ holds for every $n$ with $n_0 \le n \le N$.
If $P$ is false, its least counterexample is the least $n$ with $P(n)$ false.
The [[prime-counting function|0RQSNVTFVZ]] $\pi(x)$ is the number of primes up to $x$, and the [[logarithmic integral|VP98WSTZWT]] is
$$\operatorname{li}(x) = \int_0^x \frac{dt}{\ln t},$$
taken as a principal value at $t = 1$.
$L(n)$ is the sum of the [[Liouville function|07NN4VNYWM]] $\lambda$, and $M(x) = \sum_{k \le x} \mu(k)$ is the Mertens function, the sum of the [[Möbius function|0FANE7P0DY]] $\mu$.

## Remarks

### Three conjectures that the computers supported

Gauss noticed in his tables that $\pi(x) < \operatorname{li}(x)$, and the inequality holds at every $x$ ever computed; see [[pi(x) < li(x) for all computed x|Q61WD2AEBS]].
At $x = 10^6$, for example, $\pi(x) = 78498$ and $\operatorname{li}(x) \approx 78627.5$.
Yet [[Littlewood's theorem|D7XGABGKW8]] of 1914 says that $\pi(x) - \operatorname{li}(x)$ changes sign infinitely often.
The first change is now known to come below $1.4 \cdot 10^{316}$, far beyond any table.

The [[Mertens conjecture|4Y4HWKA2MP]] says $|M(x)| < \sqrt{x}$ for $x > 1$.
The first values $M(1), \ldots, M(10)$ are $1, 0, -1, -1, -2, -1, -2, -2, -2, -1$, all well inside the bound, and computation never found a violation.
Andrew Odlyzko and Herman te Riele proved in 1985 that the conjecture is false, and no counterexample is known.

The Pólya conjecture of the Summary is the third case.
Brian Haselgrove proved in 1958 that it is false without giving a counterexample, and Minoru Tanaka found the least one, $906150257$, in 1980.

### What strong evidence looks like

[[Goldbach partitions grow with n|RKFZV5NFXE]] shows a stronger kind of evidence.
Goldbach's conjecture has been verified up to $4 \cdot 10^{18}$.
More than that, the number of ways to write $n$ as a sum of two primes grows with $n$ at the rate that the Hardy-Littlewood heuristic predicts.
A quantitative prediction confirmed at many sizes is harder to match by chance than a yes or no property.
The [[Collatz conjecture|6PCQEXEX4N]] and the [[Riemann hypothesis|VCGF9YR36X]] also have very large verifications and remain open.

### What it is not

[[A finite check of Goldbach from 4 to 100|H7Q74MWE2S]] is not numerical evidence, because a check of every case of a statement about finitely many numbers is a proof of that statement.
A [[heuristic argument|VCQQNJ3SEZ]], such as a random model of the primes, supports a conjecture without checking any of its cases, so it is evidence of another kind.
The proof of Odlyzko and te Riele is not a check of cases either: it is a deduction about all $x$ at once.

### The rules you can use

A verification up to $N$ proves $P(n)$ for $n \le N$ and gives no logical information about $n > N$.
If the failure is controlled by a slowly growing function such as $\ln \ln x$, even a very large $N$ may lie below the first counterexample.
Agreement between the data and an independent heuristic model is stronger evidence than either one alone.
A conjecture can be disproved without a known counterexample, as the Mertens and Pólya cases show.

### Watch out

The first error is "verified up to $10^{18}$, so true".
A pattern that holds in many cases is not a proof, and the three conjectures above held in more cases than anyone checked by hand.

The second error is to ignore the scale.
A check up to $10^{18}$ covers only $\ln \ln x \le 3.72$, which is small for questions controlled by $\ln \ln x$.

The third error is to report a verification without its method.
A claim of verification is itself a computation that can contain errors, so the method and the bound must be stated.

### History

John Littlewood proved in 1914 that $\pi(x) - \operatorname{li}(x)$ changes sign infinitely often, without a bound for the first change.
Stanley Skewes gave such a bound in 1933, $e^{e^{e^{79}}}$, under the assumption of the Riemann hypothesis.
In 1955 he gave a bound without that assumption, about $10^{10^{10^{964}}}$; see [[Skewes's number|71JVW6G7M1]].
Pólya stated his conjecture in 1919, Haselgrove disproved it in 1958, and Tanaka found the least counterexample in 1980.
Franz Mertens published his conjecture in 1897, and Odlyzko and te Riele disproved it in 1985.

### Try it

Compute $L(13)$ from the list of signs and check the Pólya inequality there.
The signs for $11$, $12$ and $13$ are $-1$, $-1$ and $-1$, and $L(10) = 0$, so $L(13) = -3 \le 0$.

How far does a check up to $10^{18}$ reach on the scale of $\ln \ln x$, compared with a check up to $10^9$?
We get $\ln \ln 10^9 \approx 3.03$ and $\ln \ln 10^{18} \approx 3.72$, so a billion times more cases move the scale by less than $0.7$.

## Explanations

### L1 human

Suppose a rule about numbers works for the first billion numbers.
Most people would believe it, and most of the time they would be right.
But some rules work for billions of numbers and then fail.
The rule "there are fewer primes up to $x$ than a certain smooth estimate" works for every number ever tested, and it is known to fail far beyond.
So a computer check makes a guess more believable, but it does not make it certain.

### L2 human

We measure how far a computation reaches on the scale of $\ln \ln x$.
For $x = 10^6$ we get $\ln x \approx 13.8$ and $\ln \ln x \approx 2.63$.
For $x = 4 \cdot 10^{18}$, the Goldbach bound, we get $\ln x \approx 42.8$ and $\ln \ln x \approx 3.76$.
For $x = 1.4 \cdot 10^{316}$, near the first known region where $\pi(x) > \operatorname{li}(x)$, we get
$$\ln x \approx 728, \qquad \ln \ln x \approx 6.59.$$
Going from $10^6$ to $4 \cdot 10^{18}$ multiplies $x$ by more than $10^{12}$, but it raises $\ln \ln x$ only from $2.63$ to $3.76$.

The typical use is a question to ask before trusting a verification: which function of $x$ controls a possible failure?
Watch out for a quantity that depends on $\ln \ln x$, because then every computer range is small and the absence of counterexamples says little.

### L3 human

Littlewood's theorem states
$$\pi(x) - \operatorname{li}(x) = \Omega_{\pm}\!\left( \frac{\sqrt{x} \, \ln \ln \ln x}{\ln x} \right).$$
Under the Riemann hypothesis the explicit formula writes $\pi(x) - \operatorname{li}(x)$ as a term $-\tfrac12 \operatorname{li}(\sqrt{x})$, which comes from the squares of primes, plus a sum over the zeros of the zeta function and smaller terms.
The first term is negative and of size about $\sqrt{x}/\ln x$.
The sum over zeros overcomes it only when many zeros contribute with the same sign, which is rare.
The Mertens and Pólya conjectures fail for a similar reason: the sum over zeros has unbounded oscillations, but they grow very slowly.
This is the exact sense in which small numbers mislead, the theme of the [[strong law of small numbers|8AFXPXCE3N]].
