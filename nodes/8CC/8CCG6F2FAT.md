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

Bar recursion is a form of recursion on finite sequences, introduced by Spector in 1962, in which the recursion stops when a functional $Y$ says that the sequence is long enough.
In Spector's form, a functional $\Phi$ on finite sequences $s$ satisfies $\Phi(s) = G(s)$ if $Y(\hat s) < |s|$, and $\Phi(s) = H(s, \lambda x.\, \Phi(s * x))$ otherwise.
Here $\hat s$ is $s$ followed by zeros, $|s|$ is the length of $s$, and $s * x$ is $s$ with $x$ appended.
Adding a constant for $\Phi$ to [[Gödel's system T|A4WR995XZP]] gives the system T + BR.
The idea matters because T + BR solves the [[Dialectica interpretation|HZ17ES9PDY]] of classical analysis, by [[Spector's theorem|DSQJ1RA71N]]: every $\Pi^0_2$ theorem of analysis has a witness term in T + BR.

## Motivation

[[Primitive recursion|5NVA2JRHPV]] goes down from $n$ to $0$, so the number of steps is known in advance.
Classical analysis, with full [[comprehension|BWS0QMJJKT]] for sets of numbers, proves more total functions than T can define.
The extra principle is countable choice, and its Dialectica interpretation needs a recursion whose number of steps is not known in advance.
Bar recursion supplies it: the recursion extends a finite sequence step by step and stops when the sequence meets the condition $Y(\hat s) < |s|$.
For a continuous $Y$, every infinite path meets the condition, so the recursion is well-founded, although its depth is unbounded.
Bar recursion relates to bar induction as primitive recursion relates to induction.

## Notation

Fix types $\rho$ and $\tau$, and write $0^\rho$ for the canonical zero of type $\rho$.
A finite sequence $s = \langle s_0, \ldots, s_{k - 1} \rangle$ of objects of type $\rho$ has length $|s| = k$.
Its zero extension is the function $\hat s : 0 \to \rho$ with $\hat s(i) = s_i$ for $i < k$ and $\hat s(i) = 0^\rho$ for $i \ge k$.
For an infinite sequence $\alpha$, $\bar \alpha n = \langle \alpha(0), \ldots, \alpha(n - 1) \rangle$ is its initial segment of length $n$.
The bar recursor $\mathrm{BR}_{\rho, \tau}$ takes $Y : (0 \to \rho) \to 0$, $G : \rho^* \to \tau$ and $H : \rho^* \to (\rho \to \tau) \to \tau$, and returns $\Phi : \rho^* \to \tau$ with
$$\Phi(s) = \begin{cases} G(s) & \text{if } Y(\hat s) < |s|, \\ H(s, \lambda x^\rho.\, \Phi(s * x)) & \text{otherwise.} \end{cases}$$
Finite sequences are coded by numbers when $\rho = 0$, and by pairs of a length and a function in general.
Some books write $\overline{s}$ or $s @ 0$ for $\hat s$.

## Remarks

### Examples

- [[The depth of a bar recursion is unbounded|1598BS2RHH]]: for $Y(\alpha) = \alpha(0)$, the recursion from $\langle x \rangle$ stops at length $x + 1$.
- [[Bar recursion along a continuous functional|Z754DBNY1W]]: for $Y(\alpha) = \alpha(\alpha(0)) + 1$, the recursion stops at length $2$ unless $\alpha(0) = 1$, and at length $\alpha(1) + 2$ otherwise.
- [[Spector's theorem|DSQJ1RA71N]]: bar recursion of all types witnesses the Dialectica interpretation of classical analysis with countable choice.

### Non-examples

- [[Bar recursion for a discontinuous functional|BH27QPQ6ZN]]: for $Y(\alpha)$ the position of the first zero of $\alpha$, no $\Phi$ satisfies the equations. The condition that fails: the path $1, 1, 1, \ldots$ never meets $Y(\hat s) < |s|$.
- Primitive recursion on the length $|s|$. The condition that fails: its number of steps is fixed in advance, while bar recursion stops at a point that depends on the path.

### Basic properties

- If $Y$ is continuous, then every infinite sequence $\alpha$ has an $n$ with $Y(\widehat{\bar \alpha n}) < n$. So the recursion is well-founded along every path.
- The proof of this property: take $N$ with $Y(\beta) = Y(\alpha)$ whenever $\beta$ agrees with $\alpha$ below $N$, and take $n \ge \max(N, Y(\alpha) + 1)$.
- T + BR has models in which all functionals are continuous, such as the Kleene-Kreisel continuous functionals, and it also has a model in Bezem's strongly majorizable functionals.
- The full set-theoretic model of all functionals of finite type is not a model of T + BR, by the [[non-example|BH27QPQ6ZN]].
- Bar recursion is not definable in T: T + BR defines functions that grow faster than every function defined in T, by [[Spector's theorem|DSQJ1RA71N]].

### History

Spector introduced bar recursion in a paper published in 1962, after his death in 1961, to extend Gödel's Dialectica interpretation to classical analysis.
Later work gave other forms, such as the modified bar recursion of Berger and Oliva and the bar recursion of Berardi, Bezem and Coquand, which interpret countable choice under realizability.
Escardó and Oliva related bar recursion to products of selection functions and to backward induction in games.

### Common errors

- To take the stopping condition for the modulus of continuity of $Y$. The recursion stops when $Y(\hat s) < |s|$, which can happen before or after the modulus, as the [[continuous example|Z754DBNY1W]] shows.
- To expect a bound on the depth of the recursion. The depth is finite along each path, but it is not bounded over all paths.
- To assume that bar recursion exists in every model of T. It fails in the full set-theoretic model, as the [[non-example|BH27QPQ6ZN]] shows.

## Explanations

### L1 human

Ordinary recursion counts down from a known number, so it always knows how many steps remain.
Bar recursion builds a list one entry at a time and asks a judge, after each step, whether the list is long enough.
The judge looks at the list padded with zeros and answers with a number; if that number is less than the length, the recursion stops.
For example, if the judge reads only the first entry $x$, the recursion stops when the list has $x + 1$ entries.
Different lists stop at different lengths, with no upper bound, but every single list stops.

### L2 human

We check that the recursion is well-founded for $Y(\alpha) = \alpha(0) + \alpha(1)$ and $\rho = 0$.

1. Let $\alpha$ be any sequence, and let $c = \alpha(0) + \alpha(1)$.
2. For $n \ge 2$, $\widehat{\bar \alpha n}$ agrees with $\alpha$ at $0$ and $1$, so $Y(\widehat{\bar \alpha n}) = c$.
3. So the condition $c < n$ holds for $n = \max(2, c + 1)$, and the recursion stops on $\alpha$ at that length or earlier.

The typical use is in [[Spector's theorem|DSQJ1RA71N]], where $Y$ is a counterexample functional from the interpretation of the double negation shift.
A trap is to use the modulus of continuity alone: the bound also needs $n > Y(\alpha)$.

### L3 human

Bar recursion is the computational form of the axiom of [[dependent choice|WEMJBN339R]] in its classical, double-negated use.
In game semantics it computes optimal strategies of sequential games of unbounded length, through products of selection functions.
In realizability, its variants interpret countable choice and dependent choice in classical [[second-order arithmetic|DC60FYCSPM]], and so give programs from classical proofs in analysis.
It holds in the continuous functionals built over [[Baire space|P2WS16HKD7]] and in the strongly majorizable functionals, and it fails in the full set-theoretic model.
