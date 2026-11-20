---
tag: 3CBR9YYH4T
kind: example
name: Deciding the halting problem as a game
aliases: [halting-decision-game]
msc: ["03B70", "03D35"]
topics: [NJB94B39QK]
audience: research
instance_of: [C7CV0XMSTT]
uses: [C7CV0XMSTT, GAQBW6SB8E, Z7TN2B35B0, T62EJ749R5]
sources:
  - url: https://en.wikipedia.org/wiki/Computability_logic
    locator: Semantics, As a problem specification tool
---

## Example

Let $h(x)$ be the halting predicate: $h(x)$ is true if and only if the Turing machine with code $x$ halts on the empty input.
In [[computability logic|C7CV0XMSTT]], the problem of deciding $h$ is $D = \sqcap x\, (h(x) \sqcup \neg h(x))$.
The environment chooses $m$, and then the machine must choose $h(m)$ or $\neg h(m)$, and it wins if its choice is a true elementary game.
Compare $D$ with $D' = \sqcap x\, (h(x) \vee \neg h(x))$, which uses the parallel disjunction.

Claim 1: $D'$ is computable.

1. The machine makes no moves.
2. If the environment never chooses $m$, the machine wins, by the rule for $\sqcap$.
3. If the environment chooses $m$, the game becomes the elementary game $h(m) \vee \neg h(m)$. This is true, so the machine wins.

Claim 2: $D$ is not computable.

4. Suppose that a machine $M$ wins $D$ against every behavior of the environment.
5. Fix $m$, and let $E_m$ be the environment that moves $m$ at the start and then makes no more moves.
6. $M$ wins the play against $E_m$. By the rule for $\sqcup$, it does so only by a choice of one disjunct, at a finite time.
7. The chosen disjunct is a true elementary game, because $M$ wins.
8. So the following algorithm decides $h$: on input $m$, simulate $M$ against $E_m$ until $M$ chooses, and answer "halts" if and only if $M$ chooses $h(m)$.
9. This contradicts the [[undecidability of the halting problem|Z7TN2B35B0]]. So no such $M$ exists.

Steps 4 to 8 work for any predicate $p$ in place of $h$.
In the other direction, a machine that waits for $m$, decides $p(m)$ and chooses the true disjunct wins.
So $\sqcap x\, (p(x) \sqcup \neg p(x))$ is computable if and only if the set defined by $p$ is [[decidable|T62EJ749R5]].

## Remarks

The two problems differ only in the kind of disjunction.
For every $m$, both $h(m) \vee \neg h(m)$ and $h(m) \sqcup \neg h(m)$ are instances of excluded middle.
The parallel form is won with no moves, but the choice form asks the machine to tell which disjunct is true.

So the formula $\sqcap x\, (p(x) \sqcup \neg p(x))$ is not valid: its interpretation with $p := h$ is not computable.
The formula $\sqcap x\, (p(x) \vee \neg p(x))$ is valid, by the argument of Claim 1 for any predicate.
The same method as in [[computing a function as a game|GAQBW6SB8E]] turns a winning machine into an algorithm.

## Explanations

### L1 human

The user names a program, and the computer must say whether that program halts.
No computer can win this game every time, because the halting problem is undecidable.
But if the computer only has to make the statement "it halts or it does not halt" true, it wins with no work at all.

### L2 human

The choice disjunction $\sqcup$ asks for a decision, and the parallel disjunction $\vee$ asks only for truth.
A winning strategy for the choice form would be a decision procedure for $h$, so it cannot exist.
A trap is to think that the choice form fails because excluded middle is false; every instance $h(m) \vee \neg h(m)$ is true, and only the decision is missing.
