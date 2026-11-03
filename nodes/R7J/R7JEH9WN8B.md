---
tag: R7JEH9WN8B
kind: definition
name: Selfridge–Conway procedure
msc: [91B32, 91A06]
defines: C2PPY01RGB
uses: [KCVV28DH6R, P3GPD0S0J7, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Selfridge%E2%80%93Conway_procedure
---

## Definition

Let a cake $C$, as in [[fair cake-cutting|KCVV28DH6R]], be shared by agents $1, 2, 3$, whose valuations $V_1, V_2, V_3$ are nonatomic probability [[measures|PR11BZQQPG]].
The *Selfridge–Conway procedure* is the following.

1. Agent $1$ cuts $C$ into three pieces of equal value $1/3$ for her.
2. Agent $2$ looks at the two pieces she values most. If they have the same value for her, nothing is trimmed. Otherwise she cuts a part $T$, the *trimmings*, from her most valued piece. She cuts so that the rest has the same value for her as her second most valued piece. The trimmings $T$ are set aside.
3. Agent $3$ chooses one of the three pieces. Then agent $2$ chooses one of the two remaining pieces, and she must take the trimmed piece if it is still there. Agent $1$ gets the last piece, which is untrimmed.
4. If $T$ is not empty, let $A$ be whichever of agents $2$ and $3$ received the trimmed piece, and let $B$ be the other one. Agent $B$ cuts $T$ into three parts of equal value for her. Then $A$ chooses a part, then agent $1$, and $B$ gets the last part.

## Remarks

The result is [[envy-free|P3GPD0S0J7]].
After step 3, nobody envies anyone for the main pieces.
Agent $3$ chose first, agent $2$ still had one of her two tied favorite pieces, and agent $1$ got an untrimmed piece of value $1/3$ for her.
In step 4, $A$ chooses first, and $B$ made three parts she values equally.
Agent $1$ does not envy $A$, since $A$'s trimmed piece and all of $T$ together are worth only $1/3$ to agent $1$.

Example: if in step 2 agent $2$ values two pieces equally and most, nothing is trimmed, and step 3 alone gives an envy-free allocation with only two cuts.

Non-example: the procedure without step 2, where agent $1$ cuts three equal pieces and agents $3$, $2$, $1$ simply choose in turn, is not envy-free.
If agents $2$ and $3$ both value one piece most and the other two pieces less, agent $3$ takes it and agent $2$ envies agent $3$.
The trimming in step 2 is what prevents this.

The procedure uses at most five cuts: two in step 1, one in step 2 and two in step 4.
