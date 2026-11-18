---
tag: HVCW7QYXSW
kind: statement
role: theorem
name: Fitch's paradox of knowability
aliases: [knowability-paradox, church-fitch-paradox]
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
uses: [ERG3KAQWYF, G989VP2NGP, 09K9MWD2QQ]
about: [6YKMP1DH7M]
proofs: [HYFS9H190T]
history:
  first_stated: "Fitch, 1963"
  notes: "Fitch published the argument in A logical analysis of some value concepts (Journal of Symbolic Logic, 1963) and credited it to an anonymous referee, later identified as Alonzo Church."
sources:
  - url: https://en.wikipedia.org/wiki/Fitch%27s_paradox_of_knowability
    locator: Proof
  - url: https://plato.stanford.edu/entries/fitch-paradox/
    locator: Fitch's Paradox of Knowability
---

## Statement

Work in a [[multimodal|ERG3KAQWYF]] propositional language with a knowledge operator $K$, read "it is known by someone at some time that", and a possibility operator $\Diamond$ with dual $\Box = \neg\Diamond\neg$.
Let $\vdash$ be a deductive system that contains classical [[propositional logic|09K9MWD2QQ]] and these principles, for all formulas $\varphi, \psi$:

1. (factivity) $\vdash K\varphi \to \varphi$;
2. (distribution over conjunction) $\vdash K(\varphi \wedge \psi) \to (K\varphi \wedge K\psi)$;
3. ([[necessitation|G989VP2NGP]]) if $\vdash \varphi$, then $\vdash \Box\varphi$;
4. (duality) $\vdash \Box\neg\varphi \to \neg\Diamond\varphi$.

The knowability principle is the schema
$$
\mathrm{KP}: \quad \varphi \to \Diamond K\varphi.
$$

For every formula $p$, the instance of $\mathrm{KP}$ for the formula $p \wedge \neg Kp$ yields $p \to Kp$:
$$
(p \wedge \neg Kp) \to \Diamond K(p \wedge \neg Kp) \ \vdash\ p \to Kp.
$$
So if every truth is knowable, then every truth is known.
Equivalently, if some truth is not known, then some truth is not knowable.

The proof is in [[the proof of Fitch's paradox|HYFS9H190T]].

## Remarks

### Why each hypothesis is needed

1. Factivity: if $K$ is read as belief and need not be factive, then $K(p \wedge \neg Kp)$ is consistent, and the first step of the proof fails.
2. Distribution: without it, $K(p \wedge \neg Kp)$ need not give $Kp$, and the first step of the proof fails.
3. Necessitation: without it, the derived theorem $\neg K(p \wedge \neg Kp)$ would not become $\neg\Diamond K(p \wedge \neg Kp)$. The argument shows that $p \wedge \neg Kp$ is unknowable in every possible situation, not only in the actual one.
4. Classical logic: in intuitionistic logic, the argument yields only $\neg(p \wedge \neg Kp)$, which gives $p \to \neg\neg Kp$ and not $p \to Kp$.

### Consequences

1. A verificationist who holds that every truth is knowable must, in classical logic, hold that every truth is already known. This is the reason the result is called a paradox.
2. The formula $p \wedge \neg Kp$ is a Moore-type sentence: it can be true, but it can never be known. Compare [[a Moore sentence cannot be believed in KD45|TCAYVAVAK4]].
3. By contraposition, the existence of a single unknown truth implies the existence of an unknowable truth.

### Converse

The converse, $p \to Kp \vdash p \to \Diamond Kp$, holds whenever $\vdash \varphi \to \Diamond\varphi$, as in any modal logic containing T.
So under T the knowability principle and omniscience are equivalent.

### Generalizations

1. The same argument shows that any operator that is factive and distributes over conjunction cannot apply to $p \wedge \neg Op$. Examples include "it is proved that" and "it is verified that".
2. Restricted knowability principles avoid the collapse. Tennant restricts $\mathrm{KP}$ to Cartesian propositions, those $\varphi$ for which $K\varphi$ is consistent, and Dummett restricts it to basic statements.

## History

Fitch published the argument in 1963 in "A logical analysis of some value concepts", in the Journal of Symbolic Logic.
He credited it to an anonymous referee of an earlier paper; the referee was later identified as Alonzo Church.
The argument received wide attention as an objection to verificationism and anti-realism, and it has led to intuitionistic, restriction-based, and dynamic epistemic responses.

## Explanations

### L1 human

Suppose there is a true fact $p$ that nobody knows.
Then "$p$ is true and nobody knows $p$" is also true.
But nobody can ever know this sentence: knowing it would mean knowing $p$, and then the second half would be false.
So not every truth can be known, unless every truth is already known.

### L2 human

Work through the key instance $q = p \wedge \neg Kp$.

1. Suppose someone knows $q$. Then they know $p$ and they know $\neg Kp$.
2. Knowledge is factive, so $\neg Kp$ is true. But $Kp$ holds by step 1. So $q$ cannot be known.
3. This holds in every possible situation, so $q$ is not knowable.
4. If every truth were knowable, $q$ could not be true. So $p \to Kp$.

The typical use is as a test for anti-realist theories of truth.
A trap: the argument uses only one instance of $\mathrm{KP}$, so any restriction of $\mathrm{KP}$ must exclude sentences such as $p \wedge \neg Kp$.

### L3 human

In terms of dynamic epistemic logic, $p \wedge \neg Kp$ is unsuccessful: after a truthful public announcement of it, it becomes false.
Van Benthem and others reinterpret knowability as "becomes known after some announcement", which removes the paradox for some formulas but not for Moore-type ones.
The intuitionistic reading turns the conclusion into $p \to \neg\neg Kp$, which says that no truth is forever unknown, and many anti-realists accept this.
