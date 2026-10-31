---
records:
    - id: PBX05QBXHP
      kind: monograph
      title: Non-Riemannian Geometry
      creators:
        - name: L. Eisenhart
          role: author
      date: "1927-12-31"
      expressions:
        - key: e1
          kind: edition
          date: "1927-12-31"
          ids:
            doi: 10.1090/coll/008
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1927-12-31"
              ids:
                isbn:
                    - "9780821810088"
                    - "9780821874455"
                    - "9781470431587"
      relations:
        - kind: part_of
          to: W1VWARV4XH
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/coll/008
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: PBX6AMPVT2
      kind: preprint
      title: Asymptotically Optimal Mixed-State Cloning
      creators:
        - name: Jiani Fei
          role: author
        - name: Jinzhao Wang
          role: author
      date: "2026-09-28"
      subjects:
        - system: arxiv
          code: quant-ph
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-28"
          ids:
            arxiv: "2609.35986"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.35986"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
---
