---
tag: XR1JXQG1CD
kind: concept
name: Proof mining
msc: ["03F10", "03F60", "03F35"]
topics: [8XY7JYZKFW]
audience: research
uses: [HZ17ES9PDY, 4BCD1EM542, DSQJ1RA71N, YWZQC5E54B, 0PWX18FM4G, 0FM6N4R0VB, VF6CA0VE41, A4WR995XZP]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_mining
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Georg_Kreisel
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Variants
---

## Summary

Euclid's proof that there are infinitely many primes looks at a prime factor of $n! + 1$, so it quietly proves more: for every $n$ there is a prime $p$ with $n < p \le n! + 1$.
Proof mining is the craft of finding such hidden numbers in proofs, including proofs that use excluded middle, compactness or choice and look nonconstructive.

Precisely, proof mining (Kreisel called it the unwinding of proofs) takes a proof of a theorem of a suitable logical form and extracts explicit quantitative data with a proof that the data are correct.
The data are a bound, a [[rate of convergence|YWZQC5E54B]], or a rate of metastability.
The main tools are proof interpretations: the monotone form of the [[Dialectica interpretation|HZ17ES9PDY]] and the [[no-counterexample interpretation|4BCD1EM542]].
The general logical metatheorems guarantee in advance that the data exist and say what they depend on.

## Motivation

Many theorems of analysis have the form $\forall x \, \exists n \, A(x, n)$, and their usual proofs give no way to compute $n$ from $x$.
Proof interpretations show that, when $A$ has a simple enough form, the proof still contains a computable bound on $n$.
Often the bound depends on $x$ only through a few numbers, such as a bound on a norm or the diameter of a space, and this uniformity is new mathematical information.

For example, let $T$ be a [[nonexpansive map|VF6CA0VE41]] of a bounded convex subset $C$ of a normed space into itself, and iterate $x_{k+1} = \tfrac{1}{2}(x_k + T x_k)$.
Then $\lVert x_k - T x_k \rVert \to 0$, and the analysis of the proof gives a rate that depends only on $\varepsilon$ and a bound on the diameter of $C$.
It does not depend on $T$, on the space or on the starting point.
Results of this kind in fixed point theory, ergodic theory and approximation theory are the main applications.

Convergence theorems have the more complex form $\forall \varepsilon \, \exists n \, \forall i, j \ge n$, and then a computable rate may not exist at all.
Metastability is the finite reformulation that can always be extracted, and it is the subject of the first example below.

## Notation

Let $(a_n)$ be a sequence in a metric space.
A *rate of metastability* for it is a function $\Phi(\varepsilon, g)$ of $\varepsilon > 0$ and $g : \mathbb{N} \to \mathbb{N}$ with this property: some $n \le \Phi(\varepsilon, g)$ has $d(a_i, a_j) \le \varepsilon$ for all $i, j \in [n, n + g(n)]$.
We write $\tilde g(n) = n + g(n)$ and $\tilde g^{(k)}$ for the $k$-th iterate of $\tilde g$.

The monotone interpretation uses Howard's majorizability relation $x^* \mathrel{\mathrm{maj}} x$ between functionals of the same finite type.
At type $0$ it means $x^* \ge x$.
At type $\rho \to \tau$ it means that $y^* \mathrel{\mathrm{maj}} y$ implies $x^* y^* \mathrel{\mathrm{maj}} x y$.
Books on the subject often use Bezem's variant, strong majorizability, which adds a monotonicity condition on $x^*$.

## Remarks

### A first rate of metastability

Take a nonincreasing sequence $(a_n)$ in $[0, 1]$, so it converges by the [[monotone convergence theorem|0FM6N4R0VB]].
Fix $\varepsilon = \tfrac{1}{2}$ and the window rule $g(n) = n + 1$, so $\tilde g(n) = 2n + 1$.
Jump from window to window, starting at $0$:
$$n_0 = 0, \qquad n_1 = \tilde g(0) = 1, \qquad n_2 = \tilde g(1) = 3.$$
On each window $[n_k, n_{k+1}]$ the sequence falls by $a_{n_k} - a_{n_{k+1}}$, and two falls of more than $\tfrac{1}{2}$ would add up to more than $1$.
So one of the windows $[0, 1]$ and $[1, 3]$ is quiet, and $\Phi = 3$ bounds its start.
For the sequence $1, 0.4, 0.3, 0.3, \dots$ the first window falls by $0.6$ and the second by $0.1$, so $n = 1$ is the witness.
The [[general rate for monotone sequences|8WH2SKSAZD]] is $\Phi(\varepsilon, g) = \tilde g^{(\lceil 1/\varepsilon \rceil)}(0)$, the same for every such sequence.

### Bounds hidden in existence proofs

The proof of [[Euclid's theorem|0292EPPPT0]] gives the witness "the least prime factor of $n! + 1$", and the [[bound on the next prime|S0GAFZK93F]] works it out.
For $n = 4$ we get $4! + 1 = 25 = 5 \cdot 5$, so $p = 5$.
This is a primitive recursive witness for a $\Pi^0_2$ theorem, as [[Parsons's theorem|2VYJXZZDGB]] predicts for proofs in $\mathrm{I}\Sigma_1$.

In general, let PA prove $\forall x \, \exists n \, A(x, n)$ with $A$ quantifier-free.
The negative translation followed by the monotone Dialectica interpretation gives a closed term $t^*$ of [[Gödel's system T|A4WR995XZP]] with $n \le t^*(x)$ for some witness $n$.
Proofs that use countable or dependent choice need [[Spector's bar recursion|DSQJ1RA71N]], but most proofs in practice use only weak fragments, and these give much better bounds.

### Where extraction stops

A [[Specker sequence|P9W51PW5HK]] is computable, nondecreasing and bounded, yet it has no computable rate of convergence.
So the monotone convergence theorem, of the form $\forall \varepsilon \, \exists n \, \forall i, j \ge n$, admits no extraction of a rate of convergence.
The metastable form still holds for this sequence, with the same uniform rate, because the window argument works for rising sequences as well as for falling ones.

The same limit appears for any $\Pi^0_3$ theorem: the witness for the middle quantifier as a function of the first can be noncomputable.
The [[Skolem function for the halting formula|7RFM1XPJQV]] is the standard case.

### From convergence to metastability

The Cauchy property of $(a_n)$ reads $\forall \varepsilon \, \exists n \, \forall i, j \ge n \, (d(a_i, a_j) \le \varepsilon)$.
Its no-counterexample form takes a function $g$ that tries to refute each $n$ by a far point, and asks for an $n$ that survives the test on $[n, n + g(n)]$.
Classically the two forms are equivalent, because a counterexample to the Cauchy property gives a $g$ that defeats every $n$.
The metastable form has the shape $\forall \varepsilon \, \forall g \, \exists n$ with a bounded inner part, and that shape is what the metatheorems can handle.

### Watch out

The first slip is to expect a rate of convergence from every classical convergence proof.
The Specker sequence shows that none need exist, and the honest output is a rate of metastability.

The second slip is to read a rate of metastability as a rate of convergence.
The window rule $g$ is an input, so $\Phi(\varepsilon, g)$ says nothing about a single $n$ that works for every $g$.

The third slip is to think that the bound must be read off a formal derivation.
In practice the logical analysis guides an ordinary proof, and the final paper is written in the language of analysis.

### History

Kreisel proposed the unwinding of proofs in the 1950s, with the no-counterexample interpretation as his main tool.
Kohlenbach turned it into a systematic program in the 1990s and 2000s.
He introduced the monotone functional interpretation and proved general logical metatheorems for classes of metric and normed spaces, partly with Gerhardy.
Tao used the name metastability in 2007, in his work on finite forms of convergence principles.

### Try it

First, compute the rate $\tilde g^{(K)}(0)$ for $\varepsilon = \tfrac{1}{3}$ and $g(n) = 1$.
Here $K = 3$ and $\tilde g(n) = n + 1$, so the iterates are $1, 2, 3$ and $\Phi = 3$.

Second, does the rate for nonincreasing sequences in $[0, 1]$ also work for nonincreasing sequences in $[0, 2]$?
No: the total fall can be $2$, so we need $K = \lceil 2/\varepsilon \rceil$ windows.

## Explanations

### L1 human

Some proofs show that a number exists without saying how large it is.
Proof mining reads such a proof again with logical tools and finds an explicit bound for the number.
For example, the proof that there are infinitely many primes multiplies the numbers up to $n$ and adds $1$.
Read closely, it shows that there is always a prime between $n$ and $n! + 1$.
For $n = 3$ the number is $7$, which is itself a prime above $3$.

### L2 human

We derive the metastable form of the Cauchy property and see why it is the right target.
The Cauchy property says that for each $\varepsilon$ some $n$ has every later pair $i, j$ within $\varepsilon$.
Suppose we are given a rule $g$ that names, for each candidate $n$, a window $[n, n + g(n)]$ in which to look for a bad pair.
The metastable form asks for an $n \le \Phi(\varepsilon, g)$ whose window has no bad pair.

For monotone sequences in $[0, 1]$ we can take $\Phi(\varepsilon, g) = \tilde g^{(\lceil 1/\varepsilon \rceil)}(0)$, because each bad window uses up more than $\varepsilon$ of a total fall of at most $1$.
This $\Phi$ is computable and does not depend on the sequence, even though no computable rate of convergence exists in general.
That pattern, a uniform rate of metastability where a rate of convergence fails, is the typical result in ergodic theory and fixed point theory.
The trap is to forget that $g$ is part of the input.

### L3 human

Proof mining treats a classical proof as a program, in the spirit of the Curry-Howard correspondence, but it asks for majorants of witnesses in place of exact witnesses.
The logical metatheorems are uniform boundedness principles: for conclusions of a given logical form, compactness arguments yield bounds that are independent of the points of bounded spaces.
They rest on the [[Dialectica interpretation|HZ17ES9PDY]] combined with the negative translation, and on bar recursion when choice is used.
Metastable convergence links proof mining with the finitary methods of Tao in ergodic theory and with computable analysis.
