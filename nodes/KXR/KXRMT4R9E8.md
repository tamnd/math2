---
tag: KXRMT4R9E8
kind: example
name: Future and past in the basic tense logic
msc: ["03B45", "03B44"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [ERG3KAQWYF]
uses: [ERG3KAQWYF, 8XB117FKKV, NGHWZ9Y7ZV, 05AVARPXA2, E87G6ZTMTN]
sources:
  - url: https://en.wikipedia.org/wiki/Temporal_logic
    locator: Temporal operators
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of modal logic
---

## Example

The basic tense logic $\mathsf{K}_t$ is a [[multimodal logic|ERG3KAQWYF]] with two boxes.
$G\varphi$ says "$\varphi$ will always be true", and $H\varphi$ says "$\varphi$ has always been true".
Their duals are $F\varphi = \neg G \neg\varphi$, "at some future time", and $P\varphi = \neg H \neg\varphi$, "at some past time".
A bimodal frame $(W, R_G, R_H)$ reads $G$ by $R_G$ and $H$ by $R_H$.
It is a *tense frame* when $R_H$ is the converse of $R_G$, that is, $v \mathrel{R_H} w$ iff $w \mathrel{R_G} v$.

We first show that $p \to GPp$ is true at every world of a tense frame, under every valuation.

1. Let $w \models p$, and let $w \mathrel{R_G} v$.
2. Then $v \mathrel{R_H} w$, since $R_H$ is the converse of $R_G$.
3. So $v$ has a past world, $w$, where $p$ is true, and $v \models Pp$.
4. As $v$ was any future world of $w$, we get $w \models GPp$.
5. The same argument with $G$ and $H$ exchanged shows that $p \to HFp$ is valid on tense frames.

Now we drop the converse condition.

6. Take $W = \{ a, b \}$, $R_G = \{ (a, b) \}$, $R_H = \varnothing$ and $V(p) = \{ a \}$.
7. $p$ is true at $a$, the only $R_G$-successor of $a$ is $b$, and $b$ has no $R_H$-successor, so $Pp$ is false at $b$.
8. So $GPp$ is false at $a$, and $p \to GPp$ is false at $a$.

The same idea gives the exact frame condition.

9. Suppose $w \mathrel{R_G} v$ but not $v \mathrel{R_H} w$, and put $V(p) = \{ w \}$.
10. Then $Pp$ at $v$ needs a world $u$ with $v \mathrel{R_H} u$ and $u = w$, and there is none.
11. So $p \to GPp$ is false at $w$, and with steps 1 to 4 we get that it is valid on a frame iff $w \mathrel{R_G} v$ always implies $v \mathrel{R_H} w$.

## Remarks

$\mathsf{K}_t$ is the smallest normal bimodal logic that contains $p \to GPp$ and $p \to HFp$.
By steps 1 to 5 and [[soundness|E87G6ZTMTN]], which extends to two boxes with the same proof, its theorems are valid on every tense frame.

The two axioms are interaction axioms, since each one mentions both boxes.
The model of step 6 is a model of the fusion $\mathsf{K} \otimes \mathsf{K}$, so step 8 shows that the fusion does not prove $p \to GPp$.
Thus $\mathsf{K}_t$ is strictly larger than $\mathsf{K} \otimes \mathsf{K}$.

The relation $R_G$ is a [[binary relation|05AVARPXA2]] on times.
Adding transitivity or linearity gives the logics of [[temporal modal logic|8XB117FKKV]].

## Explanations

### L1 human

"If it rains now, then at every later time it will be true that it once rained."
This holds when "later" and "earlier" are two views of one time line.
If the past relation forgets the present, the law can fail, since a later time may not look back to now.
The two-world model shows such a failure.

### L2 human

The proof of $p \to GPp$ has one idea: from $w \mathrel{R_G} v$ we go back by $v \mathrel{R_H} w$.
Try it: on a tense frame, is $FHp \to p$ valid?
Write it as the contrapositive $\neg p \to G P \neg p$, which is an instance of $p \to GPp$ with $\neg p$ for $p$, so the answer is yes.
The typical use is to see that interaction axioms express a link between the relations of different boxes.
Watch out: on a tense frame $R_H$ is fixed by $R_G$, so the frame is really one relation used in two directions.

### L3 human

Prior introduced the operators $F$, $P$, $G$ and $H$ in the 1950s and 1960s.
Within [[multimodal logic|ERG3KAQWYF]], tense logic is the basic case of a logic with a converse modality.
Its frames are one relation read forward and backward.
