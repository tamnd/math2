---
records:
    - id: HMK2DX6WE5
      kind: problem-set
      title: Kvant 1972, no. 11
      date: "1972"
      expressions:
        - key: e1
          kind: edition
          date: "1972"
          structure: HMK2DX6WE5/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1972-11
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: HMK2QT55G7
      kind: preprint
      title: Polyconvex neural-network surrogates with learned paired directional features for anisotropic hyperelastic homogenization
      creators:
        - name: S. Ares de Parga
          role: author
        - name: A. Cornejo
          role: author
        - name: J. A. Hernández
          role: author
        - name: R. Rossi
          role: author
      date: "2026-10-08"
      subjects:
        - system: arxiv
          code: physics.comp-ph
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: cs.NA
        - system: arxiv
          code: math.NA
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-08"
          ids:
            arxiv: "2610.12801"
      scope:
        value: out
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.12801"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to out
---
