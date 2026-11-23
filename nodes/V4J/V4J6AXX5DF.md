---
tag: V4J6AXX5DF
kind: proof
name: Proof of soundness of normal modal logics
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
proves: E87G6ZTMTN
uses: [JS8W7PA6JK, 6BQ71KQ6QT, 05006AJ7DZ, 12MQ2NJ29A]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Proof

We prove part 1 of [[soundness of normal modal logics|E87G6ZTMTN]], that $\operatorname{Log}(\mathsf{C})$ has the five properties of a [[normal modal logic|JS8W7PA6JK]], and then derive part 2.
An intersection of normal logics is normal, and $\operatorname{Log}(\mathsf{C})$ is the intersection of the sets $\operatorname{Log}(\mathfrak{F})$ for $\mathfrak{F} \in \mathsf{C}$.
So it suffices to fix one frame $\mathfrak{F} = (W, R)$ and show that $\operatorname{Log}(\mathfrak{F})$ is normal.

### The axioms

Let $\varphi = \tau^\sigma$, where $\tau$ is a [[tautology|05006AJ7DZ]].
At a world $w$ of a model on $\mathfrak{F}$, the clauses for $\bot$ and $\to$ are the classical truth tables.
So $\varphi$ has at $w$ the value that $\tau$ gets when each variable $q$ of $\tau$ takes the value of $\sigma(q)$ at $w$, and this value is "true".

For the axiom $\mathrm{K}$, let $\mathfrak{M}$ be a model on $\mathfrak{F}$ with $w \models \square(p \to q)$ and $w \models \square p$.
Each successor $v$ of $w$ satisfies $p \to q$ and $p$, so $v \models q$.
Hence $w \models \square q$, and $\mathrm{K}$ is true at $w$.

### The rules

For modus ponens, let $\varphi$ and $\varphi \to \psi$ be valid on $\mathfrak{F}$.
At each world of each model on $\mathfrak{F}$ both are true, so $\psi$ is true there.

For necessitation, let $\varphi$ be valid on $\mathfrak{F}$, let $\mathfrak{M}$ be a model on $\mathfrak{F}$, and let $w \in W$.
The formula $\varphi$ is true at every world of $\mathfrak{M}$, in particular at every successor of $w$, so $w \models \square\varphi$.

### Uniform substitution

Let $\sigma$ be a substitution and let $\mathfrak{M} = (W, R, V)$.
Define $\mathfrak{M}^\sigma = (W, R, V^\sigma)$ with $V^\sigma(p) = [\![\sigma(p)]\!]^{\mathfrak{M}}$.
We claim that $\mathfrak{M}, w \models \chi^\sigma$ if and only if $\mathfrak{M}^\sigma, w \models \chi$, for every formula $\chi$ and world $w$.
The proof is a [[structural induction|12MQ2NJ29A]] on $\chi$.
For a variable $p$ the claim is the definition of $V^\sigma$, and for $\bot$ both sides are false.
For $\alpha \to \beta$ the claim follows from the hypothesis for $\alpha$ and $\beta$ at $w$.
For $\square\alpha$, both sides say that every successor $v$ of $w$ satisfies $\alpha^\sigma$ in $\mathfrak{M}$, or $\alpha$ in $\mathfrak{M}^\sigma$, and these agree by the hypothesis at $v$.

Now let $\varphi$ be valid on $\mathfrak{F}$, and let $\mathfrak{M}$ be a model on $\mathfrak{F}$.
The model $\mathfrak{M}^\sigma$ lies on the same frame, so $\varphi$ is true at every world of $\mathfrak{M}^\sigma$.
By the claim, $\varphi^\sigma$ is true at every world of $\mathfrak{M}$, so $\varphi^\sigma$ is valid on $\mathfrak{F}$.
This finishes part 1.

### Part 2

Let each formula of $\Gamma$ be valid on every frame of $\mathsf{C}$, so that $\Gamma \subseteq \operatorname{Log}(\mathsf{C})$.
By part 1, $\operatorname{Log}(\mathsf{C})$ is a normal logic that contains $\Gamma$.
Since $\mathsf{K}\Gamma$ is the smallest such logic, $\mathsf{K}\Gamma \subseteq \operatorname{Log}(\mathsf{C})$.

## Idea

Each axiom is true at every world, and each rule turns formulas valid on the frame into formulas valid on the frame.
Necessitation needs truth at all worlds, not at one world, and substitution needs truth under all valuations.
That is why validity on a frame is the right notion.

## Variants

For a Hilbert system the same steps give an induction on the length of a derivation: each line of a derivation in $\mathsf{K}\Gamma$ is valid on every frame of $\mathsf{C}$.
There is also an algebraic version.
The complex algebra of a frame is a modal algebra, and every normal logic is sound for the modal algebras that validate its axioms.
