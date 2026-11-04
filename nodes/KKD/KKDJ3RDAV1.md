---
tag: KKDJ3RDAV1
kind: statement
role: proposition
name: Skew shape formula
sources:
  - wikipedia: en:41497810@r1357150947
    locator: Hook length formula, section Semi-standard tableaux hook length formula > Skew shape formula
    note: adopted
    mention: wikipedia://en/41497810#VN4F
    sections: [Statement]
inventory: [HFSSPWQZN0]
---

## Statement

There is a generalization of this formula for skew shapes, 

$$s_{\lambda/\mu}(1,t,t^2,\cdots) = \sum_{S \in E(\lambda/\mu)} \prod_{(i,j) \in \lambda\setminus S} \frac{t^{\lambda_j'-i}}{1-t^{h(i,j)}}$$

where the sum is taken over *excited diagrams* of shape $\lambda$ and boxes distributed according to $\mu$.

A variation on the same theme is given by Okounkov and Olshanski of the form

$$\frac{\dim\lambda/\mu}{\dim\lambda}=\frac{s^*_\mu(\lambda)}{|\lambda|!/|\mu|!},$$

where $s^*_\mu$ is the so-called shifted Schur function $s^*_\mu(x_1,\dots,x_n)=\frac{\det[(x_i+n-1)!/(\mu_j+n-j)!]}{\det[(x_i+n-i)!/(n-j)!]}$.
