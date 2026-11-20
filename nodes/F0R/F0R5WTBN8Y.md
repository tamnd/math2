---
tag: F0R5WTBN8Y
kind: definition
name: Bunched implications
msc: ["03B47", "03B20"]
topics: [98QF5J4W16]
audience: research
defines: 5JKHNK7AR5
uses: [5JKHNK7AR5, 0R47MAD57S, ETCE287E2R, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Bunched_logic
    locator: Foundations, Truth-functional semantics
  - url: https://en.wikipedia.org/wiki/Bunched_logic
    locator: Foundations, Proof theory and type theory
  - doi: 10.2307/421090
    locator: pages 215-244
    note: O'Hearn and Pym, The Logic of Bunched Implications, Bulletin of Symbolic Logic 5 (1999)
---

## Definition

The *formulas* of [[bunched logic|5JKHNK7AR5]] are built from atoms $p, q, \ldots$ and the constants $\top$, $\bot$ and $I$ by the connectives $\wedge$, $\vee$, $\to$, $\ast$ and $\mathrel{-\!\!*}$.

A *bunch* is a finite rooted tree whose leaves are formulas and whose inner nodes are labeled by a comma or a semicolon.
We write $\Gamma, \Delta$ and $\Gamma ; \Delta$ for the bunch with root comma or root semicolon and the subtrees $\Gamma$ and $\Delta$.
A *judgment* $\Gamma \vdash A$ has a bunch $\Gamma$ and a formula $A$.
The proof system has the introduction rules
$$\frac{\Gamma, A \vdash B}{\Gamma \vdash A \mathrel{-\!\!*} B} \qquad \frac{\Gamma ; A \vdash B}{\Gamma \vdash A \to B}.$$
The semicolon admits weakening and contraction of whole bunches, and the comma admits neither.

A *resource model* is a tuple $(M, \bullet, e, \sqsubseteq, V)$ with these properties:

1. $(M, \bullet, e)$ is a commutative [[monoid|0R47MAD57S]].
2. $\sqsubseteq$ is a preorder on $M$, and $r \sqsubseteq r'$ implies $r \bullet s \sqsubseteq r' \bullet s$ for all $s$.
3. $V$ sends each atom to an [[upper set|ETCE287E2R]] of $(M, \sqsubseteq)$.

The *forcing relation* $r \models A$, for $r \in M$, is defined by induction on $A$:

- $r \models p$ if and only if $r \in V(p)$;
- $r \models \top$ always, and $r \models \bot$ never;
- $r \models I$ if and only if $e \sqsubseteq r$;
- $r \models A \wedge B$ if and only if $r \models A$ and $r \models B$, and $r \models A \vee B$ if and only if $r \models A$ or $r \models B$;
- $r \models A \to B$ if and only if for every $s$ with $r \sqsubseteq s$, $s \models A$ implies $s \models B$;
- $r \models A \ast B$ if and only if there are $s$ and $t$ with $s \models A$, $t \models B$ and $s \bullet t \sqsubseteq r$;
- $r \models A \mathrel{-\!\!*} B$ if and only if for every $s$ with $s \models A$, we have $r \bullet s \models B$.

In a resource model, $A$ *entails* $B$ if every $r$ with $r \models A$ also has $r \models B$.

## Notation

The paper of O'Hearn and Pym gives the complete list of rules.
The clause for $\ast$ is the one in the Wikipedia article.
The clauses for $\wedge$, $\vee$ and $\to$ are those of [[Kripke semantics|NGHWZ9Y7ZV]] for intuitionistic logic.
In the boolean variant, $r \models A \to B$ if and only if $r \not\models A$ or $r \models B$.

## Remarks

1. *Persistence.* If $r \models A$ and $r \sqsubseteq r'$, then $r' \models A$.
   The proof is by induction on $A$.
   For atoms, $V(p)$ is an upper set; for $\top$, $\bot$, $\wedge$ and $\vee$, use the induction hypothesis.
   For $I$ and $\ast$, use $e \sqsubseteq r \sqsubseteq r'$ and $s \bullet t \sqsubseteq r \sqsubseteq r'$, by transitivity.
   For $\to$, every $s$ with $r' \sqsubseteq s$ also has $r \sqsubseteq s$.
   For $\mathrel{-\!\!*}$, $r \bullet s \sqsubseteq r' \bullet s$ by property 2, and $B$ is persistent by induction.
2. The heap model of separation logic uses a partial operation $\bullet$.
   For partial $\bullet$, the clause for $\ast$ also requires that $s \bullet t$ is defined.
3. When $\sqsubseteq$ is equality, every subset of $M$ is an upper set, and the clause for $\ast$ reads $s \bullet t = r$.

## Explanations

### L1 human

A resource model says which resources exist, how two resources combine, and when one resource is at least another.
A formula is then a property of resources, and $\ast$ splits a resource into two parts.

### L2 human

We compute in the model $(\mathbb{N}, +, 0, \leq, V)$ with $V(p) = \{n : n \geq 1\}$.

1. Property 2 holds, since $r \leq r'$ implies $r + s \leq r' + s$.
2. $V(p)$ is an upper set for $\leq$.
3. $r \models p \ast p$ needs $s, t \geq 1$ with $s + t \leq r$, so it holds if and only if $r \geq 2$.
4. So $1 \models p$ but $1 \not\models p \ast p$.
5. $r \models I$ holds for every $r$, since $0 \leq r$.

The typical use of a resource model is to show that a formula is not valid, by one resource that does not force it.
A trap: $r \models A \to B$ looks at all larger resources, so $0 \not\models p \to p \ast p$, because of $s = 1$.
