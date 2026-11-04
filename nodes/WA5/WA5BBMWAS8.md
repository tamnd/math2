---
tag: WA5BBMWAS8
kind: proof
name: Proof of Counting lemma
proves: WXB05RHWTY
sources:
  - wikipedia: en:62471938@r1315423087
    locator: 'Counting lemma, section Graphon version of counting lemma > Definition (cut distance). > Proof of the graphon counting lemma:'
    note: adopted
    mention: wikipedia://en/62471938#E4EO
    sections: [Proof]
---

## Proof

It suffices to prove

$$|t(F,W)-t(F,U)|\le|E(F)|\|W-U\|_{\square}.$$

Indeed, by considering the above, with the right hand side expression having a factor $\|W-U^{\phi}\|_{\Box}$ instead of $\|W-U\|_{\Box}$, and taking the infimum of the over all measure-preserving bijections $\phi$, we obtain the desired result.

*Step 1: Reformulation.* We prove a reformulation of the cut norm, which is by definition the left hand side of the following equality. The supremum in the right hand side is taken among measurable functions $u$ and $v$:

$$\sup_{S,T\subseteq [0,1]}\left|\int_{S\times T}W\right|=\sup_{u,v:[0,1]\rightarrow [0,1]}\left| \int_{[0,1]^2}W(x,y)u(x)v(y)dxdy\right|.$$

Here's the reason for the above to hold: By taking $u=\mathbb{1}_S$ and $u=\mathbb{1}_T$, we note that the left hand side is less than or equal than the right hand side. The right hand side is less than or equal than the left hand side by bilinearity of the integrand in $u,v$, and by the fact that the extrema are attained for $u,v$ taking values at $0$ or $1$.

*Step 2: Proof for $F=K_3$.* In the case that $F=K_3$, we observe that

$$\begin{aligned} t(K_3,W)-t(K_3,U)&=\int_{[0,1]^{3}}((W(x,y)W(x,z)W(y,z)-U(x,y)U(x,z)U(y,z))dxdydz\\&=\int_{[0,1]^{3}}(W-U)(x,y)W(x,z)W(y,z)dxdydz\\&\qquad+\int_{[0,1]^{3}} U(x,y)(W-U)(x,z)W(y,z)dxdydz\\&\qquad+\int_{[0,1]^{3}} U(x,y)U(x,z)(W-U)(y,z)dxdydz. \end{aligned}$$

By Step 1, we have that for a fixed $z$ that

> $$\left|\int_{[0,1]^{2}}(W-U)(x,y)W(x,z)W(y,z)dxdy\right|\le \|W-U\|_{\square}$$

Therefore, when integrating over all $z\in[0,1]$ we get that

> $$\left|\int_{[0,1]^{3}}(W-U)(x,y)W(x,z)W(y,z)dxdydz\right|\le \|W-U\|_{\square}$$

Using this bound on each of the three summands, we get that the whole sum is bounded by $3\|W-U\|_{\square}$.

*Step 3: General case.* For a general graph $F$, we need the following lemma to make everything more convenient:

> \===== Lemma. ===== The following expression holds:
>
> $$a_1a_2\cdots a_n-b_1b_2\cdots b_n=(a_1-b_1)a_2\cdots a_n+b_1(a_2-b_2)\cdots a_n+\cdots b_1b_2\cdots (a_n-b_n).$$

The above lemma follows from a straightforward expansion of the right hand side. Then, by the [[triangle inequality|03HF5PMY5T]] of norm, we have the following

$$\begin{aligned} \left| t(F,W)-t(F,U)\right| &=\left| \int\left(\prod_{u_iv_i\in E(F)}W(u_i,v_i)-\prod_{u_iv_i\in E(F)}U(u_i,v_i)\right)\prod_{v\in V}dv\right|\\&\le\sum_{i=1}^{|E(F)|}\left| \int \left(\ \prod_{j=1}^{i-1}U(u_j,v_j)(W(u_i,v_i)-U(u_i,v_i))\prod_{k=i+1}^{|E(F)|}W(u_k,v_k)\right)\prod_{v\in V}dv\right|.\end{aligned}$$

Here, each absolute value term in the sum is bounded by the cut norm $\|W-U\|_{\square}$ if we fix all the variables except for $u_i$ and $v_i$ for each $i$-th term, altogether implying that $|t(F,W)-t(F,U)|\le |E(F)|\ \delta_{\square}(W,U)$. This finishes the proof.
