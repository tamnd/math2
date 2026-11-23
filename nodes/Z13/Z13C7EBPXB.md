---
tag: Z13C7EBPXB
kind: example
name: Announcing a Moore sentence makes it false
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [9465T2PWZT]
uses: [MFGHDHGV1D, TCAYVAVAK4, YDAHGYKQZN]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_epistemic_logic
    locator: section Public Events
  - url: https://en.wikipedia.org/wiki/Moore%27s_paradox
    locator: section The problem
---

## Example

Bob tells Ann: "it is raining, and you do not know it."
The sentence is true when he says it, and false the moment she hears it.
We check this in [[public announcement logic|9465T2PWZT]].

Use the model of [[the announcement example|YDAHGYKQZN]].
It has worlds $w$, where $p$ is true, and $v$, where $p$ is false, and Ann cannot tell them apart while Bob can.
Let $\mu = p \wedge \neg K_a p$, "it rains and Ann does not know it".

At $w$, $p$ is true, and $K_a p$ is false because Ann considers $v$, so $\mu$ is true at $w$.
At $v$, $p$ is false, so $\mu$ is false at $v$.
Bob announces $\mu$ truthfully at $w$, and the updated model $M|\mu$ keeps only $w$.
In $M|\mu$, Ann's class of $w$ is $\{w\}$, so $K_a p$ is true at $w$.
So $\mu$ is false at $w$ in $M|\mu$, and $[!\mu]\neg\mu$ is true at $w$ in $M$.

The announcement was true when made and false right after.
Announcing that Ann does not know $p$ is exactly what makes her know it.

## Remarks

A formula $\varphi$ is *successful* if $[!\varphi]\varphi$ is valid.
Atoms and their Boolean combinations are successful, and $\mu$ is not.
The example is the dynamic side of [[Moore's paradox|TCAYVAVAK4]]: a Moore sentence can be true, but it cannot be believed, and announcing it destroys it.

[[The reduction axioms|MFGHDHGV1D]] give the same result.
The negation axiom gives $[!\mu]\neg\mu \leftrightarrow (\mu \to \neg[!\mu]\mu)$, and the conjunction axiom splits $[!\mu]\mu$ into $[!\mu]p \wedge [!\mu]\neg K_a p$.
Then $[!\mu]p$ is $\mu \to p$, and $[!\mu]\neg K_a p$ is $\mu \to \neg[!\mu]K_a p$.
The knowledge axiom gives $[!\mu]K_a p \leftrightarrow (\mu \to K_a(\mu \to p))$, and $K_a(\mu \to p)$ is valid, since $\mu \to p$ is a tautology.
So wherever $\mu$ holds, $[!\mu]K_a p$ is true, $[!\mu]\neg K_a p$ is false, $[!\mu]\mu$ is false, and $[!\mu]\neg\mu$ is true.

## Explanations

### L1 human

Bob tells Ann: "it is raining, and you don't know it."
The moment Ann hears this, she knows it is raining.
So the second half of Bob's sentence stops being true.
Some sentences defeat themselves when they are said aloud.

### L2 human

To test whether an announcement survives, compute $M|\varphi$ and evaluate $\varphi$ again in the smaller model.
Here $\mu$ held only at $w$, and in the one-world model Ann knows $p$, so $\mu$ fails.
The typical use is to recognize self-refuting announcements before modeling a dialogue.
Watch out: "true announcements stay true" holds only for successful formulas, and the knowledge part of a formula is what can change.

### L3 human

Unsuccessful updates are behind [[Fitch's paradox of knowability|HVCW7QYXSW]]: if $p \wedge \neg K p$ is true, it cannot become known.
The positive knowledge formulas, built from literals with $\wedge$, $\vee$ and $K_a$, are successful, since deleting worlds cannot make them false.
