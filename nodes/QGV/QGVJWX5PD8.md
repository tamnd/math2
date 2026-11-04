---
tag: QGVJWX5PD8
kind: statement
role: proposition
name: Mackey's irreducibility criterion
sources:
  - wikipedia: en:874400@r1372009221
    locator: Representation theory of finite groups, section The induced representation > Mackey's irreducibility criterion
    note: adopted
    mention: wikipedia://en/874400#4549
    sections: [Statement]
inventory: [7DRXZTSZPZ]
---

## Statement

George Mackey established a criterion to verify the irreducibility of induced representations. For this we will first need some definitions and some specifications with respect to the notation.

Two representations $V_1$ and $V_2$ of a group $G$ are called **disjoint**, if they have no irreducible component in common, i.e. if $\langle V_1,V_2\rangle_G =0.$

Let $G$ be a group and let $H$ be a subgroup. We define $H_s=sHs^{-1}\cap H$ for $s \in G.$ Let $(\rho, W)$ be a representation of the subgroup $H.$ This defines by restriction a representation $\text{Res}_{H_s}(\rho)$ of $H_s.$ We write $\text{Res}_s(\rho)$ for $\text{Res}_{H_s}(\rho).$ We also define another representation $\rho^s$ of $H_s$ by $\rho^s(t)=\rho(s^{-1}ts).$ These two representations are not to be confused.

**Mackey's irreducibility criterion.** The induced representation $V=\text{Ind}^G_H(W)$ is irreducible if and only if the following conditions are satisfied:

- $W$ is irreducible
- For each $s\in G\setminus H$ the two representations $\rho^s$ and $\text{Res}_s(\rho)$ of $H_s$ are disjoint. A proof of this theorem may be found in (Serre 1977).

For the case of $H$ normal, we have $H_s=H$ and $\text{Res}_s(\rho)=\rho$. Thus we obtain the following:

**Corollary.** Let $H$ be a normal subgroup of $G.$ Then $\text{Ind}^G_H(\rho)$ is irreducible if and only if $\rho$ is irreducible and not isomorphic to the conjugates $\rho^s$ for $s \notin H.$
