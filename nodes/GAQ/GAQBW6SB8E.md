---
tag: GAQBW6SB8E
kind: example
name: Computing a function as a game
aliases: [function-computation-game]
msc: ["03B70", "03D10"]
topics: [NJB94B39QK]
audience: research
instance_of: [C7CV0XMSTT]
uses: [C7CV0XMSTT, KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Computability_logic
    locator: As a problem specification tool
---

## Example

Let $f$ be a total function from the natural numbers to the natural numbers.
In [[computability logic|C7CV0XMSTT]], the problem of computing $f$ is the game $G_f = \sqcap x \sqcup y\, (y = f(x))$.

The game goes as follows.
The environment makes the first move, the input: it chooses a value $m$ for $x$.
Then the game is $\sqcup y\, (y = f(m))$, and the machine must make the output move: it chooses a value $n$ for $y$.
Then the game is the elementary game $n = f(m)$, which the machine wins if and only if $n = f(m)$ is true.
In a choice game, a player who must choose and never chooses loses that game.
So if the environment never chooses $m$, the machine wins, and if the machine never chooses $n$, the machine loses.
We consider legal moves only.

Claim: $G_f$ is computable if and only if $f$ is a [[computable function|KZSB5E471K]].

1. Suppose that an algorithm $F$ computes $f$. The machine waits for the move $m$ of the environment.
2. If no such move comes, the machine wins, by the rule for $\sqcap$.
3. If the move $m$ comes, the machine runs $F$ on $m$. This halts with $f(m)$, because $f$ is total and $F$ computes it.
4. The machine moves $n = f(m)$. The elementary game $f(m) = f(m)$ is true, so the machine wins. So $G_f$ is computable.
5. Conversely, suppose that a machine $M$ wins $G_f$ against every behavior of the environment. Fix $m$.
6. Let $E_m$ be the environment that moves $m$ at the start and then makes no more moves. The machine $M$ wins the play against $E_m$.
7. $M$ cannot win this play without a move in $\sqcup y$, by the rule for $\sqcup$. So $M$ moves some $n$ at a finite time.
8. $M$ wins the elementary game $n = f(m)$, so $n = f(m)$.
9. Steps 6 to 8 give an algorithm for $f$: on input $m$, simulate $M$ against $E_m$ until $M$ makes its move $n$, and output $n$. So $f$ is computable.

So computability of a function is a special case of computability of a game.

## Remarks

The version with a blind quantifier, $\sqcap x\, \exists y\, (y = f(x))$, is different.
After the input $m$ it is the elementary game $\exists y\, (y = f(m))$, which is true, so the machine wins with no moves for every total $f$.
The choice quantifier $\sqcup y$ makes the machine give its answer as a move.
The same form gives decision problems: $\sqcap x\, (p(x) \sqcup \neg p(x))$ is the problem of deciding $p$; see [[deciding the halting problem as a game|3CBR9YYH4T]].

## Explanations

### L1 human

The user types a number $m$, and the computer must answer with $f(m)$.
The computer wins if its answer is right.
A computer can win this game every time exactly when there is a program for $f$.

### L2 human

The choice quantifier $\sqcap x$ is an input move by the environment, and $\sqcup y$ is an output move by the machine.
A winning machine must answer every input, so watching it play gives an algorithm for $f$.
A trap is to forget that the machine wins when the environment gives no input; this does not help the machine, because a winning strategy must also answer every input that does come.
