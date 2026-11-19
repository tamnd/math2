---
tag: HZ3EX5WRNE
kind: example
name: A dialogue for p implies p
msc: ["03B20", "91A80"]
topics: [38EQ20GR7M]
audience: research
instance_of: [ZCEBYYP67J]
uses: [ZCEBYYP67J]
sources:
  - url: https://en.wikipedia.org/wiki/Dialogical_logic
    locator: The local meaning of the logical constants
  - url: https://plato.stanford.edu/entries/logic-dialogical/
    locator: "2.1.1 The rules of the game: the play level"
---

## Example

We play the [[dialogue game|ZCEBYYP67J]] for the thesis $p \to p$, with the formal rule, the intuitionistic rule, and each move attacked at most once.
We check that every play is won by the Proponent $\mathbf{P}$.

1. Move 1, $\mathbf{P}$: $p \to p$. This is the thesis, so the move is legal.
2. Move 2, $\mathbf{O}$: $p$ [attacks 1]. By the particle rule for $\to$, the only attack on $p \to p$ asserts the antecedent $p$.
3. $\mathbf{O}$ has no other choice at move 2: $\mathbf{P}$ has made no attack, so $\mathbf{O}$ cannot defend.
4. Move 3, $\mathbf{P}$: $p$ [defends against 2]. The defence of an implication is its consequent $p$.
5. The formal rule allows move 3, because $\mathbf{O}$ asserted $p$ at move 2.
6. The intuitionistic rule allows move 3, because move 2 is the latest open attack of $\mathbf{O}$.
7. Now $\mathbf{O}$ has no move. The atomic formula $p$ cannot be attacked, move 1 was already attacked, and $\mathbf{P}$ made no attack to answer.
8. So $\mathbf{O}$ loses this play. Since the moves of $\mathbf{O}$ were forced, this play is the whole game tree.
9. Hence the strategy "answer the attack with $p$" is a winning strategy, and $p \to p$ is dialogically valid.

## Remarks

The example shows the formal rule at work: $\mathbf{P}$ wins by copying an atomic formula that $\mathbf{O}$ granted.
The same play is legal under the classical rule, so $p \to p$ is also classically valid in the dialogical sense.
For the thesis $p \to q$, $\mathbf{O}$ again asserts $p$, but the defence $q$ is forbidden by the formal rule.
Then $\mathbf{P}$ has no move and loses, which matches the fact that $p \to q$ is not valid.
Nothing in the game decides whether $p$ is true, and this is the difference from an evaluation game.

## Explanations

### L1 human

A speaker claims "if it rains, then it rains".
A critic attacks the claim by saying "suppose it rains, then show me that it rains".
The speaker answers "it rains", which is allowed because the critic said it first.
The critic has nothing left to attack, so the speaker wins.

### L2 human

1. Write the thesis $p \to p$ as move 1 of $\mathbf{P}$.
2. Look up the attack on $\to$ in the particle rules: the attacker asserts the antecedent. So move 2 is $\mathbf{O}$: $p$.
3. Look up the defence on $\to$: the defender asserts the consequent. So move 3 is $\mathbf{P}$: $p$.
4. Check the formal rule: $p$ was asserted by $\mathbf{O}$ at move 2, so move 3 is allowed.
5. List the moves left for $\mathbf{O}$: none. So $\mathbf{P}$ wins.

The typical use of this example is to learn the notation of plays before longer dialogues, such as the [[dialogues for excluded middle|9RYNGHEBXG]].
A trap: $\mathbf{P}$ may not assert $p$ at move 3 if $\mathbf{O}$ has not asserted it, even though $p$ is the consequent required by the particle rule.
