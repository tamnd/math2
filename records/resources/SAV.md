---
records:
    - id: SAVFTAK3R3
      kind: problem-set
      title: Kvant 1987, no. 11
      date: "1987"
      expressions:
        - key: e1
          kind: edition
          date: "1987"
          structure: SAVFTAK3R3/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1987-11
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: SAVNP6BB03
      kind: preprint
      title: Rigidity of Right-Angled Coxeter Groups
      creators:
        - name: David G. Radcliffe
          role: author
      date: "1999-01-12"
      subjects:
        - system: arxiv
          code: math.GR
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "1999-01-12"
          ids:
            arxiv: math/9901049
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: math/9901049
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
