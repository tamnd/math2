---
tag: E2RM9N1PV7
kind: proof
name: Proof of Grushko decomposition theorem
proves: KJSQAAXP54
sources:
  - wikipedia: en:18715724@r1354577450
    locator: Grushko theorem, section Sketch of Stalling's proof > Lemma
    note: adopted
    mention: wikipedia://en/18715724#IK7C
    sections: [Proof]
---

## Proof

**Proof:** We give the proof assuming that *F* has no generator which is mapped to the identity of $G_1\ast G_2$, for if there are such generators, they may be added to any of $F_1$ or $F_2$.

The following general results are used in the proof.

\1. There is a one or two dimensional CW complex, *Z* with fundamental group *F*. By Van Kampen theorem, the wedge of *n* circles is one such space.

\2. There exists a two complex $X=X_1\cup X_2$ where $\{p\}=X_1\cap X_2$ is a point on a one cell of *X* such that *X<sub>1</sub>* and *X<sub>2</sub>* are two complexes with fundamental groups *G<sub>1</sub>* and *G<sub>2</sub>* respectively. Note that by the Van Kampen theorem, this implies that the fundamental group of *X* is $G_1\ast G_2$.

\3. There exists a map $f:Z\rightarrow X$ such that the induced map $f_\ast$ on the fundamental groups is same as $\phi$

For the sake of convenience, let us denote $f^{-1}(X_1)=:Z_1$ and $f^{-1}(X_2)=:Z_2$. Since no generator of *F* maps to identity, the set $Z_1\cap Z_2$ has no loops, for if it does, these will correspond to circles of *Z* which map to $p\in X$, which in turn correspond to generators of *F* which go to the identity. So, the components of $Z_1\cap Z_2$ are contractible. In the case where $Z_1\cap Z_2$ has only one component, by Van Kampen's theorem, we are done, as in that case, :$F=\Pi_1(Z_1)\ast\Pi_1(Z_2)$.

The general proof follows by reducing *Z* to a space homotopically equivalent to it, but with fewer components in $Z_1\cap Z_2$, and thus by induction on the components of $Z_1\cap Z_2$.

Such a reduction of *Z* is done by attaching discs along binding ties.

We call a map $\gamma :[0,1]\rightarrow Z$ a **binding tie** if it satisfies the following properties

\1. It is **monochromatic** i.e. $\gamma([0,1])\subseteq Z_1$ or $\gamma([0,1])\subseteq Z_2$

\2. It is a **tie** i.e. $\gamma(0)$ and $\gamma(1)$ lie in different components of $Z_1\cap Z_2$.

\3. It is **null** i.e. $f \circ \gamma([0,1])$ is null homotopic in **X**.

Let us assume that such a binding tie exists. Let $\gamma$ be the binding tie.

Consider the map $g:[0,1]\rightarrow D^2$ given by $g(t)= e^{it}$. This map is a [[homeomorphism|0QT00PB5G2]] onto its image. Define the space $Z'$ as

$Z'= Z \coprod\! D^2/\! \sim$ where :$x\!\!\sim y \text{ iff} \begin{cases} x=y, \mbox{ or }\\ x=\gamma (t) \text{ and } y= g(t) \text{ for some } t\in [0,1]\mbox{ or }\\ x=g (t) \text{ and } y= \gamma (t) \text{ for some } t\in [0,1] \end{cases}$

Note that the space *Z'* deformation retracts to *Z* We first extend *f* to a function $''f'':Z\coprod \partial D^2/\!\sim$ as

$$f''(x) = \begin{cases}f(x),\ x\in Z\\ p \text{ otherwise.}\end{cases}$$

Since the $f(\gamma)$ is null homotopic, $f''$ further extends to the interior of the disc, and therefore, to $Z'$. Let $Z_i' = f'^{-1}(X_i)$ *i = 1,2*. As $\gamma(0)$ and $\gamma(1)$ lay in different components of $Z_1\cap Z_2$, $Z_1' \cap Z_2'$ has one less component than $Z_1\cap Z_2$.
