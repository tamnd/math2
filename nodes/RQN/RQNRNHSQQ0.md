---
tag: RQNRNHSQQ0
kind: example
name: Revision sequences for the truth-teller
aliases: [truth-teller-revision-sequence]
msc: ["03A05", "03B50"]
topics: [6Q4JJ2MMV8]
audience: grad
instance_of: [ZQ4TWM7K6E]
illustrates: [ZQ4TWM7K6E]
uses: [ZQ4TWM7K6E, XADBJH4872, SFPSB6JPTC, 0ZHQMQ2C1N]
sources:
  - url: https://plato.stanford.edu/entries/truth-revision/
    locator: "The Revision Theory of Truth, 3.2 Revision sequences"
  - url: https://plato.stanford.edu/entries/truth-revision/
    locator: "The Revision Theory of Truth, 4.5 The supervenience of semantics"
---

## Example

We use the [[revision theory|ZQ4TWM7K6E]] over $\mathcal{N}$, with the revision rule $\rho(h) = \{\ulcorner \varphi \urcorner : (\mathcal{N}, h) \models \varphi\}$.
Let $\tau := \exists y\,(D(\underline{k}, y) \wedge T(y))$ be the [[truth-teller|XADBJH4872]], with $D(\underline{k}, m)$ true only for $m = \ulcorner \tau \urcorner$.
We show that $\tau$ keeps its initial value in every revision sequence.

1. For every hypothesis $h$: $(\mathcal{N}, h) \models \tau$ if and only if $\ulcorner \tau \urcorner \in h$. The only witness $y$ is $\ulcorner \tau \urcorner$.
2. So $\ulcorner \tau \urcorner \in \rho(h)$ if and only if $\ulcorner \tau \urcorner \in h$.
3. Let $S$ be a revision sequence. We show by [[transfinite induction|0ZHQMQ2C1N]] on $\zeta$: $\ulcorner \tau \urcorner \in S_\zeta$ if and only if $\ulcorner \tau \urcorner \in S_0$.
4. *Case $\zeta = 0$.* This holds.
5. *Successor case.* $S_{\zeta + 1} = \rho(S_\zeta)$. By step 2 and the induction hypothesis, $\ulcorner \tau \urcorner \in S_{\zeta + 1}$ if and only if $\ulcorner \tau \urcorner \in S_0$.
6. *Limit case $\eta$, with $\ulcorner \tau \urcorner \in S_0$.* By the induction hypothesis, $\ulcorner \tau \urcorner \in S_\zeta$ for all $\zeta < \eta$. So it is stably in below $\eta$, and the limit rule puts it in $S_\eta$.
7. *Limit case $\eta$, with $\ulcorner \tau \urcorner \notin S_0$.* In the same way, it is stably out below $\eta$, and the limit rule keeps it out of $S_\eta$.
8. So, if $\ulcorner \tau \urcorner \in S_0$, then $\tau$ is stably true in $S$, with starting ordinal $0$.
9. If $\ulcorner \tau \urcorner \notin S_0$, then $\tau$ is stably false in $S$.
10. Both kinds of sequences exist: start from $S_0 = \{\ulcorner \tau \urcorner\}$ or from $S_0 = \emptyset$.
11. So $\tau$ is neither categorically true nor categorically false. It is stable in every sequence.

| stage | $0$ | $1$ | $2$ | $\dots$ | $\omega$ | $\omega + 1$ | $\dots$ |
|---|---|---|---|---|---|---|---|
| $S_0 = \emptyset$ | no | no | no | $\dots$ | no | no | $\dots$ |
| $S_0 = \{\ulcorner \tau \urcorner\}$ | yes | yes | yes | $\dots$ | yes | yes | $\dots$ |

## Remarks

The SEP entry states that the revision theory says that the truth-teller is neither categorically true nor categorically false.
It stresses that this differs from the claim that the truth-teller is neither true nor false.
The liar differs in kind: it is [[unstable in every sequence|SK12Q51C0M]], while the truth-teller is stable in every sequence.
In Kripke's semantics the SEP entry gives three acceptable values for the truth-teller: true, false, and neither.
So the revision theory has one fewer option, because each stage is two-valued.

## Explanations

### L1 human

The sentence "this sentence is true" agrees with any guess.
If we guess true, the next round says true again.
If we guess false, the next round says false again.
So the sentence never changes, but our first guess decides its value.

### L2 human

1. Take $S_0 = \emptyset$. Then $\tau$ is false in $(\mathcal{N}, S_0)$, so $\ulcorner \tau \urcorner \notin S_1$.
2. In the same way $\ulcorner \tau \urcorner \notin S_n$ for every finite $n$.
3. At $\omega$, the code is stably out, so the limit rule keeps it out.
4. With $S_0 = \{\ulcorner \tau \urcorner\}$, the same steps keep the code in.

The typical use is to show that "stable" and "categorical" are different notions.
The trap is to call the truth-teller stably true without naming the sequence.
