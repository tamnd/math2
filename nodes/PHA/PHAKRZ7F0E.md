---
tag: PHAKRZ7F0E
kind: example
name: Probability formulas that are finitely satisfiable but not satisfiable
aliases: [probability-logic-is-not-compact]
msc: ["03B48"]
topics: [WZP584JQ06]
audience: research
instance_of: [Z2WRGJDRQT]
uses: [1NR3HAWG9D, 21SXYJYC59]
sources:
  - url: https://plato.stanford.edu/entries/logic-probability/
    locator: 2.1 Probabilistic Semantics; 3.2 Sums and Products of Probability Terms
---

## Example

We use a [[probability logic|Z2WRGJDRQT]] with linear probability formulas, of the kind that SEP describes for Fagin, Halpern and Megiddo (1990).
A basic formula has the form $a_1 P(\varphi_1) + \dots + a_n P(\varphi_n) \ge b$, with rational $a_i, b$ and propositional formulas $\varphi_i$.
The other formulas are Boolean combinations of basic formulas.
A model is a probability function $P$ on the propositional formulas, and it satisfies a basic formula when the inequality holds for $P$.
Let
$$\Gamma = \set{P(p) > 0} \cup \set{P(p) \le \tfrac{1}{k} : k = 1, 2, 3, \dots},$$
where $P(p) > 0$ abbreviates $\neg (-P(p) \ge 0)$, and $P(p) \le \tfrac1k$ abbreviates $-P(p) \ge -\tfrac1k$.

1. Let $\Gamma_0 \subseteq \Gamma$ be finite, and let $K$ be the largest $k$ with $P(p) \le \tfrac1k$ in $\Gamma_0$. If there is no such $k$, let $K = 1$.
2. Let $v_1$ and $v_0$ be classical valuations with $v_1(p) = 1$ and $v_0(p) = 0$.
3. Put $P = \tfrac{1}{2K} v_1 + (1 - \tfrac{1}{2K}) v_0$. A [[convex combination|21SXYJYC59]] of probability functions satisfies the three properties, so $P$ is a probability function.
4. Then $P(p) = \tfrac{1}{2K} > 0$, and $P(p) \le \tfrac1K \le \tfrac1k$ for every $k \le K$. So $P$ satisfies every formula of $\Gamma_0$.
5. Now let $P$ satisfy all of $\Gamma$. Then $0 \le P(p) \le \tfrac1k$ for every $k \ge 1$.
6. For every $\varepsilon > 0$ there is $k$ with $\tfrac1k < \varepsilon$, so $P(p) < \varepsilon$. Hence $P(p) = 0$.
7. This contradicts $P(p) > 0$. So $\Gamma$ has no model.

Every finite subset of $\Gamma$ has a model, and $\Gamma$ has none, so this probability logic is not compact.

## Remarks

The example shows the main difference from classical logic, where the [[compactness theorem|1NR3HAWG9D]] holds.
SEP uses the same set, with all positive reals in place of $\tfrac1k$.

It has a consequence for proof systems.
Assume that a sound proof system with finite proofs derives a contradiction from every set without a model.
Then it derives one from $\Gamma$, and the derivation uses only a finite $\Gamma_0 \subseteq \Gamma$.
By soundness $\Gamma_0$ has no model, which contradicts step 4.
So such a system can be complete for single formulas, called weakly complete, but not for all sets of premises.
SEP states that the proof system of Fagin, Halpern and Megiddo is sound and weakly complete.

Change one parameter: replace $P(p) > 0$ by $P(p) \ge 0$.
Then the probability function with $P(p) = 0$ satisfies the whole set, so the set has a model.

## Explanations

### L1 human

Take the claims "the chance of $p$ is more than zero", "it is at most one half", "at most one third", and so on.
Any finite list of these claims can hold together: choose a chance that is small enough.
All the claims together can not hold, because no positive number is below every fraction $\tfrac1k$.
In ordinary logic this can not happen, and this is a difference between the two logics.

### L2 human

1. Take the finite subset $\set{P(p) > 0, P(p) \le \tfrac12, P(p) \le \tfrac15}$.
2. Here $K = 5$, so take $P(p) = \tfrac{1}{10}$.
3. Check: $\tfrac{1}{10} > 0$, $\tfrac{1}{10} \le \tfrac12$ and $\tfrac{1}{10} \le \tfrac15$.

The typical use is to show that a logic needs an infinitary rule for a strong completeness theorem.
A trap: the failure comes from strict inequalities and the Archimedean property of $\mathbb{R}$, and not from the propositional part.
