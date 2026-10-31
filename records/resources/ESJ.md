---
records:
    - id: ESJ886CJJS
      kind: problem-set
      title: Kvant 1981, no. 7
      date: "1981"
      expressions:
        - key: e1
          kind: edition
          date: "1981"
          structure: ESJ886CJJS/e1.json
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
          native_id: 1981-7
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: ESJJE4G0R2
      kind: preprint
      title: Stably exotic knotted surfaces up to equivalence
      creators:
        - name: Daniel Galvin
          role: author
        - name: Daniel Kasprowski
          role: author
      date: "2026-10-13"
      subjects:
        - system: arxiv
          code: math.GT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-13"
          ids:
            arxiv: "2610.18783"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.18783"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
