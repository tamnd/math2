---
tag: ZYJ2VC7S74
kind: example
name: A bimodal frame whose past is not the converse of its future
msc: ["03B44", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: 8XB117FKKV
    note: the past relation is not the converse of the future relation, so the frame is not a temporal frame, and the tense axiom p → GPp fails
uses: [8XB117FKKV, ERG3KAQWYF, KXRMT4R9E8]
sources:
  - url: https://en.wikipedia.org/wiki/Temporal_logic
    locator: Temporal operators
  - book: isbn:9780521527149
    locator: Blackburn, de Rijke and Venema, Modal Logic, chapter 1
---

## Example

Read the tense language on a [[bimodal|ERG3KAQWYF]] Kripke frame, with one relation for the future operators and one for the past operators:
$$W = \{a, b\}, \qquad R_F = \{(a, b)\}, \qquad R_P = \emptyset.$$
Here $F\varphi$ is true at $w$ when $\varphi$ holds at some $v$ with $w R_F v$, and $P\varphi$ is true at $w$ when $\varphi$ holds at some $v$ with $w R_P v$.
In a [[temporal frame|8XB117FKKV]] the past relation is the converse of the future relation, so $R_P$ should be $\{(b, a)\}$.
We check that the tense axiom $p \to GPp$ fails.

1. The frame is not a temporal frame, because $a R_F b$ holds and $b R_P a$ fails.
2. Put $V(p) = \{a\}$, so $p$ is true at $a$.
3. $GPp$ at $a$ asks that $Pp$ holds at every $R_F$-successor of $a$, that is, at $b$.
4. $Pp$ at $b$ asks for some $v$ with $b R_P v$.
   Since $R_P$ is empty, $Pp$ is false at $b$.
5. So $GPp$ is false at $a$, and $p \to GPp$ fails at $a$.

On a real temporal frame the axiom cannot fail.
If $p$ holds at $t$ and $t < u$, then $t$ is a point before $u$ with $p$, so $Pp$ holds at $u$.

## Remarks

The two axioms $p \to GPp$ and $p \to HFp$ say exactly that the two relations are converse to each other.
On a bimodal frame, $p \to GPp$ is valid if and only if $w R_F v$ implies $v R_P w$.
In the same way, $p \to HFp$ is valid if and only if $w R_P v$ implies $v R_F w$.
If we add $(b, a)$ to $R_P$, the frame becomes the temporal frame of the two-point order $a < b$, and both axioms hold.
The basic tense logic with these two axioms is worked in [[future and past in the basic tense logic|KXRMT4R9E8]].

## Explanations

### L1 human

Suppose "tomorrow" is reachable from "today", but from tomorrow you cannot look back to today.
Then something true today is not remembered tomorrow as "it was true".
Real time does not behave this way, so this picture is not a model of time.

### L2 human

To test a bimodal frame, check the condition "future then past returns": for each pair $(w, v)$ in $R_F$, ask whether $(v, w) \in R_P$.
Here the pair $(a, b)$ fails the test.
To see the failure in a formula, put $p$ at $a$ only and evaluate $p \to GPp$ at $a$, as in steps 2 to 5.
The typical use is to see why tense logic is not just any bimodal logic: its two boxes are tied together by the converse.
Watch out: $p \to GPp$ is not the axiom $\mathrm{T}$ or $\mathrm{B}$ of one modality, because it mixes two modalities.
