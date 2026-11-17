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

Numerical evidence for a [[conjecture|WMEMMHZ3BH]] is the verification, by computation, of many of its special cases.
A typical form is "the statement holds for every $n \leq N$" with a large bound $N$.
Such evidence supports the conjecture by [[plausible reasoning|8DHD3H1CJ9]], and it proves nothing about the cases beyond $N$.
Its weight depends on whether the checked range reaches the scale at which a failure could appear.
Some conjectures with enormous numerical evidence are false: the inequality $\pi(x) < \operatorname{li}(x)$ holds for every $x$ ever computed, and it fails for some $x$ below $1.4 \cdot 10^{316}$.

## Motivation

Many conjectures in number theory and combinatorics are statements about all integers.
A computer can check the first $10^{12}$ or $10^{18}$ cases, and for most such conjectures it finds no [[counterexample|0ED72CTBNP]].
The question is how much belief such a check should produce.

The answer is not a simple count of cases.
In number theory many quantities grow like $\ln x$ or $\ln \ln x$, and $\ln \ln 10^{18} \approx 3.7$.
A failure that needs $\ln \ln x$ to be about $6.6$ can stay invisible to every possible computer.
So numerical evidence must be read together with an idea of the scale of the problem, often supplied by a [[heuristic argument|VCQQNJ3SEZ]].

## Notation

For a statement $P(n)$ about integers $n \geq n_0$, "$P$ is verified up to $N$" means that $P(n)$ holds for every $n$ with $n_0 \leq n \leq N$.
If $P$ is false, its least counterexample is the least $n$ with $P(n)$ false.
[[$\pi(x)$|0RQSNVTFVZ]] is the number of primes up to $x$, and $\operatorname{li}(x) = \int_0^x dt/\ln t$ is the [[logarithmic integral|VP98WSTZWT]], taken as a principal value at $t = 1$.
$L(n) = \sum_{k \leq n} \lambda(k)$ is the summatory [[Liouville function|07NN4VNYWM]], and $M(x) = \sum_{k \leq x} \mu(k)$ is the Mertens function of the [[Möbius function|0FANE7P0DY]].

## Remarks

### Examples

1. [[Goldbach partitions grow with n|RKFZV5NFXE]]: Goldbach's conjecture is verified up to $4 \cdot 10^{18}$. The number of ways to write $n$ as a sum of two primes grows with $n$, which makes the evidence stronger than a count of cases.
2. [[pi(x) < li(x) for all computed x|Q61WD2AEBS]]: the inequality holds at every computed value, yet Littlewood proved in 1914 that $\pi(x) - \operatorname{li}(x)$ changes sign infinitely often.
3. The Pólya conjecture: $L(n) \leq 0$ for $2 \leq n < 906150257$, and $L(906150257) = 1$. The conjecture was true for more than $9 \cdot 10^8$ cases; see the [[counterexample|0ED72CTBNP]] page.
4. The [[Mertens conjecture|4Y4HWKA2MP]]: $|M(x)| < \sqrt{x}$ holds for every computed $x$. Andrew Odlyzko and Herman te Riele proved in 1985 that it is false, without finding a counterexample.
5. The [[Collatz conjecture|6PCQEXEX4N]] and the [[Riemann hypothesis|VCGF9YR36X]] have extensive numerical verification and remain open.

### Non-examples

1. [[A finite check of Goldbach from 4 to 100|H7Q74MWE2S]]: a computation of every case of a statement about finitely many numbers is a proof of that statement, not evidence for it.
2. A [[heuristic argument|VCQQNJ3SEZ]], such as a probabilistic model of the primes, supports a conjecture without checking any of its cases. It is evidence of another kind.
3. A [[proof|0B94TKFQJX]] that a counterexample exists, such as the proof of Odlyzko and te Riele, is a deduction about all cases, not a verification of particular cases.

### Basic properties

1. Verification up to $N$ proves $P(n)$ for $n \leq N$ and gives no logical information about $n > N$.
2. If the deviation from the conjectured behaviour is controlled by a slowly growing function, such as $\ln \ln x$, then even a very large $N$ may lie below the scale of the first counterexample.
3. A quantitative prediction tested at many sizes is stronger evidence than a yes or no property tested at many sizes. The growth of the Goldbach counts at the predicted rate is an example.
4. Agreement between the data and an independent heuristic model is stronger evidence than either alone.
5. A conjecture can be disproved without a known counterexample, as the Mertens conjecture shows. The least counterexample can be far beyond any computation.

### History

Gauss guessed the [[prime number theorem|0EHBY5Y84N]] from tables of primes, and he observed that $\operatorname{li}(x)$ exceeds $\pi(x)$ in his tables.
John Littlewood proved in 1914 that the sign of $\pi(x) - \operatorname{li}(x)$ changes infinitely often.
Stanley Skewes gave in 1933, assuming the Riemann hypothesis, an explicit bound for the first change, and in 1955 a bound without that assumption; see [[Skewes's number|71JVW6G7M1]].
Pólya stated his conjecture in 1919; Brian Haselgrove disproved it in 1958, and Minoru Tanaka found the least counterexample in 1980.
The Mertens conjecture dates from 1897 and was disproved in 1985.

### Common errors

1. "Verified up to $10^{18}$, so true." Verification is evidence, and the cases above show that it can mislead.
2. Ignoring the scale. A check up to $10^{18}$ covers only $\ln \ln x \leq 3.8$, which is small for questions controlled by $\ln \ln x$.
3. Reporting a verification without its method. A claim of verification is itself a computation that can contain errors, and the method and the bound must be stated.

## Explanations

### L1 human

Suppose a rule about numbers works for the first billion numbers.
Most people would believe it, and most of the time they would be right.
But some rules work for billions of numbers and then fail.
The rule "there are always fewer primes up to $x$ than a certain smooth estimate" works for every number ever tested, and it is known to fail far beyond.
So a computer check makes a guess more believable, but it does not make it certain.

### L2 human

We measure how far a computation reaches on the scale of $\ln \ln x$.

1. For $x = 10^6$: $\ln x \approx 13.8$ and $\ln \ln x \approx 2.63$.
2. For $x = 4 \cdot 10^{18}$, the Goldbach bound: $\ln x \approx 42.8$ and $\ln \ln x \approx 3.76$.
3. For $x \approx 1.4 \cdot 10^{316}$, near the first known region where $\pi(x) > \operatorname{li}(x)$: $\ln x \approx 728$ and $\ln \ln x \approx 6.59$.
4. Going from $10^6$ to $10^{18}$ multiplies $x$ by $10^{12}$, but it raises $\ln \ln x$ only from $2.63$ to $3.72$.

The typical use: before trusting a verification, ask which function of $x$ controls the possible failure.
A trap: a phenomenon that depends on $\ln \ln x$ is invisible in any computer range, so the absence of counterexamples says little.

### L3 human

The theorem of Littlewood is $\pi(x) - \operatorname{li}(x) = \Omega_{\pm}\!\left(\dfrac{\sqrt{x}\, \ln \ln \ln x}{\ln x}\right)$.
Under the Riemann hypothesis, and up to smaller terms, the explicit formula writes $\pi(x) - \operatorname{li}(x)$ as $-\tfrac12 \operatorname{li}(\sqrt{x})$, from the prime squares, plus a sum over the zeros of the zeta function.
The first term is negative and of size about $\sqrt{x}/\ln x$, and the sum over zeros overcomes it only when many zeros contribute with the same sign, a rare event.
The Mertens and Pólya conjectures fail for a similar reason: the sum over zeros has unbounded oscillations, but they grow very slowly.

This is the precise sense in which the small numbers mislead, the theme of the [[strong law of small numbers|8AFXPXCE3N]].
