---
tag: 8BBZ649XXP
kind: definition
name: Pi-calculus
msc: [68Q85, 68Q55]
defines: WHQE2KR445
uses: [1CQRPEWCFD, N8SGDCGJTW, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Π-calculus
---

## Definition

Fix an infinite set of names $x, y, z, \dots$.
The processes of the *$\pi$-calculus* are given by a grammar.
The grammar is
$$P ::= 0 \;\mid\; \overline{x}\langle y \rangle.P \;\mid\; x(z).P \;\mid\; (P \mathbin{|} P) \;\mid\; (\nu x)P \;\mid\; {!P}.$$
The forms are inaction, output of the name $y$ on the channel $x$, and input of a name on $x$ bound to $z$.
They are followed by parallel composition, creation of a new name $x$, and replication.
In $x(z).P$ the name $z$ is bound in $P$, and in $(\nu x)P$ the name $x$ is bound in $P$.
*Structural congruence* $\equiv$ is the least congruence that identifies processes equal up to renaming of bound names and satisfies these laws.

1. $P \mid 0 \equiv P$, $P \mid Q \equiv Q \mid P$ and $(P \mid Q) \mid R \equiv P \mid (Q \mid R)$.
2. $(\nu x)0 \equiv 0$, $(\nu x)(\nu y)P \equiv (\nu y)(\nu x)P$, and $(\nu x)(P \mid Q) \equiv P \mid (\nu x)Q$ when $x$ is not free in $P$.
3. $!P \equiv P \mid\, !P$.

The *reduction relation* $\to$ is the least relation closed under these rules.

1. Communication: $\overline{x}\langle y \rangle.P \mid x(z).Q \to P \mid Q[y/z]$, where $Q[y/z]$ is the [[substitution|NCDZ969V7X]] of $y$ for the free occurrences of $z$ in $Q$.
2. Context: if $P \to P'$, then $P \mid Q \to P' \mid Q$ and $(\nu x)P \to (\nu x)P'$.
3. Structure: if $P \equiv P'$, $P' \to Q'$ and $Q' \equiv Q$, then $P \to Q$.

## Remarks

Example: $(\nu w)\,\overline{x}\langle w \rangle.\overline{w}\langle v \rangle.0 \mid x(z).z(u).0$ reduces in two steps.
By rule 3 with law 2 the process is $\equiv$ to $(\nu w)(\overline{x}\langle w \rangle.\overline{w}\langle v \rangle.0 \mid x(z).z(u).0)$, since $w$ is not free in the receiver.
Communication on $x$ sends the private name $w$, giving $(\nu w)(\overline{w}\langle v \rangle.0 \mid w(u).0)$.
Communication on $w$ then gives $(\nu w)(0 \mid 0) \equiv 0$.
The receiver first learned the channel $w$ and then used it; this movement of names is the mobility of the calculus.

Non-example: $\overline{x}\langle y \rangle.0 \mid w(z).0$ with $x \ne w$ has no reduction, since an output and an input communicate only on the same name.

This is the monadic, synchronous calculus with replication; many presentations add a choice operator $P + Q$ or a matching operator $[x = y]P$.
Behaviour is compared with bisimilarity defined on a labelled [[operational semantics|N8SGDCGJTW]], where the bound output of a private name has its own kind of label.
