---
tag: 9BX0XHX2D5
kind: statement
role: theorem
name: Epsilon nought is the least fixed point of the map α ↦ ω^α
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
uses: [0YSCSX5YZC, KAEDCQ8RM6, ERTAM0SFVB, 6GD30FGYDZ, 01TQB88H4C]
about: [KT50SMH3EC, PQSHBKCE7V]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_arithmetic
    locator: Exponentiation
---

## Statement

The theorem says that the limit of the tower $\omega, \omega^\omega, \omega^{\omega^\omega}, \ldots$ is the first ordinal that the map $\alpha \mapsto \omega^\alpha$ does not move, and that everything below it is moved upward.

All [[ordinals|0YSCSX5YZC]] and operations below are those of [[ordinal arithmetic|KAEDCQ8RM6]].
Define $\tau_0 = 1$ and $\tau_{n+1} = \omega^{\tau_n}$ for $n \in \mathbb{N}$, so that $\tau_1 = \omega$, $\tau_2 = \omega^\omega$ and $\tau_3 = \omega^{\omega^\omega}$, and let $\varepsilon_0 = \sup_{n} \tau_n$.
Then the following hold.

1. $\omega^{\varepsilon_0} = \varepsilon_0$.
2. If $\beta$ is an ordinal with $\omega^\beta = \beta$, then $\varepsilon_0 \le \beta$.
3. For every ordinal $\alpha < \varepsilon_0$, $\alpha < \omega^\alpha$.
4. If $\alpha < \varepsilon_0$ and $\beta < \varepsilon_0$, then $\alpha + \beta < \varepsilon_0$ and $\omega^\alpha < \varepsilon_0$.
5. $\varepsilon_0$ is a [[countable|01TQB88H4C]] limit ordinal.

So $\varepsilon_0$ is the least fixed point of $\alpha \mapsto \omega^\alpha$, that is, the least [[epsilon number|PQSHBKCE7V]].
The [[proof by the tower of powers|YXCBVNHYHK]] proves all five parts.

## Remarks

### Why each hypothesis is needed

The base matters.
For the base $2$, the map $\alpha \mapsto 2^\alpha$ already fixes $\omega$, since $2^\omega = \sup_n 2^n = \omega$.
So the least fixed point depends on the base, and the theorem is about the base $\omega$.

Continuity at limits matters.
The map $\alpha \mapsto \omega^\alpha + 1$ is strictly increasing but jumps at limits, and it has no fixed point at all, because $\omega^\alpha + 1 > \omega^\alpha \ge \alpha$ for every $\alpha$.
The proof of part 1 uses exactly the continuity $\omega^{\sup_n \tau_n} = \sup_n \omega^{\tau_n}$.

The supremum over all $n$ matters.
Each stage is moved, since $\tau_n < \omega^{\tau_n} = \tau_{n+1}$, so no finite stage of the tower is a fixed point.

### What it gives you

Every $\alpha$ with $0 < \alpha < \varepsilon_0$ has a [[Cantor normal form|6GD30FGYDZ]] $\omega^{\beta_1} c_1 + \cdots + \omega^{\beta_k} c_k$, and part 3 gives $\beta_1 < \alpha$.
The reason: $\beta_1 \le \alpha$ always, and $\beta_1 = \alpha$ would give $\omega^\alpha \le \alpha$, which part 3 forbids.
So writing the exponents in normal form again ends after finitely many steps, and this gives the notation system of [[epsilon nought|KT50SMH3EC]].

The set of ordinals below $\varepsilon_0$ is the least set that contains $0$ and is closed under $+$ and $\alpha \mapsto \omega^\alpha$.
Part 4 gives the closure, and the Cantor normal form shows that every ordinal below $\varepsilon_0$ is built from $0$ by these operations.

### The converse

Part 3 says that being below $\varepsilon_0$ forces $\alpha < \omega^\alpha$.
The converse fails: $\alpha = \varepsilon_0 + 1$ satisfies $\omega^{\varepsilon_0 + 1} = \varepsilon_0 \cdot \omega > \varepsilon_0 + 1$, but it is not below $\varepsilon_0$.
The fixed points of $\alpha \mapsto \omega^\alpha$ are exactly the epsilon numbers, and they form a proper class, so part 2 picks out only the first of many.

### Generalizations

Every [[normal function|ERTAM0SFVB]] $f$ has a least fixed point above any given $\gamma$, namely $\sup_n f^n(\gamma + 1)$, by the same argument.
With $f(\alpha) = \omega^\alpha$ and $\gamma = \varepsilon_0$ this gives $\varepsilon_1$.
The [[Veblen function|JQFAE9S2F4]] lists these fixed points as $\varphi_1(\alpha) = \varepsilon_\alpha$, and iterates the step.

### Try it

Is $\omega^\omega$ a fixed point of $\alpha \mapsto \omega^\alpha$?
No: $\omega^{\omega^\omega} > \omega^\omega$, because $\omega^\omega > \omega$ and $\alpha \mapsto \omega^\alpha$ is strictly increasing.

Show that $\varepsilon_0 + \varepsilon_0 < \varepsilon_0 \cdot \omega = \omega^{\varepsilon_0 + 1}$.
We have $\varepsilon_0 + \varepsilon_0 = \varepsilon_0 \cdot 2 < \varepsilon_0 \cdot \omega$, and $\omega^{\varepsilon_0 + 1} = \omega^{\varepsilon_0} \cdot \omega = \varepsilon_0 \cdot \omega$ by part 1.

## History

Cantor introduced the epsilon numbers, and the letter $\varepsilon$ for them, in his work on ordinal arithmetic in the 1890s.
The role of $\varepsilon_0$ in proof theory comes from Gentzen's consistency proof for arithmetic of 1936.

## Explanations

### L1 human

Start with $1$ and keep putting $\omega$ underneath as a base: $1$, $\omega$, $\omega^\omega$, $\omega^{\omega^\omega}$, and so on.
Each step gives a much larger ordinal, but the list never stops.
The ordinal $\varepsilon_0$ is the first ordinal after all the stages of this list.
The theorem says that $\varepsilon_0$ does not change when we raise $\omega$ to it.
Every smaller ordinal does grow: for example, $\omega^2$ is bigger than $2$, and $\omega^\omega$ is bigger than $\omega$.

### L2 human

Let us find the least fixed point of $f(\alpha) = \omega^\alpha$ above $\varepsilon_0$, which is $\varepsilon_1$.
Start at $\varepsilon_0 + 1$, which is not a fixed point, since $\omega^{\varepsilon_0 + 1} = \varepsilon_0 \cdot \omega > \varepsilon_0 + 1$.
Iterate to get $\omega^{\varepsilon_0 + 1}$, then $\omega^{\omega^{\varepsilon_0 + 1}}$, and so on.
The supremum $\varepsilon_1$ of these stages is a fixed point, by the continuity argument of the proof.
Any fixed point $\beta > \varepsilon_0$ is at least $\varepsilon_0 + 1$, and applying $f$ to both sides again and again puts $\beta$ above every stage, so $\beta \ge \varepsilon_1$.
The typical use of the theorem is to show that the Cantor normal form notation reaches exactly the ordinals below $\varepsilon_0$.
Watch out: $\varepsilon_0$ is not the least fixed point of every exponential map, since $\alpha \mapsto 2^\alpha$ already fixes $\omega$.

### L3 human

The theorem is the first case of the fixed-point lemma for normal functions.
A strictly increasing function that is continuous at limits has a closed unbounded class of fixed points, and the least one above $\gamma$ is the supremum of the iterates.
Iterating this step, and taking common fixed points at limit stages, gives the [[Veblen function|JQFAE9S2F4]], which names the ordinals up to the [[Feferman-Schütte ordinal|CNN7BK5YAW]].
In proof theory, $\varepsilon_0$ is the [[proof-theoretic ordinal|C72RBH0CDR]] of Peano arithmetic, and the tower $\tau_n$ is the sequence of ordinals along which Peano arithmetic proves [[transfinite induction|ZE54ABPMJ0]].
