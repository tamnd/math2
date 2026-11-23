---
tag: 8CCG6F2FAT
kind: concept
name: Bar recursion
msc: ["03F10", "03D65", "03F35"]
topics: [8XY7JYZKFW]
audience: research
uses: [A4WR995XZP, HZ17ES9PDY, 5NVA2JRHPV, P2WS16HKD7, DC60FYCSPM, BWS0QMJJKT, WEMJBN339R, 0M4JJT780X]
sources:
  - url: https://en.wikipedia.org/wiki/Bar_recursion
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bar_recursion
    locator: Technical definition
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Comprehension
---

## Summary

Bar recursion is a recursion on finite sequences that extends the sequence one entry at a time and stops when a functional $Y$ says that the sequence is long enough.
Spector introduced it in 1962.
In his form, a functional $\Phi$ on finite sequences $s$ satisfies $\Phi(s) = G(s)$ if $Y(\hat s) < |s|$, and $\Phi(s) = H(s, \lambda x.\, \Phi(s * x))$ otherwise.
Here $\hat s$ is $s$ followed by zeros, $|s|$ is the length of $s$, and $s * x$ is $s$ with $x$ appended.

For $Y(\alpha) = \alpha(0)$ the recursion that starts at $\langle 3 \rangle$ stops at length $4$, the first length above $3$.
Adding a constant for $\Phi$ to [[Gödel's system T|A4WR995XZP]] gives the system T + BR.
By [[Spector's theorem|DSQJ1RA71N]], T + BR solves the [[Dialectica interpretation|HZ17ES9PDY]] of classical analysis: every $\Pi^0_2$ theorem of analysis has a witness term in T + BR.

## Motivation

[[Primitive recursion|5NVA2JRHPV]] goes down from $n$ to $0$, so the number of steps is known in advance.
Classical analysis, with full [[comprehension|BWS0QMJJKT]] for sets of numbers, proves more functions total than T can define.
The extra principle is countable choice, and its Dialectica interpretation needs a recursion whose number of steps is not known in advance.
Bar recursion supplies it: the recursion extends a finite sequence step by step and stops when the sequence meets the condition $Y(\hat s) < |s|$.
For a continuous $Y$, every infinite path meets the condition, so the recursion is well-founded, although its depth is unbounded.
Bar recursion relates to bar induction as primitive recursion relates to induction.

## Notation

Fix types $\rho$ and $\tau$, and write $0^\rho$ for the canonical zero of type $\rho$.
A finite sequence $s = \langle s_0, \ldots, s_{k - 1} \rangle$ of objects of type $\rho$ has length $|s| = k$, and $\rho^*$ is the type of such sequences.
Its zero extension is the function $\hat s : \mathbb{N} \to \rho$ with $\hat s(i) = s_i$ for $i < k$ and $\hat s(i) = 0^\rho$ for $i \ge k$.
For an infinite sequence $\alpha$, the initial segment of length $n$ is $\bar \alpha n = \langle \alpha(0), \ldots, \alpha(n - 1) \rangle$.
The bar recursor $\mathrm{BR}_{\rho, \tau}$ takes $Y : (\mathbb{N} \to \rho) \to \mathbb{N}$, $G : \rho^* \to \tau$ and $H : \rho^* \to (\rho \to \tau) \to \tau$, and it returns the $\Phi : \rho^* \to \tau$ given by the following equations:
$$\Phi(s) = \begin{cases} G(s) & \text{if } Y(\hat s) < |s|, \\ H(s, \lambda x^\rho.\, \Phi(s * x)) & \text{otherwise.} \end{cases}$$
Finite sequences are coded by numbers when $\rho = \mathbb{N}$, and by pairs of a length and a function in general.
Older books write $0$ for the type $\mathbb{N}$ and $1$ for $\mathbb{N} \to \mathbb{N}$, and some write $\overline{s}$ or $s @ 0$ for $\hat s$.

## Remarks

### A first bar recursion

Take $\rho = \tau = \mathbb{N}$, $Y(\alpha) = \alpha(0)$, $G(s) = |s|$ and $H(s, k) = k(0)$.
At $\langle 3 \rangle$ the condition $Y(\hat s) < |s|$ reads $3 < 1$, which fails, so $\Phi(\langle 3 \rangle) = H(\langle 3 \rangle, \lambda x.\, \Phi(\langle 3, x \rangle)) = \Phi(\langle 3, 0 \rangle)$.
In the same way $\Phi(\langle 3, 0 \rangle) = \Phi(\langle 3, 0, 0 \rangle) = \Phi(\langle 3, 0, 0, 0 \rangle)$, since $3 < 2$ and $3 < 3$ fail.
At length $4$ the condition $3 < 4$ holds, so $\Phi(\langle 3 \rangle) = G(\langle 3, 0, 0, 0 \rangle) = 4$.
The [[unbounded depth example|1598BS2RHH]] runs the same functional $Y$ from every start $\langle x \rangle$.

### Why the recursion stops

Let $Y$ be continuous, and let $\alpha$ be an infinite sequence.
Take $N$ such that $Y(\beta) = Y(\alpha)$ whenever $\beta$ agrees with $\alpha$ below $N$.
For $n \ge \max(N, Y(\alpha) + 1)$ the sequence $\widehat{\bar \alpha n}$ agrees with $\alpha$ below $N$, so $Y(\widehat{\bar \alpha n}) = Y(\alpha) < n$.
Hence every path meets the stopping condition, and the recursion is well-founded.
The depth is finite on each path but not bounded over all paths, since in the example above the start $\langle x \rangle$ needs $x$ steps.

### More cases

For $Y(\alpha) = \alpha(\alpha(0)) + 1$ the recursion from the empty sequence stops at length $2$ if $\alpha(0) \ne 1$, and at length $\alpha(1) + 2$ if $\alpha(0) = 1$, as the [[continuous example|Z754DBNY1W]] computes.

For $Y(\alpha)$ the position of the first zero of $\alpha$, and $0$ if there is none, no $\Phi$ satisfies the equations in the full set-theoretic model.
The path $1, 1, 1, \ldots$ never meets the condition, since $Y(\hat s) = |s|$ for every $s$ of ones, as the [[discontinuous non-example|BH27QPQ6ZN]] shows.

Primitive recursion on the length $|s|$ is not bar recursion, because its number of steps is fixed in advance, while bar recursion stops at a point that depends on the path.

### Models and strength

T + BR has models in which all functionals are continuous, such as the Kleene-Kreisel continuous functionals over [[Baire space|P2WS16HKD7]].
It also has a model in Bezem's strongly majorizable functionals.
The full set-theoretic model of all functionals of finite type is not a model of T + BR, by the discontinuous non-example.

Bar recursion is not definable in T.
Classical analysis proves that every term of T normalizes, so by Spector's theorem T + BR defines the evaluation function of T, and that function is not definable in T.

### Watch out

The first slip is to take the stopping length for the modulus of continuity of $Y$.
The recursion stops when $Y(\hat s) < |s|$, which can happen before or after the modulus, as the continuous example shows.

The second slip is to expect a bound on the depth of the recursion.
The depth is finite along each path, but it is not bounded over all paths.

The third slip is to assume that bar recursion exists in every model of T.
It fails in the full set-theoretic model.

### History

Spector introduced bar recursion in a paper published in 1962, after his death in 1961, to extend Gödel's Dialectica interpretation to classical analysis.
Later work gave other forms, such as the modified bar recursion of Berger and Oliva and the bar recursion of Berardi, Bezem and Coquand, which interpret countable choice under realizability.
Escardó and Oliva related bar recursion to products of selection functions and to backward induction in games.

### Try it

First, for $Y(\alpha) = \alpha(0) + \alpha(1)$ and a path with $\alpha(0) = 3$ and $\alpha(1) = 1$, find the length at which the recursion from the empty sequence stops.
At length $0$ and $1$ the values are $0$ and $3$, which fail $0 < 0$ and $3 < 1$, and from length $2$ on the value is $4$, so the first length with $4 < n$ is $n = 5$.

Second, compute $\Phi(\langle \rangle)$ for the functional of the first bar recursion above.
The condition $0 < 0$ fails, so $\Phi(\langle \rangle) = \Phi(\langle 0 \rangle)$, and at $\langle 0 \rangle$ the condition $0 < 1$ holds, so the value is $G(\langle 0 \rangle) = 1$.

## Explanations

### L1 human

Ordinary recursion counts down from a known number, so it always knows how many steps remain.
Bar recursion builds a list one entry at a time and asks a judge, after each step, whether the list is long enough.
The judge looks at the list padded with zeros and answers with a number, and if that number is less than the length, the recursion stops.
For example, if the judge reads only the first entry $x$, the recursion stops when the list has $x + 1$ entries.
Different lists stop at different lengths, with no upper bound, but every single list stops.

### L2 human

We check that the recursion is well-founded for $Y(\alpha) = \alpha(0) + \alpha(1)$ and $\rho = \mathbb{N}$.
Let $\alpha$ be any sequence, and let $c = \alpha(0) + \alpha(1)$.
For $n \ge 2$ the sequence $\widehat{\bar \alpha n}$ agrees with $\alpha$ at $0$ and $1$, so $Y(\widehat{\bar \alpha n}) = c$.
So the condition $c < n$ holds for $n = \max(2, c + 1)$, and the recursion stops on $\alpha$ at that length or earlier.

The typical use is in [[Spector's theorem|DSQJ1RA71N]], where $Y$ is a counterexample functional from the interpretation of the double negation shift.
Watch out: the modulus of continuity alone does not give the stopping length, which also needs $n > Y(\alpha)$.

### L3 human

Bar recursion is the computational content of countable choice in classical proofs, through the double negation shift.
Its variants also interpret [[dependent choice|WEMJBN339R]], and under realizability they give programs from classical proofs in [[second-order arithmetic|DC60FYCSPM]].
In the work of Escardó and Oliva it computes optimal strategies of sequential games of unbounded length, through products of selection functions.
It holds in the continuous functionals and in the strongly majorizable functionals, and it fails in the full set-theoretic model.
