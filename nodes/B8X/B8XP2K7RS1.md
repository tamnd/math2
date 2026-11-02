---
tag: B8XP2K7RS1
kind: statement
role: theorem
name: Ravenel conjectures
msc: [55P42, 55Q51, 55P60]
uses: [300V40FC1B, 1GHF4EKBXS, 9N027RT5R6, 01826KMG2H]
about: [300V40FC1B]
sources:
  - url: https://en.wikipedia.org/wiki/Ravenel's_conjectures
same_as:
  wikidata: Q7296445
  wikipedia: Ravenel's conjectures
---

## Statement

Fix a [[prime number|01826KMG2H]] $p$.
Let $K(n)$ be the $n$-th Morava K-theory, with $K(0) = H\Q$.
Let $L_n$ be Bousfield localization with respect to the Johnson–Wilson spectrum $E(n)$, as in [[chromatic homotopy theory|300V40FC1B]].
A finite $p$-local [[spectrum|1GHF4EKBXS]] $X$ has *type* $n$ if $K(n)_* X \ne 0$ and $K(m)_* X = 0$ for all $m < n$.
The following conjectures of Ravenel are theorems.

1. (Nilpotence) A self-map $f \colon \Sigma^d X \to X$ of a finite $p$-local spectrum is nilpotent if $K(n)_*(f)$ is nilpotent for every $n \ge 0$.
   This is a form of the [[nilpotence theorem|9N027RT5R6]].
2. (Periodicity) If $X$ has type $n \ge 1$, there is a map $v \colon \Sigma^d X \to X$ such that $K(n)_*(v)$ is an isomorphism and $K(m)_*(v)$ is nilpotent for $m \ne n$.
3. (Thick subcategories) Let $\mathcal{C}_n$ be the category of finite $p$-local spectra of type at least $n$.
   Every thick subcategory of $\mathcal{C}_0$ is either some $\mathcal{C}_n$ or the zero subcategory.
4. (Smash product) For every spectrum $X$, the natural map $X \wedge L_n S \to L_n X$ is an equivalence, where $S$ is the $p$-local sphere spectrum.
5. (Chromatic convergence) For every finite $p$-local spectrum $X$, the map $X \to \operatorname{holim}_n L_n X$ is an equivalence.

## Remarks

Ravenel posed these conjectures in 1984, together with the telescope conjecture.
Devinatz, Hopkins and Smith proved the nilpotence theorem, and Hopkins and Smith deduced the periodicity and thick subcategory theorems from it.
Hopkins and Ravenel proved the smash product and chromatic convergence theorems.
The [[telescope conjecture|68650624FF]] is the exception: it holds at heights $0$ and $1$ but fails at every height $n \ge 2$.

At work: the sphere has type $0$, and the mod $p$ Moore spectrum has type $1$.
For $p$ odd, the periodicity theorem is realised by Adams' map $v_1 \colon \Sigma^{2p-2} S/p \to S/p$, whose iterates give infinite families in the stable homotopy groups of spheres.

## Explanations

### L1 human

Ravenel predicted a precise structure for the stable homotopy category, organized by the Morava K-theories.
Every finite spectrum has a height, and at its height it admits a periodic self-map.
The only ways to cut the category into closed pieces are by height.
Almost all of these predictions are now theorems.

### L2 human

The thick subcategory theorem lets one prove a property for all finite spectra of type at least $n$ by checking it on a single example.
The periodicity theorem produces the $v_n$-periodic families in the homotopy of spheres that chromatic homotopy theory studies.
The smash product theorem says that $L_n$ is a smashing localization, so it is determined by $L_n S$.
Chromatic convergence says that nothing is lost by studying a finite spectrum layer by layer.
