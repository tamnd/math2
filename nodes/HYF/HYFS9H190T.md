---
tag: HYFS9H190T
kind: proof
name: Proof of Fitch's paradox of knowability
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
proves: HVCW7QYXSW
uses: [G989VP2NGP, 09K9MWD2QQ]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Fitch%27s_paradox_of_knowability
    locator: Proof
---

## Proof

We use the notation of [[Fitch's paradox|HVCW7QYXSW]].
First we show, without the knowability principle, that $p \wedge \neg Kp$ can never be known, and then we apply one instance of the principle.
Fix a formula $p$ and put $q = p \wedge \neg Kp$.

1. Assume $K q$, that is, $K(p \wedge \neg Kp)$.
2. Distribution gives $Kp$ and $K\neg Kp$.
3. Factivity applied to $K\neg Kp$ gives $\neg Kp$.
4. Steps 2 and 3 give $Kp \wedge \neg Kp$, a contradiction.
   Discharging the assumption of step 1 gives $\vdash \neg K q$, and this derivation uses no instance of $\mathrm{KP}$.
5. [[Necessitation|G989VP2NGP]] applied to the theorem of step 4 gives $\vdash \Box \neg K q$.
6. Duality gives $\vdash \neg \Diamond K q$.
7. Now assume the instance $q \to \Diamond K q$ of $\mathrm{KP}$.
   By step 6 and contraposition we get $\neg q$, that is, $\neg(p \wedge \neg Kp)$.
8. In classical [[propositional logic|09K9MWD2QQ]], $\neg(p \wedge \neg Kp)$ is equivalent to $p \to Kp$.

So $q \to \Diamond K q \vdash p \to Kp$, which proves the theorem.

## Idea

The sentence "$p$, but nobody knows $p$" defeats itself when known, because knowing it requires knowing $p$, which falsifies its second half.
So it is a theorem that this sentence is never known, and necessitation upgrades this to "it is never knowable".
The knowability principle then forbids the sentence from being true, which is omniscience.

## Variants

Step 5 applies necessitation only to a theorem proved without $\mathrm{KP}$.
Applying it to the assumption $\mathrm{KP}$ itself would be unsound, and it is not needed.

Intuitionistically, steps 1 to 7 go through unchanged, and step 8 gives only $p \to \neg\neg Kp$.
The reason is that $\neg(p \wedge \neg r)$ does not give $p \to r$ without double negation elimination.

In a possible-worlds semantics where $K$ is factive and distributes over conjunction, step 4 says that $Kq$ is false at every world.
So $\Diamond Kq$ is false at every world, and $\mathrm{KP}$ fails at every world where $q$ is true.
