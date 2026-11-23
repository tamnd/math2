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

If every truth can be known, then every truth is already known.
A few weak principles about knowledge and possibility are enough to prove this.

Work in a [[multimodal|ERG3KAQWYF]] propositional language with a knowledge operator $K$, read "it is known by someone at some time that", and a possibility operator $\Diamond$ with dual $\Box = \neg\Diamond\neg$.
Let $\vdash$ be a deductive system that contains classical [[propositional logic|09K9MWD2QQ]] and the following principles, for all formulas $\varphi$ and $\psi$.

1. Factivity: $\vdash K\varphi \to \varphi$.
2. Distribution over conjunction: $\vdash K(\varphi \wedge \psi) \to (K\varphi \wedge K\psi)$.
3. [[Necessitation|G989VP2NGP]]: if $\vdash \varphi$, then $\vdash \Box\varphi$.
4. Duality: $\vdash \Box\neg\varphi \to \neg\Diamond\varphi$.

The knowability principle is the following schema.
$$\mathrm{KP}: \quad \varphi \to \Diamond K\varphi.$$
For every formula $p$, the single instance of $\mathrm{KP}$ for the formula $p \wedge \neg Kp$ yields $p \to Kp$.
$$(p \wedge \neg Kp) \to \Diamond K(p \wedge \neg Kp) \ \vdash\ p \to Kp.$$
So if every truth is knowable, then every truth is known.
Equivalently, if some truth is not known, then some truth is not knowable.

## Remarks

### Why each hypothesis is needed

Factivity is needed for the first step of [[the proof|HYFS9H190T]].
If $K$ is read as belief and need not be factive, then $K(p \wedge \neg Kp)$ is consistent.
Distribution is needed too, since without it $K(p \wedge \neg Kp)$ need not give $Kp$.

Necessitation turns the theorem $\neg K(p \wedge \neg Kp)$ into $\neg\Diamond K(p \wedge \neg Kp)$.
So the argument shows that $p \wedge \neg Kp$ is unknown in every possible situation, not only in the actual one.
Classical logic is used in the last step.
In intuitionistic logic the argument yields only $\neg(p \wedge \neg Kp)$, which gives $p \to \neg\neg Kp$ and not $p \to Kp$.

### What it gives you

A verificationist who holds that every truth is knowable must, in classical logic, hold that every truth is already known, and that is why the result is called a paradox.
The formula $p \wedge \neg Kp$ is a Moore-type sentence, which can be true but can never be known.
Compare [[a Moore sentence cannot be believed in KD45|TCAYVAVAK4]].
By contraposition, a single unknown truth implies the existence of an unknowable truth.

### The converse

The converse, $p \to Kp \vdash p \to \Diamond Kp$, holds whenever $\vdash \varphi \to \Diamond\varphi$, as in any modal logic containing $\mathsf{T}$.
So under $\mathsf{T}$ the knowability principle and omniscience are equivalent.

### Generalizations

The same argument shows that no operator that is factive and distributes over conjunction can apply to $p \wedge \neg Op$.
Examples are "it is proved that" and "it is verified that".
Restricted knowability principles avoid the collapse.
Tennant restricts $\mathrm{KP}$ to Cartesian propositions, those $\varphi$ for which $K\varphi$ is consistent, and Dummett restricts it to basic statements.

## History

Fitch published the argument in 1963 in "A logical analysis of some value concepts", in the Journal of Symbolic Logic.
He credited it to an anonymous referee of an earlier paper, and the referee was later identified as Alonzo Church.
The argument received wide attention as an objection to verificationism and anti-realism.
It has led to intuitionistic, restriction-based and dynamic epistemic responses.

## Explanations

### L1 human

Suppose there is a true fact $p$ that nobody knows.
Then "$p$ is true and nobody knows $p$" is also true.
But nobody can ever know this sentence, because knowing it would mean knowing $p$, and then the second half would be false.
So not every truth can be known, unless every truth is already known.

### L2 human

Work through the key instance $q = p \wedge \neg Kp$.
Suppose someone knows $q$.
Then they know $p$ and they know $\neg Kp$, and since knowledge is factive, $\neg Kp$ is true, which contradicts $Kp$.
So $q$ cannot be known, and since this argument works in every possible situation, $q$ is not knowable.
If every truth were knowable, $q$ could not be true, and that gives $p \to Kp$.

The typical use is as a test for anti-realist theories of truth.
Watch out: the argument uses only one instance of $\mathrm{KP}$, so any restriction of $\mathrm{KP}$ must exclude sentences such as $p \wedge \neg Kp$.

### L3 human

In terms of [[dynamic epistemic logic|9465T2PWZT]], $p \wedge \neg Kp$ is unsuccessful: after a truthful public announcement of it, it becomes false, as in [[the Moore announcement example|Z13C7EBPXB]].
Van Benthem and others reinterpret knowability as "becomes known after some announcement", which removes the paradox for some formulas but not for Moore-type ones.
The intuitionistic reading turns the conclusion into $p \to \neg\neg Kp$, which says that no truth is forever unknown, and many anti-realists accept this.
